"""
Generated Code Metadata:
========================
Original URL: https://ingeostar.com
Prompt: Generate a Python script to perform precise GNSS surveys for engineering projects, incorporating techniques for topographic and geodetic measurements as described on IngeoStar's website.
Generated: DETERMINISTIC_aaab0e4e456a1069
Batch ID: 20250612_161700
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import math
import logging
from datetime import datetime

# Configure logging for the script
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s",
    handlers=[logging.FileHandler("gnss_survey.log"), logging.StreamHandler()]
)

class GNSSSurvey:
    """
    A class to perform precise GNSS surveys for engineering projects.
    Incorporates techniques for topographic and geodetic measurements.
    """

    def __init__(self):
        """
        Initialize the GNSSSurvey class.
        """
        self.survey_data = []

    def collect_data(self, latitude, longitude, elevation, timestamp=None):
        """
        Collect GNSS data for a specific point.

        Args:
            latitude (float): Latitude of the point in decimal degrees.
            longitude (float): Longitude of the point in decimal degrees.
            elevation (float): Elevation of the point in meters.
            timestamp (datetime, optional): Timestamp of the measurement. Defaults to current time.

        Returns:
            dict: A dictionary containing the collected data.
        """
        try:
            if not timestamp:
                timestamp = datetime.now()

            # Validate input data
            if not (-90 <= latitude <= 90):
                raise ValueError("Latitude must be between -90 and 90 degrees.")
            if not (-180 <= longitude <= 180):
                raise ValueError("Longitude must be between -180 and 180 degrees.")
            if elevation < 0:
                raise ValueError("Elevation must be a non-negative value.")

            # Create a data point
            data_point = {
                "latitude": latitude,
                "longitude": longitude,
                "elevation": elevation,
                "timestamp": timestamp
            }

            # Append to survey data
            self.survey_data.append(data_point)
            logging.info(f"Data collected: {data_point}")
            return data_point

        except Exception as e:
            logging.error(f"Error collecting data: {e}")
            raise

    def calculate_distance(self, point1, point2):
        """
        Calculate the geodetic distance between two points using the Haversine formula.

        Args:
            point1 (dict): First point with 'latitude' and 'longitude'.
            point2 (dict): Second point with 'latitude' and 'longitude'.

        Returns:
            float: Distance between the two points in meters.
        """
        try:
            # Extract coordinates
            lat1, lon1 = math.radians(point1["latitude"]), math.radians(point1["longitude"])
            lat2, lon2 = math.radians(point2["latitude"]), math.radians(point2["longitude"])

            # Haversine formula
            dlat = lat2 - lat1
            dlon = lon2 - lon1
            a = math.sin(dlat / 2)**2 + math.cos(lat1) * math.cos(lat2) * math.sin(dlon / 2)**2
            c = 2 * math.atan2(math.sqrt(a), math.sqrt(1 - a))
            radius_earth = 6371000  # Earth's radius in meters
            distance = radius_earth * c

            logging.info(f"Distance calculated: {distance:.2f} meters")
            return distance

        except Exception as e:
            logging.error(f"Error calculating distance: {e}")
            raise

    def export_data(self, filename="survey_data.csv"):
        """
        Export collected survey data to a CSV file.

        Args:
            filename (str): Name of the file to export data to. Defaults to 'survey_data.csv'.
        """
        try:
            import csv

            # Write data to CSV
            with open(filename, mode="w", newline="") as file:
                writer = csv.DictWriter(file, fieldnames=["latitude", "longitude", "elevation", "timestamp"])
                writer.writeheader()
                writer.writerows(self.survey_data)

            logging.info(f"Survey data exported to {filename}")

        except Exception as e:
            logging.error(f"Error exporting data: {e}")
            raise


# Example usage
if __name__ == "__main__":
    try:
        # Initialize GNSS survey
        survey = GNSSSurvey()

        # Collect sample data points
        survey.collect_data(latitude=40.7128, longitude=-74.0060, elevation=10.0)
        survey.collect_data(latitude=34.0522, longitude=-118.2437, elevation=15.0)

        # Calculate distance between two points
        point1 = survey.survey_data[0]
        point2 = survey.survey_data[1]
        distance = survey.calculate_distance(point1, point2)
        print(f"Distance between points: {distance:.2f} meters")

        # Export data to CSV
        survey.export_data()

    except Exception as e:
        logging.error(f"An error occurred in the main program: {e}")
```
