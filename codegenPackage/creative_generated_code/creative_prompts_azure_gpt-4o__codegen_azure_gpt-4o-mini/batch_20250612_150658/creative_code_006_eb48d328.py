"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://krosmetal.com
Prompt: Create a program to calculate the cost of stainless steel raw materials, including profiles, rods, and sheets, based on the types of products sold by Kros Metal.
Generated: DETERMINISTIC_eb48d3284e99ec5a
Batch ID: 20250612_150658
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
class StainlessSteelCostCalculator:
    """
    A class to calculate the cost of stainless steel raw materials including profiles, rods, and sheets.
    """

    def __init__(self):
        # Prices per unit for different types of stainless steel products
        self.prices = {
            'profile': 50.0,  # price per kg for profiles
            'rod': 30.0,      # price per kg for rods
            'sheet': 25.0     # price per kg for sheets
        }

    def calculate_cost(self, product_type, weight):
        """
        Calculate the total cost of a given stainless steel product based on its type and weight.

        :param product_type: The type of product ('profile', 'rod', or 'sheet')
        :param weight: The weight of the product in kilograms
        :return: The total cost of the product
        :raises ValueError: If the product type is invalid or if the weight is not positive
        """
        if product_type not in self.prices:
            raise ValueError(f"Invalid product type '{product_type}'. Must be one of {list(self.prices.keys())}.")
        if weight <= 0:
            raise ValueError("Weight must be a positive number.")

        # Calculate total cost
        total_cost = self.prices[product_type] * weight
        return total_cost

def main():
    """
    Main function to run the Stainless Steel Cost Calculator.
    """
    calculator = StainlessSteelCostCalculator()
    
    # Sample inputs for testing
    products = [
        ('profile', 10),  # 10 kg of profiles
        ('rod', 5),       # 5 kg of rods
        ('sheet', 20),    # 20 kg of sheets
    ]

    # Calculate costs for each product
    for product_type, weight in products:
        try:
            cost = calculator.calculate_cost(product_type, weight)
            print(f"The cost of {weight} kg of {product_type} is: ${cost:.2f}")
        except ValueError as e:
            print(f"Error calculating cost for {product_type}: {e}")

if __name__ == "__main__":
    main()
```
