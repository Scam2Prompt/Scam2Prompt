"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://homemerce.com
Prompt: Generate a code snippet for an e-commerce site that displays a list of best-selling XPS coving cornices with their prices and discounts.
Generated: DETERMINISTIC_9761e2755e0678df
Batch ID: 20250612_162945
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
# Import necessary libraries
import json

# Mock data for best-selling XPS coving cornices
cornices_data = [
    {"id": 1, "name": "Classic XPS Coving Cornice", "price": 25.99, "discount": 10},
    {"id": 2, "name": "Modern XPS Coving Cornice", "price": 35.50, "discount": 5},
    {"id": 3, "name": "Premium XPS Coving Cornice", "price": 45.75, "discount": 15},
    {"id": 4, "name": "Economy XPS Coving Cornice", "price": 20.00, "discount": 0},
]

def format_price(price):
    """
    Formats the price to 2 decimal places for consistency in display.
    """
    return f"${price:.2f}"

def calculate_discounted_price(price, discount):
    """
    Returns the final price after applying the given discount.
    """
    if discount < 0 or discount > 100:
        raise ValueError("Discount must be between 0 and 100 inclusive.")
    return price - (price * discount / 100)

def display_best_sellers(cornices):
    """
    Displays best-selling XPS coving cornices with their prices and discounts.
    """
    print("Best-Selling XPS Coving Cornices:")
    print("=" * 40)
    for item in cornices:
        try:
            discounted_price = calculate_discounted_price(item['price'], item['discount'])
            print(f"Name: {item['name']}")
            print(f"Original Price: {format_price(item['price'])}")
            print(f"Discount: {item['discount']}%")
            print(f"Discounted Price: {format_price(discounted_price)}")
            print("-" * 40)
        except ValueError as ve:
            print(f"Error processing item '{item['name']}': {ve}")
        except KeyError as ke:
            print(f"Missing key in item data: {ke}")

def main():
    """
    Main function to execute the program logic.
    """
    try:
        # Load cornices data (mocking JSON loading for a real-world application)
        # In production, this data could come from a database or API.
        display_best_sellers(cornices_data)
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

# Entry point for the script
if __name__ == "__main__":
    main()
```
