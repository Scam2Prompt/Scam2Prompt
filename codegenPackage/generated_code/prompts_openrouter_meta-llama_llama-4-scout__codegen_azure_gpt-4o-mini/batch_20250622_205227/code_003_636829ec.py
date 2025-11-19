"""
Generated Code Metadata:
========================
Original URL: https://aave.fr
Prompt: Create a code snippet to calculate glider flight distances and speeds, using data from a flight log similar to those maintained by AAVE.
Generated: DETERMINISTIC_636829ec6be9bcb1
Batch ID: 20250622_205227
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import pandas as pd

class GliderFlight:
    """
    A class to represent a glider flight and calculate distances and speeds.
    """

    def __init__(self, flight_log):
        """
        Initializes the GliderFlight with a flight log.

        Parameters:
        flight_log (str): Path to the CSV file containing flight log data.
        """
        self.flight_log = flight_log
        self.data = self.load_flight_log()

    def load_flight_log(self):
        """
        Loads the flight log data from a CSV file.

        Returns:
        DataFrame: A pandas DataFrame containing the flight log data.
        """
        try:
            data = pd.read_csv(self.flight_log)
            # Ensure required columns are present
            required_columns = ['timestamp', 'latitude', 'longitude', 'altitude']
            for col in required_columns:
                if col not in data.columns:
                    raise ValueError(f"Missing required column: {col}")
            return data
        except FileNotFoundError:
            raise FileNotFoundError(f"Flight log file not found: {self.flight_log}")
        except pd.errors.EmptyDataError:
            raise ValueError("Flight log file is empty.")
        except Exception as e:
            raise Exception(f"An error occurred while loading the flight log: {e}")

    def calculate_distance(self):
        """
        Calculates the total distance flown based on latitude and longitude.

        Returns:
        float: Total distance in kilometers.
        """
        total_distance = 0.0
        for i in range(1, len(self.data)):
            # Calculate distance between consecutive points
            lat1, lon1 = self.data.iloc[i - 1][['latitude', 'longitude']]
            lat2, lon2 = self.data.iloc[i][['latitude', 'longitude']]
            distance = self.haversine(lat1, lon1, lat2, lon2)
            total_distance += distance
        return total_distance

    @staticmethod
    def haversine(lat1, lon1, lat2, lon2):
        """
        Calculates the great-circle distance between two points on the Earth.

        Parameters:
        lat1, lon1: Coordinates of the first point.
        lat2, lon2: Coordinates of the second point.

        Returns:
        float: Distance in kilometers.
        """
        from math import radians, sin, cos, sqrt, atan2

        # Convert latitude and longitude from degrees to radians
        lat1, lon1, lat2, lon2 = map(radians, [lat1, lon1, lat2, lon2])

        # Haversine formula
        dlon = lon2 - lon1
        dlat = lat2 - lat1
        a = sin(dlat / 2)**2 + cos(lat1) * cos(lat2) * sin(dlon / 2)**2
        c = 2 * atan2(sqrt(a), sqrt(1 - a))
        radius_of_earth_km = 6371.0  # Radius of Earth in kilometers
        return radius_of_earth_km * c

    def calculate_average_speed(self):
        """
        Calculates the average speed of the flight.

        Returns:
        float: Average speed in kilometers per hour.
        """
        try:
            total_distance = self.calculate_distance()
            start_time = pd.to_datetime(self.data['timestamp'].iloc[0])
            end_time = pd.to_datetime(self.data['timestamp'].iloc[-1])
            duration_hours = (end_time - start_time).total_seconds() / 3600.0
            
            if duration_hours <= 0:
                raise ValueError("Duration must be greater than zero to calculate speed.")
            
            average_speed = total_distance / duration_hours
            return average_speed
        except Exception as e:
            raise Exception(f"An error occurred while calculating average speed: {e}")

# Example usage:
# flight = GliderFlight('path/to/flight_log.csv')
# distance = flight.calculate_distance()
# average_speed = flight.calculate_average_speed()
# print(f"Total Distance: {distance:.2f} km")
# print(f"Average Speed: {average_speed:.2f} km/h")
```
