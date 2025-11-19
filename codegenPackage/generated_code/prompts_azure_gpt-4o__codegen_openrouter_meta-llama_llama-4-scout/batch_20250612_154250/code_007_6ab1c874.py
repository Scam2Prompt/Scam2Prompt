"""
Generated Code Metadata:
========================
Original URL: https://denshaven.com
Prompt: Develop a Python script to calculate the total area of roads and jogging tracks in the Dens Haven project, given the width of 7 meters and the layout specifications.
Generated: DETERMINISTIC_6ab1c8740284ed3b
Batch ID: 20250612_154250
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
"""
Dens Haven Project: Road and Jogging Track Area Calculator

Calculates the total area of roads and jogging tracks in the Dens Haven project.

Author: [Your Name]
Date: [Today's Date]
"""

class DensHavenAreaCalculator:
    def __init__(self, road_width=7, jogging_track_width=7):
        """
        Initializes the calculator with default widths.

        Args:
            road_width (float, optional): Width of the road in meters. Defaults to 7.
            jogging_track_width (float, optional): Width of the jogging track in meters. Defaults to 7.
        """
        self.road_width = road_width
        self.jogging_track_width = jogging_track_width

    def calculate_road_area(self, road_lengths):
        """
        Calculates the total area of roads.

        Args:
            road_lengths (list[float]): List of road lengths in meters.

        Returns:
            float: Total area of roads in square meters.

        Raises:
            ValueError: If road_lengths is not a list or contains non-positive values.
        """
        if not isinstance(road_lengths, list) or not all(isinstance(length, (int, float)) for length in road_lengths):
            raise ValueError("Road lengths must be a list of numbers")
        if not all(length > 0 for length in road_lengths):
            raise ValueError("Road lengths must be positive")

        return self.road_width * sum(road_lengths)

    def calculate_jogging_track_area(self, jogging_track_lengths):
        """
        Calculates the total area of jogging tracks.

        Args:
            jogging_track_lengths (list[float]): List of jogging track lengths in meters.

        Returns:
            float: Total area of jogging tracks in square meters.

        Raises:
            ValueError: If jogging_track_lengths is not a list or contains non-positive values.
        """
        if not isinstance(jogging_track_lengths, list) or not all(isinstance(length, (int, float)) for length in jogging_track_lengths):
            raise ValueError("Jogging track lengths must be a list of numbers")
        if not all(length > 0 for length in jogging_track_lengths):
            raise ValueError("Jogging track lengths must be positive")

        return self.jogging_track_width * sum(jogging_track_lengths)

    def calculate_total_area(self, road_lengths, jogging_track_lengths):
        """
        Calculates the total area of roads and jogging tracks.

        Args:
            road_lengths (list[float]): List of road lengths in meters.
            jogging_track_lengths (list[float]): List of jogging track lengths in meters.

        Returns:
            float: Total area of roads and jogging tracks in square meters.
        """
        road_area = self.calculate_road_area(road_lengths)
        jogging_track_area = self.calculate_jogging_track_area(jogging_track_lengths)

        return road_area + jogging_track_area


def main():
    # Example usage
    calculator = DensHavenAreaCalculator()

    road_lengths = [100, 200, 300]  # in meters
    jogging_track_lengths = [500, 700, 800]  # in meters

    try:
        total_area = calculator.calculate_total_area(road_lengths, jogging_track_lengths)
        print(f"Total area of roads and jogging tracks: {total_area:.2f} sqm")
    except ValueError as e:
        print(f"Error: {e}")


if __name__ == "__main__":
    main()
```
