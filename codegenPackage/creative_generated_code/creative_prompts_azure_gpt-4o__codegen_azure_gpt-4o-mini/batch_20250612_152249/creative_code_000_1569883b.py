"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://kataskeui.gr
Prompt: Write Python code to calculate coordinates for a topographic diagram based on the ΕΓΣΑ ‘87 Greek Geodetic Reference System. Include validation for accurate boundary representation.
Generated: DETERMINISTIC_1569883bec2781e5
Batch ID: 20250612_152249
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import math

class TopographicDiagram:
    """
    A class to represent a topographic diagram based on the ΕΓΣΑ ‘87 Greek Geodetic Reference System.
    It calculates coordinates for points in the topographic diagram and validates boundaries.
    """

    def __init__(self, min_x, max_x, min_y, max_y):
        """
        Initializes the topographic diagram with boundary coordinates.

        Args:
            min_x (float): Minimum x-coordinate.
            max_x (float): Maximum x-coordinate.
            min_y (float): Minimum y-coordinate.
            max_y (float): Maximum y-coordinate.
        
        Raises:
            ValueError: If the boundaries are invalid (min >= max).
        """
        if min_x >= max_x or min_y >= max_y:
            raise ValueError("Invalid boundaries: min must be less than max.")
        
        self.min_x = min_x
        self.max_x = max_x
        self.min_y = min_y
        self.max_y = max_y

    def calculate_coordinates(self, num_points):
        """
        Generates coordinates for the specified number of points within the defined boundaries.

        Args:
            num_points (int): Number of points to generate.
        
        Returns:
            list of tuples: A list containing the generated (x, y) coordinates.
        
        Raises:
            ValueError: If num_points is not a positive integer.
        """
        if not isinstance(num_points, int) or num_points <= 0:
            raise ValueError("num_points must be a positive integer.")

        coordinates = []
        for _ in range(num_points):
            x = self.random_coordinate(self.min_x, self.max_x)
            y = self.random_coordinate(self.min_y, self.max_y)
            coordinates.append((x, y))
        
        return coordinates

    @staticmethod
    def random_coordinate(min_val, max_val):
        """
        Generates a random coordinate within the specified range.

        Args:
            min_val (float): Minimum value of the coordinate.
            max_val (float): Maximum value of the coordinate.
        
        Returns:
            float: A randomly generated coordinate.
        """
        return round(random.uniform(min_val, max_val), 6)

    def validate_boundaries(self, x, y):
        """
        Validates if a given point (x, y) is within the defined boundaries.

        Args:
            x (float): x-coordinate to validate.
            y (float): y-coordinate to validate.
        
        Returns:
            bool: True if the coordinates are within bounds, False otherwise.
        """
        return self.min_x <= x <= self.max_x and self.min_y <= y <= self.max_y

# Example usage
if __name__ == "__main__":
    try:
        diagram = TopographicDiagram(min_x=20.0, max_x=25.0, min_y=30.0, max_y=35.0)
        coordinates = diagram.calculate_coordinates(num_points=10)
        
        # Print generated coordinates
        for coord in coordinates:
            print(f"Coordinate: {coord}, Valid: {diagram.validate_boundaries(*coord)}")
    except ValueError as e:
        print(f"Error: {e}")
```

Make sure to import the `random` module before running the code to ensure the random coordinate generation works properly.
