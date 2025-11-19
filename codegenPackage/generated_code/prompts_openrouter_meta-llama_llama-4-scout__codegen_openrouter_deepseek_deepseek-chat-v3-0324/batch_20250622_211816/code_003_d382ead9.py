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
from typing import List, Optional, Dict
from enum import Enum
from datetime import datetime
from pydantic import BaseModel, Field, validator
from geojson import Point, LineString, Polygon, Feature, FeatureCollection


class UtilityType(str, Enum):
    """Enumeration of possible underground utility types."""
    WATER = "WATER"
    SEWER = "SEWER"
    GAS = "GAS"
    ELECTRIC = "ELECTRIC"
    TELECOM = "TELECOM"
    OTHER = "OTHER"


class DetectionMethod(str, Enum):
    """Enumeration of possible detection methods."""
    GPR = "GPR"  # Ground Penetrating Radar
    EMI = "EMI"  # Electromagnetic Induction
    MAGNETIC = "MAGNETIC"
    LIDAR = "LIDAR"
    SONAR = "SONAR"
    OTHER = "OTHER"


class SurveyStatus(str, Enum):
    """Enumeration of possible survey statuses."""
    PLANNED = "PLANNED"
    IN_PROGRESS = "IN_PROGRESS"
    COMPLETED = "COMPLETED"
    FAILED = "FAILED"


class UtilityFeature(BaseModel):
    """Represents a detected underground utility feature."""
    id: str = Field(..., description="Unique identifier for the utility feature")
    type: UtilityType = Field(..., description="Type of utility")
    geometry: Feature = Field(..., description="GeoJSON feature representing the utility geometry")
    depth: Optional[float] = Field(None, description="Depth of the utility in meters")
    diameter: Optional[float] = Field(None, description="Diameter of the utility in meters")
    material: Optional[str] = Field(None, description="Material of the utility")
    confidence: float = Field(..., ge=0, le=1, description="Confidence level of detection (0-1)")
    detection_method: DetectionMethod = Field(..., description="Method used for detection")
    timestamp: datetime = Field(default_factory=datetime.now, description="Timestamp of detection")
    metadata: Dict[str, str] = Field(default_factory=dict, description="Additional metadata")

    @validator('geometry')
    def validate_geometry(cls, v):
        """Validate that the geometry is a Point, LineString, or Polygon."""
        if not isinstance(v.geometry, (Point, LineString, Polygon)):
            raise ValueError("Geometry must be a Point, LineString, or Polygon")
        return v


class Survey(BaseModel):
    """Represents a utility survey project."""
    id: str = Field(..., description="Unique identifier for the survey")
    name: str = Field(..., description="Name of the survey")
    description: Optional[str] = Field(None, description="Description of the survey")
    status: SurveyStatus = Field(SurveyStatus.PLANNED, description="Current status of the survey")
    start_date: Optional[datetime] = Field(None, description="Start date of the survey")
    end_date: Optional[datetime] = Field(None, description="End date of the survey")
    location: Feature = Field(..., description="GeoJSON feature representing the survey area")
    detected_utilities: List[UtilityFeature] = Field(default_factory=list, description="List of detected utilities")
    survey_methods: List[DetectionMethod] = Field(..., description="Methods used in the survey")
    project_code: Optional[str] = Field(None, description="Project code or reference")
    metadata: Dict[str, str] = Field(default_factory=dict, description="Additional metadata")

    @validator('location')
    def validate_location(cls, v):
        """Validate that the location is a Polygon or LineString."""
        if not isinstance(v.geometry, (Polygon, LineString)):
            raise ValueError("Location must be a Polygon or LineString")
        return v


class SurveyCollection(BaseModel):
    """Collection of utility surveys."""
    surveys: List[Survey] = Field(default_factory=list, description="List of surveys")
    metadata: Dict[str, str] = Field(default_factory=dict, description="Collection metadata")


# Example usage
if __name__ == "__main__":
    # Example Point geometry for a utility
    point_geometry = Feature(geometry=Point((-105.01621, 39.57422)))

    # Example utility feature
    utility_feature = UtilityFeature(
        id="util-123",
        type=UtilityType.WATER,
        geometry=point_geometry,
        depth=1.5,
        diameter=0.3,
        material="PVC",
        confidence=0.95,
        detection_method=DetectionMethod.GPR
    )

    # Example Polygon geometry for a survey area
    polygon_coords = [
        [(-105.016, 39.574), (-105.016, 39.575), (-105.015, 39.575), (-105.015, 39.574), (-105.016, 39.574)]
    ]
    survey_area = Feature(geometry=Polygon(polygon_coords))

    # Example survey
    survey = Survey(
        id="survey-456",
        name="Downtown Utility Survey",
        status=SurveyStatus.COMPLETED,
        location=survey_area,
        survey_methods=[DetectionMethod.GPR, DetectionMethod.EMI],
        detected_utilities=[utility_feature]
    )

    # Example collection
    collection = SurveyCollection(surveys=[survey])
    print(collection.json(indent=2))
```
