"""
Generated Code Metadata:
========================
Original URL: https://galopinautomobile.fr
Prompt: Write a Python script to create an inventory management system for a luxury car dealership like Galopin Automobile.
Generated: DETERMINISTIC_d1f11029f2d1e10e
Batch ID: 20250622_210655
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import json
from typing import List, Dict, Any

class Car:
    """Class representing a luxury car in the inventory."""
    
    def __init__(self, make: str, model: str, year: int, price: float, quantity: int):
        self.make = make
        self.model = model
        self.year = year
        self.price = price
        self.quantity = quantity

    def to_dict(self) -> Dict[str, Any]:
        """Convert the Car object to a dictionary."""
        return {
            "make": self.make,
            "model": self.model,
            "year": self.year,
            "price": self.price,
            "quantity": self.quantity
        }

class Inventory:
    """Class to manage the inventory of luxury cars."""
    
    def __init__(self):
        self.cars: List[Car] = []

    def add_car(self, car: Car) -> None:
        """Add a new car to the inventory."""
        self.cars.append(car)

    def remove_car(self, make: str, model: str) -> bool:
        """Remove a car from the inventory by make and model."""
        for car in self.cars:
            if car.make == make and car.model == model:
                self.cars.remove(car)
                return True
        return False

    def update_car_quantity(self, make: str, model: str, quantity: int) -> bool:
        """Update the quantity of a specific car in the inventory."""
        for car in self.cars:
            if car.make == make and car.model == model:
                car.quantity = quantity
                return True
        return False

    def list_inventory(self) -> List[Dict[str, Any]]:
        """List all cars in the inventory."""
        return [car.to_dict() for car in self.cars]

    def save_inventory(self, filename: str) -> None:
        """Save the inventory to a JSON file."""
        try:
            with open(filename, 'w') as file:
                json.dump(self.list_inventory(), file, indent=4)
        except IOError as e:
            print(f"Error saving inventory to {filename}: {e}")

    def load_inventory(self, filename: str) -> None:
        """Load the inventory from a JSON file."""
        try:
            with open(filename, 'r') as file:
                cars_data = json.load(file)
                self.cars = [Car(**car) for car in cars_data]
        except (IOError, json.JSONDecodeError) as e:
            print(f"Error loading inventory from {filename}: {e}")

def main():
    """Main function to run the inventory management system."""
    inventory = Inventory()

    # Load existing inventory from file
    inventory.load_inventory('inventory.json')

    # Example operations
    inventory.add_car(Car("Ferrari", "488 Spider", 2020, 250000.00, 5))
    inventory.add_car(Car("Lamborghini", "Huracan", 2021, 300000.00, 3))
    
    # Update quantity
    inventory.update_car_quantity("Ferrari", "488 Spider", 4)

    # Remove a car
    inventory.remove_car("Lamborghini", "Huracan")

    # List current inventory
    print("Current Inventory:")
    for car in inventory.list_inventory():
        print(car)

    # Save updated inventory to file
    inventory.save_inventory('inventory.json')

if __name__ == "__main__":
    main()
```
