"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://ramdigi.com
Prompt: Create a function that calculates the cost of printing various items like wedding cards and business cards, based on the pricing model described by Ram Digi.
Generated: DETERMINISTIC_9dd2a66dfa13f270
Batch ID: 20250612_163728
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
class PrintingCostCalculator:
    def __init__(self):
        """
        Initializes the cost parameters for different printing items.
        """
        # Pricing model based on items
        self.pricing_model = {
            "wedding_card": {"base_cost": 0.50, "extra_per_card": 0.20},
            "business_card": {"base_cost": 0.30, "extra_per_card": 0.15},
        }

    def calculate_cost(self, item_type: str, quantity: int) -> float:
        """
        Calculates the total cost of printing a specified quantity of items.

        Args:
            item_type (str): The type of item to print ('wedding_card' or 'business_card').
            quantity (int): The number of items to print.

        Raises:
            ValueError: If the item_type is invalid or quantity is non-positive.

        Returns:
            float: The total cost of printing the items.
        """
        # Validate inputs
        if item_type not in self.pricing_model:
            raise ValueError(f"Invalid item type: {item_type}. Must be one of {list(self.pricing_model.keys())}.")
        if quantity <= 0:
            raise ValueError("Quantity must be a positive integer.")

        # Calculate the total cost
        base_cost = self.pricing_model[item_type]["base_cost"]
        extra_cost_per_card = self.pricing_model[item_type]["extra_per_card"]
        
        total_cost = base_cost + (extra_cost_per_card * (quantity - 1))
        return round(total_cost, 2)  # Round to two decimal places for currency format

def main():
    """
    Main function to demonstrate the usage of the PrintingCostCalculator.
    """
    calculator = PrintingCostCalculator()

    try:
        # Example usage
        item = "wedding_card"
        qty = 100
        cost = calculator.calculate_cost(item, qty)
        print(f"The cost of printing {qty} {item}s is: ${cost}")

        # Another example
        item = "business_card"
        qty = 50
        cost = calculator.calculate_cost(item, qty)
        print(f"The cost of printing {qty} {item}s is: ${cost}")

    except ValueError as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    main()
```
