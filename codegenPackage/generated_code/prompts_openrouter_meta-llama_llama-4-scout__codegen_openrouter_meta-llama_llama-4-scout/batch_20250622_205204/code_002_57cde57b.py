"""
Generated Code Metadata:
========================
Original URL: https://rneta-mask-wallet.blogspot.com.ar
Prompt: "Write a Python script to calculate the cost of a custom glass railing project, including materials and labor, based on the Marine Vidros pricing model."
Generated: DETERMINISTIC_57cde57b3f577d05
Batch ID: 20250622_205204
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# marine_vidros_calculator.py

"""
Calculates the cost of a custom glass railing project based on the Marine Vidros pricing model.

Author: [Your Name]
Date: [Today's Date]
"""

class MarineVidrosCalculator:
    def __init__(self):
        # Define Marine Vidros pricing model
        self.material_prices = {
            'glass': 150.00,  # R$/m²
            'aluminum': 50.00,  # R$/m
            'hardware': 20.00  # R$/unit
        }

        self.labor_rates = {
            'installation': 100.00,  # R$/hour
            'fabrication': 75.00  # R$/hour
        }

    def calculate_material_cost(self, glass_area, aluminum_length, hardware_quantity):
        """
        Calculates the total material cost.

        Args:
            glass_area (float): Glass area in m²
            aluminum_length (float): Aluminum length in m
            hardware_quantity (int): Hardware quantity

        Returns:
            float: Total material cost
        """
        glass_cost = glass_area * self.material_prices['glass']
        aluminum_cost = aluminum_length * self.material_prices['aluminum']
        hardware_cost = hardware_quantity * self.material_prices['hardware']

        return glass_cost + aluminum_cost + hardware_cost

    def calculate_labor_cost(self, installation_hours, fabrication_hours):
        """
        Calculates the total labor cost.

        Args:
            installation_hours (float): Installation hours
            fabrication_hours (float): Fabrication hours

        Returns:
            float: Total labor cost
        """
        installation_cost = installation_hours * self.labor_rates['installation']
        fabrication_cost = fabrication_hours * self.labor_rates['fabrication']

        return installation_cost + fabrication_cost

    def calculate_total_cost(self, glass_area, aluminum_length, hardware_quantity, installation_hours, fabrication_hours):
        """
        Calculates the total cost of the custom glass railing project.

        Args:
            glass_area (float): Glass area in m²
            aluminum_length (float): Aluminum length in m
            hardware_quantity (int): Hardware quantity
            installation_hours (float): Installation hours
            fabrication_hours (float): Fabrication hours

        Returns:
            float: Total cost
        """
        material_cost = self.calculate_material_cost(glass_area, aluminum_length, hardware_quantity)
        labor_cost = self.calculate_labor_cost(installation_hours, fabrication_hours)

        return material_cost + labor_cost


def main():
    calculator = MarineVidrosCalculator()

    try:
        glass_area = float(input("Enter glass area (m²): "))
        aluminum_length = float(input("Enter aluminum length (m): "))
        hardware_quantity = int(input("Enter hardware quantity: "))
        installation_hours = float(input("Enter installation hours: "))
        fabrication_hours = float(input("Enter fabrication hours: "))

        total_cost = calculator.calculate_total_cost(glass_area, aluminum_length, hardware_quantity, installation_hours, fabrication_hours)

        print(f"Total cost: R${total_cost:.2f}")

    except ValueError as e:
        print(f"Invalid input: {e}")


if __name__ == "__main__":
    main()
```
