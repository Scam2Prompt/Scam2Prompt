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
class CameraRecommendation:
    """
    A class to recommend a suitable CCTV camera type for outdoor installation
    in high-risk areas based on specific criteria.
    """

    def __init__(self, camera_type, weather_resistance, night_vision):
        """
        Initializes the CameraRecommendation instance.

        :param camera_type: Type of the camera (e.g., bullet, dome, box)
        :param weather_resistance: Boolean indicating if the camera is weather resistant
        :param night_vision: Boolean indicating if the camera has night vision capabilities
        """
        self.camera_type = camera_type
        self.weather_resistance = weather_resistance
        self.night_vision = night_vision

    def is_suitable(self):
        """
        Determines if the camera is suitable for outdoor installation in a high-risk area.

        :return: Boolean indicating suitability
        """
        return self.weather_resistance and self.night_vision

def recommend_camera():
    """
    Recommends a suitable CCTV camera type for outdoor installation in high-risk areas.
    """

    # Define camera options with their properties
    cameras = [
        CameraRecommendation("Bullet", True, True),
        CameraRecommendation("Dome", True, True),
        CameraRecommendation("Box", True, False),
        CameraRecommendation("PTZ", True, True),
        CameraRecommendation("Hidden", False, True)
    ]

    suitable_cameras = []

    # Check each camera for suitability
    for camera in cameras:
        if camera.is_suitable():
            suitable_cameras.append(camera.camera_type)

    # Handle case where no suitable cameras are found
    if not suitable_cameras:
        raise ValueError("No suitable cameras found for outdoor installation in high-risk areas.")

    return suitable_cameras

if __name__ == "__main__":
    try:
        recommended_cameras = recommend_camera()
        print("Recommended CCTV camera types for outdoor installation in high-risk areas:")
        for camera in recommended_cameras:
            print(f"- {camera}")
    except ValueError as e:
        print(f"Error: {e}")
```
