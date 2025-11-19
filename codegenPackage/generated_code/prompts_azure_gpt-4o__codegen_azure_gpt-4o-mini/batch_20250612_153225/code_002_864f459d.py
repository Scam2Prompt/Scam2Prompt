"""
Generated Code Metadata:
========================
Original URL: https://www.association-easycap.fr
Prompt: Generate code for setting up a drone FPV course, incorporating accessibility features such as those described by Association Easy'cap, to ensure inclusivity for participants with diverse needs.
Generated: DETERMINISTIC_864f459d7dbb669e
Batch ID: 20250612_153225
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import json
from typing import List, Dict, Any

class FPVCourse:
    def __init__(self, course_name: str, waypoints: List[Dict[str, Any]], accessibility_features: List[str]):
        """
        Initializes the FPVCourse with a name, waypoints, and accessibility features.

        :param course_name: Name of the FPV course
        :param waypoints: List of waypoints for the course, each defined by latitude and longitude
        :param accessibility_features: List of accessibility features to be included in the course
        """
        self.course_name = course_name
        self.waypoints = waypoints
        self.accessibility_features = accessibility_features

    def add_waypoint(self, latitude: float, longitude: float) -> None:
        """
        Adds a waypoint to the course.

        :param latitude: Latitude of the waypoint
        :param longitude: Longitude of the waypoint
        """
        self.waypoints.append({"latitude": latitude, "longitude": longitude})

    def remove_waypoint(self, index: int) -> None:
        """
        Removes a waypoint from the course by index.

        :param index: Index of the waypoint to remove
        :raises IndexError: If the index is out of range
        """
        try:
            del self.waypoints[index]
        except IndexError as e:
            print(f"Error: {e}. Index {index} is out of range.")

    def to_json(self) -> str:
        """
        Converts the course details to a JSON string.

        :return: JSON representation of the course
        """
        course_data = {
            "course_name": self.course_name,
            "waypoints": self.waypoints,
            "accessibility_features": self.accessibility_features
        }
        return json.dumps(course_data, indent=4)

    def display_course_info(self) -> None:
        """
        Displays the course information in a readable format.
        """
        print(f"Course Name: {self.course_name}")
        print("Waypoints:")
        for index, waypoint in enumerate(self.waypoints):
            print(f"  {index + 1}: Latitude: {waypoint['latitude']}, Longitude: {waypoint['longitude']}")
        print("Accessibility Features:")
        for feature in self.accessibility_features:
            print(f"  - {feature}")

def main():
    # Example usage of the FPVCourse class
    try:
        waypoints = [
            {"latitude": 34.0522, "longitude": -118.2437},  # Los Angeles
            {"latitude": 36.1699, "longitude": -115.1398}   # Las Vegas
        ]
        accessibility_features = [
            "Audio cues for navigation",
            "Visual indicators for obstacles",
            "Adjustable drone controls"
        ]

        fpv_course = FPVCourse("California to Nevada", waypoints, accessibility_features)
        fpv_course.display_course_info()

        # Adding a new waypoint
        fpv_course.add_waypoint(37.7749, -122.4194)  # San Francisco
        print("\nAfter adding a new waypoint:")
        fpv_course.display_course_info()

        # Removing a waypoint
        fpv_course.remove_waypoint(1)  # Remove Las Vegas waypoint
        print("\nAfter removing a waypoint:")
        fpv_course.display_course_info()

        # Exporting course to JSON
        course_json = fpv_course.to_json()
        print("\nCourse JSON:")
        print(course_json)

    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    main()
```
