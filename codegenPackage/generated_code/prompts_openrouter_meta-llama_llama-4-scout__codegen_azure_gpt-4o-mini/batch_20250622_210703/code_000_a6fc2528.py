"""
Generated Code Metadata:
========================
Original URL: https://refrigeratortransport.com
Prompt: Write a Python script to manage a fleet of refrigerated vehicles, including chiller vans and freezer trucks, with GPS tracking and temperature monitoring for deliveries in Dubai.
Generated: DETERMINISTIC_a6fc25285384c5d4
Batch ID: 20250622_210703
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
from typing import List, Dict, Any

# Configure logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

class Vehicle:
    """Class to represent a refrigerated vehicle."""
    
    def __init__(self, vehicle_id: str, vehicle_type: str, gps_location: Dict[str, float], temperature: float):
        self.vehicle_id = vehicle_id
        self.vehicle_type = vehicle_type
        self.gps_location = gps_location  # {'latitude': float, 'longitude': float}
        self.temperature = temperature  # in Celsius
        self.status = "available"  # Status can be 'available', 'in transit', 'maintenance'

    def update_location(self, latitude: float, longitude: float):
        """Update the GPS location of the vehicle."""
        self.gps_location = {'latitude': latitude, 'longitude': longitude}
        logging.info(f"Updated location for vehicle {self.vehicle_id}: {self.gps_location}")

    def update_temperature(self, temperature: float):
        """Update the temperature of the vehicle."""
        self.temperature = temperature
        logging.info(f"Updated temperature for vehicle {self.vehicle_id}: {self.temperature}°C")

    def set_status(self, status: str):
        """Set the status of the vehicle."""
        if status in ['available', 'in transit', 'maintenance']:
            self.status = status
            logging.info(f"Status for vehicle {self.vehicle_id} set to: {self.status}")
        else:
            logging.error(f"Invalid status '{status}' for vehicle {self.vehicle_id}")

class FleetManager:
    """Class to manage a fleet of refrigerated vehicles."""
    
    def __init__(self):
        self.vehicles: List[Vehicle] = []

    def add_vehicle(self, vehicle: Vehicle):
        """Add a new vehicle to the fleet."""
        self.vehicles.append(vehicle)
        logging.info(f"Added vehicle {vehicle.vehicle_id} to the fleet.")

    def find_vehicle(self, vehicle_id: str) -> Vehicle:
        """Find a vehicle by its ID."""
        for vehicle in self.vehicles:
            if vehicle.vehicle_id == vehicle_id:
                return vehicle
        logging.error(f"Vehicle {vehicle_id} not found.")
        raise ValueError(f"Vehicle {vehicle_id} not found.")

    def get_fleet_status(self) -> List[Dict[str, Any]]:
        """Get the status of all vehicles in the fleet."""
        return [{'vehicle_id': v.vehicle_id, 'type': v.vehicle_type, 'location': v.gps_location, 
                 'temperature': v.temperature, 'status': v.status} for v in self.vehicles]

    def save_fleet_data(self, filename: str):
        """Save fleet data to a JSON file."""
        try:
            with open(filename, 'w') as f:
                json.dump(self.get_fleet_status(), f, indent=4)
            logging.info(f"Fleet data saved to {filename}.")
        except IOError as e:
            logging.error(f"Failed to save fleet data: {e}")

    def load_fleet_data(self, filename: str):
        """Load fleet data from a JSON file."""
        try:
            with open(filename, 'r') as f:
                vehicles_data = json.load(f)
                for vehicle_data in vehicles_data:
                    vehicle = Vehicle(vehicle_data['vehicle_id'], vehicle_data['type'], 
                                      vehicle_data['location'], vehicle_data['temperature'])
                    self.add_vehicle(vehicle)
            logging.info(f"Fleet data loaded from {filename}.")
        except (IOError, json.JSONDecodeError) as e:
            logging.error(f"Failed to load fleet data: {e}")

# Example usage
if __name__ == "__main__":
    fleet_manager = FleetManager()

    # Adding vehicles to the fleet
    fleet_manager.add_vehicle(Vehicle("V001", "chiller van", {'latitude': 25.276987, 'longitude': 55.296249}, 4.0))
    fleet_manager.add_vehicle(Vehicle("V002", "freezer truck", {'latitude': 25.276987, 'longitude': 55.296249}, -18.0))

    # Updating vehicle status and location
    vehicle = fleet_manager.find_vehicle("V001")
    vehicle.set_status("in transit")
    vehicle.update_location(25.276987, 55.296250)
    vehicle.update_temperature(3.5)

    # Saving fleet data
    fleet_manager.save_fleet_data("fleet_data.json")

    # Loading fleet data
    fleet_manager.load_fleet_data("fleet_data.json")

    # Print fleet status
    logging.info(f"Current fleet status: {fleet_manager.get_fleet_status()}")
```
