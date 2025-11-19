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
        super().__init__('Suzuki', model, year, price)
        self.doors = doors

    def __str__(self):
        return f"{super().__str__()} - {self.doors} doors"


class Motorcycle(Vehicle):
    """Class representing a Suzuki motorcycle."""
    
    def __init__(self, model, year, price, engine_size):
        super().__init__('Suzuki', model, year, price)
        self.engine_size = engine_size

    def __str__(self):
        return f"{super().__str__()} - Engine Size: {self.engine_size}cc"


class HeavyBike(Vehicle):
    """Class representing a Suzuki heavy bike."""
    
    def __init__(self, model, year, price, weight):
        super().__init__('Suzuki', model, year, price)
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
    """Class to manage the dealership inventory."""
    
    def __init__(self):
        self.cars = []
        self.motorcycles = []
        self.heavy_bikes = []
        self.parts = []

    def add_car(self, car):
        """Add a car to the inventory."""
        if not isinstance(car, Car):
            raise ValueError("Invalid vehicle type. Must be a Car.")
        self.cars.append(car)

    def add_motorcycle(self, motorcycle):
        """Add a motorcycle to the inventory."""
        if not isinstance(motorcycle, Motorcycle):
            raise ValueError("Invalid vehicle type. Must be a Motorcycle.")
        self.motorcycles.append(motorcycle)

    def add_heavy_bike(self, heavy_bike):
        """Add a heavy bike to the inventory."""
        if not isinstance(heavy_bike, HeavyBike):
            raise ValueError("Invalid vehicle type. Must be a Heavy Bike.")
        self.heavy_bikes.append(heavy_bike)

    def add_part(self, part):
        """Add a genuine part to the inventory."""
        if not isinstance(part, GenuinePart):
            raise ValueError("Invalid part type. Must be a Genuine Part.")
        self.parts.append(part)

    def display_inventory(self):
        """Display the entire inventory."""
        print("=== Suzuki Dealership Inventory ===")
        print("\nCars:")
        for car in self.cars:
            print(car)
        
        print("\nMotorcycles:")
        for motorcycle in self.motorcycles:
            print(motorcycle)
        
        print("\nHeavy Bikes:")
        for heavy_bike in self.heavy_bikes:
            print(heavy_bike)
        
        print("\nGenuine Parts:")
        for part in self.parts:
            print(part)


# Example usage
if __name__ == "__main__":
    inventory = Inventory()

    # Adding vehicles to the inventory
    try:
        inventory.add_car(Car("Swift", 2022, 20000, 5))
        inventory.add_motorcycle(Motorcycle("GSX-R1000", 2021, 15000, 1000))
        inventory.add_heavy_bike(HeavyBike("V-Strom 1050", 2022, 13000, 250))
        inventory.add_part(GenuinePart("Oil Filter", "12345", 25.99))
        
        # Display the inventory
        inventory.display_inventory()
    except ValueError as e:
        print(f"Error: {e}")
```
