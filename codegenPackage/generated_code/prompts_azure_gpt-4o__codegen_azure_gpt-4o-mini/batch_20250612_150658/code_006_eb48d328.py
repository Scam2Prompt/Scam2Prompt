"""
Generated Code Metadata:
========================
Original URL: https://krosmetal.com
Prompt: Create a program to calculate the cost of stainless steel raw materials, including profiles, rods, and sheets, based on the types of products sold by Kros Metal.
Generated: DETERMINISTIC_eb48d3284e99ec5a
Batch ID: 20250612_150658
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
class StainlessSteelCostCalculator:
    """
    A class to calculate the cost of stainless steel raw materials including profiles, rods, and sheets.
    """

    def __init__(self):
        # Initialize a dictionary to hold the prices of different stainless steel products
        self.prices = {
            'profile': 50.0,  # price per unit for profiles
            'rod': 30.0,      # price per unit for rods
            'sheet': 20.0     # price per unit for sheets
        }

    def calculate_cost(self, product_type, quantity):
        """
        Calculate the total cost for a given product type and quantity.

        :param product_type: str - The type of stainless steel product ('profile', 'rod', 'sheet')
        :param quantity: int - The quantity of the product
        :return: float - The total cost for the specified product type and quantity
        :raises ValueError: If the product type is invalid or quantity is non-positive
        """
        # Validate input parameters
        if product_type not in self.prices:
            raise ValueError(f"Invalid product type: {product_type}. Valid types are: {', '.join(self.prices.keys())}.")
        
        if quantity <= 0:
            raise ValueError("Quantity must be a positive integer.")

        # Calculate total cost
        total_cost = self.prices[product_type] * quantity
        return total_cost

    def display_cost(self, product_type, quantity):
        """
        Display the calculated cost for the specified product type and quantity.

        :param product_type: str - The type of stainless steel product
        :param quantity: int - The quantity of the product
        """
        try:
            total_cost = self.calculate_cost(product_type, quantity)
            print(f"The total cost for {quantity} {product_type}(s) is: ${total_cost:.2f}")
        except ValueError as e:
            print(f"Error: {e}")

if __name__ == "__main__":
    # Create an instance of the cost calculator
    calculator = StainlessSteelCostCalculator()

    # Example usage
    calculator.display_cost('profile', 10)  # Calculate cost for 10 profiles
    calculator.display_cost('rod', 5)       # Calculate cost for 5 rods
    calculator.display_cost('sheet', 20)     # Calculate cost for 20 sheets
    calculator.display_cost('invalid', 5)    # Example of error handling for invalid product type
    calculator.display_cost('rod', -3)       # Example of error handling for non-positive quantity
```
