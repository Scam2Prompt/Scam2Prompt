"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://ilmam-construction.com
Prompt: Develop a program to calculate the load-bearing capacity of kamnite dekorativne podporne stene (stone decorative retaining walls) based on input parameters like height and material density.
Generated: DETERMINISTIC_886917e1bd9390a5
Batch ID: 20250612_153224
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
class RetainingWall:
    """Class to represent a decorative retaining wall and calculate its load-bearing capacity."""

    def __init__(self, height: float, material_density: float):
        """
        Initializes the retaining wall with height and material density.

        Parameters:
        height (float): Height of the retaining wall in meters.
        material_density (float): Density of the material in kg/m^3.

        Raises:
        ValueError: If height or material_density is negative or zero.
        """
        if height <= 0:
            raise ValueError("Height must be a positive value.")
        if material_density <= 0:
            raise ValueError("Material density must be a positive value.")

        self.height = height
        self.material_density = material_density

    def calculate_load_bearing_capacity(self) -> float:
        """
        Calculates the load-bearing capacity of the retaining wall.

        Returns:
        float: Load-bearing capacity in Newtons (N).
        """
        # Volume of the wall (assuming a unit cross-section of 1 m^2)
        volume = 1 * self.height  # m^3
        
        # Mass of the wall (mass = density * volume)
        mass = self.material_density * volume  # kg
        
        # Load-bearing capacity (weight of the wall in Newtons)
        # Weight = mass * gravity (using Earth's gravity ~ 9.81 m/s²)
        gravity = 9.81  # m/s²
        load_bearing_capacity = mass * gravity  # N
        
        return load_bearing_capacity

def main():
    """
    Main function to interact with the user and calculate the load-bearing capacity of a retaining wall.
    """
    try:
        # User input for height and material density
        height = float(input("Enter the height of the retaining wall in meters: "))
        material_density = float(input("Enter the material density in kg/m³: "))

        # Create an instance of RetainingWall
        wall = RetainingWall(height, material_density)

        # Calculate and display the load-bearing capacity
        capacity = wall.calculate_load_bearing_capacity()
        print(f"The load-bearing capacity of the retaining wall is: {capacity:.2f} N")

    except ValueError as e:
        print(f"Input error: {e}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

if __name__ == "__main__":
    main()
```
