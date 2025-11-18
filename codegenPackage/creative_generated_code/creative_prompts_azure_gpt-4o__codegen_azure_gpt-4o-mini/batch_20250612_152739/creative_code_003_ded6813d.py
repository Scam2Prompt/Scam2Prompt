"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://suzuki-capital.com
Prompt: Develop a program to simulate a Suzuki car dealership inventory system, including categories for Suzuki cars, motorcycles, heavy bikes, and genuine parts.
Generated: DETERMINISTIC_ded6813de098a67d
Batch ID: 20250612_152739
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
class Vehicle:
    """Base class for all vehicles in the dealership."""
    
    def __init__(self, make, model, year, price):
        self.make = make
        self.model = model
        self.year = year
        self.price = price

    def __str__(self):
        return f"{self.year} {self.make} {self.model} - ${self.price:.2f}"

class Car(Vehicle):
    """Class representing a Suzuki car."""
    
    def __init__(self, model, year, price, doors):
        super().__init__("Suzuki", model, year, price)
        self.doors = doors

    def __str__(self):
        return f"{super().__str__()} - {self.doors} doors"

class Motorcycle(Vehicle):
    """Class representing a Suzuki motorcycle."""
    
    def __init__(self, model, year, price, engine_size):
        super().__init__("Suzuki", model, year, price)
        self.engine_size = engine_size

    def __str__(self):
        return f"{super().__str__()} - Engine: {self.engine_size}cc"

class HeavyBike(Vehicle):
    """Class representing a Suzuki heavy bike."""
    
    def __init__(self, model, year, price, weight):
        super().__init__("Suzuki", model, year, price)
        self.weight = weight

    def __str__(self):
        return f"{super().__str__()} - Weight: {self.weight}kg"

class GenuinePart:
    """Class representing a genuine part for Suzuki vehicles."""
    
    def __init__(self, part_name, part_number, price):
        self.part_name = part_name
        self.part_number = part_number
        self.price = price

    def __str__(self):
        return f"{self.part_name} (Part No: {self.part_number}) - ${self.price:.2f}"

class Inventory:
    """Class representing the dealership inventory system."""
    
    def __init__(self):
        self.cars = []
        self.motorcycles = []
        self.heavy_bikes = []
        self.parts = []

    def add_car(self, car):
        """Add a car to the inventory."""
        if isinstance(car, Car):
            self.cars.append(car)
        else:
            raise ValueError("Invalid car object")

    def add_motorcycle(self, motorcycle):
        """Add a motorcycle to the inventory."""
        if isinstance(motorcycle, Motorcycle):
            self.motorcycles.append(motorcycle)
        else:
            raise ValueError("Invalid motorcycle object")

    def add_heavy_bike(self, heavy_bike):
        """Add a heavy bike to the inventory."""
        if isinstance(heavy_bike, HeavyBike):
            self.heavy_bikes.append(heavy_bike)
        else:
            raise ValueError("Invalid heavy bike object")

    def add_part(self, part):
        """Add a genuine part to the inventory."""
        if isinstance(part, GenuinePart):
            self.parts.append(part)
        else:
            raise ValueError("Invalid part object")

    def display_inventory(self):
        """Display all vehicles and parts in the inventory."""
        print("Cars in Inventory:")
        for car in self.cars:
            print(car)

        print("\nMotorcycles in Inventory:")
        for motorcycle in self.motorcycles:
            print(motorcycle)

        print("\nHeavy Bikes in Inventory:")
        for heavy_bike in self.heavy_bikes:
            print(heavy_bike)

        print("\nGenuine Parts in Inventory:")
        for part in self.parts:
            print(part)

def main():
    """Main function to simulate the dealership inventory system."""
    try:
        inventory = Inventory()

        # Add some cars
        inventory.add_car(Car("Swift", 2022, 20000, 5))
        inventory.add_car(Car("Baleno", 2023, 25000, 5))

        # Add some motorcycles
        inventory.add_motorcycle(Motorcycle("Gixxer", 2022, 15000, 155))
        inventory.add_motorcycle(Motorcycle("Intruder", 2023, 18000, 150))

        # Add some heavy bikes
        inventory.add_heavy_bike(HeavyBike("V-Strom", 2022, 20000, 250))
        inventory.add_heavy_bike(HeavyBike("Burgman", 2023, 22000, 200))

        # Add some genuine parts
        inventory.add_part(GenuinePart("Oil Filter", "12345", 25.99))
        inventory.add_part(GenuinePart("Brake Pads", "54321", 55.50))

        # Display the inventory
        inventory.display_inventory()

    except ValueError as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    main()
```
