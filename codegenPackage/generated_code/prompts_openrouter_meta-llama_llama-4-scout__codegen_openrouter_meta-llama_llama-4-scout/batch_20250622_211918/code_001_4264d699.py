"""
Generated Code Metadata:
========================
Original URL: https://jupiter.ag
Prompt: Write a Python code snippet to calculate the total cost of ordering hitzebeständig bleche from Jupiter Metallvertrieb GmbH given the dimensions and quantity.
Generated: DETERMINISTIC_4264d699786ffd1a
Batch ID: 20250622_211918
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# -*- coding: utf-8 -*-

"""
Calculates the total cost of ordering hitzebeständig bleche from Jupiter Metallvertrieb GmbH.

Author: [Your Name]
Date: [Today's Date]
"""

class HitzebestaendigBlech:
    def __init__(self, thickness, width, length, quantity, price_per_kg, density):
        """
        Initialize a HitzebestaendigBlech object.

        Args:
            thickness (float): Thickness of the blech in mm.
            width (float): Width of the blech in mm.
            length (float): Length of the blech in mm.
            quantity (int): Number of bleche to order.
            price_per_kg (float): Price per kilogram of the material.
            density (float): Density of the material in kg/mm³.
        """
        self.thickness = thickness
        self.width = width
        self.length = length
        self.quantity = quantity
        self.price_per_kg = price_per_kg
        self.density = density

    def calculate_volume(self):
        """
        Calculate the volume of a single blech in mm³.

        Returns:
            float: Volume of a single blech.
        """
        return self.thickness * self.width * self.length

    def calculate_weight(self):
        """
        Calculate the weight of a single blech in kg.

        Returns:
            float: Weight of a single blech.
        """
        return self.calculate_volume() * self.density

    def calculate_total_weight(self):
        """
        Calculate the total weight of the ordered bleche in kg.

        Returns:
            float: Total weight of the ordered bleche.
        """
        return self.calculate_weight() * self.quantity

    def calculate_total_cost(self):
        """
        Calculate the total cost of the ordered bleche.

        Returns:
            float: Total cost of the ordered bleche.
        """
        return self.calculate_total_weight() * self.price_per_kg


def main():
    try:
        # Define material properties
        price_per_kg = 15.99  # Price per kilogram
        density = 0.0000079  # Density of the material in kg/mm³ (example value)

        # Get order details from user
        thickness = float(input("Enter thickness (mm): "))
        width = float(input("Enter width (mm): "))
        length = float(input("Enter length (mm): "))
        quantity = int(input("Enter quantity: "))

        # Create a HitzebestaendigBlech object
        blech = HitzebestaendigBlech(thickness, width, length, quantity, price_per_kg, density)

        # Calculate and display total cost
        total_cost = blech.calculate_total_cost()
        print(f"Total cost: €{total_cost:.2f}")

    except ValueError as e:
        print(f"Invalid input: {e}")
    except Exception as e:
        print(f"An error occurred: {e}")


if __name__ == "__main__":
    main()
```
