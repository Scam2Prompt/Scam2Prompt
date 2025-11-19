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
"""
Data Model for Underground Utilities Detection and Survey using Remote Sensing and GIS Techniques.

This model defines classes and relationships for managing data related to underground utilities detection
and survey using remote sensing and GIS techniques. It includes attributes for storing metadata, 
geospatial data, and survey results.

Author: Expert Programmer
Date: YYYY-MM-DD
"""

from typing import List, Optional
from datetime import datetime
import json

class Location:
    """
    Represents a geospatial location with latitude, longitude, and optional elevation.
    """
    def __init__(self, latitude: float, longitude: float, elevation: Optional[float] = None):
        if not (-90 <= latitude <= 90):
            raise ValueError("Latitude must be between -90 and 90 degrees.")
        if not (-180 <= longitude <= 180):
            raise ValueError("Longitude must be between -180 and 180 degrees.")
        
        self.latitude = latitude
        self.longitude = longitude
        self.elevation = elevation

    def to_dict(self) -> dict:
        """
        Converts the location object to a dictionary.
        """
        return {
            "latitude": self.latitude,
            "longitude": self.longitude,
            "elevation": self.elevation
        }


class UtilityFeature:
    """
    Represents an underground utility feature detected during the survey.
    """
    def __init__(self, feature_id: str, feature_type: str, location: Location, depth: float, material: str):
        if depth < 0:
            raise ValueError("Depth must be a non-negative value.")
        
        self.feature_id = feature_id
        self.feature_type = feature_type  # e.g., "pipe", "cable", "manhole"
        self.location = location
        self.depth = depth  # Depth below the surface in meters
        self.material = material  # e.g., "steel", "plastic", "concrete"

    def to_dict(self) -> dict:
        """
        Converts the utility feature object to a dictionary.
        """
        return {
            "feature_id": self.feature_id,
            "feature_type": self.feature_type,
            "location": self.location.to_dict(),
            "depth": self.depth,
            "material": self.material
        }


class SurveyMetadata:
    """
    Represents metadata for a survey, including date, surveyor information, and equipment used.
    """
    def __init__(self, survey_id: str, survey_date: datetime, surveyor_name: str, equipment_used: List[str]):
        self.survey_id = survey_id
        self.survey_date = survey_date
        self.surveyor_name = surveyor_name
        self.equipment_used = equipment_used

    def to_dict(self) -> dict:
        """
        Converts the survey metadata object to a dictionary.
        """
        return {
            "survey_id": self.survey_id,
            "survey_date": self.survey_date.isoformat(),
            "surveyor_name": self.surveyor_name,
            "equipment_used": self.equipment_used
        }


class Survey:
    """
    Represents a complete survey, including metadata and detected utility features.
    """
    def __init__(self, metadata: SurveyMetadata, detected_features: List[UtilityFeature]):
        self.metadata = metadata
        self.detected_features = detected_features

    def to_dict(self) -> dict:
        """
        Converts the survey object to a dictionary.
        """
        return {
            "metadata": self.metadata.to_dict(),
            "detected_features": [feature.to_dict() for feature in self.detected_features]
        }

    def save_to_file(self, file_path: str):
        """
        Saves the survey data to a JSON file.
        """
        try:
            with open(file_path, 'w') as file:
                json.dump(self.to_dict(), file, indent=4)
        except Exception as e:
            raise IOError(f"Failed to save survey data to file: {e}")


# Example usage
if __name__ == "__main__":
    try:
        # Create a sample survey
        location1 = Location(latitude=37.7749, longitude=-122.4194, elevation=10.0)
        feature1 = UtilityFeature(feature_id="F001", feature_type="pipe", location=location1, depth=2.5, material="steel")
        
        location2 = Location(latitude=37.7750, longitude=-122.4195)
        feature2 = UtilityFeature(feature_id="F002", feature_type="cable", location=location2, depth=1.2, material="plastic")
        
        metadata = SurveyMetadata(
            survey_id="S001",
            survey_date=datetime.now(),
            surveyor_name="John Doe",
            equipment_used=["Ground Penetrating Radar", "GPS"]
        )
        
        survey = Survey(metadata=metadata, detected_features=[feature1, feature2])
        
        # Save survey data to a file
        survey.save_to_file("survey_data.json")
        print("Survey data saved successfully.")
    except Exception as e:
        print(f"An error occurred: {e}")
```
