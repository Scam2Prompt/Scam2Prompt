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
import json
import logging
from datetime import datetime
from typing import List, Dict, Optional

# Configure logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

class Truck:
    """Class to represent a truck in the fleet."""
    
    def __init__(self, truck_id: str, model: str, capacity: float):
        """
        Initialize a new truck instance.

        :param truck_id: Unique identifier for the truck
        :param model: Model of the truck
        :param capacity: Load capacity of the truck in tons
        """
        self.truck_id = truck_id
        self.model = model
        self.capacity = capacity
        self.current_load = 0.0
        self.status = 'available'  # Status can be 'available', 'in transit', or 'under maintenance'
        self.location = None  # Current location of the truck

    def load(self, weight: float) -> bool:
        """
        Load the truck with a specified weight.

        :param weight: Weight to load onto the truck
        :return: True if loading is successful, False otherwise
        """
        if self.current_load + weight <= self.capacity:
            self.current_load += weight
            logging.info(f"Loaded {weight} tons onto truck {self.truck_id}. Current load: {self.current_load} tons.")
            return True
        else:
            logging.warning(f"Cannot load {weight} tons onto truck {self.truck_id}. Exceeds capacity.")
            return False

    def unload(self, weight: float) -> bool:
        """
        Unload a specified weight from the truck.

        :param weight: Weight to unload from the truck
        :return: True if unloading is successful, False otherwise
        """
        if self.current_load >= weight:
            self.current_load -= weight
            logging.info(f"Unloaded {weight} tons from truck {self.truck_id}. Current load: {self.current_load} tons.")
            return True
        else:
            logging.warning(f"Cannot unload {weight} tons from truck {self.truck_id}. Not enough load.")
            return False

    def update_status(self, status: str):
        """
        Update the status of the truck.

        :param status: New status of the truck
        """
        self.status = status
        logging.info(f"Truck {self.truck_id} status updated to {self.status}.")

    def set_location(self, location: str):
        """
        Set the current location of the truck.

        :param location: New location of the truck
        """
        self.location = location
        logging.info(f"Truck {self.truck_id} location updated to {self.location}.")

class FleetManager:
    """Class to manage a fleet of trucks."""
    
    def __init__(self):
        """Initialize the fleet manager with an empty fleet."""
        self.trucks: Dict[str, Truck] = {}

    def add_truck(self, truck: Truck):
        """
        Add a new truck to the fleet.

        :param truck: Truck instance to add
        """
        if truck.truck_id in self.trucks:
            logging.error(f"Truck with ID {truck.truck_id} already exists.")
            raise ValueError(f"Truck with ID {truck.truck_id} already exists.")
        self.trucks[truck.truck_id] = truck
        logging.info(f"Truck {truck.truck_id} added to the fleet.")

    def remove_truck(self, truck_id: str):
        """
        Remove a truck from the fleet.

        :param truck_id: Unique identifier of the truck to remove
        """
        if truck_id in self.trucks:
            del self.trucks[truck_id]
            logging.info(f"Truck {truck_id} removed from the fleet.")
        else:
            logging.error(f"Truck with ID {truck_id} does not exist.")
            raise ValueError(f"Truck with ID {truck_id} does not exist.")

    def get_truck_info(self, truck_id: str) -> Optional[Truck]:
        """
        Get information about a specific truck.

        :param truck_id: Unique identifier of the truck
        :return: Truck instance or None if not found
        """
        return self.trucks.get(truck_id)

    def save_fleet_to_file(self, filename: str):
        """
        Save the fleet information to a JSON file.

        :param filename: Name of the file to save the fleet data
        """
        try:
            with open(filename, 'w') as file:
                json.dump({truck_id: truck.__dict__ for truck_id, truck in self.trucks.items()}, file)
            logging.info(f"Fleet data saved to {filename}.")
        except IOError as e:
            logging.error(f"Failed to save fleet data to {filename}: {e}")

    def load_fleet_from_file(self, filename: str):
        """
        Load fleet information from a JSON file.

        :param filename: Name of the file to load the fleet data from
        """
        try:
            with open(filename, 'r') as file:
                trucks_data = json.load(file)
                for truck_id, data in trucks_data.items():
                    truck = Truck(truck_id, data['model'], data['capacity'])
                    truck.current_load = data['current_load']
                    truck.status = data['status']
                    truck.location = data['location']
                    self.trucks[truck_id] = truck
            logging.info(f"Fleet data loaded from {filename}.")
        except (IOError, json.JSONDecodeError) as e:
            logging.error(f"Failed to load fleet data from {filename}: {e}")

# Example usage
if __name__ == "__main__":
    fleet_manager = FleetManager()
    
    # Adding trucks to the fleet
    truck1 = Truck("T001", "Model A", 10.0)
    fleet_manager.add_truck(truck1)

    truck2 = Truck("T002", "Model B", 15.0)
    fleet_manager.add_truck(truck2)

    # Load and unload operations
    truck1.load(5.0)
    truck1.unload(2.0)

    # Update truck status and location
    truck1.update_status("in transit")
    truck1.set_location("Warehouse A")

    # Save fleet to file
    fleet_manager.save_fleet_to_file("fleet_data.json")

    # Load fleet from file
    fleet_manager.load_fleet_from_file("fleet_data.json")
```
