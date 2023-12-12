# Toronto Bus Arrival Tracker
### Link: https://www.youtube.com/watch?v=xhusXZsagrM
#### Toronto Bus Arrival Tracker is a live TTC(Toronto Transit Commission) bus locator, created to provide real-time bus arrival scheduling to Torontonians. 

#### The program works by first asking the user for a Bus. This can either be inputted as the bus's route name(e.g, Milner, McCowan), or the bus's assigned 1-3 digit numeric code(e.g 132, 16). It then prompts the user for the number of the bus stop the user is waiting at. This information is available on a posted sign near the bus stop, on the TTC website, or on Google Maps if planning the trip ahead of time. It will then output the bus's next arrival time, as well as how crowded the bus is. The sentence structure of each run is randomized using a list of sentence openings and endings, in an effort to avoid repetitivity. After receiving the first bus time, the user will then be asked if they would like the second bus's arrival time, which can be useful if you are unlikely to reach the first bus, or planning your trip ahead of time. If the TTC is ending or near end of bus service for the night(approximately 1 AM to 5 AM EST), the program will inform the user that TTC service is ending, and when they will be able to try again. 

#### The first file, "project.py", contains the program. The requirements for this program are also listed in file "requirements.txt", as the requests module was used to access multiple different json files, for the purpose of accessing information and inrceasing usability (allowing the user to input the bus name, instead of only its lesser known designated bus number). The last file is the pytest script used to test the project, under "test_project.py". As the random module is used in my code, the test program runs using a set seed, in order to ensure that I receive the correct output despite the random elements of the code. The test script tests various aspects of project, including its ability to verify user input, its ability to parse the json file I use, and its ability to generate an output in string format.

#### This program solves the problem of people having to wait idly at bus stops with no information of the next bus. It lets Torontonians plan ahead for buses they would be interested in taking, as the arrival of any future buses can be provided quickly and accurately, straight from the TTC's API.

#### For specific input examples, run the program through the terminal with the 'examples' argument in the command line: "$ python project.py examples"

### Future project improvements:
- Add a GUI to improve the user experience
- Implement support for TTC night buses, as well as subways and streetcars
