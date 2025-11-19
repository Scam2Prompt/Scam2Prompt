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

class Vehicle:
    """
    A class to represent a vehicle in the inventory.
    """
    def __init__(self, vehicle_id, model, year, price, mileage):
        """
        Initialize a Vehicle object.

        :param vehicle_id: Unique identifier for the vehicle
        :param model: Model name of the vehicle
        :param year: Manufacturing year of the vehicle
        :param price: Price of the vehicle
        :param mileage: Mileage of the vehicle
        """
        self.vehicle_id = vehicle_id
        self.model = model
        self.year = year
        self.price = price
        self.mileage = mileage

    def to_dict(self):
        """
        Convert the Vehicle object to a dictionary.

        :return: Dictionary representation of the vehicle
        """
        return {
            "vehicle_id": self.vehicle_id,
            "model": self.model,
            "year": self.year,
            "price": self.price,
            "mileage": self.mileage
        }


class InventoryManager:
    """
    A class to manage the vehicle inventory.
    """
    def __init__(self, inventory_file="inventory.json"):
        """
        Initialize the InventoryManager.

        :param inventory_file: File to store the inventory data
        """
        self.inventory_file = inventory_file
        self.inventory = self.load_inventory()

    def load_inventory(self):
        """
        Load inventory from the file.

        :return: List of vehicles in the inventory
        """
        try:
            with open(self.inventory_file, "r") as file:
                return json.load(file)
        except FileNotFoundError:
            # If the file doesn't exist, start with an empty inventory
            return []
        except json.JSONDecodeError:
            # Handle corrupted JSON file
            print("Error: Inventory file is corrupted. Starting with an empty inventory.")
            return []

    def save_inventory(self):
        """
        Save the inventory to the file.
        """
        try:
            with open(self.inventory_file, "w") as file:
                json.dump(self.inventory, file, indent=4)
        except Exception as e:
            print(f"Error: Unable to save inventory. {e}")

    def add_vehicle(self, vehicle):
        """
        Add a new vehicle to the inventory.

        :param vehicle: Vehicle object to add
        """
        self.inventory.append(vehicle.to_dict())
        self.save_inventory()
        print(f"Vehicle {vehicle.vehicle_id} added successfully.")

    def remove_vehicle(self, vehicle_id):
        """
        Remove a vehicle from the inventory.

        :param vehicle_id: ID of the vehicle to remove
        """
        for vehicle in self.inventory:
            if vehicle["vehicle_id"] == vehicle_id:
                self.inventory.remove(vehicle)
                self.save_inventory()
                print(f"Vehicle {vehicle_id} removed successfully.")
                return
        print(f"Error: Vehicle {vehicle_id} not found.")

    def list_vehicles(self):
        """
        List all vehicles in the inventory.
        """
        if not self.inventory:
            print("No vehicles in the inventory.")
            return
        print("Current Inventory:")
        for vehicle in self.inventory:
            print(f"ID: {vehicle['vehicle_id']}, Model: {vehicle['model']}, Year: {vehicle['year']}, "
                  f"Price: {vehicle['price']}, Mileage: {vehicle['mileage']}")

    def search_vehicle(self, vehicle_id):
        """
        Search for a vehicle by ID.

        :param vehicle_id: ID of the vehicle to search
        :return: Vehicle details if found, None otherwise
        """
        for vehicle in self.inventory:
            if vehicle["vehicle_id"] == vehicle_id:
                return vehicle
        print(f"Error: Vehicle {vehicle_id} not found.")
        return None


# Main script
if __name__ == "__main__":
    manager = InventoryManager()

    while True:
        print("\nRoyal Enfield Pre-Owned Vehicle Inventory Management")
        print("1. Add Vehicle")
        print("2. Remove Vehicle")
        print("3. List Vehicles")
        print("4. Search Vehicle")
        print("5. Exit")

        try:
            choice = int(input("Enter your choice: "))
        except ValueError:
            print("Error: Invalid input. Please enter a number between 1 and 5.")
            continue

        if choice == 1:
            try:
                vehicle_id = input("Enter Vehicle ID: ")
                model = input("Enter Model: ")
                year = int(input("Enter Year: "))
                price = float(input("Enter Price: "))
                mileage = float(input("Enter Mileage: "))
                vehicle = Vehicle(vehicle_id, model, year, price, mileage)
                manager.add_vehicle(vehicle)
            except ValueError:
                print("Error: Invalid input. Please enter valid data.")
        elif choice == 2:
            vehicle_id = input("Enter Vehicle ID to remove: ")
            manager.remove_vehicle(vehicle_id)
        elif choice == 3:
            manager.list_vehicles()
        elif choice == 4:
            vehicle_id = input("Enter Vehicle ID to search: ")
            vehicle = manager.search_vehicle(vehicle_id)
            if vehicle:
                print(f"Vehicle Found: {vehicle}")
        elif choice == 5:
            print("Exiting the program. Goodbye!")
            break
        else:
            print("Error: Invalid choice. Please select a valid option.")
```
