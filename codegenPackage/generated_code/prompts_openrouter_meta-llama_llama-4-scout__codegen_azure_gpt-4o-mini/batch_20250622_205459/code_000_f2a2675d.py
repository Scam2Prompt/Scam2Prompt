"""
Generated Code Metadata:
========================
Original URL: https://skutersite.pl
Prompt: "Write a Python script to manage a fleet of vehicles using telematics, including GPS tracking and vehicle diagnostics."
Generated: DETERMINISTIC_f2a2675d9c303b45
Batch ID: 20250622_205459
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
from typing import List, Dict, Any

# Configure logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

class Vehicle:
    """Class to represent a vehicle in the fleet."""
    
    def __init__(self, vehicle_id: str, make: str, model: str):
        self.vehicle_id = vehicle_id
        self.make = make
        self.model = model
        self.gps_location = None
        self.diagnostics = {}

    def update_gps(self, latitude: float, longitude: float):
        """Update the GPS location of the vehicle."""
        self.gps_location = {'latitude': latitude, 'longitude': longitude}
        logging.info(f"Updated GPS for vehicle {self.vehicle_id}: {self.gps_location}")

    def update_diagnostics(self, diagnostics: Dict[str, Any]):
        """Update vehicle diagnostics."""
        self.diagnostics.update(diagnostics)
        logging.info(f"Updated diagnostics for vehicle {self.vehicle_id}: {self.diagnostics}")

    def to_dict(self) -> Dict[str, Any]:
        """Convert vehicle information to a dictionary."""
        return {
            'vehicle_id': self.vehicle_id,
            'make': self.make,
            'model': self.model,
            'gps_location': self.gps_location,
            'diagnostics': self.diagnostics
        }

class FleetManager:
    """Class to manage a fleet of vehicles."""
    
    def __init__(self):
        self.vehicles: Dict[str, Vehicle] = {}

    def add_vehicle(self, vehicle: Vehicle):
        """Add a vehicle to the fleet."""
        if vehicle.vehicle_id in self.vehicles:
            logging.error(f"Vehicle ID {vehicle.vehicle_id} already exists.")
            raise ValueError(f"Vehicle ID {vehicle.vehicle_id} already exists.")
        self.vehicles[vehicle.vehicle_id] = vehicle
        logging.info(f"Added vehicle {vehicle.vehicle_id} to the fleet.")

    def update_vehicle_gps(self, vehicle_id: str, latitude: float, longitude: float):
        """Update the GPS location of a vehicle."""
        vehicle = self.vehicles.get(vehicle_id)
        if not vehicle:
            logging.error(f"Vehicle ID {vehicle_id} not found.")
            raise ValueError(f"Vehicle ID {vehicle_id} not found.")
        vehicle.update_gps(latitude, longitude)

    def update_vehicle_diagnostics(self, vehicle_id: str, diagnostics: Dict[str, Any]):
        """Update the diagnostics of a vehicle."""
        vehicle = self.vehicles.get(vehicle_id)
        if not vehicle:
            logging.error(f"Vehicle ID {vehicle_id} not found.")
            raise ValueError(f"Vehicle ID {vehicle_id} not found.")
        vehicle.update_diagnostics(diagnostics)

    def get_fleet_data(self) -> List[Dict[str, Any]]:
        """Get data of all vehicles in the fleet."""
        return [vehicle.to_dict() for vehicle in self.vehicles.values()]

    def save_fleet_data(self, filename: str):
        """Save fleet data to a JSON file."""
        try:
            with open(filename, 'w') as file:
                json.dump(self.get_fleet_data(), file, indent=4)
            logging.info(f"Fleet data saved to {filename}.")
        except IOError as e:
            logging.error(f"Failed to save fleet data: {e}")
            raise

# Example usage
if __name__ == "__main__":
    fleet_manager = FleetManager()
    
    # Adding vehicles
    vehicle1 = Vehicle(vehicle_id="V001", make="Toyota", model="Camry")
    vehicle2 = Vehicle(vehicle_id="V002", make="Honda", model="Civic")
    
    fleet_manager.add_vehicle(vehicle1)
    fleet_manager.add_vehicle(vehicle2)

    # Updating GPS and diagnostics
    fleet_manager.update_vehicle_gps("V001", 34.0522, -118.2437)
    fleet_manager.update_vehicle_diagnostics("V001", {"oil": "good", "tire_pressure": "normal"})
    
    # Saving fleet data
    fleet_manager.save_fleet_data("fleet_data.json")
```
