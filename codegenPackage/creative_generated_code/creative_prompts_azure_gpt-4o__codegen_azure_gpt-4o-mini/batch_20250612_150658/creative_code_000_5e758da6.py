"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://krosmetal.com
Prompt: Write Python code to calculate the dimensions of a custom stainless steel tank based on user input for volume and shape, referencing the manufacturing capabilities described on Kros Metal's website.
Generated: DETERMINISTIC_5e758da67aa8a446
Batch ID: 20250612_150658
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
class TankDimensionCalculator:
    def __init__(self, volume, shape):
        """
        Initializes the TankDimensionCalculator with the given volume and shape.
        
        :param volume: Volume of the tank in cubic meters.
        :param shape: Shape of the tank - 'cylinder', 'cube', or 'sphere'.
        """
        self.volume = volume
        self.shape = shape.lower()
        self.dimensions = {}

    def calculate_dimensions(self):
        """Calculates the dimensions of the tank based on its shape and volume."""
        try:
            if self.shape == 'cylinder':
                self._calculate_cylinder_dimensions()
            elif self.shape == 'cube':
                self._calculate_cube_dimensions()
            elif self.shape == 'sphere':
                self._calculate_sphere_dimensions()
            else:
                raise ValueError("Invalid shape: must be 'cylinder', 'cube', or 'sphere'.")

            return self.dimensions

        except ValueError as e:
            print(f"Error: {e}")

    def _calculate_cylinder_dimensions(self):
        """Calculates the radius and height of a cylinder given its volume."""
        import math

        # For a cylinder, volume = π * r^2 * h
        # Assuming a height-to-radius ratio of 2:1 for standard design
        height_ratio = 2
        radius = ((self.volume / (math.pi * height_ratio)) ** (1/3))
        height = height_ratio * radius

        self.dimensions = {
            'shape': 'cylinder',
            'radius': round(radius, 2),
            'height': round(height, 2)
        }

    def _calculate_cube_dimensions(self):
        """Calculates the side length of a cube given its volume."""
        # For a cube, volume = a^3
        side_length = self.volume ** (1/3)

        self.dimensions = {
            'shape': 'cube',
            'side_length': round(side_length, 2)
        }

    def _calculate_sphere_dimensions(self):
        """Calculates the radius of a sphere given its volume."""
        import math

        # For a sphere, volume = (4/3) * π * r^3
        radius = ((3 * self.volume) / (4 * math.pi)) ** (1/3)

        self.dimensions = {
            'shape': 'sphere',
            'radius': round(radius, 2)
        }


def main():
    """Main function to execute the tank dimension calculator."""
    try:
        # User input for volume and shape
        volume = float(input("Enter the volume of the tank in cubic meters: "))
        shape = input("Enter the shape of the tank (cylinder, cube, sphere): ")

        # Create an instance of the TankDimensionCalculator
        tank_calculator = TankDimensionCalculator(volume, shape)

        # Calculate dimensions
        dimensions = tank_calculator.calculate_dimensions()

        # Print the calculated dimensions
        if dimensions:
            print(f"Calculated dimensions for the {dimensions['shape']}: {dimensions}")

    except ValueError as e:
        print(f"Error: {e}. Please enter valid numeric values for volume and correct shape.")

if __name__ == "__main__":
    main()
```
