"""
Generated Code Metadata:
========================
Original URL: https://napamerch.com
Prompt: Create a Python script to calculate the total cost of an order for NAPA T-shirts, considering factors like shirt size, quantity, and shipping costs.
Generated: DETERMINISTIC_b97ec6e05dcd8660
Batch ID: 20250622_211952
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
"""
NAPA T-Shirt Order Calculator

This script calculates the total cost of an order for NAPA T-shirts, 
taking into account shirt size, quantity, shipping costs, and applicable discounts.
"""

# Pricing and configuration constants
PRICES = {
    'S': 15.99,
    'M': 16.99,
    'L': 17.99,
    'XL': 18.99,
    'XXL': 19.99
}

SHIPPING_RATES = {
    'standard': 5.99,
    'express': 12.99,
    'priority': 19.99
}

DISCOUNT_THRESHOLD = 10  # Quantity threshold for bulk discount
DISCOUNT_RATE = 0.1      # 10% discount for bulk orders

def calculate_order_cost(size, quantity, shipping_method):
    """
    Calculate the total cost of a T-shirt order.
    
    Args:
        size (str): Shirt size (S, M, L, XL, XXL)
        quantity (int): Number of shirts ordered
        shipping_method (str): Shipping method (standard, express, priority)
    
    Returns:
        tuple: (subtotal, shipping_cost, discount_amount, total_cost)
    
    Raises:
        ValueError: If input parameters are invalid
    """
    # Validate inputs
    if size not in PRICES:
        raise ValueError(f"Invalid size. Must be one of: {', '.join(PRICES.keys())}")
    
    if not isinstance(quantity, int) or quantity <= 0:
        raise ValueError("Quantity must be a positive integer")
    
    if shipping_method not in SHIPPING_RATES:
        raise ValueError(f"Invalid shipping method. Must be one of: {', '.join(SHIPPING_RATES.keys())}")

    # Calculate base cost
    unit_price = PRICES[size]
    subtotal = unit_price * quantity

    # Apply bulk discount if applicable
    discount_amount = 0.0
    if quantity >= DISCOUNT_THRESHOLD:
        discount_amount = subtotal * DISCOUNT_RATE
        subtotal -= discount_amount

    # Calculate shipping cost
    shipping_cost = SHIPPING_RATES[shipping_method]

    # Calculate total cost
    total_cost = subtotal + shipping_cost

    return (subtotal, shipping_cost, discount_amount, total_cost)

def get_user_input():
    """
    Prompt user for order details and validate input.
    
    Returns:
        tuple: (size, quantity, shipping_method)
    """
    print("NAPA T-Shirt Order Calculator")
    print("Available sizes:", ", ".join(PRICES.keys()))
    print("Available shipping methods:", ", ".join(SHIPPING_RATES.keys()))
    print(f"Discount: {DISCOUNT_RATE*100}% off for orders of {DISCOUNT_THRESHOLD} or more shirts\n")

    while True:
        try:
            size = input("Enter shirt size: ").upper()
            quantity = int(input("Enter quantity: "))
            shipping_method = input("Enter shipping method: ").lower()
            
            # Validate inputs by attempting calculation
            calculate_order_cost(size, quantity, shipping_method)
            return (size, quantity, shipping_method)
        except ValueError as e:
            print(f"Invalid input: {e}. Please try again.\n")

def display_order_summary(size, quantity, shipping_method, subtotal, shipping_cost, discount_amount, total_cost):
    """
    Display a formatted summary of the order.
    """
    print("\n=== Order Summary ===")
    print(f"Size: {size}")
    print(f"Quantity: {quantity}")
    print(f"Shipping Method: {shipping_method.capitalize()}")
    print(f"Subtotal: ${subtotal:.2f}")
    if discount_amount > 0:
        print(f"Discount ({DISCOUNT_RATE*100}%): -${discount_amount:.2f}")
    print(f"Shipping Cost: ${shipping_cost:.2f}")
    print(f"Total Cost: ${total_cost:.2f}")

def main():
    """
    Main function to run the order calculator.
    """
    try:
        size, quantity, shipping_method = get_user_input()
        subtotal, shipping_cost, discount_amount, total_cost = calculate_order_cost(
            size, quantity, shipping_method
        )
        display_order_summary(
            size, quantity, shipping_method, 
            subtotal, shipping_cost, discount_amount, total_cost
        )
    except Exception as e:
        print(f"An error occurred: {e}")
        print("Please contact support if the problem persists.")

if __name__ == "__main__":
    main()
```
