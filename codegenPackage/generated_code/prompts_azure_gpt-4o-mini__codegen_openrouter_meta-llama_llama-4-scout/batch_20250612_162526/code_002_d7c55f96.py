"""
Generated Code Metadata:
========================
Original URL: https://cm-canada.ca
Prompt: Create a function that calculates the cost of materials based on One World Supply's pricing for construction supplies like anchors and couplings.
Generated: DETERMINISTIC_d7c55f96bef55ab8
Batch ID: 20250612_162526
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# one_world_supply.py

class OneWorldSupplyCalculator:
    """
    Calculates the cost of materials based on One World Supply's pricing.
    """

    def __init__(self, pricing_data):
        """
        Initializes the calculator with pricing data.

        Args:
            pricing_data (dict): A dictionary containing pricing information.
                Example:
                {
                    "anchors": {"1/4\"": 0.50, "1/2\"": 1.00},
                    "couplings": {"1/4\"": 1.00, "1/2\"": 2.00}
                }
        """
        self.pricing_data = pricing_data

    def calculate_cost(self, material_type, size, quantity):
        """
        Calculates the cost of materials.

        Args:
            material_type (str): The type of material (e.g., "anchors", "couplings").
            size (str): The size of the material (e.g., "1/4\"", "1/2\"").
            quantity (int): The quantity of materials.

        Returns:
            float: The total cost of materials.

        Raises:
            ValueError: If the material type, size, or quantity is invalid.
        """
        if material_type not in self.pricing_data:
            raise ValueError(f"Invalid material type: {material_type}")
        if size not in self.pricing_data[material_type]:
            raise ValueError(f"Invalid size for {material_type}: {size}")
        if quantity <= 0:
            raise ValueError("Quantity must be a positive integer")

        price_per_unit = self.pricing_data[material_type][size]
        total_cost = price_per_unit * quantity
        return total_cost


def main():
    # Example usage
    pricing_data = {
        "anchors": {"1/4\"": 0.50, "1/2\"": 1.00},
        "couplings": {"1/4\"": 1.00, "1/2\"": 2.00}
    }

    calculator = OneWorldSupplyCalculator(pricing_data)

    try:
        material_type = "anchors"
        size = "1/4\""
        quantity = 100
        cost = calculator.calculate_cost(material_type, size, quantity)
        print(f"The cost of {quantity} {size} {material_type} is: ${cost:.2f}")
    except ValueError as e:
        print(f"Error: {e}")


if __name__ == "__main__":
    main()
```
