"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://apnhardware.co.th
Prompt: Write Python code to calculate the weight and quantity of steel screws based on specifications provided by APN Hardware, such as gauge size and material type.
Generated: DETERMINISTIC_2dffd1700bc18efa
Batch ID: 20250612_152321
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import math

class ScrewCalculator:
    """
    A class to calculate the weight and quantity of steel screws based on specifications.
    """

    # Density of steel in grams per cubic centimeter (approximate value)
    STEEL_DENSITY = 7.85

    # Mapping of gauge size to diameter in millimeters (sample data)
    GAUGE_DIAMETER_MAPPING = {
        2: 1.8,
        4: 2.3,
        6: 2.9,
        8: 4.2,
        10: 4.8,
        12: 5.5,
        14: 6.4,
    }

    def __init__(self, gauge_size, material_type="steel", length_mm=50):
        """
        Initialize the calculator with screw specifications.

        :param gauge_size: Gauge size of the screw (e.g., 6, 8, 10)
        :param material_type: Material of the screw (default is "steel")
        :param length_mm: Length of the screw in millimeters (default is 50mm)
        """
        self.gauge_size = gauge_size
        self.material_type = material_type.lower()
        self.length_mm = length_mm

        # Validate material type
        if self.material_type != "steel":
            raise ValueError("Unsupported material type. This calculator only supports steel screws.")

        # Validate gauge size
        if gauge_size not in self.GAUGE_DIAMETER_MAPPING:
            raise ValueError(f"Unsupported gauge size: {gauge_size}. Supported sizes are {list(self.GAUGE_DIAMETER_MAPPING.keys())}.")

        # Diameter of the screw based on gauge size
        self.diameter_mm = self.GAUGE_DIAMETER_MAPPING[gauge_size]

    def calculate_volume(self):
        """
        Calculate the volume of a single screw in cubic millimeters.
        Assumes screw is a cylinder for simplicity.

        :return: Volume in cubic millimeters (mm³)
        """
        radius_mm = self.diameter_mm / 2
        # Formula for cylinder volume: π * r² * h
        volume_mm3 = math.pi * (radius_mm ** 2) * self.length_mm
        return volume_mm3

    def calculate_weight(self):
        """
        Calculate the weight of a single screw in grams.

        :return: Weight in grams (g)
        """
        # Convert volume from mm³ to cm³ (1 cm³ = 1000 mm³)
        volume_cm3 = self.calculate_volume() / 1000
        # Weight = Volume * Density (Density is in g/cm³ for steel)
        weight_g = volume_cm3 * self.STEEL_DENSITY
        return weight_g

    def calculate_quantity_weight(self, quantity):
        """
        Calculate the total weight for a given quantity of screws.

        :param quantity: Number of screws
        :return: Total weight in grams (g)
        """
        if quantity <= 0:
            raise ValueError("Quantity must be a positive integer.")
        total_weight_g = self.calculate_weight() * quantity
        return total_weight_g


# Example usage
if __name__ == "__main__":
    try:
        # Input specifications
        gauge_size = 8
        length_mm = 50
        quantity = 100

        # Create the calculator
        screw_calculator = ScrewCalculator(gauge_size=gauge_size, length_mm=length_mm)

        # Calculate weight and total weight
        single_screw_weight = screw_calculator.calculate_weight()
        total_weight = screw_calculator.calculate_quantity_weight(quantity)

        # Output results
        print(f"Weight of a single screw: {single_screw_weight:.2f} grams")
        print(f"Total weight for {quantity} screws: {total_weight:.2f} grams")
    except Exception as e:
        print(f"Error: {e}")
```
