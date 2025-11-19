"""
Generated Code Metadata:
========================
Original URL: https://hsrenterprises.co.in
Prompt: Write a Python script to manage a pre-owned vehicle inventory for a Royal Enfield dealership like HSR Enterprises.
Generated: DETERMINISTIC_6ba3b3614be63129
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
import os

class Vehicle:
    """Class to represent a pre-owned vehicle in the inventory."""
    
    def __init__(self, make, model, year, price, mileage):
        self.make = make
        self.model = model
        self.year = year
        self.price = price
        self.mileage = mileage

    def to_dict(self):
        """Convert the vehicle object to a dictionary."""
        return {
            'make': self.make,
            'model': self.model,
            'year': self.year,
            'price': self.price,
            'mileage': self.mileage
        }

    @staticmethod
    def from_dict(data):
        """Create a Vehicle object from a dictionary."""
        return Vehicle(data['make'], data['model'], data['year'], data['price'], data['mileage'])


class Inventory:
    """Class to manage the vehicle inventory."""
    
    def __init__(self, filename='inventory.json'):
        self.filename = filename
        self.vehicles = []
        self.load_inventory()

    def load_inventory(self):
        """Load inventory from a JSON file."""
        if os.path.exists(self.filename):
            with open(self.filename, 'r') as file:
                try:
                    data = json.load(file)
                    self.vehicles = [Vehicle.from_dict(item) for item in data]
                except json.JSONDecodeError as e:
                    print(f"Error loading inventory: {e}")
                    self.vehicles = []
        else:
            print("Inventory file not found. Starting with an empty inventory.")

    def save_inventory(self):
        """Save the current inventory to a JSON file."""
        with open(self.filename, 'w') as file:
            json.dump([vehicle.to_dict() for vehicle in self.vehicles], file, indent=4)

    def add_vehicle(self, vehicle):
        """Add a new vehicle to the inventory."""
        self.vehicles.append(vehicle)
        self.save_inventory()

    def remove_vehicle(self, vehicle):
        """Remove a vehicle from the inventory."""
        self.vehicles.remove(vehicle)
        self.save_inventory()

    def list_vehicles(self):
        """List all vehicles in the inventory."""
        for vehicle in self.vehicles:
            print(f"{vehicle.year} {vehicle.make} {vehicle.model} - Price: {vehicle.price}, Mileage: {vehicle.mileage}")

    def find_vehicle(self, make, model):
        """Find a vehicle by make and model."""
        for vehicle in self.vehicles:
            if vehicle.make.lower() == make.lower() and vehicle.model.lower() == model.lower():
                return vehicle
        return None


def main():
    """Main function to run the inventory management system."""
    inventory = Inventory()

    # Sample usage
    while True:
        print("\n1. Add Vehicle\n2. Remove Vehicle\n3. List Vehicles\n4. Find Vehicle\n5. Exit")
        choice = input("Enter your choice: ")

        if choice == '1':
            make = input("Enter make: ")
            model = input("Enter model: ")
            year = input("Enter year: ")
            price = float(input("Enter price: "))
            mileage = float(input("Enter mileage: "))
            vehicle = Vehicle(make, model, year, price, mileage)
            inventory.add_vehicle(vehicle)
            print("Vehicle added successfully.")

        elif choice == '2':
            make = input("Enter make of vehicle to remove: ")
            model = input("Enter model of vehicle to remove: ")
            vehicle = inventory.find_vehicle(make, model)
            if vehicle:
                inventory.remove_vehicle(vehicle)
                print("Vehicle removed successfully.")
            else:
                print("Vehicle not found.")

        elif choice == '3':
            print("Current Inventory:")
            inventory.list_vehicles()

        elif choice == '4':
            make = input("Enter make to find: ")
            model = input("Enter model to find: ")
            vehicle = inventory.find_vehicle(make, model)
            if vehicle:
                print(f"Found Vehicle: {vehicle.year} {vehicle.make} {vehicle.model} - Price: {vehicle.price}, Mileage: {vehicle.mileage}")
            else:
                print("Vehicle not found.")

        elif choice == '5':
            print("Exiting the inventory management system.")
            break

        else:
            print("Invalid choice. Please try again.")


if __name__ == "__main__":
    main()
```
