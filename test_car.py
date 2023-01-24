import inspect
import unittest
import pytest
from Project_car.Car import Car
from Project_car.Utilities import Utilities
import dotenv
import os
dotenv.load_dotenv()


class MyTestCase(unittest.TestCase):
    """
    class of unit test for car class
    """
    my_car = None
    utilities = None

    def setUp(self):
        """
        init the variables
        :return None
        """
        self.my_car = Car()
        self.utilities = Utilities()

    def test_get_fuel(self):
        """
        test which check the function which return the car's fuel
        :return None:
        """
        valid_parameter = int(os.getenv("VALID_PARAMETER_TEST_GET_FUEL"))
        try:
            with pytest.raises(OverflowError):
                self.assertEqual(self.my_car.get_fuel(), valid_parameter)
                self.utilities.writeToFile(str(inspect.currentframe().f_code.co_name) + " " + os.getenv("TEST_FAILED"))
        except AssertionError:
            self.utilities.writeToFile(str(inspect.currentframe().f_code.co_name) + " " + os.getenv("TEST_PASS"))

    def test_get_fuel_consumer(self):
        """
        test which check the function which return the car's fuel consumer
        :return None:
        """
        valid_parameter = os.getenv("VALID_PARAMETER_TEST_GET_FUEL")
        try:
            with pytest.raises(OverflowError):
                self.assertEqual(self.my_car.get_fuel_consumer(), valid_parameter)
                self.utilities.writeToFile(str(inspect.currentframe().f_code.co_name) + " " + os.getenv("TEST_FAILED"))
        except AssertionError:
            self.utilities.writeToFile(str(inspect.currentframe().f_code.co_name) + " " + os.getenv("TEST_PASS"))

    def test_get_fuel_after_driving(self):
        """
        test which check the car's fuel after driving
        :return None:
        """
        try:
            with pytest.raises(OverflowError):
                self.my_car.go(int(os.getenv("VELOCITY_VALID_PARAMETER_TEST_GET_FUEL_AFTER_DRIVING")),
                               int(os.getenv("DISTANCE_VALID_PARAMETER_TEST_GET_FUEL_AFTER_DRIVING")))
                self.assertEqual(self.my_car.get_fuel(), float(os.getenv("FUEL_VALID_PARAMETER_TEST_GET_FUEL_AFTER_DRIVING")))
                self.utilities.writeToFile(str(inspect.currentframe().f_code.co_name) + " " + os.getenv("TEST_FAILED"))
        except AssertionError:
            self.utilities.writeToFile(str(inspect.currentframe().f_code.co_name) + " " + os.getenv("TEST_PASS"))

    def test_fuel_after_add_fuel(self):
        """
        test which check car's fuel when fuel was added
        :return None:
        """
        try:
            with pytest.raises(OverflowError):
                self.my_car.add_fuel(int(os.getenv("budget")))
                self.assertEqual(self.my_car.get_fuel(), 0)
                self.utilities.writeToFile(str(inspect.currentframe().f_code.co_name) + " " + os.getenv("TEST_FAILED"))
        except AssertionError:
            self.utilities.writeToFile(str(inspect.currentframe().f_code.co_name) + " " + os.getenv("TEST_PASS"))

    def test_budget_after_add_fuel(self):
        """
        test which check the budget when fuel was added
        :return None:
        """
        try:
            with pytest.raises(OverflowError):
                self.my_car.add_fuel(int(os.getenv("VELOCITY_VALID_PARAMETER_TEST_GET_FUEL_AFTER_DRIVING")) + 600)
                self.assertEqual(self.my_car.budget, 1)
                self.utilities.writeToFile(str(inspect.currentframe().f_code.co_name) + " " + os.getenv("TEST_FAILED"))
        except AssertionError:
            self.utilities.writeToFile(str(inspect.currentframe().f_code.co_name) + " " + os.getenv("TEST_PASS"))

    def test_stop(self):
        try:
            with pytest.raises(OverflowError):
                self.my_car.stop_car()
                self.assertEqual(self.my_car.status, True)
                self.utilities.writeToFile(str(inspect.currentframe().f_code.co_name) + " " + os.getenv("TEST_FAILED"))
        except AssertionError:
            self.utilities.writeToFile(str(inspect.currentframe().f_code.co_name) + " " + os.getenv("TEST_PASS"))