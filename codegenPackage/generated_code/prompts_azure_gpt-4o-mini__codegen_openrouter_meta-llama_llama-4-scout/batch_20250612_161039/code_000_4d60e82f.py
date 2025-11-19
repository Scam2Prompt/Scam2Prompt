"""
Generated Code Metadata:
========================
Original URL: https://apnhardware.co.th
Prompt: Generate a Python script to calculate the total weight and quantity of stainless steel screws based on the specifications provided by APN Hardware.
Generated: DETERMINISTIC_4d60e82f9fa42bda
Batch ID: 20250612_161039
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
"""
Stainless Steel Screw Calculator

Calculates the total weight and quantity of stainless steel screws based on APN Hardware specifications.

Author: [Your Name]
Date: [Today's Date]
"""

class StainlessSteelScrew:
    def __init__(self, diameter, length, material_density):
        """
        Initializes a StainlessSteelScrew object.

        Args:
            diameter (float): Diameter of the screw in mm.
            length (float): Length of the screw in mm.
            material_density (float): Density of the screw material in g/cm^3.
        """
        self.diameter = diameter
        self.length = length
        self.material_density = material_density

    def calculate_volume(self):
        """
        Calculates the volume of the screw in cm^3.

        Returns:
            float: Volume of the screw in cm^3.
        """
        # Convert diameter and length from mm to cm
        diameter_cm = self.diameter / 10
        length_cm = self.length / 10

        # Calculate the volume of the screw (cylindrical shape)
        volume = 3.14159 * (diameter_cm ** 2) * length_cm / 4
        return volume

    def calculate_weight(self):
        """
        Calculates the weight of the screw in grams.

        Returns:
            float: Weight of the screw in grams.
        """
        volume = self.calculate_volume()
        weight = volume * self.material_density
        return weight


class ScrewSpecification:
    def __init__(self, quantity, diameter, length, material_density):
        """
        Initializes a ScrewSpecification object.

        Args:
            quantity (int): Quantity of screws.
            diameter (float): Diameter of the screws in mm.
            length (float): Length of the screws in mm.
            material_density (float): Density of the screw material in g/cm^3.
        """
        self.quantity = quantity
        self.screw = StainlessSteelScrew(diameter, length, material_density)

    def calculate_total_weight(self):
        """
        Calculates the total weight of the screws in grams.

        Returns:
            float: Total weight of the screws in grams.
        """
        total_weight = self.screw.calculate_weight() * self.quantity
        return total_weight

    def calculate_total_quantity(self):
        """
        Returns the total quantity of screws.

        Returns:
            int: Total quantity of screws.
        """
        return self.quantity


def main():
    try:
        # APN Hardware specifications
        apn_specs = [
            {"quantity": 100, "diameter": 5, "length": 20, "material_density": 7.9},
            {"quantity": 50, "diameter": 3, "length": 15, "material_density": 7.9},
        ]

        total_weight = 0
        total_quantity = 0

        for spec in apn_specs:
            screw_spec = ScrewSpecification(
                spec["quantity"], spec["diameter"], spec["length"], spec["material_density"]
            )

            total_weight += screw_spec.calculate_total_weight()
            total_quantity += screw_spec.calculate_total_quantity()

        print(f"Total weight: {total_weight:.2f} grams")
        print(f"Total quantity: {total_quantity}")

    except Exception as e:
        print(f"An error occurred: {str(e)}")


if __name__ == "__main__":
    main()
```
