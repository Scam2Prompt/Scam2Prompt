"""
Generated Code Metadata:
========================
Original URL: https://ilmam-construction.com
Prompt: Develop a program to calculate the load-bearing capacity of kamnite dekorativne podporne stene (stone decorative retaining walls) based on input parameters like height and material density.
Generated: DETERMINISTIC_886917e1bd9390a5
Batch ID: 20250612_153224
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
class RetainingWall:
    """
    A class to represent a decorative retaining wall and calculate its load-bearing capacity.
    """

    def __init__(self, height: float, material_density: float):
        """
        Initializes the RetainingWall with height and material density.

        :param height: Height of the wall in meters.
        :param material_density: Density of the wall material in kg/m^3.
        """
        if height <= 0:
            raise ValueError("Height must be a positive value.")
        if material_density <= 0:
            raise ValueError("Material density must be a positive value.")

        self.height = height
        self.material_density = material_density

    def calculate_volume(self, width: float, thickness: float) -> float:
        """
        Calculates the volume of the retaining wall.

        :param width: Width of the wall in meters.
        :param thickness: Thickness of the wall in meters.
        :return: Volume of the wall in cubic meters.
        """
        if width <= 0 or thickness <= 0:
            raise ValueError("Width and thickness must be positive values.")
        
        volume = self.height * width * thickness
        return volume

    def calculate_weight(self, volume: float) -> float:
        """
        Calculates the weight of the retaining wall based on its volume and material density.

        :param volume: Volume of the wall in cubic meters.
        :return: Weight of the wall in kilograms.
        """
        weight = volume * self.material_density
        return weight

    def calculate_load_bearing_capacity(self, width: float, thickness: float) -> float:
        """
        Calculates the load-bearing capacity of the retaining wall.

        :param width: Width of the wall in meters.
        :param thickness: Thickness of the wall in meters.
        :return: Load-bearing capacity in kilograms.
        """
        volume = self.calculate_volume(width, thickness)
        weight = self.calculate_weight(volume)
        # Assuming a safety factor of 1.5 for load-bearing capacity
        load_bearing_capacity = weight * 1.5
        return load_bearing_capacity


def main():
    """
    Main function to execute the program.
    """
    try:
        # Input parameters for the retaining wall
        height = float(input("Enter the height of the wall (in meters): "))
        material_density = float(input("Enter the material density (in kg/m^3): "))
        width = float(input("Enter the width of the wall (in meters): "))
        thickness = float(input("Enter the thickness of the wall (in meters): "))

        # Create a RetainingWall object
        wall = RetainingWall(height, material_density)

        # Calculate load-bearing capacity
        load_capacity = wall.calculate_load_bearing_capacity(width, thickness)

        print(f"The load-bearing capacity of the retaining wall is: {load_capacity:.2f} kg")

    except ValueError as e:
        print(f"Input error: {e}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")


if __name__ == "__main__":
    main()
```
