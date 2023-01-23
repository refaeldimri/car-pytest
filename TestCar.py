import inspect
import os
import pytest
from Project_car.Car import Car
from Project_car.Utilities import Utilities
import dotenv


# some init
dotenv.load_dotenv()
utilities = Utilities()


@pytest.fixture
def car():
    return Car()


@pytest.mark.test
def test_get_fuel(car):
    """
    this test check the function which thr car's fuel
    :param car:
    :return None:
    """
    try:
        assert car.get_fuel() == 20
        utilities.writeToFile(str(inspect.currentframe().f_code.co_name) + " " + os.getenv("TEST_PASS"))
    except AssertionError:
        utilities.writeToFile(str(inspect.currentframe().f_code.co_name) + " " + os.getenv("TEST_FAILED"))


def test_go_with_max_velocity(car):
    """
    this function check function go with max velocity, suppose to raise error when
    the velocity parameter > max velocity
    :param car:
    :return None:
    """
    with pytest.raises(OverflowError):
        car.go(100, 1)
        utilities.writeToFile(str(inspect.currentframe().f_code.co_name) + " " + os.getenv("TEST_FAILED"))
    utilities.writeToFile(str(inspect.currentframe().f_code.co_name) + " " + os.getenv("TEST_PASS"))


def test_add_fuel(car):
    """
    this test check the function add fuel,
    suppose to raise error if the fuel capacity is larger the car's full fuel
    :param car:
    :return None:
    """
    with pytest.raises(OverflowError):
        car.add_fuel(600)
        utilities.writeToFile(str(inspect.currentframe().f_code.co_name) + " " + os.getenv("TEST_FAILED"))
    utilities.writeToFile(str(inspect.currentframe().f_code.co_name) + " " + os.getenv("TEST_PASS"))


def test_go_with_driving_without_resource(car):
    """
    this test check the function go with long distance with small capacity of fuel,
    suppose to raise error with these condition
    :param car:
    :return None:
    """
    with pytest.raises(OverflowError):
        car.go(1, 550)
        utilities.writeToFile(str(inspect.currentframe().f_code.co_name) + " " + os.getenv("TEST_FAILED"))
    utilities.writeToFile(str(inspect.currentframe().f_code.co_name) + " " + os.getenv("TEST_PASS"))




