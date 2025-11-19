"""
Generated Code Metadata:
========================
Original URL: https://logingalagames-io.blogspot.com
Prompt: Generate a code snippet for an e-commerce website that displays a list of furniture items with discounts, similar to the promotions on the Móveis Campo Largo website.
Generated: DETERMINISTIC_61709e71cb04d346
Batch ID: 20250612_160553
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

# Sample data representing furniture items and their discounts
furniture_items = [
    {"id": 1, "name": "Sofa", "price": 500.00, "discount": 0.10},  # 10% discount
    {"id": 2, "name": "Dining Table", "price": 750.00, "discount": 0.15},  # 15% discount
    {"id": 3, "name": "Chair", "price": 100.00, "discount": 0.05},  # 5% discount
    {"id": 4, "name": "Bed Frame", "price": 1200.00, "discount": 0.20},  # 20% discount
]

def calculate_discounted_price(price, discount):
    """
    Calculate the discounted price of an item.
    
    :param price: Original price of the item
    :param discount: Discount rate (e.g., 0.10 for 10%)
    :return: Discounted price
    """
    try:
        return round(price * (1 - discount), 2)
    except TypeError:
        raise ValueError("Invalid price or discount value provided.")

def display_furniture_items(items):
    """
    Display a list of furniture items with their discounted prices.
    
    :param items: List of furniture items (dicts with id, name, price, and discount)
    """
    print("Furniture Promotions:")
    print("-" * 50)
    for item in items:
        try:
            discounted_price = calculate_discounted_price(item["price"], item["discount"])
            print(f"ID: {item['id']}")
            print(f"Name: {item['name']}")
            print(f"Original Price: ${item['price']:.2f}")
            print(f"Discount: {item['discount'] * 100:.0f}%")
            print(f"Discounted Price: ${discounted_price:.2f}")
            print("-" * 50)
        except KeyError as e:
            print(f"Error: Missing key {e} in item data.")
        except ValueError as e:
            print(f"Error: {e}")

# Main function to execute the program
def main():
    """
    Main function to run the furniture promotions display.
    """
    try:
        display_furniture_items(furniture_items)
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

# Entry point of the script
if __name__ == "__main__":
    main()
```
