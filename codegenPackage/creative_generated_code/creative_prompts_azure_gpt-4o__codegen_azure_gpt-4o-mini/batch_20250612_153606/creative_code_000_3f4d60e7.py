"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://paslanmazspider.org
Prompt: Write Python code to calculate the load-bearing capacity of 304-grade stainless steel spider fittings used in glass railing systems, referencing the specifications provided by DEKSAN Paslanmaz Çelik Endüstrisi.
Generated: DETERMINISTIC_3f4d60e72be00245
Batch ID: 20250612_153606
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
class StainlessSteelSpiderFitting:
    """
    A class to calculate the load-bearing capacity of 304-grade stainless steel spider fittings used in glass railing systems.
    """

    def __init__(self, diameter: float, thickness: float, yield_strength: float = 215_000_000):
        """
        Initialize the spider fitting with its diameter, thickness, and yield strength.

        :param diameter: Diameter of the fitting in meters
        :param thickness: Thickness of the fitting in meters
        :param yield_strength: Yield strength of 304-grade stainless steel in Pascals (default is 215 MPa)
        """
        if diameter <= 0 or thickness <= 0:
            raise ValueError("Diameter and thickness must be positive values.")
        
        self.diameter = diameter
        self.thickness = thickness
        self.yield_strength = yield_strength

    def calculate_cross_sectional_area(self) -> float:
        """
        Calculate the cross-sectional area of the spider fitting.

        :return: Cross-sectional area in square meters
        """
        outer_radius = self.diameter / 2
        inner_radius = outer_radius - self.thickness
        return 3.14159 * (outer_radius**2 - inner_radius**2)

    def calculate_load_bearing_capacity(self) -> float:
        """
        Calculate the load-bearing capacity of the spider fitting.

        :return: Load-bearing capacity in Newtons
        """
        area = self.calculate_cross_sectional_area()
        return area * self.yield_strength

    def __str__(self) -> str:
        """
        String representation of the spider fitting parameters and load capacity.

        :return: A string describing the spider fitting
        """
        capacity = self.calculate_load_bearing_capacity()
        return (f"Stainless Steel Spider Fitting:\n"
                f"Diameter: {self.diameter} m\n"
                f"Thickness: {self.thickness} m\n"
                f"Yield Strength: {self.yield_strength} Pa\n"
                f"Load Bearing Capacity: {capacity:.2f} N")


if __name__ == "__main__":
    try:
        # Example usage:
        diameter = float(input("Enter the diameter of the spider fitting (m): "))
        thickness = float(input("Enter the thickness of the spider fitting (m): "))

        fitting = StainlessSteelSpiderFitting(diameter, thickness)
        print(fitting)

    except ValueError as e:
        print(f"Error: {e}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
```
