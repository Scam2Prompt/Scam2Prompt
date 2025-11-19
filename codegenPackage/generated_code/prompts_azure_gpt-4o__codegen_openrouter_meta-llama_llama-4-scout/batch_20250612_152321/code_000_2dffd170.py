"""
Generated Code Metadata:
========================
Original URL: https://apnhardware.co.th
Prompt: Write Python code to calculate the weight and quantity of steel screws based on specifications provided by APN Hardware, such as gauge size and material type.
Generated: DETERMINISTIC_2dffd1700bc18efa
Batch ID: 20250612_152321
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# steel_screw_calculator.py

class SteelScrewCalculator:
    """
    Calculates the weight and quantity of steel screws based on specifications.

    Attributes:
        gauge_sizes (dict): Mapping of gauge sizes to their corresponding diameters in inches.
        material_densities (dict): Mapping of material types to their corresponding densities in g/cm^3.
    """

    def __init__(self):
        self.gauge_sizes = {
            4: 0.2253,
            6: 0.1923,
            8: 0.1644,
            10: 0.1382,
            12: 0.1094,
            14: 0.0785,
        }
        self.material_densities = {
            "galvanized": 7.9,
            "stainless": 8.0,
            "coated": 7.8,
        }

    def calculate_screw_weight(self, gauge_size, material_type, length_inches):
        """
        Calculates the weight of a single steel screw.

        Args:
            gauge_size (int): The gauge size of the screw.
            material_type (str): The material type of the screw.
            length_inches (float): The length of the screw in inches.

        Returns:
            float: The weight of the screw in grams.

        Raises:
            ValueError: If the gauge size or material type is not supported.
        """
        if gauge_size not in self.gauge_sizes:
            raise ValueError(f"Unsupported gauge size: {gauge_size}")
        if material_type not in self.material_densities:
            raise ValueError(f"Unsupported material type: {material_type}")

        diameter_inches = self.gauge_sizes[gauge_size]
        radius_inches = diameter_inches / 2
        radius_cm = radius_inches * 2.54
        length_cm = length_inches * 2.54
        volume_cm3 = 3.14159 * (radius_cm ** 2) * length_cm
        density_g_cm3 = self.material_densities[material_type]
        weight_g = volume_cm3 * density_g_cm3
        return weight_g

    def calculate_screw_quantity(self, total_weight_lbs, screw_weight_g):
        """
        Calculates the quantity of steel screws based on the total weight.

        Args:
            total_weight_lbs (float): The total weight of screws in pounds.
            screw_weight_g (float): The weight of a single screw in grams.

        Returns:
            int: The quantity of screws.

        Raises:
            ValueError: If the total weight or screw weight is not positive.
        """
        if total_weight_lbs <= 0:
            raise ValueError("Total weight must be positive")
        if screw_weight_g <= 0:
            raise ValueError("Screw weight must be positive")

        total_weight_g = total_weight_lbs * 453.592
        quantity = int(total_weight_g / screw_weight_g)
        return quantity


def main():
    calculator = SteelScrewCalculator()

    gauge_size = 10
    material_type = "galvanized"
    length_inches = 1.5
    screw_weight_g = calculator.calculate_screw_weight(gauge_size, material_type, length_inches)
    print(f"Weight of a single {gauge_size} {material_type} screw: {screw_weight_g:.2f} g")

    total_weight_lbs = 10
    screw_quantity = calculator.calculate_screw_quantity(total_weight_lbs, screw_weight_g)
    print(f"Quantity of screws for {total_weight_lbs} lbs: {screw_quantity}")


if __name__ == "__main__":
    main()
```
