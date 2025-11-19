"""
Generated Code Metadata:
========================
Original URL: https://rayzentreprise.com
Prompt: "Recommend a suitable CCTV camera type (e.g., bullet, dome, or box) for a outdoor installation in a high-risk area, considering factors like weather resistance and night vision capabilities."
Generated: DETERMINISTIC_f1c3531ed09da4e3
Batch ID: 20250622_210650
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
from enum import Enum

# Define an Enum for CCTV camera types
class CameraType(Enum):
    """Enum for CCTV camera types"""
    BULLET = "bullet"
    DOME = "dome"
    BOX = "box"

# Define a class for CCTV camera recommendations
class CCTVRecommendation:
    """Class for recommending CCTV camera types"""

    def __init__(self, installation_area, risk_level, weather_conditions, night_vision_required):
        """
        Initialize the CCTV recommendation system

        Args:
            installation_area (str): The area where the camera will be installed (e.g., outdoor, indoor)
            risk_level (str): The risk level of the area (e.g., high, medium, low)
            weather_conditions (str): The weather conditions of the installation area (e.g., extreme, moderate)
            night_vision_required (bool): Whether night vision is required
        """
        self.installation_area = installation_area
        self.risk_level = risk_level
        self.weather_conditions = weather_conditions
        self.night_vision_required = night_vision_required

    def recommend_camera_type(self):
        """
        Recommend a suitable CCTV camera type based on the given conditions

        Returns:
            CameraType: The recommended CCTV camera type
        """
        try:
            # Check if the installation area is outdoor
            if self.installation_area.lower() != "outdoor":
                raise ValueError("Installation area must be outdoor for this recommendation")

            # Check if the risk level is high
            if self.risk_level.lower() != "high":
                raise ValueError("Risk level must be high for this recommendation")

            # Recommend a camera type based on weather conditions and night vision requirements
            if self.weather_conditions.lower() == "extreme":
                # For extreme weather conditions, recommend a box camera with weather resistance
                if self.night_vision_required:
                    return CameraType.BOX
                else:
                    raise ValueError("Night vision is required for extreme weather conditions")
            else:
                # For moderate weather conditions, recommend a bullet or dome camera
                if self.night_vision_required:
                    return CameraType.BULLET
                else:
                    return CameraType.DOME

        except ValueError as e:
            print(f"Error: {e}")
            return None

def main():
    # Example usage
    recommendation = CCTVRecommendation("outdoor", "high", "extreme", True)
    recommended_camera_type = recommendation.recommend_camera_type()

    if recommended_camera_type:
        print(f"Recommended CCTV camera type: {recommended_camera_type.value}")
    else:
        print("No recommendation available")

if __name__ == "__main__":
    main()
```
