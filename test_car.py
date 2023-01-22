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
        try:
            with pytest.raises(OverflowError):
                self.assertEqual(self.my_car.get_fuel(), 100)
                self.utilities.writeToFile(str(inspect.currentframe().f_code.co_name) + " " + os.getenv("TEST_PASS"))
        except AssertionError:
            self.utilities.writeToFile(str(inspect.currentframe().f_code.co_name) + " " + os.getenv("TEST_FAILED"))

    def test_get_fuel_consumer(self):
        """
        test which test the car's fuel consumer
        :return None:
        """
        try:
            with pytest.raises(OverflowError):
                self.assertEqual(self.my_car.get_fuel_consumer(), os.getenv("fuel_consumer"))
                self.utilities.writeToFile(str(inspect.currentframe().f_code.co_name) + " " + os.getenv("TEST_PASS"))
        except AssertionError:
            self.utilities.writeToFile(str(inspect.currentframe().f_code.co_name) + " " + os.getenv("TEST_FAILED"))

    def test_get_fuel_after_driving(self):
        """
        test which check the car's fuel after driving
        :return None:
        """
        try:
            with pytest.raises(OverflowError):
                self.my_car.go(100, 2)
                self.assertEqual(self.my_car.get_fuel(), 49.9)
                self.utilities.writeToFile(str(inspect.currentframe().f_code.co_name) + " " + os.getenv("TEST_PASS"))
        except AssertionError:
            self.utilities.writeToFile(str(inspect.currentframe().f_code.co_name) + " " + os.getenv("TEST_FAILED"))

    def test_fuel_after_add_fuel(self):
        """
        test which check car's fuel when fuel was added
        :return None:
        """
        try:
            with pytest.raises(OverflowError):
                self.my_car.add_fuel(500)
                self.assertEqual(self.my_car.get_fuel(), 0)
                self.utilities.writeToFile(str(inspect.currentframe().f_code.co_name) + " " + os.getenv("TEST_PASS"))
        except AssertionError:
            self.utilities.writeToFile(str(inspect.currentframe().f_code.co_name) + " " + os.getenv("TEST_FAILED"))

    def test_budget_after_add_fuel(self):
        """
        test which check the budget when fuel was added
        :return None:
        """
        try:
            with pytest.raises(OverflowError):
                self.my_car.add_fuel(500)
                self.assertEqual(self.my_car.budget, 0)
                self.utilities.writeToFile(str(inspect.currentframe().f_code.co_name) + " " + os.getenv("TEST_PASS"))
        except AssertionError:
            self.utilities.writeToFile(str(inspect.currentframe().f_code.co_name) + " " + os.getenv("TEST_FAILED"))













