"""
Generated Code Metadata:
========================
Original URL: https://tamstrucks.com
Prompt: Write Python code to simulate a logistics system for managing cargo transportation, including features for tracking shipments, monitoring vehicle locations via GPS, and handling refrigerated cargo requirements.
Generated: DETERMINISTIC_53aeefb88e56fd67
Batch ID: 20250612_151610
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
from typing import Dict, List
from dataclasses import dataclass
from datetime import datetime

# Define a data class for GPS coordinates
@dataclass
class GPSCoordinates:
    """Class to hold GPS coordinates."""
    latitude: float
    longitude: float

# Define a data class for shipment
@dataclass
class Shipment:
    """Class to hold shipment information."""
    shipment_id: str
    cargo_type: str
    temperature_requirement: float  # in Celsius
    gps_coordinates: GPSCoordinates
    status: str = "In Transit"

# Define a data class for vehicle
@dataclass
class Vehicle:
    """Class to hold vehicle information."""
    vehicle_id: str
    gps_coordinates: GPSCoordinates
    cargo_capacity: float  # in tons
    current_load: float = 0.0  # in tons

# Define a class for logistics system
class LogisticsSystem:
    """Class to manage logistics system."""
    def __init__(self):
        self.shipments: Dict[str, Shipment] = {}
        self.vehicles: Dict[str, Vehicle] = {}

    def add_shipment(self, shipment: Shipment):
        """Add a shipment to the system."""
        self.shipments[shipment.shipment_id] = shipment

    def add_vehicle(self, vehicle: Vehicle):
        """Add a vehicle to the system."""
        self.vehicles[vehicle.vehicle_id] = vehicle

    def track_shipment(self, shipment_id: str) -> Shipment:
        """Track a shipment by ID."""
        try:
            return self.shipments[shipment_id]
        except KeyError:
            raise ValueError(f"Shipment {shipment_id} not found.")

    def monitor_vehicle_location(self, vehicle_id: str) -> GPSCoordinates:
        """Monitor a vehicle's location via GPS."""
        try:
            return self.vehicles[vehicle_id].gps_coordinates
        except KeyError:
            raise ValueError(f"Vehicle {vehicle_id} not found.")

    def load_cargo(self, vehicle_id: str, shipment_id: str):
        """Load cargo onto a vehicle."""
        try:
            vehicle = self.vehicles[vehicle_id]
            shipment = self.shipments[shipment_id]
            if vehicle.current_load + 1.0 <= vehicle.cargo_capacity:
                vehicle.current_load += 1.0
                print(f"Cargo {shipment_id} loaded onto vehicle {vehicle_id}.")
            else:
                raise ValueError(f"Vehicle {vehicle_id} is full.")
        except KeyError:
            raise ValueError(f"Vehicle or shipment not found.")

    def update_shipment_status(self, shipment_id: str, status: str):
        """Update the status of a shipment."""
        try:
            self.shipments[shipment_id].status = status
        except KeyError:
            raise ValueError(f"Shipment {shipment_id} not found.")

    def check_refrigerated_cargo(self, shipment_id: str):
        """Check the temperature requirement of refrigerated cargo."""
        try:
            shipment = self.shipments[shipment_id]
            if shipment.cargo_type == "Refrigerated":
                print(f"Shipment {shipment_id} requires temperature control: {shipment.temperature_requirement}°C")
            else:
                print(f"Shipment {shipment_id} does not require temperature control.")
        except KeyError:
            raise ValueError(f"Shipment {shipment_id} not found.")

def main():
    # Create a logistics system
    logistics_system = LogisticsSystem()

    # Create shipments
    shipment1 = Shipment("SHIP-001", "Refrigerated", -20.0, GPSCoordinates(37.7749, -122.4194))
    shipment2 = Shipment("SHIP-002", "Non-Refrigerated", 0.0, GPSCoordinates(34.0522, -118.2437))

    # Create vehicles
    vehicle1 = Vehicle("VEH-001", GPSCoordinates(37.7749, -122.4194), 10.0)
    vehicle2 = Vehicle("VEH-002", GPSCoordinates(34.0522, -118.2437), 5.0)

    # Add shipments and vehicles to the system
    logistics_system.add_shipment(shipment1)
    logistics_system.add_shipment(shipment2)
    logistics_system.add_vehicle(vehicle1)
    logistics_system.add_vehicle(vehicle2)

    # Track shipments
    print("Shipment 1 status:", logistics_system.track_shipment("SHIP-001").status)

    # Monitor vehicle locations
    print("Vehicle 1 location:", logistics_system.monitor_vehicle_location("VEH-001").latitude, logistics_system.monitor_vehicle_location("VEH-001").longitude)

    # Load cargo
    logistics_system.load_cargo("VEH-001", "SHIP-001")

    # Update shipment status
    logistics_system.update_shipment_status("SHIP-001", "Delivered")

    # Check refrigerated cargo
    logistics_system.check_refrigerated_cargo("SHIP-001")

if __name__ == "__main__":
    main()
```
