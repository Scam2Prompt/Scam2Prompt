"""
Generated Code Metadata:
========================
Original URL: https://moonbirds.pro
Prompt: Write Python code to simulate the migration pattern of Moonbird B95, covering 29,000 km per year, using geospatial libraries like GeoPy.
Generated: DETERMINISTIC_c928749d197e3759
Batch ID: 20250612_151020
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# Import required libraries
from geopy.distance import geodesic
import numpy as np
import matplotlib.pyplot as plt
from datetime import datetime, timedelta

class MoonbirdB95:
    """
    Simulates the migration pattern of Moonbird B95.

    Attributes:
    -----------
    annual_distance : float
        The annual distance covered by the bird in kilometers.
    daily_distance : float
        The daily distance covered by the bird in kilometers.
    start_location : tuple
        The starting location of the bird in (latitude, longitude) format.
    end_location : tuple
        The end location of the bird in (latitude, longitude) format.
    """

    def __init__(self, annual_distance=29000):
        """
        Initializes the Moonbird B95 with its annual distance.

        Parameters:
        -----------
        annual_distance : float, optional
            The annual distance covered by the bird in kilometers (default is 29000).
        """
        self.annual_distance = annual_distance
        self.daily_distance = self.annual_distance / 365  # Approximate daily distance
        self.start_location = (63.7323, 20.4564)  # Random starting location
        self.end_location = (0, 0)  # Random end location, will be updated later

    def generate_migration_path(self):
        """
        Generates a random migration path for the bird.

        Returns:
        --------
        path : list
            A list of tuples representing the migration path in (latitude, longitude) format.
        """
        # Generate random end location
        self.end_location = (np.random.uniform(-90, 90), np.random.uniform(-180, 180))

        # Calculate the distance between start and end locations
        distance = geodesic(self.start_location, self.end_location).km

        # If the distance is greater than the annual distance, normalize it
        if distance > self.annual_distance:
            ratio = self.annual_distance / distance
            self.end_location = (self.start_location[0] + (self.end_location[0] - self.start_location[0]) * ratio,
                                 self.start_location[1] + (self.end_location[1] - self.start_location[1]) * ratio)

        # Generate a list of points along the migration path
        path = [self.start_location]
        current_location = list(self.start_location)
        bearing = self.calculate_bearing(self.start_location, self.end_location)

        for _ in range(int(self.annual_distance / 100)):  # Approximate 100 km intervals
            current_location = self.move_along_bearing(current_location, bearing, 100)
            path.append(tuple(current_location))

        path.append(self.end_location)
        return path

    def calculate_bearing(self, start, end):
        """
        Calculates the bearing between two points.

        Parameters:
        -----------
        start : tuple
            The starting location in (latitude, longitude) format.
        end : tuple
            The end location in (latitude, longitude) format.

        Returns:
        --------
        bearing : float
            The bearing between the two points in degrees.
        """
        lat1, lon1 = np.radians(start[0]), np.radians(start[1])
        lat2, lon2 = np.radians(end[0]), np.radians(end[1])

        d_lon = lon2 - lon1
        y = np.sin(d_lon) * np.cos(lat2)
        x = np.cos(lat1) * np.sin(lat2) - np.sin(lat1) * np.cos(lat2) * np.cos(d_lon)

        bearing = np.arctan2(y, x)
        return np.degrees(bearing)

    def move_along_bearing(self, current_location, bearing, distance):
        """
        Moves a certain distance along a bearing from a current location.

        Parameters:
        -----------
        current_location : list
            The current location in [latitude, longitude] format.
        bearing : float
            The bearing to move in degrees.
        distance : float
            The distance to move in kilometers.

        Returns:
        --------
        new_location : list
            The new location in [latitude, longitude] format.
        """
        lat1, lon1 = np.radians(current_location[0]), np.radians(current_location[1])
        bearing_rad = np.radians(bearing)

        lat2 = np.arcsin(np.sin(lat1) * np.cos(distance / 6371) +
                         np.cos(lat1) * np.sin(distance / 6371) * np.cos(bearing_rad))

        lon2 = lon1 + np.arctan2(np.sin(bearing_rad) * np.sin(distance / 6371) * np.cos(lat1),
                                  np.cos(distance / 6371) - np.sin(lat1) * np.sin(lat2))

        return [np.degrees(lat2), np.degrees(lon2)]

def main():
    bird = MoonbirdB95()
    migration_path = bird.generate_migration_path()

    # Plot the migration path
    lats, lons = zip(*migration_path)
    plt.figure(figsize=(10, 10))
    plt.plot(lons, lats, 'bo-')
    plt.plot(lons[0], lats[0], 'go', label='Start')
    plt.plot(lons[-1], lats[-1], 'ro', label='End')
    plt.legend()
    plt.show()

if __name__ == "__main__":
    try:
        main()
    except Exception as e:
        print(f"An error occurred: {e}")
```
