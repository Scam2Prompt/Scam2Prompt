"""
Generated Code Metadata:
========================
Original URL: https://konveksibajumurah.com
Prompt: Write a Python script to calculate the cost of bulk uniform production, including accessories like hats and belts, based on the pricing model described by Real Garment Konveksi Seragam in Surabaya.
Generated: DETERMINISTIC_145500c14ca58846
Batch ID: 20250612_153225
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
class BulkProductionCostCalculator:
    """
    A class to calculate the cost of bulk uniform production including accessories.
    """

    def __init__(self, base_price_per_uniform, accessory_prices, min_order_quantity):
        """
        Initializes the calculator with base price, accessory prices, and minimum order quantity.

        :param base_price_per_uniform: float, base price for a single uniform
        :param accessory_prices: dict, prices for accessories (e.g., {'hat': 10.0, 'belt': 5.0})
        :param min_order_quantity: int, minimum quantity required for bulk pricing
        """
        self.base_price_per_uniform = base_price_per_uniform
        self.accessory_prices = accessory_prices
        self.min_order_quantity = min_order_quantity

    def calculate_total_cost(self, quantity, include_accessories=False):
        """
        Calculates the total cost for the given quantity of uniforms.

        :param quantity: int, number of uniforms to produce
        :param include_accessories: bool, whether to include accessories in the cost
        :return: float, total cost of production
        :raises ValueError: if quantity is less than 1 or not an integer
        """
        if not isinstance(quantity, int) or quantity < 1:
            raise ValueError("Quantity must be a positive integer.")

        # Calculate the cost of uniforms
        total_cost = self.base_price_per_uniform * quantity

        # Include accessories if specified
        if include_accessories:
            total_cost += self.calculate_accessory_cost(quantity)

        return total_cost

    def calculate_accessory_cost(self, quantity):
        """
        Calculates the total cost of accessories based on the quantity.

        :param quantity: int, number of uniforms to produce
        :return: float, total cost of accessories
        """
        total_accessory_cost = 0.0
        for accessory, price in self.accessory_prices.items():
            total_accessory_cost += price * quantity
        return total_accessory_cost

    def display_cost_breakdown(self, quantity, include_accessories=False):
        """
        Displays a breakdown of the costs for the given quantity of uniforms.

        :param quantity: int, number of uniforms to produce
        :param include_accessories: bool, whether to include accessories in the breakdown
        """
        try:
            total_cost = self.calculate_total_cost(quantity, include_accessories)
            print(f"Total cost for {quantity} uniforms: ${total_cost:.2f}")

            if include_accessories:
                accessory_cost = self.calculate_accessory_cost(quantity)
                print(f"Accessory cost for {quantity} uniforms: ${accessory_cost:.2f}")
                print(f"Base cost for {quantity} uniforms: ${self.base_price_per_uniform * quantity:.2f}")

        except ValueError as e:
            print(f"Error: {e}")


# Example usage
if __name__ == "__main__":
    # Define base price and accessory prices
    base_price = 50.0  # Base price per uniform
    accessories = {'hat': 10.0, 'belt': 5.0}  # Prices for accessories
    min_order = 10  # Minimum order quantity

    # Create an instance of the calculator
    calculator = BulkProductionCostCalculator(base_price, accessories, min_order)

    # Calculate and display costs
    quantity_to_order = 20
    calculator.display_cost_breakdown(quantity_to_order, include_accessories=True)
```
