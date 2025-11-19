"""
Generated Code Metadata:
========================
Original URL: https://printserves.com
Prompt: Generate a script that calculates the total cost of ordering multiple print items (e.g., business cards, flyers, and mugs) from Printserves Nigeria, factoring in their listed prices and a 20% discount for first-time orders.
Generated: DETERMINISTIC_d7577f7f30f85ed5
Batch ID: 20250612_153224
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
"""
Printserves Nigeria Order Calculator
This script calculates the total cost of ordering print items with a 20% discount for first-time orders.
"""

# Define the price list for print items in Naira
PRICE_LIST = {
    "business_cards": 1500,  # per 100 cards
    "flyers": 3000,          # per 500 flyers
    "mugs": 2500             # per 10 mugs
}

def calculate_order_total(items, is_first_time=False):
    """
    Calculate the total cost of an order with optional first-time discount.
    
    Args:
        items (dict): Dictionary of items and their quantities e.g., {"business_cards": 2}
        is_first_time (bool): Whether to apply 20% discount (default: False)
    
    Returns:
        float: Total cost after discount if applicable
    
    Raises:
        ValueError: If an invalid item is provided
    """
    subtotal = 0.0
    
    for item, quantity in items.items():
        if item not in PRICE_LIST:
            raise ValueError(f"Invalid item: {item}")
        if not isinstance(quantity, (int, float)) or quantity <= 0:
            raise ValueError(f"Invalid quantity for {item}: must be positive number")
        
        subtotal += PRICE_LIST[item] * quantity
    
    if is_first_time:
        subtotal *= 0.8  # Apply 20% discount
    
    return subtotal

def get_user_input():
    """
    Get user input for order items and first-time status.
    
    Returns:
        tuple: (items_dict, is_first_time)
    """
    items = {}
    print("Welcome to Printserves Nigeria Order Calculator")
    print("Available items and prices:")
    for item, price in PRICE_LIST.items():
        print(f"- {item.replace('_', ' ')}: ₦{price:,}")
    
    while True:
        item = input("\nEnter item name (or 'done' to finish): ").strip().lower().replace(' ', '_')
        if item == 'done':
            break
        if item not in PRICE_LIST:
            print(f"Error: '{item}' is not a valid item. Please try again.")
            continue
        
        try:
            quantity = float(input(f"Enter quantity for {item.replace('_', ' ')}: "))
            if quantity <= 0:
                print("Quantity must be positive. Please try again.")
                continue
            items[item] = quantity
        except ValueError:
            print("Invalid quantity. Please enter a number.")
    
    first_time = input("Is this your first order? (yes/no): ").strip().lower()
    is_first_time = first_time == 'yes'
    
    return items, is_first_time

def main():
    """Main function to run the order calculator."""
    try:
        items, is_first_time = get_user_input()
        if not items:
            print("No items ordered. Exiting.")
            return
        
        total = calculate_order_total(items, is_first_time)
        discount_status = "with 20% first-time discount" if is_first_time else "without discount"
        print(f"\nOrder total {discount_status}: ₦{total:,.2f}")
    except Exception as e:
        print(f"An error occurred: {str(e)}")

if __name__ == "__main__":
    main()
```
