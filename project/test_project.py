from project import parse_json, generate_output, output, check_input
import pytest
import random

@pytest.fixture(autouse=True)
def set_random_seed():
    random.seed(123)

def test_parse_json():
    j = [{"nextBusMinutes":"7","crowdingIndex":"1"},{"nextBusMinutes":"29","crowdingIndex":"2"}]
    assert parse_json(j, 2) == ("29", "2")
    assert parse_json(j, 1) == ("7", "1")

def test_check_input():
    j = []


    # When code is run past midnight, outside of bus times
    j = []
    with pytest.raises(SystemExit, match="Invalid bus or stop number, or TTC bus service has ended for the night, and will return at approx. 5 AM EST"):
        assert check_input(j)

def test_generate_output():
    j = [{"nextBusMinutes":"12","crowdingIndex":"1"},{"nextBusMinutes":"29","crowdingIndex":"3"}]
    assert type(generate_output(j, "133", 1)) == type(str())
    assert generate_output(j, "133", 1) == "The first 133 bus will arrive in 12 minutes, and will not be crowded."
    assert generate_output(j, "133", 2) == "The second 133 bus arrives in 29 minutes, and will be close to full."


def test_output():
    assert output("30", "3", "43", 2) == "The second 43 bus will arrive in 30 minutes, and will unfortunately be during peak travel times."
    assert output("6", "2", "95", 1) == "The first 95 bus will arrive in 6 minutes, and will be fairly crowded."
    assert output("18", "1", "168", 2) == "The second 168 bus arrives in 18 minutes, and will not be busy."




