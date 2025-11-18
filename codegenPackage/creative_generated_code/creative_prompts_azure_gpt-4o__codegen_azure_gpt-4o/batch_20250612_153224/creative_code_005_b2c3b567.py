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
import time
import logging
from datetime import datetime
from typing import List

# Configure logging settings
logging.basicConfig(
    filename='gps_tracking.log',
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s'
)

class GPSLocation:
    """
    Class to represent a GPS location with latitude and longitude.
    """
    def __init__(self, latitude: float, longitude: float, timestamp: str = None):
        self.latitude = latitude
        self.longitude = longitude
        self.timestamp = timestamp or datetime.now().strftime('%Y-%m-%d %H:%M:%S')

    def __str__(self):
        return f"Latitude: {self.latitude}, Longitude: {self.longitude}, Timestamp: {self.timestamp}"


class GPSTracker:
    """
    Class to manage GPS tracking for security purposes.
    """
    def __init__(self):
        self._locations: List[GPSLocation] = []  # List to store GPS locations

    def add_location(self, latitude: float, longitude: float):
        """
        Adds a new location to the tracker.

        Args:
            latitude (float): Latitude of the location.
            longitude (float): Longitude of the location.

        Raises:
            ValueError: If latitude or longitude is invalid.
        """
        try:
            # Validate latitude and longitude values
            if not (-90 <= latitude <= 90):
                raise ValueError("Latitude must be in the range -90 to 90.")
            if not (-180 <= longitude <= 180):
                raise ValueError("Longitude must be in the range -180 to 180.")

            # Create and store the GPSLocation object
            location = GPSLocation(latitude, longitude)
            self._locations.append(location)
            logging.info(f"Added location: {location}")
        except ValueError as ve:
            logging.error(f"Failed to add location: {ve}")
            raise

    def get_locations(self) -> List[GPSLocation]:
        """
        Retrieve all recorded GPS locations.

        Returns:
            List[GPSLocation]: List of GPS locations.
        """
        return self._locations

    def latest_location(self) -> GPSLocation:
        """
        Retrieve the most recent GPS location.

        Returns:
            GPSLocation: The most recent location object.

        Raises:
            ValueError: If no locations are available.
        """
        if not self._locations:
            raise ValueError("No locations recorded.")
        return self._locations[-1]

    def save_locations_to_file(self, filename: str):
        """
        Save all tracked locations to a file for record-keeping.

        Args:
            filename (str): Name of file to save locations.
        """
        try:
            with open(filename, 'w') as file:
                file.write("Latitude,Longitude,Timestamp\n")
                for location in self._locations:
                    file.write(f"{location.latitude},{location.longitude},{location.timestamp}\n")
            logging.info(f"Locations saved to file: {filename}")
        except Exception as e:
            logging.error(f"Failed to save locations to file: {e}")
            raise


# Example usage (Uncomment to test functionality):
# if __name__ == "__main__":
#     tracker = GPSTracker()
#     tracker.add_location(37.7749, -122.4194)  # San Francisco
#     tracker.add_location(34.0522, -118.2437)  # Los Angeles
#     print("Latest Location:", tracker.latest_location())
#     tracker.save_locations_to_file("gps_locations.csv")
```
