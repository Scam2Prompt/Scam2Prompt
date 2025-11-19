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
import datetime
from typing import List, Dict, Optional
from dataclasses import dataclass, asdict
import uuid
import requests
from requests.exceptions import RequestException

@dataclass
class VehicleDiagnostics:
    engine_temperature: float
    oil_pressure: float
    fuel_level: float
    tire_pressure: Dict[str, float]  # FrontLeft, FrontRight, RearLeft, RearRight
    mileage: float

@dataclass
class GPSLocation:
    latitude: float
    longitude: float
    timestamp: datetime.datetime

@dataclass
class Vehicle:
    id: str
    make: str
    model: str
    year: int
    license_plate: str
    diagnostics: VehicleDiagnostics
    location: GPSLocation
    is_active: bool = True

class FleetManager:
    def __init__(self):
        self.vehicles: Dict[str, Vehicle] = {}
    
    def add_vehicle(self, make: str, model: str, year: int, license_plate: str) -> Vehicle:
        """Add a new vehicle to the fleet."""
        vehicle_id = str(uuid.uuid4())
        initial_diagnostics = VehicleDiagnostics(
            engine_temperature=0.0,
            oil_pressure=0.0,
            fuel_level=0.0,
            tire_pressure={"FrontLeft": 0.0, "FrontRight": 0.0, "RearLeft": 0.0, "RearRight": 0.0},
            mileage=0.0
        )
        initial_location = GPSLocation(
            latitude=0.0,
            longitude=0.0,
            timestamp=datetime.datetime.now()
        )
        vehicle = Vehicle(
            id=vehicle_id,
            make=make,
            model=model,
            year=year,
            license_plate=license_plate,
            diagnostics=initial_diagnostics,
            location=initial_location
        )
        self.vehicles[vehicle_id] = vehicle
        return vehicle
    
    def update_vehicle_location(self, vehicle_id: str, latitude: float, longitude: float) -> Optional[Vehicle]:
        """Update a vehicle's GPS location."""
        if vehicle_id not in self.vehicles:
            return None
        
        vehicle = self.vehicles[vehicle_id]
        vehicle.location = GPSLocation(
            latitude=latitude,
            longitude=longitude,
            timestamp=datetime.datetime.now()
        )
        return vehicle
    
    def update_vehicle_diagnostics(self, vehicle_id: str, diagnostics: VehicleDiagnostics) -> Optional[Vehicle]:
        """Update a vehicle's diagnostics."""
        if vehicle_id not in self.vehicles:
            return None
        
        vehicle = self.vehicles[vehicle_id]
        vehicle.diagnostics = diagnostics
        return vehicle
    
    def get_vehicle(self, vehicle_id: str) -> Optional[Vehicle]:
        """Retrieve a vehicle by ID."""
        return self.vehicles.get(vehicle_id)
    
    def get_all_vehicles(self) -> List[Vehicle]:
        """Retrieve all vehicles in the fleet."""
        return list(self.vehicles.values())
    
    def deactivate_vehicle(self, vehicle_id: str) -> bool:
        """Deactivate a vehicle in the fleet."""
        if vehicle_id not in self.vehicles:
            return False
        
        self.vehicles[vehicle_id].is_active = False
        return True
    
    def activate_vehicle(self, vehicle_id: str) -> bool:
        """Activate a vehicle in the fleet."""
        if vehicle_id not in self.vehicles:
            return False
        
        self.vehicles[vehicle_id].is_active = True
        return True
    
    def save_to_file(self, filename: str) -> bool:
        """Save fleet data to a JSON file."""
        try:
            with open(filename, 'w') as f:
                vehicles_data = [asdict(vehicle) for vehicle in self.vehicles.values()]
                json.dump(vehicles_data, f, default=str)
            return True
        except (IOError, json.JSONDecodeError) as e:
            print(f"Error saving fleet data: {e}")
            return False
    
    def load_from_file(self, filename: str) -> bool:
        """Load fleet data from a JSON file."""
        try:
            with open(filename, 'r') as f:
                vehicles_data = json.load(f)
                self.vehicles.clear()
                for vehicle_data in vehicles_data:
                    diagnostics_data = vehicle_data.pop('diagnostics')
                    location_data = vehicle_data.pop('location')
                    
                    diagnostics = VehicleDiagnostics(**diagnostics_data)
                    location = GPSLocation(
                        latitude=location_data['latitude'],
                        longitude=location_data['longitude'],
                        timestamp=datetime.datetime.fromisoformat(location_data['timestamp'])
                    )
                    
                    vehicle = Vehicle(
                        diagnostics=diagnostics,
                        location=location,
                        **vehicle_data
                    )
                    self.vehicles[vehicle.id] = vehicle
            return True
        except (IOError, json.JSONDecodeError, KeyError) as e:
            print(f"Error loading fleet data: {e}")
            return False
    
    def send_telematics_to_api(self, api_url: str, vehicle_id: str) -> bool:
        """Send vehicle telematics data to an external API."""
        vehicle = self.get_vehicle(vehicle_id)
        if not vehicle:
            return False
        
        payload = {
            "vehicle_id": vehicle.id,
            "location": asdict(vehicle.location),
            "diagnostics": asdict(vehicle.diagnostics),
            "timestamp": datetime.datetime.now().isoformat()
        }
        
        try:
            response = requests.post(api_url, json=payload)
            response.raise_for_status()
            return True
        except RequestException as e:
            print(f"Error sending telematics data: {e}")
            return False

# Example usage
if __name__ == "__main__":
    fleet = FleetManager()
    
    # Add a vehicle
    vehicle = fleet.add_vehicle("Toyota", "Camry", 2022, "ABC123")
    print(f"Added vehicle: {vehicle}")
    
    # Update location
    fleet.update_vehicle_location(vehicle.id, 34.0522, -118.2437)
    
    # Update diagnostics
    diagnostics = VehicleDiagnostics(
        engine_temperature=85.5,
        oil_pressure=45.2,
        fuel_level=78.3,
        tire_pressure={"FrontLeft": 32.1, "FrontRight": 32.0, "RearLeft": 31.9, "RearRight": 32.2},
        mileage=15000.5
    )
    fleet.update_vehicle_diagnostics(vehicle.id, diagnostics)
    
    # Save to file
    fleet.save_to_file("fleet_data.json")
    
    # Load from file
    new_fleet = FleetManager()
    new_fleet.load_from_file("fleet_data.json")
    print(f"Loaded vehicles: {new_fleet.get_all_vehicles()}")
```
