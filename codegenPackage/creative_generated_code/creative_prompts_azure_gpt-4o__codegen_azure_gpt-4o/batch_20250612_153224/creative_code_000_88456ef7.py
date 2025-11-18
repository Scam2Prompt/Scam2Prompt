"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://dolphiniran.com
Prompt: Write a Python script to calculate the total cost of purchasing multiple items from Dolphin Iran's product categories, such as "آینه بک‌لایت لمسی" and "ست کابینت و روشویی دلفین," using their listed prices.
Generated: DETERMINISTIC_88456ef71b20d5a1
Batch ID: 20250612_153224
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
# Python script to calculate the total cost of purchasing multiple items
# from Dolphin Iran's product categories.

# Import necessary modules
import sys

def fetch_product_prices():
    """
    Fetches the prices of products from Dolphin Iran's categories.
    In a real-world scenario, this could involve an API call or database query.
    For this example, we'll use a predefined dictionary.
    
    Returns:
        dict: A dictionary with product names as keys and their prices as values.
    """
    return {
        "آینه بک‌لایت لمسی": 1500000,  # Price in Iranian Rial
        "ست کابینت و روشویی دلفین": 2500000,  # Price in Iranian Rial
        "قاب آینه کلاسیک": 800000,  # Additional example item
    }

def calculate_total_cost(cart, product_prices):
    """
    Calculates the total cost of items in the cart.
    
    Args:
        cart (dict): A dictionary with product names as keys and quantities as values.
        product_prices (dict): A dictionary with product names as keys and their prices as values.
        
    Returns:
        int: Total cost of items in the cart.
        
    Raises:
        ValueError: If a product in the cart is not found in the price list.
    """
    total_cost = 0
    
    for product, quantity in cart.items():
        if product not in product_prices:
            raise ValueError(f"Product '{product}' not found in price list.")
        if quantity < 0:
            raise ValueError(f"Quantity for product '{product}' cannot be negative.")
        total_cost += product_prices[product] * quantity
    
    return total_cost

def main():
    """
    Main function to interact with the user and calculate the total cost.
    """
    try:
        # Fetch product prices
        product_prices = fetch_product_prices()

        # Display available products
        print("Available Products and Prices:")
        for product, price in product_prices.items():
            print(f"{product}: {price} IRR")

        # User input for shopping cart
        print("\nEnter your shopping cart details.")
        print("For each product, specify the quantity (enter 0 if not purchasing).")
        cart = {}
        
        for product in product_prices.keys():
            try:
                quantity = int(input(f"Quantity of '{product}': "))
                cart[product] = quantity
            except ValueError:
                print("Invalid input. Please enter a valid number.")
                sys.exit(1)

        # Calculate total cost
        total_cost = calculate_total_cost(cart, product_prices)
        print(f"\nTotal cost of your purchase: {total_cost} IRR")
    
    except ValueError as ve:
        print(f"Error: {ve}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

# Entry point of the script
if __name__ == "__main__":
    main()
```
