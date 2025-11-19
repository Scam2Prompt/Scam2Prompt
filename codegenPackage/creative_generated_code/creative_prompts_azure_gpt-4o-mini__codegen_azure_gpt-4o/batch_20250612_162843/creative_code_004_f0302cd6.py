"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://ton.coinsend.top
Prompt: Illustrate how to implement a checkout process for track cycling gear, referencing the Velodrome Shop's product categories like "Track Gearing" and "Track Clothing."
Generated: DETERMINISTIC_f0302cd6d2d6f5f4
Batch ID: 20250612_162843
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import json

# Constants representing product categories
PRODUCT_CATEGORIES = ["Track Gearing", "Track Clothing"]

# Mock inventory for demonstration purposes
INVENTORY = {
    "Track Gearing": [
        {"id": 1, "name": "Chainring - 50T", "price": 50.00},
        {"id": 2, "name": "Cog - 15T", "price": 20.00},
    ],
    "Track Clothing": [
        {"id": 3, "name": "Cycling Jersey", "price": 45.00},
        {"id": 4, "name": "Cycling Shorts", "price": 35.00},
    ],
}

class CheckoutError(Exception):
    """Custom exception for checkout errors."""
    pass

def display_products():
    """Display available products from the inventory."""
    print("Available Products:\n")
    for category in PRODUCT_CATEGORIES:
        print(f"Category: {category}")
        for product in INVENTORY[category]:
            print(f"  ID: {product['id']}, Name: {product['name']}, Price: ${product['price']:.2f}")
        print()

def get_product_by_id(product_id):
    """
    Retrieve product details by ID.
    Args:
        product_id (int): Product ID.
    Returns:
        dict: Product details if found.
    Raises:
        CheckoutError: If the product ID does not exist.
    """
    for category in PRODUCT_CATEGORIES:
        for product in INVENTORY[category]:
            if product["id"] == product_id:
                return product
    raise CheckoutError(f"Product with ID {product_id} not found.")

def calculate_total(cart):
    """
    Calculate the total cost of the items in the cart.
    Args:
        cart (list): List of product dictionaries in the cart.
    Returns:
        float: Total cost.
    """
    return sum(item["price"] for item in cart)

def checkout():
    """
    Handles the checkout process.
    Allows customers to add products to the cart and finalize the purchase.
    """
    cart = []
    while True:
        try:
            display_products()
            product_id = input("Enter the product ID to add to your cart (or type 'done' to finish): ").strip()
            if product_id.lower() == 'done':
                break
            
            product_id = int(product_id)  # Convert input to integer
            product = get_product_by_id(product_id)
            cart.append(product)
            print(f"Added '{product['name']}' to your cart.\n")
        except ValueError:
            print("Invalid input. Please enter a numeric product ID.")
        except CheckoutError as e:
            print(f"Error: {e}")

    if not cart:
        print("Your cart is empty. No items to checkout.")
        return

    print("\nYour Cart:")
    for item in cart:
        print(f"  Name: {item['name']}, Price: ${item['price']:.2f}")
    
    total_cost = calculate_total(cart)
    print(f"\nTotal Cost: ${total_cost:.2f}")

    try:
        confirmation = input("Type 'confirm' to finalize the purchase, or 'cancel' to abort: ").strip().lower()
        if confirmation == 'confirm':
            print("Purchase confirmed! Thank you for shopping with us.")
        elif confirmation == 'cancel':
            print("Purchase canceled. Your cart has been cleared.")
        else:
            raise CheckoutError("Invalid confirmation input. Please type 'confirm' or 'cancel'.")
    except CheckoutError as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    print("Welcome to the Velodrome Shop Checkout System!")
    checkout()
```
