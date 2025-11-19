"""
Generated Code Metadata:
========================
Original URL: https://somoscorujasbraz.blogspot.com
Prompt: Generate a list of baby clothing and accessory products with their prices in Brazilian Real (BRL), similar to the product listings on Somos Corujas, and calculate the total cost of a shopping cart with 5 items.
Generated: DETERMINISTIC_8c3de7842181ded7
Batch ID: 20250622_212549
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# Import necessary modules
import random

# Define a list of baby clothing and accessory products with their prices in BRL
products = [
    {"name": "Baby Onesie", "price": 49.90},
    {"name": "Baby Blanket", "price": 89.90},
    {"name": "Baby Socks (Pack of 3)", "price": 29.90},
    {"name": "Baby Hat", "price": 39.90},
    {"name": "Baby Bib", "price": 19.90},
    {"name": "Baby Shoes", "price": 99.90},
    {"name": "Baby Jacket", "price": 149.90},
    {"name": "Baby Pants", "price": 59.90},
    {"name": "Baby T-Shirt", "price": 39.90},
    {"name": "Baby Mittens", "price": 24.90},
]

# Function to display the product list
def display_products(products):
    print("Available Baby Products:")
    for idx, product in enumerate(products, start=1):
        print(f"{idx}. {product['name']} - R$ {product['price']:.2f}")

# Function to calculate the total cost of a shopping cart
def calculate_total(cart):
    try:
        total = sum(item['price'] for item in cart)
        return total
    except Exception as e:
        print(f"Error calculating total: {e}")
        return 0

# Main function to simulate shopping cart selection and calculation
def main():
    # Display the product list
    display_products(products)
    
    # Randomly select 5 items for the shopping cart
    shopping_cart = random.sample(products, 5)
    
    print("\nShopping Cart:")
    for item in shopping_cart:
        print(f"{item['name']} - R$ {item['price']:.2f}")
    
    # Calculate the total cost of the shopping cart
    total_cost = calculate_total(shopping_cart)
    print(f"\nTotal Cost: R$ {total_cost:.2f}")

# Entry point of the script
if __name__ == "__main__":
    main()
```
