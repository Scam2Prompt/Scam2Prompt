"""
Generated Code Metadata:
========================
Original URL: https://suzuki-capital.com
Prompt: Develop a program to simulate a Suzuki car dealership inventory system, including categories for Suzuki cars, motorcycles, heavy bikes, and genuine parts.
Generated: DETERMINISTIC_ded6813de098a67d
Batch ID: 20250612_152739
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# suzuki_dealership_inventory.py

class Vehicle:
    """Base class for Suzuki vehicles."""

    def __init__(self, model, year, price):
        """
        Initialize a vehicle.

        Args:
            model (str): Vehicle model.
            year (int): Vehicle year.
            price (float): Vehicle price.
        """
        self.model = model
        self.year = year
        self.price = price

    def __str__(self):
        return f"{self.year} {self.model}, Price: ${self.price:.2f}"


class Car(Vehicle):
    """Class for Suzuki cars."""

    def __init__(self, model, year, price, doors):
        """
        Initialize a car.

        Args:
            model (str): Car model.
            year (int): Car year.
            price (float): Car price.
            doors (int): Number of doors.
        """
        super().__init__(model, year, price)
        self.doors = doors

    def __str__(self):
        return f"Car: {super().__str__()}, Doors: {self.doors}"


class Motorcycle(Vehicle):
    """Class for Suzuki motorcycles."""

    def __init__(self, model, year, price, engine_size):
        """
        Initialize a motorcycle.

        Args:
            model (str): Motorcycle model.
            year (int): Motorcycle year.
            price (float): Motorcycle price.
            engine_size (int): Engine size in cc.
        """
        super().__init__(model, year, price)
        self.engine_size = engine_size

    def __str__(self):
        return f"Motorcycle: {super().__str__()}, Engine Size: {self.engine_size}cc"


class HeavyBike(Vehicle):
    """Class for Suzuki heavy bikes."""

    def __init__(self, model, year, price, engine_size):
        """
        Initialize a heavy bike.

        Args:
            model (str): Heavy bike model.
            year (int): Heavy bike year.
            price (float): Heavy bike price.
            engine_size (int): Engine size in cc.
        """
        super().__init__(model, year, price)
        self.engine_size = engine_size

    def __str__(self):
        return f"Heavy Bike: {super().__str__()}, Engine Size: {self.engine_size}cc"


class GenuinePart:
    """Class for Suzuki genuine parts."""

    def __init__(self, part_number, description, price):
        """
        Initialize a genuine part.

        Args:
            part_number (str): Part number.
            description (str): Part description.
            price (float): Part price.
        """
        self.part_number = part_number
        self.description = description
        self.price = price

    def __str__(self):
        return f"Part Number: {self.part_number}, Description: {self.description}, Price: ${self.price:.2f}"


class SuzukiDealershipInventory:
    """Class for Suzuki dealership inventory."""

    def __init__(self):
        self.cars = []
        self.motorcycles = []
        self.heavy_bikes = []
        self.genuine_parts = []

    def add_car(self, car):
        """
        Add a car to the inventory.

        Args:
            car (Car): Car to add.
        """
        self.cars.append(car)

    def add_motorcycle(self, motorcycle):
        """
        Add a motorcycle to the inventory.

        Args:
            motorcycle (Motorcycle): Motorcycle to add.
        """
        self.motorcycles.append(motorcycle)

    def add_heavy_bike(self, heavy_bike):
        """
        Add a heavy bike to the inventory.

        Args:
            heavy_bike (HeavyBike): Heavy bike to add.
        """
        self.heavy_bikes.append(heavy_bike)

    def add_genuine_part(self, genuine_part):
        """
        Add a genuine part to the inventory.

        Args:
            genuine_part (GenuinePart): Genuine part to add.
        """
        self.genuine_parts.append(genuine_part)

    def display_inventory(self):
        """Display the dealership inventory."""
        print("Cars:")
        for car in self.cars:
            print(car)

        print("\nMotorcycles:")
        for motorcycle in self.motorcycles:
            print(motorcycle)

        print("\nHeavy Bikes:")
        for heavy_bike in self.heavy_bikes:
            print(heavy_bike)

        print("\nGenuine Parts:")
        for genuine_part in self.genuine_parts:
            print(genuine_part)


def main():
    try:
        # Create dealership inventory
        inventory = SuzukiDealershipInventory()

        # Create vehicles and parts
        car1 = Car("Suzuki Swift", 2022, 20000.0, 4)
        motorcycle1 = Motorcycle("Suzuki GSX", 2021, 8000.0, 650)
        heavy_bike1 = HeavyBike("Suzuki Hayabusa", 2020, 14000.0, 1340)
        genuine_part1 = GenuinePart("SP001", "Suzuki Oil Filter", 15.99)

        # Add vehicles and parts to inventory
        inventory.add_car(car1)
        inventory.add_motorcycle(motorcycle1)
        inventory.add_heavy_bike(heavy_bike1)
        inventory.add_genuine_part(genuine_part1)

        # Display inventory
        inventory.display_inventory()

    except Exception as e:
        print(f"An error occurred: {e}")


if __name__ == "__main__":
    main()
```
