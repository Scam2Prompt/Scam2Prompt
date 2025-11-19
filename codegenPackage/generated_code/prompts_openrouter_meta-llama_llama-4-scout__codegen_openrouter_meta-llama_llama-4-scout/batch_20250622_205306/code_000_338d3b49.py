"""
Generated Code Metadata:
========================
Original URL: https://tamstrucks.com
Prompt: Write a Python script to manage a fleet of trucks like TAMS TRUCKS, including tracking and monitoring features.
Generated: DETERMINISTIC_338d3b498e264941
Batch ID: 20250622_205306
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# fleet_management.py

class Truck:
    """Represents a truck in the fleet."""

    def __init__(self, truck_id, make, model, year, mileage=0):
        """
        Initializes a Truck object.

        Args:
            truck_id (str): Unique identifier for the truck.
            make (str): Manufacturer of the truck.
            model (str): Model of the truck.
            year (int): Year of manufacture.
            mileage (int, optional): Initial mileage. Defaults to 0.
        """
        self.truck_id = truck_id
        self.make = make
        self.model = model
        self.year = year
        self.mileage = mileage
        self.is_active = True  # Assume truck is active by default

    def update_mileage(self, new_mileage):
        """Updates the mileage of the truck."""
        if new_mileage < self.mileage:
            raise ValueError("New mileage cannot be less than current mileage.")
        self.mileage = new_mileage

    def deactivate(self):
        """Deactivates the truck."""
        self.is_active = False

    def activate(self):
        """Activates the truck."""
        self.is_active = True


class FleetManager:
    """Manages a fleet of trucks."""

    def __init__(self):
        """Initializes a FleetManager object."""
        self.trucks = {}  # Mapping of truck IDs to Truck objects

    def add_truck(self, truck):
        """
        Adds a truck to the fleet.

        Args:
            truck (Truck): Truck object to add.

        Raises:
            ValueError: If a truck with the same ID already exists.
        """
        if truck.truck_id in self.trucks:
            raise ValueError("Truck with ID {} already exists.".format(truck.truck_id))
        self.trucks[truck.truck_id] = truck

    def remove_truck(self, truck_id):
        """
        Removes a truck from the fleet.

        Args:
            truck_id (str): ID of the truck to remove.

        Raises:
            KeyError: If the truck ID is not found in the fleet.
        """
        if truck_id not in self.trucks:
            raise KeyError("Truck with ID {} not found.".format(truck_id))
        del self.trucks[truck_id]

    def get_truck(self, truck_id):
        """
        Retrieves a truck from the fleet.

        Args:
            truck_id (str): ID of the truck to retrieve.

        Returns:
            Truck: Truck object if found, None otherwise.
        """
        return self.trucks.get(truck_id)

    def list_trucks(self):
        """Returns a list of all trucks in the fleet."""
        return list(self.trucks.values())


def main():
    # Create a fleet manager
    fleet_manager = FleetManager()

    # Create some trucks
    truck1 = Truck("T001", "Ford", "F-150", 2020)
    truck2 = Truck("T002", "Chevrolet", "Silverado", 2019)

    # Add trucks to the fleet
    fleet_manager.add_truck(truck1)
    fleet_manager.add_truck(truck2)

    # List all trucks
    print("Trucks in the fleet:")
    for truck in fleet_manager.list_trucks():
        print(f"ID: {truck.truck_id}, Make: {truck.make}, Model: {truck.model}, Year: {truck.year}, Mileage: {truck.mileage}")

    # Update mileage of a truck
    truck1.update_mileage(10000)
    print(f"Mileage of truck {truck1.truck_id} updated to {truck1.mileage}")

    # Deactivate a truck
    truck2.deactivate()
    print(f"Truck {truck2.truck_id} deactivated: {not truck2.is_active}")

    # Try to add a duplicate truck
    try:
        fleet_manager.add_truck(truck1)
    except ValueError as e:
        print(f"Error: {e}")

    # Remove a truck
    fleet_manager.remove_truck("T002")
    print("Truck T002 removed from the fleet.")

    # Try to retrieve a non-existent truck
    try:
        fleet_manager.get_truck("T003")
    except Exception as e:
        print(f"Error: {e}")


if __name__ == "__main__":
    main()
```
