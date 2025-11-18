"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://quedge.io
Prompt: Develop a tool to calculate the cost and pricing tiers for bulk purchases of Aethir Edge devices, including custom pricing packages for orders exceeding 11 units as outlined on the website.
Generated: DETERMINISTIC_2c6a98df1128739b
Batch ID: 20250612_154954
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
class AethirEdgePricing:
    def __init__(self):
        # Base price per unit for Aethir Edge device
        self.base_price = 100.00  # Example base price
        # Custom pricing tiers for bulk purchases
        self.pricing_tiers = {
            1: 100.00,
            5: 95.00,
            10: 90.00,
            11: 85.00,  # Custom pricing for orders exceeding 11 units
        }

    def calculate_cost(self, quantity):
        """
        Calculates the total cost based on the quantity of Aethir Edge devices being purchased.

        :param quantity: The number of devices to purchase.
        :return: The total cost for the specified quantity.
        :raises ValueError: If the quantity is less than 1.
        """
        if quantity < 1:
            raise ValueError("Quantity must be at least 1.")

        # Determine price per unit based on quantity
        price_per_unit = self.get_price_per_unit(quantity)
        total_cost = price_per_unit * quantity
        return total_cost

    def get_price_per_unit(self, quantity):
        """
        Retrieves the price per unit based on the quantity.

        :param quantity: The number of devices to purchase.
        :return: The price per unit for the specified quantity.
        """
        # Check for the highest tier applicable
        applicable_price = self.base_price
        for tier in sorted(self.pricing_tiers.keys(), reverse=True):
            if quantity >= tier:
                applicable_price = self.pricing_tiers[tier]
                break
        return applicable_price

    def print_pricing_tiers(self):
        """
        Prints the pricing tiers for the Aethir Edge devices.
        """
        print("Aethir Edge Device Pricing Tiers:")
        for quantity, price in self.pricing_tiers.items():
            print(f"{quantity} device(s): ${price:.2f} each")

# Example usage of the AethirEdgePricing class
if __name__ == "__main__":
    pricing_tool = AethirEdgePricing()
    pricing_tool.print_pricing_tiers()

    try:
        quantity = int(input("Enter the quantity of Aethir Edge devices to purchase: "))
        total_cost = pricing_tool.calculate_cost(quantity)
        print(f"The total cost for {quantity} device(s) is: ${total_cost:.2f}")
    except ValueError as e:
        print(f"Error: {e}")
```
