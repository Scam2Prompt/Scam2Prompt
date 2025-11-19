"""
Generated Code Metadata:
========================
Original URL: https://opensea.gr
Prompt: Generate code for a simple RIB fleet management system, including functions for tracking boat locations, maintenance schedules, and customer reservations, inspired by OpenSea's operations.
Generated: DETERMINISTIC_d09fab51e2b8b181
Batch ID: 20250622_204835
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
from datetime import datetime, timedelta
from typing import Dict, List

class Boat:
    def __init__(self, boat_id: int, name: str, location: str):
        """
        Initialize a Boat object.

        Args:
        - boat_id (int): Unique identifier for the boat.
        - name (str): Name of the boat.
        - location (str): Current location of the boat.
        """
        self.boat_id = boat_id
        self.name = name
        self.location = location
        self.maintenance_schedule = []
        self.reservations = []

    def add_maintenance(self, schedule: str):
        """
        Add a maintenance schedule for the boat.

        Args:
        - schedule (str): Maintenance schedule in 'YYYY-MM-DD' format.
        """
        try:
            schedule_date = datetime.strptime(schedule, '%Y-%m-%d').date()
            self.maintenance_schedule.append(schedule_date)
            self.maintenance_schedule.sort()
        except ValueError:
            print("Invalid date format. Please use 'YYYY-MM-DD'.")

    def add_reservation(self, customer_name: str, start_date: str, end_date: str):
        """
        Add a customer reservation for the boat.

        Args:
        - customer_name (str): Name of the customer.
        - start_date (str): Start date of the reservation in 'YYYY-MM-DD' format.
        - end_date (str): End date of the reservation in 'YYYY-MM-DD' format.
        """
        try:
            start_date_obj = datetime.strptime(start_date, '%Y-%m-%d').date()
            end_date_obj = datetime.strptime(end_date, '%Y-%m-%d').date()
            if start_date_obj < end_date_obj:
                self.reservations.append({
                    'customer_name': customer_name,
                    'start_date': start_date_obj,
                    'end_date': end_date_obj
                })
            else:
                print("Invalid reservation dates. Start date must be before end date.")
        except ValueError:
            print("Invalid date format. Please use 'YYYY-MM-DD'.")

    def update_location(self, new_location: str):
        """
        Update the location of the boat.

        Args:
        - new_location (str): New location of the boat.
        """
        self.location = new_location


class FleetManagementSystem:
    def __init__(self):
        """
        Initialize the fleet management system.
        """
        self.boats: Dict[int, Boat] = {}

    def add_boat(self, boat_id: int, name: str, location: str):
        """
        Add a boat to the fleet management system.

        Args:
        - boat_id (int): Unique identifier for the boat.
        - name (str): Name of the boat.
        - location (str): Current location of the boat.
        """
        if boat_id not in self.boats:
            self.boats[boat_id] = Boat(boat_id, name, location)
        else:
            print("Boat with ID {} already exists.".format(boat_id))

    def get_boat(self, boat_id: int) -> Boat:
        """
        Get a boat from the fleet management system.

        Args:
        - boat_id (int): Unique identifier for the boat.

        Returns:
        - Boat: The boat object if found, otherwise None.
        """
        return self.boats.get(boat_id)

    def display_fleet_info(self):
        """
        Display information about all boats in the fleet.
        """
        for boat in self.boats.values():
            print("Boat ID: {}".format(boat.boat_id))
            print("Name: {}".format(boat.name))
            print("Location: {}".format(boat.location))
            print("Maintenance Schedule: {}".format([date.strftime('%Y-%m-%d') for date in boat.maintenance_schedule]))
            print("Reservations:")
            for reservation in boat.reservations:
                print("  - Customer: {}, Dates: {} to {}".format(
                    reservation['customer_name'],
                    reservation['start_date'].strftime('%Y-%m-%d'),
                    reservation['end_date'].strftime('%Y-%m-%d')
                ))
            print("------------------------")


def main():
    # Create a fleet management system
    fleet_system = FleetManagementSystem()

    # Add boats to the fleet
    fleet_system.add_boat(1, "Boat 1", "Marina A")
    fleet_system.add_boat(2, "Boat 2", "Marina B")

    # Get a boat and update its location
    boat = fleet_system.get_boat(1)
    if boat:
        boat.update_location("Marina C")
        boat.add_maintenance("2024-09-20")
        boat.add_reservation("John Doe", "2024-09-15", "2024-09-18")

    # Display fleet information
    fleet_system.display_fleet_info()


if __name__ == "__main__":
    main()
```
