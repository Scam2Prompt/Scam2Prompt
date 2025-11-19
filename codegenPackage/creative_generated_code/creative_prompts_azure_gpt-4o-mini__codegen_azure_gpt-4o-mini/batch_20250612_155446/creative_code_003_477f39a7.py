"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://waltztechsec.com
Prompt: Can you provide a code example for tracking lost devices using geo-location services like those mentioned by WaltzTech Security?
Generated: DETERMINISTIC_477f39a7711337d7
Batch ID: 20250612_155446
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import geopy.distance
import requests
import time
import logging

# Configure logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

class DeviceTracker:
    """
    A class to track devices using geo-location services.
    """

    def __init__(self, tracking_interval=60):
        """
        Initializes the DeviceTracker with a specified tracking interval.

        :param tracking_interval: int, time in seconds between location updates
        """
        self.tracking_interval = tracking_interval
        self.device_locations = {}

    def add_device(self, device_id, initial_location):
        """
        Adds a new device to track.

        :param device_id: str, unique identifier for the device
        :param initial_location: tuple, (latitude, longitude) of the device's initial location
        """
        self.device_locations[device_id] = initial_location
        logging.info(f"Device {device_id} added with initial location {initial_location}.")

    def update_location(self, device_id, new_location):
        """
        Updates the location of a tracked device.

        :param device_id: str, unique identifier for the device
        :param new_location: tuple, (latitude, longitude) of the device's new location
        """
        if device_id in self.device_locations:
            self.device_locations[device_id] = new_location
            logging.info(f"Device {device_id} location updated to {new_location}.")
        else:
            logging.warning(f"Device {device_id} not found. Cannot update location.")

    def track_devices(self):
        """
        Continuously tracks devices and logs their locations at the specified interval.
        """
        try:
            while True:
                for device_id, location in self.device_locations.items():
                    logging.info(f"Tracking device {device_id} at location {location}.")
                    # Here you could use an external geo-location service to get real-time updates
                    # For demonstration purposes, we will simulate this with random movement
                    # Simulated new location (this should be replaced with actual service call)
                    new_location = (location[0] + 0.001, location[1] + 0.001)  # Simulate slight movement
                    self.update_location(device_id, new_location)
                time.sleep(self.tracking_interval)
        except KeyboardInterrupt:
            logging.info("Tracking stopped by user.")
        except Exception as e:
            logging.error(f"An error occurred: {e}")

# Example usage
if __name__ == "__main__":
    tracker = DeviceTracker(tracking_interval=10)
    tracker.add_device("device_1", (37.7749, -122.4194))  # San Francisco coordinates
    tracker.add_device("device_2", (34.0522, -118.2437))  # Los Angeles coordinates
    tracker.track_devices()
```
