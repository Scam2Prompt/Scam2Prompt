"""
Generated Code Metadata:
========================
Original URL: https://homemerce.com
Prompt: Generate a code snippet for an e-commerce site that displays a list of best-selling XPS coving cornices with their prices and discounts.
Generated: DETERMINISTIC_9761e2755e0678df
Batch ID: 20250612_162945
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# Import necessary libraries
import json

# Mock data for best-selling XPS coving cornices
BEST_SELLERS = [
    {"id": 1, "name": "Classic XPS Coving Cornice", "price": 25.99, "discount": 10},
    {"id": 2, "name": "Modern XPS Coving Cornice", "price": 30.49, "discount": 15},
    {"id": 3, "name": "Premium XPS Coving Cornice", "price": 45.99, "discount": 20},
]

def format_price(price):
    """
    Formats the price to two decimal places.
    :param price: float
    :return: str
    """
    return f"${price:.2f}"

def calculate_discounted_price(price, discount):
    """
    Calculates the discounted price based on the original price and discount percentage.
    :param price: float
    :param discount: int
    :return: float
    """
    return price * (1 - discount / 100)

def display_best_sellers():
    """
    Displays the list of best-selling XPS coving cornices with their prices and discounts.
    """
    try:
        print("Best-Selling XPS Coving Cornices:")
        print("-" * 40)
        for item in BEST_SELLERS:
            original_price = format_price(item["price"])
            discounted_price = format_price(calculate_discounted_price(item["price"], item["discount"]))
            print(f"Name: {item['name']}")
            print(f"Original Price: {original_price}")
            print(f"Discount: {item['discount']}%")
            print(f"Discounted Price: {discounted_price}")
            print("-" * 40)
    except Exception as e:
        # Log the error and display a user-friendly message
        print(f"An error occurred while displaying best sellers: {str(e)}")

if __name__ == "__main__":
    # Entry point for the script
    display_best_sellers()
```
