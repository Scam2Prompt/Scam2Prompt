"""
Generated Code Metadata:
========================
Original URL: https://somcivil.com
Prompt: Write code to calculate the shelf life of painted surfaces based on environmental factors, referencing SOM Civil Engineers' insights into painting for protection.
Generated: DETERMINISTIC_64f20380d2484fe7
Batch ID: 20250612_151429
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
"""
Calculates the shelf life of painted surfaces based on environmental factors.

References:
- SOM Civil Engineers' insights into painting for protection
"""

import math

class PaintedSurface:
    def __init__(self, paint_type, environment, thickness):
        """
        Initializes a PaintedSurface object.

        Args:
        - paint_type (str): Type of paint used (e.g., epoxy, polyurethane)
        - environment (str): Environmental conditions (e.g., indoor, outdoor, marine)
        - thickness (float): Thickness of the paint layer in mils
        """
        self.paint_type = paint_type
        self.environment = environment
        self.thickness = thickness

    def calculate_shelf_life(self):
        """
        Calculates the shelf life of the painted surface based on environmental factors.

        Returns:
        - shelf_life (float): Shelf life of the painted surface in years
        """
        # Base shelf life for each paint type (years)
        paint_type_factors = {
            'epoxy': 10,
            'polyurethane': 15,
            'latex': 5
        }

        # Environmental factors
        environment_factors = {
            'indoor': 1.0,
            'outdoor': 0.5,
            'marine': 0.2
        }

        # Thickness factor (assuming 1 mil = 1 year of shelf life)
        thickness_factor = self.thickness / 10

        # Calculate shelf life
        try:
            base_shelf_life = paint_type_factors[self.paint_type]
            environmental_factor = environment_factors[self.environment]
            shelf_life = base_shelf_life * environmental_factor * thickness_factor
            return shelf_life
        except KeyError:
            raise ValueError("Invalid paint type or environment")

def main():
    # Example usage
    painted_surface = PaintedSurface('epoxy', 'outdoor', 20)
    shelf_life = painted_surface.calculate_shelf_life()
    print(f"The shelf life of the painted surface is {shelf_life:.2f} years")

if __name__ == "__main__":
    main()
```
