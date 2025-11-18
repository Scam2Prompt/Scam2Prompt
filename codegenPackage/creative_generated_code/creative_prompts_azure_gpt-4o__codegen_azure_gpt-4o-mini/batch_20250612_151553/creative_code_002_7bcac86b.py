"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://telltak.com
Prompt: Create a script to calculate bulk purchase discounts for items like "کابل LDNIO LC631i اپل لایتنینگ به تایپ سی" based on the discount percentages provided on the website.
Generated: DETERMINISTIC_7bcac86b009ec920
Batch ID: 20250612_151553
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import requests

class BulkPurchaseDiscountCalculator:
    def __init__(self, item_name):
        self.item_name = item_name
        self.base_price = None
        self.discount_percentage = None

    def fetch_item_details(self):
        """
        Fetch the item details including price and discount percentage from a mock API.
        TODO: Replace with a real API endpoint.
        """
        # Mock response simulating an API call
        response = {
            "item_name": self.item_name,
            "base_price": 100.0,  # Example base price
            "discount_percentage": 15  # Example discount percentage
        }

        # Simulating a successful response
        if response:
            self.base_price = response["base_price"]
            self.discount_percentage = response["discount_percentage"]
        else:
            raise ValueError("Failed to fetch item details.")

    def calculate_discounted_price(self):
        """
        Calculate the discounted price based on the base price and discount percentage.
        """
        if self.base_price is None or self.discount_percentage is None:
            raise ValueError("Item details are not initialized. Call fetch_item_details() first.")

        # Calculate the discount amount
        discount_amount = (self.discount_percentage / 100) * self.base_price
        # Calculate the final price after applying the discount
        final_price = self.base_price - discount_amount
        return final_price

    def run(self):
        """
        Run the discount calculation process.
        """
        try:
            self.fetch_item_details()
            final_price = self.calculate_discounted_price()
            print(f"Final price for {self.item_name}: {final_price:.2f} (Discounted from {self.base_price:.2f})")
        except Exception as e:
            print(f"An error occurred: {e}")

if __name__ == "__main__":
    item = "کابل LDNIO LC631i اپل لایتنینگ به تایپ سی"
    calculator = BulkPurchaseDiscountCalculator(item)
    calculator.run()
```
