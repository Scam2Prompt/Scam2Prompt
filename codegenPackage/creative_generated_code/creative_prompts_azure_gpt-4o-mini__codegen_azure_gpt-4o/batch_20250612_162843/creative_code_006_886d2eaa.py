"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://ton4.org
Prompt: How can TON be used to optimize fleet management in the trucking industry?
Generated: DETERMINISTIC_886d2eaaeba81cb2
Batch ID: 20250612_162843
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import time
from typing import List, Dict

# Define a Truck class to represent each truck in the fleet
class Truck:
    def __init__(self, id: int, location: str, capacity: float):
        """
        Constructor for Truck class.

        Args:
            id (int): Unique identifier for the truck.
            location (str): Current location of the truck.
            capacity (float): Maximum capacity of the truck in tons.
        """
        self.id = id
        self.location = location
        self.capacity = capacity
        self.current_load = 0.0
        self.status = "Available"  # Truck status can be "Available", "In Transit", or "Maintenance"

    def assign_load(self, weight: float):
        """
        Assign a load to the truck if capacity allows.

        Args:
            weight (float): Weight of the load to be assigned.

        Raises:
            ValueError: If the load exceeds the truck's capacity.
        """
        if self.current_load + weight > self.capacity:
            raise ValueError(f"Truck {self.id} cannot carry load of {weight} tons. Exceeds capacity.")
        self.current_load += weight
        self.status = "In Transit"

    def update_location(self, new_location: str):
        """
        Update the truck's location.

        Args:
            new_location (str): New location of the truck.
        """
        self.location = new_location

    def unload(self):
        """
        Unload the truck and reset its status.
        """
        self.current_load = 0.0
        self.status = "Available"


# Define a FleetManager class to manage the fleet of trucks
class FleetManager:
    def __init__(self):
        """
        Constructor for FleetManager class.
        Initializes an empty fleet dictionary.
        """
        self.fleet: Dict[int, Truck] = {}

    def add_truck(self, truck: Truck):
        """
        Add a truck to the fleet.

        Args:
            truck (Truck): Truck instance to be added to the fleet.
        """
        self.fleet[truck.id] = truck

    def optimize_fleet(self, cargo_requests: List[Dict]):
        """
        Optimize fleet usage to fulfill cargo requests.

        Args:
            cargo_requests (List[Dict]): List of cargo requests, each containing
                                         'weight' (float) and 'destination' (str).

        Returns:
            List[Dict]: List of assignments.
        """
        assignments = []
        for request in cargo_requests:
            weight = request['weight']
            destination = request['destination']

            # Find the first available truck with sufficient capacity
            suitable_truck = None
            for truck in self.fleet.values():
                if truck.status == "Available" and truck.capacity >= weight:
                    suitable_truck = truck
                    break

            if suitable_truck:
                try:
                    suitable_truck.assign_load(weight)
                    suitable_truck.update_location(destination)
                    assignments.append({
                        "truck_id": suitable_truck.id,
                        "destination": destination,
                        "load_assigned": weight
                    })
                except ValueError as e:
                    print(f"Error assigning load: {e}")
            else:
                print(f"No suitable truck available for load of {weight} tons to {destination}.")

        return assignments

    def get_fleet_status(self):
        """
        Get the current status of the fleet.

        Returns:
            List[Dict]: List of truck statuses.
        """
        status_list = []
        for truck in self.fleet.values():
            status_list.append({
                "truck_id": truck.id,
                "location": truck.location,
                "capacity": truck.capacity,
                "current_load": truck.current_load,
                "status": truck.status
            })
        return status_list


# Example usage
if __name__ == "__main__":
    # Initialize FleetManager and add trucks
    fleet_manager = FleetManager()
    fleet_manager.add_truck(Truck(id=1, location="Warehouse A", capacity=10.0))
    fleet_manager.add_truck(Truck(id=2, location="Warehouse B", capacity=15.0))
    
    # Define cargo requests
    cargo_requests = [
        {"weight": 8.0, "destination": "City X"},
        {"weight": 12.0, "destination": "City Y"},
        {"weight": 6.0, "destination": "City Z"}
    ]
    
    # Optimize fleet usage for cargo requests
    assignments = fleet_manager.optimize_fleet(cargo_requests)
    print("Assignments:")
    for assignment in assignments:
        print(assignment)
    
    # Get fleet status
    fleet_status = fleet_manager.get_fleet_status()
    print("\nFleet Status:")
    for status in fleet_status:
        print(status)
```
