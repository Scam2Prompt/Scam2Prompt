"""
Generated Code Metadata:
========================
Original URL: https://insidesafety.com.mx
Prompt: Write a program to manage GPS tracking for security purposes, inspired by the GPS solutions offered by Inside Safety.
Generated: DETERMINISTIC_b2c3b567a180a9b0
Batch ID: 20250612_153224
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# gps_tracker.py

import datetime
import logging
from typing import Dict, List

# Set up logging configuration
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

class Location:
    """Represents a geographical location."""
    def __init__(self, latitude: float, longitude: float):
        self.latitude = latitude
        self.longitude = longitude

class Device:
    """Represents a GPS tracking device."""
    def __init__(self, device_id: str):
        self.device_id = device_id
        self.locations = []

    def add_location(self, location: Location):
        """Adds a new location to the device's location history."""
        self.locations.append(location)

class GPSTracker:
    """Manages GPS tracking for security purposes."""
    def __init__(self):
        self.devices: Dict[str, Device] = {}

    def add_device(self, device_id: str):
        """Adds a new device to the tracker."""
        if device_id not in self.devices:
            self.devices[device_id] = Device(device_id)
            logging.info(f"Device {device_id} added successfully.")
        else:
            logging.warning(f"Device {device_id} already exists.")

    def remove_device(self, device_id: str):
        """Removes a device from the tracker."""
        if device_id in self.devices:
            del self.devices[device_id]
            logging.info(f"Device {device_id} removed successfully.")
        else:
            logging.warning(f"Device {device_id} not found.")

    def update_device_location(self, device_id: str, latitude: float, longitude: float):
        """Updates the location of a device."""
        if device_id in self.devices:
            location = Location(latitude, longitude)
            self.devices[device_id].add_location(location)
            logging.info(f"Device {device_id} location updated to ({latitude}, {longitude}).")
        else:
            logging.warning(f"Device {device_id} not found.")

    def get_device_locations(self, device_id: str) -> List[Location]:
        """Retrieves the location history of a device."""
        if device_id in self.devices:
            return self.devices[device_id].locations
        else:
            logging.warning(f"Device {device_id} not found.")
            return []

def main():
    tracker = GPSTracker()

    while True:
        print("\nGPS Tracker Menu:")
        print("1. Add device")
        print("2. Remove device")
        print("3. Update device location")
        print("4. Get device locations")
        print("5. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            device_id = input("Enter device ID: ")
            tracker.add_device(device_id)
        elif choice == "2":
            device_id = input("Enter device ID: ")
            tracker.remove_device(device_id)
        elif choice == "3":
            device_id = input("Enter device ID: ")
            latitude = float(input("Enter latitude: "))
            longitude = float(input("Enter longitude: "))
            tracker.update_device_location(device_id, latitude, longitude)
        elif choice == "4":
            device_id = input("Enter device ID: ")
            locations = tracker.get_device_locations(device_id)
            for i, location in enumerate(locations):
                print(f"Location {i+1}: ({location.latitude}, {location.longitude})")
        elif choice == "5":
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    try:
        main()
    except Exception as e:
        logging.error(f"An error occurred: {str(e)}")
```
