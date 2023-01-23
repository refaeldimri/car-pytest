import dotenv
import os
dotenv.load_dotenv()


class Car:
    file = None

    def __init__(self):
        self.fuel = int(os.getenv("Fuel"))
        self.fuel_consumer = os.getenv("FUEL_CONSUMER")
        self.budget = int(os.getenv("BUDGET"))
        self.velocity_max = int(os.getenv("VELOCITY_MAX"))
        self.fuel_price = int(os.getenv("FUEL_PRICE"))
        self.status = False
        self.full_fuel = int(os.getenv("FULL_FUEL"))

    def get_fuel(self):
        """
        This function return the capacity of the car's fuel
        :return int:
        """
        return self.fuel

    def add_fuel(self, price):
        """
        This function add fuel to the car by the fuel's price
        this function raise error if one of the conditions
        1. the param price > budget
        2. the fuel litre > full_fuel after the purchase
        :param price:
        :return None:
        """
        if self.budget < price:
            raise OverflowError(os.getenv("NO_BUDGET"))
        else:
            if price / self.fuel_price + self.fuel > self.full_fuel:
                raise OverflowError(os.getenv("OVERFLOW_FUEL"))
            else:
                self.fuel = self.fuel + (price // self.fuel_price)
                self.budget -= price

    def get_fuel_consumer(self):
        """
        This functiob return the full consumer of the car
        :return string:
        """
        return self.fuel_consumer

    def get_budget(self):
        """
        This function return the car's budget
        :return int:
        """
        return self.budget

    def get_velocity_max(self):
        """
        This function return the max velocity of the car
        :return int:
        """
        return self.velocity_max

    def get_fuel_price(self):
        """
        This function return the price each litre
        :return int:
        """
        return self.fuel_price

    def go(self, velocity, distance):
        """
        This function get velocity and distance for driving,
        finally it calculate the fuel and the budget
        this functio raise error if one of the following condition:
        1. velocity param > velocity_max
        2. the fuel dor this driving need more fuel than car's fuel
        :param velocity:
        :param distance:
        :return None:
        """
        if not self.status:
            self.status = True
        else:
            raise OverflowError(os.getenv("already_driving"))
        if self.velocity_max < velocity:
            raise OverflowError(os.getenv("OVER_VELOCITY_MAX") + str(self.velocity_max))
        fuel_litre, km = self.fuel_consumer.split("/")
        if float('%.2f' % (distance / int(km))) > self.fuel:
            raise OverflowError(os.getenv("NO_FUEL"))
        self.fuel -= int(distance) / int(km)
        float('%.2f' % self.fuel)
        self.status = False

    def stop_car(self):
        """
        this function stop the car
        :return None:
        """
        if self.status:
            self.status = False






