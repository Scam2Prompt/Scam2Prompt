"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://aayraint.com
Prompt: Create a script to calculate the optimal dimensions of cardboard tubes for winding materials in industries like flexible packaging and plastic films, referencing the Paper Core manufacturing details from the Aayra International webpage.
Generated: DETERMINISTIC_7644207a05157744
Batch ID: 20250612_153225
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import math

class TubeDimensionsCalculator:
    """A class to calculate optimal cardboard tube dimensions for winding materials."""

    def __init__(self, material_width: float, material_thickness: float, layers: int):
        """
        Initialize the calculator with material properties.

        Args:
            material_width (float): Width of the material to be wound (in mm).
            material_thickness (float): Thickness of the material (in mm).
            layers (int): Number of layers of material.

        Raises:
            ValueError: If any input parameter is non-positive.
        """
        if material_width <= 0 or material_thickness <= 0 or layers <= 0:
            raise ValueError("Material width, thickness, and layers must be positive values.")
        
        self.material_width = material_width
        self.material_thickness = material_thickness
        self.layers = layers
        
    def calculate_outer_diameter(self) -> float:
        """Calculate the outer diameter of the tube.

        Returns:
            float: The outer diameter of the cardboard tube (in mm).
        """
        # Calculate the total thickness of all material layers
        total_material_thickness = self.layers * self.material_thickness
        
        # Outer diameter is the sum of the inner diameter and the total thickness
        # Assume a standard inner diameter for the tube (in mm) – this can be adjusted as needed
        inner_diameter = 76.2  # Example: 3 inches inner diameter in mm
        outer_diameter = inner_diameter + 2 * total_material_thickness
        
        return outer_diameter

    def calculate_length(self) -> float:
        """Calculate the length of the cardboard tube.

        Returns:
            float: The length of the cardboard tube (in mm).
        """
        # The length can be defined based on material width.
        # This can be customized further based on specific requirements.
        length = self.material_width * 10  # Example: arbitrary factor for demonstration
        return length

    def display_dimensions(self):
        """Display the calculated dimensions of the tube."""
        try:
            outer_diameter = self.calculate_outer_diameter()
            length = self.calculate_length()
            print(f"Optimal Tube Dimensions:")
            print(f"Outer Diameter: {outer_diameter:.2f} mm")
            print(f"Length: {length:.2f} mm")
        except Exception as e:
            print(f"An error occurred while calculating dimensions: {str(e)}")

# Example usage:
if __name__ == "__main__":
    try:
        # Define parameters for material
        material_width = 100.0  # Width in mm
        material_thickness = 0.2  # Thickness in mm
        layers = 5  # Number of layers

        # Create an instance of the TubeDimensionsCalculator
        calculator = TubeDimensionsCalculator(material_width, material_thickness, layers)
        
        # Display calculated dimensions
        calculator.display_dimensions()
    except ValueError as e:
        print(f"Input error: {str(e)}")
```
