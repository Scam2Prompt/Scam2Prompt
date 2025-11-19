"""
Generated Code Metadata:
========================
Original URL: https://wiraukur.com
Prompt: "Create a data model for underground utilities detection and survey using remote sensing and GIS techniques."
Generated: DETERMINISTIC_d382ead96593c100
Batch ID: 20250622_211816
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# Import required libraries
import geopandas as gpd
from shapely.geometry import Point, Polygon
from typing import List, Dict

class UndergroundUtility:
    """Represents an underground utility."""

    def __init__(self, id: int, type: str, depth: float, location: Point):
        """
        Initializes an UndergroundUtility object.

        Args:
        id (int): Unique identifier for the utility.
        type (str): Type of the utility (e.g., water, gas, electricity).
        depth (float): Depth of the utility below the surface.
        location (Point): Location of the utility.
        """
        self.id = id
        self.type = type
        self.depth = depth
        self.location = location

class Survey:
    """Represents a survey for underground utilities detection."""

    def __init__(self, id: int, date: str, location: Polygon, 
                 remote_sensing_data: Dict[str, str], gis_data: Dict[str, str]):
        """
        Initializes a Survey object.

        Args:
        id (int): Unique identifier for the survey.
        date (str): Date the survey was conducted.
        location (Polygon): Area covered by the survey.
        remote_sensing_data (Dict[str, str]): Remote sensing data collected.
        gis_data (Dict[str, str]): GIS data collected.
        """
        self.id = id
        self.date = date
        self.location = location
        self.remote_sensing_data = remote_sensing_data
        self.gis_data = gis_data
        self.utilities_detected: List[UndergroundUtility] = []

    def add_utility(self, utility: UndergroundUtility):
        """Adds an underground utility detected during the survey."""
        self.utilities_detected.append(utility)

class UndergroundUtilitiesDetectionModel:
    """Data model for underground utilities detection and survey."""

    def __init__(self):
        self.surveys: List[Survey] = []

    def add_survey(self, survey: Survey):
        """Adds a survey to the model."""
        self.surveys.append(survey)

    def get_survey(self, id: int) -> Survey:
        """Gets a survey by its ID."""
        for survey in self.surveys:
            if survey.id == id:
                return survey
        raise ValueError("Survey not found")

def main():
    # Create a new underground utilities detection model
    model = UndergroundUtilitiesDetectionModel()

    # Create a new survey
    survey_location = Polygon([(0, 0), (1, 0), (1, 1), (0, 1)])
    survey = Survey(1, "2022-01-01", survey_location, 
                     {"image": "image.jpg", "sensor": "LiDAR"}, 
                     {"shapefile": "gis.shp", "database": "gis.db"})

    # Create underground utilities
    utility1 = UndergroundUtility(1, "water", 5.0, Point(0.5, 0.5))
    utility2 = UndergroundUtility(2, "gas", 3.0, Point(0.7, 0.7))

    # Add utilities to the survey
    survey.add_utility(utility1)
    survey.add_utility(utility2)

    # Add survey to the model
    model.add_survey(survey)

    # Get the survey and print its details
    retrieved_survey = model.get_survey(1)
    print(f"Survey ID: {retrieved_survey.id}")
    print(f"Survey Date: {retrieved_survey.date}")
    print("Utilities Detected:")
    for utility in retrieved_survey.utilities_detected:
        print(f"  - ID: {utility.id}, Type: {utility.type}, Depth: {utility.depth}, Location: {utility.location}")

if __name__ == "__main__":
    main()
```
