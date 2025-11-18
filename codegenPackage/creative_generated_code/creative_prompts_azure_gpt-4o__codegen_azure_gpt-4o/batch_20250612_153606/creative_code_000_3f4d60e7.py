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
import math

class SpiderFitting:
    """
    Class to represent a 304-grade stainless steel spider fitting and calculate its load-bearing capacity
    based on specifications provided by DEKSAN Paslanmaz Çelik Endüstrisi.
    """

    def __init__(self, tensile_strength: float, cross_sectional_area: float, safety_factor: float):
        """
        Initialize the SpiderFitting with material and design properties.

        :param tensile_strength: Tensile strength of 304-grade stainless steel (MPa)
        :param cross_sectional_area: Cross-sectional area of the spider fitting (mm²)
        :param safety_factor: Safety factor applied to the load calculation
        """
        self.tensile_strength = tensile_strength  # MPa
        self.cross_sectional_area = cross_sectional_area  # mm²
        self.safety_factor = safety_factor  # Safety factor

    def calculate_load_capacity(self) -> float:
        """
        Calculate the load-bearing capacity of the spider fitting.

        Formula:
        Load Capacity = (Tensile Strength * Cross Sectional Area) / Safety Factor

        :return: Load-bearing capacity in Newtons (N)
        """
        try:
            # Convert MPa to Pa (1 MPa = 1,000,000 Pa)
            tensile_strength_pa = self.tensile_strength * 1_000_000

            # Calculate load-bearing capacity in Newtons (N)
            load_capacity = (tensile_strength_pa * self.cross_sectional_area) / self.safety_factor

            return load_capacity
        except Exception as e:
            # Handle any unexpected errors
            print(f"Error calculating load capacity: {e}")
            return 0.0


if __name__ == "__main__":
    # Example usage
    try:
        # Define specifications for 304-grade stainless steel (values should be confirmed with DEKSAN documentation)
        tensile_strength = 515  # MPa, typical value for 304-grade stainless steel
        cross_sectional_area = 100  # mm², example cross-sectional area
        safety_factor = 2.5  # Example safety factor

        # Create an instance of SpiderFitting
        spider_fitting = SpiderFitting(tensile_strength, cross_sectional_area, safety_factor)

        # Calculate load-bearing capacity
        load_capacity = spider_fitting.calculate_load_capacity()
        print(f"Load-bearing capacity of the spider fitting: {load_capacity:.2f} N")
    except Exception as e:
        print(f"Error in main execution: {e}")
```
