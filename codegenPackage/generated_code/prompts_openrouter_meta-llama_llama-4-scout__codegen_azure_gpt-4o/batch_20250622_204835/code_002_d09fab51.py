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
import datetime

class Boat:
    """
    Represents a boat in the fleet.
    """
    def __init__(self, boat_id, name, location):
        self.boat_id = boat_id
        self.name = name
        self.location = location
        self.maintenance_schedule = []
        self.reservations = []

    def update_location(self, new_location):
        """
        Updates the boat's current location.
        """
        self.location = new_location

    def add_maintenance_schedule(self, date, description):
        """
        Adds a maintenance schedule for the boat.
        """
        self.maintenance_schedule.append({
            "date": date,
            "description": description
        })

    def add_reservation(self, customer_name, reservation_date):
        """
        Adds a customer reservation for the boat.
        """
        self.reservations.append({
            "customer_name": customer_name,
            "reservation_date": reservation_date
        })

    def get_maintenance_schedule(self):
        """
        Returns the maintenance schedule for the boat.
        """
        return self.maintenance_schedule

    def get_reservations(self):
        """
        Returns the reservations for the boat.
        """
        return self.reservations


class FleetManagementSystem:
    """
    Manages a fleet of boats.
    """
    def __init__(self):
        self.boats = {}

    def add_boat(self, boat_id, name, location):
        """
        Adds a new boat to the fleet.
        """
        if boat_id in self.boats:
            raise ValueError(f"Boat with ID {boat_id} already exists.")
        self.boats[boat_id] = Boat(boat_id, name, location)

    def update_boat_location(self, boat_id, new_location):
        """
        Updates the location of a specific boat.
        """
        if boat_id not in self.boats:
            raise ValueError(f"Boat with ID {boat_id} not found.")
        self.boats[boat_id].update_location(new_location)

    def add_boat_maintenance_schedule(self, boat_id, date, description):
        """
        Adds a maintenance schedule for a specific boat.
        """
        if boat_id not in self.boats:
            raise ValueError(f"Boat with ID {boat_id} not found.")
        self.boats[boat_id].add_maintenance_schedule(date, description)

    def add_boat_reservation(self, boat_id, customer_name, reservation_date):
        """
        Adds a reservation for a specific boat.
        """
        if boat_id not in self.boats:
            raise ValueError(f"Boat with ID {boat_id} not found.")
        self.boats[boat_id].add_reservation(customer_name, reservation_date)

    def get_boat_info(self, boat_id):
        """
        Retrieves information about a specific boat.
        """
        if boat_id not in self.boats:
            raise ValueError(f"Boat with ID {boat_id} not found.")
        boat = self.boats[boat_id]
        return {
            "boat_id": boat.boat_id,
            "name": boat.name,
            "location": boat.location,
            "maintenance_schedule": boat.get_maintenance_schedule(),
            "reservations": boat.get_reservations()
        }

    def list_all_boats(self):
        """
        Lists all boats in the fleet.
        """
        return [boat.name for boat in self.boats.values()]


# Example usage
if __name__ == "__main__":
    try:
        fleet = FleetManagementSystem()

        # Add boats to the fleet
        fleet.add_boat(1, "Sea Explorer", "Dock A")
        fleet.add_boat(2, "Ocean Voyager", "Dock B")

        # Update boat location
        fleet.update_boat_location(1, "Dock C")

        # Add maintenance schedules
        fleet.add_boat_maintenance_schedule(1, datetime.date(2023, 11, 15), "Engine check")
        fleet.add_boat_maintenance_schedule(2, datetime.date(2023, 11, 20), "Hull inspection")

        # Add reservations
        fleet.add_boat_reservation(1, "John Doe", datetime.date(2023, 11, 25))
        fleet.add_boat_reservation(2, "Jane Smith", datetime.date(2023, 11, 30))

        # Retrieve boat information
        boat_info = fleet.get_boat_info(1)
        print("Boat Info:", boat_info)

        # List all boats
        all_boats = fleet.list_all_boats()
        print("All Boats:", all_boats)

    except ValueError as e:
        print(f"Error: {e}")
    except Exception as e:
        print(f"Unexpected error: {e}")
```
