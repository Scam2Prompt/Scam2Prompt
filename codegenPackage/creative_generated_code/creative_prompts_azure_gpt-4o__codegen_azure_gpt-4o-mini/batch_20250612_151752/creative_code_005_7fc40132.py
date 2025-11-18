"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://chandkalaco.com
Prompt: Develop a Python script to calculate shipping costs for orders containing items from categories like "تجهیزات اداری و فروشگاهی" and "لوازم شخصی برقی," as described on chandkala.com.
Generated: DETERMINISTIC_7fc40132af7a93c2
Batch ID: 20250612_151752
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import requests

class ShippingCalculator:
    """
    A class to calculate shipping costs for specific product categories.
    """

    def __init__(self, base_rate=5.0, category_rates=None):
        """
        Initializes the ShippingCalculator with a base rate and category rates.

        Parameters:
        - base_rate (float): The base shipping rate.
        - category_rates (dict): A dictionary of additional rates per category.
        """
        self.base_rate = base_rate
        # Set default category rates if none provided
        self.category_rates = category_rates if category_rates is not None else {
            "تجهیزات اداری و فروشگاهی": 2.0,
            "لوازم شخصی برقی": 3.0
        }

    def calculate_shipping(self, order_items):
        """
        Calculate the total shipping cost based on the order items.

        Parameters:
        - order_items (list): A list of tuples where each tuple contains
                              (item_name, category, weight).

        Returns:
        - float: Total shipping cost.
        """
        total_cost = self.base_rate
        try:
            for item_name, category, weight in order_items:
                if category in self.category_rates:
                    total_cost += self.category_rates[category] * weight
                else:
                    print(f"Warning: Category '{category}' not recognized. No additional charge.")
        except Exception as e:
            print(f"Error calculating shipping: {e}")
        return total_cost

def main():
    """
    The main function to execute the shipping cost calculation.
    """
    # Sample order items with (item_name, category, weight)
    order_items = [
        ("Item1", "تجهیزات اداری و فروشگاهی", 1.5),
        ("Item2", "لوازم شخصی برقی", 2.0),
        ("Item3", "غیر موجود", 1.0)  # Example of an unrecognized category
    ]

    # Create a shipping calculator instance
    calculator = ShippingCalculator()

    # Calculate the shipping cost
    total_shipping_cost = calculator.calculate_shipping(order_items)

    # Display the total shipping cost
    print(f"Total Shipping Cost: {total_shipping_cost:.2f} USD")

if __name__ == "__main__":
    main()
```
