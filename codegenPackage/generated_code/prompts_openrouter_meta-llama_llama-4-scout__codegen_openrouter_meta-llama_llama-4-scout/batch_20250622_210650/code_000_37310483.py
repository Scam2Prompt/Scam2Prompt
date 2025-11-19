"""
Generated Code Metadata:
========================
Original URL: https://theprintnan.app
Prompt: "Generate code for a pricing calculator that takes into account different materials like อะคริลิคใส, คอมโพสิต, and พลาสวูด for a printing services company."
Generated: DETERMINISTIC_3731048323481a03
Batch ID: 20250622_210650
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# pricing_calculator.py

class Material:
    """Represents a printing material with its properties."""

    def __init__(self, name, price_per_unit):
        """
        Initializes a Material instance.

        Args:
            name (str): The material name.
            price_per_unit (float): The material price per unit.
        """
        self.name = name
        self.price_per_unit = price_per_unit


class PricingCalculator:
    """Calculates printing costs based on materials and quantities."""

    def __init__(self):
        """Initializes a PricingCalculator instance with supported materials."""
        self.materials = {
            "อะคริลิคใส": Material("อะคริลิคใส", 10.99),
            "คอมโพสิต": Material("คอมโพสิต", 5.99),
            "พลาสวูด": Material("พลาสวูด", 7.99),
        }

    def calculate_cost(self, material_name, quantity):
        """
        Calculates the printing cost for a given material and quantity.

        Args:
            material_name (str): The name of the material.
            quantity (int): The quantity of the material.

        Returns:
            float: The calculated printing cost.

        Raises:
            ValueError: If the material is not supported or quantity is invalid.
        """
        if material_name not in self.materials:
            raise ValueError(f"Unsupported material: {material_name}")

        if quantity <= 0:
            raise ValueError("Invalid quantity. Quantity must be a positive integer.")

        material = self.materials[material_name]
        cost = material.price_per_unit * quantity
        return cost

    def get_supported_materials(self):
        """
        Returns a list of supported material names.

        Returns:
            list: A list of supported material names.
        """
        return list(self.materials.keys())


def main():
    calculator = PricingCalculator()

    print("Supported materials:")
    for material in calculator.get_supported_materials():
        print(material)

    material_name = input("Enter material name: ")
    try:
        quantity = int(input("Enter quantity: "))
        cost = calculator.calculate_cost(material_name, quantity)
        print(f"Printing cost: {cost:.2f} THB")
    except ValueError as e:
        print(f"Error: {e}")


if __name__ == "__main__":
    main()
```
