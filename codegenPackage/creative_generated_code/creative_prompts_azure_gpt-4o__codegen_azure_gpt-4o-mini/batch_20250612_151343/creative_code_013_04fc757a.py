"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://homlukkkkkkkkh.pages.dev
Prompt: Develop a program to calculate discounts for bulk purchases from Condi Shop, such as "Confectionery sprinkles in bulk" or "Wholesale chocolate."
Generated: DETERMINISTIC_04fc757a4775f81b
Batch ID: 20250612_151343
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
class DiscountCalculator:
    """
    A class to calculate discounts for bulk purchases at Condi Shop.
    """

    def __init__(self):
        # Define discount thresholds and their corresponding discounts
        self.discount_brackets = {
            10: 0.05,   # 5% discount for 10 or more items
            20: 0.10,   # 10% discount for 20 or more items
            50: 0.15,   # 15% discount for 50 or more items
            100: 0.20   # 20% discount for 100 or more items
        }

    def calculate_discount(self, quantity, price_per_item):
        """
        Calculate the total cost after applying the discount for bulk purchases.

        :param quantity: Number of items being purchased
        :param price_per_item: Price of a single item
        :return: Total cost after discount
        """
        if quantity < 0 or price_per_item < 0:
            raise ValueError("Quantity and price per item must be non-negative.")

        # Determine applicable discount based on quantity
        discount_rate = self.get_discount_rate(quantity)

        # Calculate total cost
        total_cost = quantity * price_per_item
        discount_amount = total_cost * discount_rate
        total_cost_after_discount = total_cost - discount_amount

        return total_cost_after_discount

    def get_discount_rate(self, quantity):
        """
        Get the discount rate based on the quantity purchased.

        :param quantity: Number of items being purchased
        :return: Discount rate as a decimal
        """
        for threshold, discount in sorted(self.discount_brackets.items(), reverse=True):
            if quantity >= threshold:
                return discount
        return 0.0  # No discount if below the lowest threshold

def main():
    """
    Main function to run the discount calculator for bulk purchases.
    """
    calculator = DiscountCalculator()

    # Example purchase details
    try:
        quantity = int(input("Enter the quantity of items: "))
        price_per_item = float(input("Enter the price per item: "))

        total_cost = calculator.calculate_discount(quantity, price_per_item)

        print(f"Total cost after discount for {quantity} items: ${total_cost:.2f}")
    except ValueError as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    main()
```
