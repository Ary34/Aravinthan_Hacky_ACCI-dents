import requests
import random
import sys
import re
import pprint

def first_check(bus):
    if not bus[0].isalpha():
        return bus
    url = f"https://www.ttc.ca/ttcapi/routedetail/listroutes"
    headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/116.0.0.0 Safari/537.36"}
    j = requests.get(url, headers=headers).json()
    bus = bus.replace(".", "")
    if bus == "o'connor":
        return 70
    for i in j:
        m = re.search(r"(\d+)\s*" + re.escape(bus) + r"\s*bus", i["description"], re.IGNORECASE)
        if m:
            return m.group(1)

def get_input():
    bus = input("Bus: ").lower().strip()
    stop = input("Bus stop number: ").lower().strip()
    return first_check(bus), stop

def examples():
    try:
        if sys.argv[1].lower().strip() == "examples":
            d = {
                ("Graydon Hall", "122"): ["3262", "3259", "2110", "9654"],
                ("Kennedy", "43"): ["4065", "4131", "4091", "4097"],
                ("Jane", "35"): ["1602", "1593", "3911"]
            }
            print("On the left are the buses, which support input through their name or their designated 1-3 digit number. The right shows a list of several available bus stops. For a greater collection of buses and stops, access the TTC website.")
            pprint.pprint(d)
            sys.exit()
    except IndexError:
        print("Not a Toronto local? Run the program with 'examples' in the command line to display a list of some TTC buses and some of their stop numbers!")

def check_input(json):
    try:
        _ = json[0]["nextBusMinutes"], json[0]["crowdingIndex"]
    except IndexError:
        sys.exit("Invalid bus or stop number, or TTC bus service has ended for the night, and will return at approx. 5 AM EST")

def parse_json(json, n):
    if n == 1:
        return json[0]["nextBusMinutes"], json[0]["crowdingIndex"]

    elif n == 2:
        try:
            return json[1]["nextBusMinutes"], json[1]["crowdingIndex"]
        except IndexError:
            sys.exit("Unfortunately, the TTC currently only provides the 1 latest bus arrival time for this stop, likely due to the infrequency of such buses at night. Thank you for using this service.")

def output(minutes, crowd, bus, n):
    if crowd == "1":
        crowd = random.choice(["will not be crowded.", "will practically be empty.", "will not be busy.", "will have plenty of space for a comfortable ride.", "will have plenty of room for passengers."])
    elif crowd == "2":
        crowd = random.choice(["will be fairly crowded.", "will be lightly crowded", "may have fewer seats available", "will have a moderate number of passengers onboard.", "will be reasonably occupied."])
    elif crowd == "3":
        crowd = random.choice(["will unfortunately be during peak travel times.", "will be heavily crowded.", "will be close to full.", "will experience high demand and limited space.", "will be quite busy,  consider catching a different bus.", "will have limited space available due to high demand."])
    if n == 1:
        order = "first"
    elif n == 2:
        order = "second"
    return random.choice([f"The {order} {bus} bus arrives in {minutes} minutes, and {crowd}", f"The {order} {bus} bus will arrive in {minutes} minutes, and {crowd}"])

def generate_output(j, bus, n):
    x,y = parse_json(j, n)
    result = output(x,y,bus,n)
    return result

def next_bus(j, bus, n):
    while True:
        s = input("Don't think you'll make it? We would be glad to provide you the next available bus time! Enter (yes/no) ").strip().lower()
        if s == "yes":
            print(generate_output(j, bus, n))
            print("Thank you for using this service, we hope you enjoy your travel!")
            break
        elif s == "no":
            print("Thank you for using this service, we hope you enjoy your travel!")
            break
        else:
            continue

def info(bus, stop):
    url = f"https://www.ttc.ca/ttcapi/routedetail/GetNextBuses?routeId={bus}&stopCode={stop}"
    headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/116.0.0.0 Safari/537.36"}
    r = requests.get(url, headers=headers)
    return r.json()

def main():
    examples()
    bus, stop = get_input()
    j = info(bus, stop)
    check_input(j)
    print(generate_output(j, bus, 1))
    next_bus(j, bus, 2)

if __name__ == "__main__":
    main()