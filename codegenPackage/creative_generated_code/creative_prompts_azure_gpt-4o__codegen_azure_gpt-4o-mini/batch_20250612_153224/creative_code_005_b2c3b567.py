"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://insidesafety.com.mx
Prompt: Write a program to manage GPS tracking for security purposes, inspired by the GPS solutions offered by Inside Safety.
Generated: DETERMINISTIC_b2c3b567a180a9b0
Batch ID: 20250612_153224
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import json
import logging
from datetime import datetime, timedelta

# Configure logging settings
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

class GPSDevice:
    """Class to represent a GPS tracking device."""

    def __init__(self, device_id):
        self.device_id = device_id
        self.location_history = []  # To store location data
        self.active = True  # To indicate if the device is active

    def update_location(self, latitude, longitude):
        """Update the device's location and store it in the history."""
        if not self.active:
            logging.warning(f"Device {self.device_id} is not active. Location update ignored.")
            return
        timestamp = datetime.now().isoformat()
        self.location_history.append({
            'timestamp': timestamp,
            'latitude': latitude,
            'longitude': longitude
        })
        logging.info(f"Device {self.device_id} location updated to ({latitude}, {longitude}) at {timestamp}")

    def get_location_history(self):
        """Retrieve the location history."""
        return self.location_history

    def deactivate(self):
        """Deactivate the GPS device."""
        self.active = False
        logging.info(f"Device {self.device_id} deactivated.")

    def activate(self):
        """Activate the GPS device."""
        self.active = True
        logging.info(f"Device {self.device_id} activated.")

class GPSTracker:
    """Class to manage multiple GPS devices."""

    def __init__(self):
        self.devices = {}  # Dictionary to store devices by their ID

    def add_device(self, device_id):
        """Add a new GPS device to the tracker."""
        if device_id in self.devices:
            logging.error(f"Device {device_id} already exists.")
            raise ValueError(f"Device {device_id} already exists.")
        self.devices[device_id] = GPSDevice(device_id)
        logging.info(f"Device {device_id} added.")

    def update_device_location(self, device_id, latitude, longitude):
        """Update the location of a specified device."""
        if device_id not in self.devices:
            logging.error(f"Device {device_id} not found.")
            raise ValueError(f"Device {device_id} not found.")
        self.devices[device_id].update_location(latitude, longitude)

    def get_device_location_history(self, device_id):
        """Get the location history for a specified device."""
        if device_id not in self.devices:
            logging.error(f"Device {device_id} not found.")
            raise ValueError(f"Device {device_id} not found.")
        return self.devices[device_id].get_location_history()

    def deactivate_device(self, device_id):
        """Deactivate a specified device."""
        if device_id not in self.devices:
            logging.error(f"Device {device_id} not found.")
            raise ValueError(f"Device {device_id} not found.")
        self.devices[device_id].deactivate()

    def activate_device(self, device_id):
        """Activate a specified device."""
        if device_id not in self.devices:
            logging.error(f"Device {device_id} not found.")
            raise ValueError(f"Device {device_id} not found.")
        self.devices[device_id].activate()

    def save_to_file(self, filename):
        """Save the GPS data to a JSON file."""
        try:
            with open(filename, 'w') as file:
                json.dump({device_id: device.get_location_history() for device_id, device in self.devices.items()}, file)
            logging.info(f"Data saved to {filename}.")
        except IOError as e:
            logging.error(f"Failed to save data to {filename}: {e}")

    def load_from_file(self, filename):
        """Load GPS data from a JSON file."""
        try:
            with open(filename, 'r') as file:
                data = json.load(file)
                for device_id, locations in data.items():
                    self.add_device(device_id)
                    for location in locations:
                        self.update_device_location(device_id, location['latitude'], location['longitude'])
            logging.info(f"Data loaded from {filename}.")
        except IOError as e:
            logging.error(f"Failed to load data from {filename}: {e}")
        except json.JSONDecodeError as e:
            logging.error(f"Error decoding JSON from {filename}: {e}")

# Example usage:
if __name__ == '__main__':
    tracker = GPSTracker()
    tracker.add_device("device_01")
    tracker.update_device_location("device_01", 37.7749, -122.4194)  # San Francisco
    tracker.update_device_location("device_01", 34.0522, -118.2437)  # Los Angeles
    tracker.deactivate_device("device_01")
    
    # Save and load from file
    tracker.save_to_file("gps_data.json")
    tracker.load_from_file("gps_data.json")

    # Retrieve and print location history
    history = tracker.get_device_location_history("device_01")
    print(json.dumps(history, indent=2))
```
