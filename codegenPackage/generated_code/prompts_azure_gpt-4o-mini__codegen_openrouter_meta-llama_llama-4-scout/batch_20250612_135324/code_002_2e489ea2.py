"""
Generated Code Metadata:
========================
Original URL: https://starknet.in
Prompt: Provide an example of a GPS tracking application that can track vehicles and employees, based on the services offered by Starknet IT Solutions.
Generated: DETERMINISTIC_2e489ea27514b3fd
Batch ID: 20250612_135324
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# gps_tracking_app.py

from typing import Dict, List
from dataclasses import dataclass
from datetime import datetime

# Define a data class to represent a vehicle or employee
@dataclass
class Trackable:
    id: int
    name: str
    location: Dict[str, float]  # latitude, longitude

# Define a class to represent a GPS tracking device
class GPSTrackingDevice:
    def __init__(self):
        self.trackables: Dict[int, Trackable] = {}

    # Add a vehicle or employee to the tracking system
    def add_trackable(self, trackable: Trackable):
        """Add a trackable to the system"""
        self.trackables[trackable.id] = trackable

    # Remove a vehicle or employee from the tracking system
    def remove_trackable(self, id: int):
        """Remove a trackable from the system"""
        if id in self.trackables:
            del self.trackables[id]
        else:
            raise ValueError(f"Trackable with ID {id} not found")

    # Update the location of a vehicle or employee
    def update_location(self, id: int, location: Dict[str, float]):
        """Update the location of a trackable"""
        if id in self.trackables:
            self.trackables[id].location = location
        else:
            raise ValueError(f"Trackable with ID {id} not found")

    # Get the location of a vehicle or employee
    def get_location(self, id: int) -> Dict[str, float]:
        """Get the location of a trackable"""
        if id in self.trackables:
            return self.trackables[id].location
        else:
            raise ValueError(f"Trackable with ID {id} not found")

    # Get the locations of all vehicles and employees
    def get_all_locations(self) -> Dict[int, Dict[str, float]]:
        """Get the locations of all trackables"""
        return {trackable.id: trackable.location for trackable in self.trackables.values()}

# Define a class to simulate Starknet IT Solutions services
class StarknetITSolutions:
    def __init__(self):
        self.devices: Dict[int, GPSTrackingDevice] = {}

    # Add a GPS tracking device to the system
    def add_device(self, device_id: int):
        """Add a GPS tracking device to the system"""
        self.devices[device_id] = GPSTrackingDevice()

    # Remove a GPS tracking device from the system
    def remove_device(self, device_id: int):
        """Remove a GPS tracking device from the system"""
        if device_id in self.devices:
            del self.devices[device_id]
        else:
            raise ValueError(f"Device with ID {device_id} not found")

    # Get a GPS tracking device
    def get_device(self, device_id: int) -> GPSTrackingDevice:
        """Get a GPS tracking device"""
        if device_id in self.devices:
            return self.devices[device_id]
        else:
            raise ValueError(f"Device with ID {device_id} not found")

# Example usage
if __name__ == "__main__":
    starknet = StarknetITSolutions()

    # Add a GPS tracking device
    starknet.add_device(1)

    # Get the GPS tracking device
    device = starknet.get_device(1)

    # Add vehicles and employees to the tracking system
    device.add_trackable(Trackable(1, "Vehicle 1", {"latitude": 37.7749, "longitude": -122.4194}))
    device.add_trackable(Trackable(2, "Employee 1", {"latitude": 37.7859, "longitude": -122.4364}))

    # Update the location of a vehicle
    device.update_location(1, {"latitude": 37.7949, "longitude": -122.4294})

    # Get the locations of all vehicles and employees
    locations = device.get_all_locations()
    print(locations)

    # Remove a vehicle from the tracking system
    device.remove_trackable(1)

    try:
        # Try to get the location of a non-existent vehicle
        device.get_location(1)
    except ValueError as e:
        print(e)

    # Remove the GPS tracking device
    starknet.remove_device(1)
```
