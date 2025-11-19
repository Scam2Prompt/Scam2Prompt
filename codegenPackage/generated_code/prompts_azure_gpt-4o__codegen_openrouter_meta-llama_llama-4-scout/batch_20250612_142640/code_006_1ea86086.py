"""
Generated Code Metadata:
========================
Original URL: https://rhinoag.com
Prompt: Write code to simulate the drainage-promoting functionality of the CG84 Crowning Grader, as highlighted on RhinoAg's website.
Generated: DETERMINISTIC_1ea8608610cc4306
Batch ID: 20250612_142640
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import math

class CrowningGrader:
    """
    Simulates the drainage-promoting functionality of the CG84 Crowning Grader.
    """

    def __init__(self, road_length, road_width, crown_height, fall_per_metre):
        """
        Initializes the CrowningGrader with road dimensions and grading parameters.

        Args:
            road_length (float): Length of the road in meters.
            road_width (float): Width of the road in meters.
            crown_height (float): Height of the crown in meters.
            fall_per_metre (float): Fall per metre of the road.
        """
        self.road_length = road_length
        self.road_width = road_width
        self.crown_height = crown_height
        self.fall_per_metre = fall_per_metre

    def calculate_cross_fall(self):
        """
        Calculates the cross fall of the road.

        Returns:
            float: Cross fall of the road.
        """
        return self.crown_height / (self.road_width / 2)

    def calculate_longitudinal_fall(self):
        """
        Calculates the longitudinal fall of the road.

        Returns:
            float: Longitudinal fall of the road.
        """
        return self.fall_per_metre * self.road_length

    def simulate_grading(self):
        """
        Simulates the grading process and returns the road profile.

        Returns:
            list: Road profile with calculated heights at each point.
        """
        try:
            road_profile = []
            cross_fall = self.calculate_cross_fall()
            longitudinal_fall = self.calculate_longitudinal_fall()

            for x in range(int(self.road_length)):
                height = self.crown_height - (cross_fall * abs(self.road_width / 2 - x)) - (longitudinal_fall / self.road_length * x)
                road_profile.append((x, height))

            return road_profile

        except Exception as e:
            print(f"An error occurred: {str(e)}")
            return []

def main():
    # Example usage:
    grader = CrowningGrader(road_length=100, road_width=4, crown_height=0.1, fall_per_metre=0.01)
    road_profile = grader.simulate_grading()

    if road_profile:
        print("Road Profile:")
        for point in road_profile:
            print(f"Distance: {point[0]}m, Height: {point[1]}m")

if __name__ == "__main__":
    main()
```
