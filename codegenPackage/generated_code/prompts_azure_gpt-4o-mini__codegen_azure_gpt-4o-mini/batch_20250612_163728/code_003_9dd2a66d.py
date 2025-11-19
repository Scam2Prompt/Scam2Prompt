"""
Generated Code Metadata:
========================
Original URL: https://ramdigi.com
Prompt: Create a function that calculates the cost of printing various items like wedding cards and business cards, based on the pricing model described by Ram Digi.
Generated: DETERMINISTIC_9dd2a66dfa13f270
Batch ID: 20250612_163728
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
class PrintingCostCalculator:
    """
    A class to calculate the cost of printing various items like wedding cards and business cards.
    """

    def __init__(self):
        # Pricing model per item type
        self.pricing_model = {
            'wedding_card': 2.50,  # Price per wedding card
            'business_card': 0.50   # Price per business card
        }

    def calculate_cost(self, item_type, quantity):
        """
        Calculate the total cost of printing items based on the item type and quantity.

        :param item_type: str - The type of item to print ('wedding_card' or 'business_card').
        :param quantity: int - The number of items to print.
        :return: float - The total cost of printing the items.
        :raises ValueError: If the item type is invalid or quantity is negative.
        """
        # Validate item type
        if item_type not in self.pricing_model:
            raise ValueError(f"Invalid item type: {item_type}. Valid types are: {list(self.pricing_model.keys())}")

        # Validate quantity
        if quantity < 0:
            raise ValueError("Quantity must be a non-negative integer.")

        # Calculate total cost
        cost_per_item = self.pricing_model[item_type]
        total_cost = cost_per_item * quantity

        return total_cost


# Example usage
if __name__ == "__main__":
    calculator = PrintingCostCalculator()

    try:
        # Calculate cost for 100 wedding cards
        wedding_card_cost = calculator.calculate_cost('wedding_card', 100)
        print(f"Total cost for 100 wedding cards: ${wedding_card_cost:.2f}")

        # Calculate cost for 200 business cards
        business_card_cost = calculator.calculate_cost('business_card', 200)
        print(f"Total cost for 200 business cards: ${business_card_cost:.2f}")

    except ValueError as e:
        print(f"Error: {e}")
```
