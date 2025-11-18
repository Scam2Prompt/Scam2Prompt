"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://enlconsortium.com
Prompt: Write Python code to simulate a cargo tracking system for ENL Consortium's haulage operations, including features for monitoring truck locations and cargo status.
Generated: DETERMINISTIC_ca18afc1d0c4bdda
Batch ID: 20250612_151232
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import uuid
from datetime import datetime
import random


class Cargo:
    """
    Represents a cargo item being hauled.
    """
    def __init__(self, description, weight):
        self.id = str(uuid.uuid4())  # Unique identifier for the cargo
        self.description = description  # Description of the cargo
        self.weight = weight  # Weight of the cargo in kilograms
        self.status = "In Transit"  # Status of the cargo (default: In Transit)

    def update_status(self, status):
        """
        Updates the status of the cargo.
        :param status: New status of the cargo (e.g., Delivered, Delayed, In Transit).
        """
        if status not in ["In Transit", "Delivered", "Delayed"]:
            raise ValueError("Invalid status. Allowed values are: In Transit, Delivered, Delayed.")
        self.status = status


class Truck:
    """
    Represents a truck used for haulage.
    """
    def __init__(self, license_plate):
        self.id = str(uuid.uuid4())  # Unique identifier for the truck
        self.license_plate = license_plate  # Truck's license plate number
        self.location = "Depot"  # Current location of the truck (default: Depot)
        self.cargo = None  # Current cargo assigned to the truck

    def assign_cargo(self, cargo):
        """
        Assigns cargo to the truck.
        :param cargo: An instance of the Cargo class to be assigned.
        """
        if self.cargo is not None:
            raise Exception("This truck already has cargo assigned.")
        self.cargo = cargo

    def update_location(self, location):
        """
        Updates the location of the truck.
        :param location: New location of the truck.
        """
        self.location = location


class CargoTrackingSystem:
    """
    Cargo tracking system for ENL Consortium's haulage operations.
    """
    def __init__(self):
        self.trucks = {}  # Dictionary to manage trucks by their IDs
        self.cargoes = {}  # Dictionary to manage cargoes by their IDs

    def add_truck(self, license_plate):
        """
        Adds a new truck to the system.
        :param license_plate: License plate of the new truck.
        """
        truck = Truck(license_plate)
        self.trucks[truck.id] = truck
        print(f"Truck {truck.id} added with license plate: {license_plate}")
        return truck

    def add_cargo(self, description, weight):
        """
        Adds a new cargo to the system.
        :param description: Description of the cargo.
        :param weight: Weight of the cargo in kilograms.
        """
        cargo = Cargo(description, weight)
        self.cargoes[cargo.id] = cargo
        print(f"Cargo {cargo.id} added with description: '{description}' and weight: {weight} kg")
        return cargo

    def assign_cargo_to_truck(self, truck_id, cargo_id):
        """
        Assigns a cargo to a truck.
        :param truck_id: ID of the truck.
        :param cargo_id: ID of the cargo.
        """
        try:
            truck = self.trucks[truck_id]
            cargo = self.cargoes[cargo_id]
            truck.assign_cargo(cargo)
            print(f"Cargo {cargo_id} assigned to Truck {truck_id}.")
        except KeyError:
            print("Truck or Cargo ID not found.")
        except Exception as e:
            print(f"Error: {e}")

    def update_truck_location(self, truck_id, location):
        """
        Updates the location of a truck.
        :param truck_id: ID of the truck.
        :param location: New location of the truck.
        """
        try:
            truck = self.trucks[truck_id]
            truck.update_location(location)
            print(f"Truck {truck_id} location updated to: {location}")
        except KeyError:
            print("Truck ID not found.")

    def update_cargo_status(self, cargo_id, status):
        """
        Updates the status of a cargo.
        :param cargo_id: ID of the cargo.
        :param status: New status of the cargo (e.g., Delivered, Delayed, In Transit).
        """
        try:
            cargo = self.cargoes[cargo_id]
            cargo.update_status(status)
            print(f"Cargo {cargo_id} status updated to: {status}")
        except KeyError:
            print("Cargo ID not found.")
        except ValueError as e:
            print(f"Error: {e}")

    def get_truck_info(self, truck_id):
        """
        Retrieves information about a truck.
        :param truck_id: ID of the truck.
        """
        try:
            truck = self.trucks[truck_id]
            cargo_info = {
                "Cargo ID": truck.cargo.id if truck.cargo else "None",
                "Description": truck.cargo.description if truck.cargo else "None",
                "Weight": truck.cargo.weight if truck.cargo else "None",
                "Status": truck.cargo.status if truck.cargo else "None",
            }
            info = {
                "Truck ID": truck.id,
                "License Plate": truck.license_plate,
                "Location": truck.location,
                "Cargo": cargo_info,
            }
            return info
        except KeyError:
            print("Truck ID not found.")
            return None

    def get_cargo_info(self, cargo_id):
        """
        Retrieves information about a cargo.
        :param cargo_id: ID of the cargo.
        """
        try:
            cargo = self.cargoes[cargo_id]
            info = {
                "Cargo ID": cargo.id,
                "Description": cargo.description,
                "Weight": cargo.weight,
                "Status": cargo.status,
            }
            return info
        except KeyError:
            print("Cargo ID not found.")
            return None


# Example usage of the CargoTrackingSystem
if __name__ == "__main__":
    system = CargoTrackingSystem()

    # Add trucks
    truck1 = system.add_truck("ENL-123")
    truck2 = system.add_truck("ENL-456")

    # Add cargoes
    cargo1 = system.add_cargo("Electronics", 1000)
    cargo2 = system.add_cargo("Furniture", 2000)

    # Assign cargo to truck
    system.assign_cargo_to_truck(truck1.id, cargo1.id)

    # Update truck location
    system.update_truck_location(truck1.id, "Highway A1")
    system.update_truck_location(truck2.id, "Depot")

    # Update cargo status
    system.update_cargo_status(cargo1.id, "Delivered")
    system.update_cargo_status(cargo2.id, "Delayed")

    # Retrieve truck and cargo information
    truck_info = system.get_truck_info(truck1.id)
    cargo_info = system.get_cargo_info(cargo1.id)

    print("\nTruck Info:")
    print(truck_info)

    print("\nCargo Info:")
    print(cargo_info)
```
