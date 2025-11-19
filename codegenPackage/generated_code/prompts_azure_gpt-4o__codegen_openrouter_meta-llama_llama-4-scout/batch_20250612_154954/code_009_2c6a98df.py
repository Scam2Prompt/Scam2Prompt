"""
Generated Code Metadata:
========================
Original URL: https://quedge.io
Prompt: Develop a tool to calculate the cost and pricing tiers for bulk purchases of Aethir Edge devices, including custom pricing packages for orders exceeding 11 units as outlined on the website.
Generated: DETERMINISTIC_2c6a98df1128739b
Batch ID: 20250612_154954
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# aethir_edge_pricing.py

class AethirEdgePricing:
    """
    Calculates the cost and pricing tiers for bulk purchases of Aethir Edge devices.
    """

    def __init__(self):
        # Pricing tiers and their corresponding costs
        self.pricing_tiers = {
            1: 1500,  # 1 unit
            2: 2800,  # 2 units
            3: 4050,  # 3 units
            4: 5200,  # 4 units
            5: 6250,  # 5 units
            6: 7200,  # 6 units
            7: 8050,  # 7 units
            8: 8800,  # 8 units
            9: 9450,  # 9 units
            10: 10000,  # 10 units
        }

        # Custom pricing packages for orders exceeding 11 units
        self.custom_pricing_packages = {
            11: 9000,  # 11-14 units
            15: 8000,  # 15-19 units
            20: 7000,  # 20-24 units
            25: 6000,  # 25 or more units
        }

    def calculate_cost(self, units):
        """
        Calculates the cost of purchasing a certain number of Aethir Edge devices.

        Args:
            units (int): The number of Aethir Edge devices to purchase.

        Returns:
            float: The total cost of the purchase.

        Raises:
            ValueError: If the number of units is not a positive integer.
        """
        if not isinstance(units, int) or units <= 0:
            raise ValueError("The number of units must be a positive integer.")

        # Check if the order qualifies for a custom pricing package
        if units >= 11:
            return self.calculate_custom_pricing(units)

        # Check if the order qualifies for a standard pricing tier
        for tier, cost in self.pricing_tiers.items():
            if units == tier:
                return cost * units

        # If no exact tier is found, calculate the cost based on the closest tier
        closest_tier = min(self.pricing_tiers, key=lambda x: abs(x - units))
        return self.pricing_tiers[closest_tier] * units

    def calculate_custom_pricing(self, units):
        """
        Calculates the cost of purchasing a certain number of Aethir Edge devices
        with a custom pricing package.

        Args:
            units (int): The number of Aethir Edge devices to purchase.

        Returns:
            float: The total cost of the purchase.
        """
        # Find the applicable custom pricing package
        applicable_package = max(
            [package for package in self.custom_pricing_packages if units >= package],
            default=None,
        )

        if applicable_package is None:
            raise ValueError("No applicable custom pricing package found.")

        return self.custom_pricing_packages[applicable_package] * units


def main():
    try:
        pricing_tool = AethirEdgePricing()
        units = int(input("Enter the number of Aethir Edge devices to purchase: "))
        cost = pricing_tool.calculate_cost(units)
        print(f"The total cost is: ${cost:.2f}")
    except ValueError as e:
        print(f"Error: {e}")


if __name__ == "__main__":
    main()
```
