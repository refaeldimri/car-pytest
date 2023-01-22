import inspect
import os
import pytest
from Project_car.Car import Car
from Project_car.Utilities import Utilities
import dotenv
dotenv.load_dotenv()
utilities = Utilities()


@pytest.fixture
def car():
    return Car()


@pytest.mark.test
def test_get_fuel(car):
    try:
        assert car.get_fuel() == 20
        utilities.writeToFile(str(inspect.currentframe().f_code.co_name) + " " + os.getenv("TEST_PASS"))
    except AssertionError:
        utilities.writeToFile(str(inspect.currentframe().f_code.co_name) + " " + os.getenv("TEST_FAILED"))


def test_go_with_max_velocity(car):
    with pytest.raises(OverflowError):
        car.go(100, 1)
        utilities.writeToFile(str(inspect.currentframe().f_code.co_name) + " " + os.getenv("TEST_FAILED"))
    utilities.writeToFile(str(inspect.currentframe().f_code.co_name) + " " + os.getenv("TEST_PASS"))


def test_add_fuel(car):
    with pytest.raises(OverflowError):
        car.add_fuel(600)
        utilities.writeToFile(str(inspect.currentframe().f_code.co_name) + " " + os.getenv("TEST_FAILED"))
    utilities.writeToFile(str(inspect.currentframe().f_code.co_name) + " " + os.getenv("TEST_PASS"))


def test_go_with_driving_without_resource(car):
    with pytest.raises(OverflowError):
        car.go(1, 550)
        utilities.writeToFile(str(inspect.currentframe().f_code.co_name) + " " + os.getenv("TEST_FAILED"))
    utilities.writeToFile(str(inspect.currentframe().f_code.co_name) + " " + os.getenv("TEST_PASS"))




