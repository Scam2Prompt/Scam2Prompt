"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://konveksibajumurah.com
Prompt: Write a Python script to calculate the cost of bulk uniform production, including accessories like hats and belts, based on the pricing model described by Real Garment Konveksi Seragam in Surabaya.
Generated: DETERMINISTIC_145500c14ca58846
Batch ID: 20250612_153225
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
class BulkProductionCostCalculator:
    """
    A class to calculate the total cost of bulk uniform production including accessories.
    """

    def __init__(self, unit_price, quantity, accessory_prices=None):
        """
        Initializes the calculator with unit price, quantity, and optional accessory prices.

        :param unit_price: Price per unit for the uniform
        :param quantity: Number of uniforms to be produced
        :param accessory_prices: Dictionary containing accessory names and their prices
        """
        self.unit_price = unit_price
        self.quantity = quantity
        self.accessory_prices = accessory_prices if accessory_prices is not None else {}

    def calculate_uniform_cost(self):
        """
        Calculate the total cost of uniforms.

        :return: Total cost for uniforms
        """
        return self.unit_price * self.quantity

    def calculate_accessory_cost(self):
        """
        Calculate the total cost of accessories.

        :return: Total cost for accessories
        """
        return sum(self.accessory_prices.values())

    def calculate_total_cost(self):
        """
        Calculate the total cost including uniforms and accessories.

        :return: Total cost for the entire order
        """
        try:
            total_uniform_cost = self.calculate_uniform_cost()
            total_accessory_cost = self.calculate_accessory_cost()
            total_cost = total_uniform_cost + total_accessory_cost
            return total_cost
        except Exception as e:
            print(f"Error calculating total cost: {e}")
            return None

    def display_cost_breakdown(self):
        """
        Display a detailed breakdown of costs for the order.
        """
        total_uniform_cost = self.calculate_uniform_cost()
        total_accessory_cost = self.calculate_accessory_cost()
        total_cost = self.calculate_total_cost()

        print("Cost Breakdown:")
        print(f"Uniforms Cost: {total_uniform_cost:.2f}")
        print("Accessories Cost:")
        for accessory, price in self.accessory_prices.items():
            print(f"  {accessory}: {price:.2f}")
        print(f"Total Cost: {total_cost:.2f}")


if __name__ == "__main__":
    # Example usage of the BulkProductionCostCalculator
    try:
        # Define the base unit price and quantity
        unit_price = float(input("Enter the unit price for the uniform: "))
        quantity = int(input("Enter the quantity of uniforms: "))

        # Define optional accessory prices
        accessory_prices = {
            'Hats': float(input("Enter the price for hats: ")),
            'Belts': float(input("Enter the price for belts: ")),
        }

        # Create an instance of the calculator
        calculator = BulkProductionCostCalculator(unit_price, quantity, accessory_prices)

        # Display the cost breakdown
        calculator.display_cost_breakdown()

    except ValueError as ve:
        print(f"Invalid input: {ve}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
```
