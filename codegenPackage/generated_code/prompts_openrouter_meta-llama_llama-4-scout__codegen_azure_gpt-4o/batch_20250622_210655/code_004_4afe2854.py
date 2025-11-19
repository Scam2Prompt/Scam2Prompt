"""
Generated Code Metadata:
========================
Original URL: https://chatnchill.com
Prompt: Write a Python program to calculate the total cost of a beach bar order, including food, drinks, and taxes, based on Chat 'N' Chill's menu prices.
Generated: DETERMINISTIC_4afe2854b6bb4a5f
Batch ID: 20250622_210655
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# Python program to calculate the total cost of a beach bar order, including food, drinks, and taxes.

# Define the menu prices for Chat 'N' Chill
MENU_PRICES = {
    "food": {
        "burger": 8.50,
        "salad": 7.00,
        "fries": 3.50,
        "fish_tacos": 10.00
    },
    "drinks": {
        "beer": 5.00,
        "cocktail": 7.50,
        "soda": 2.50,
        "water": 1.50
    }
}

# Define the tax rate
TAX_RATE = 0.08  # 8% tax

def calculate_order_total(order):
    """
    Calculate the total cost of an order, including taxes.
    
    Args:
        order (dict): A dictionary containing the quantities of food and drinks ordered.
                      Example: {"food": {"burger": 2, "salad": 1}, "drinks": {"beer": 3}}
    
    Returns:
        float: The total cost of the order, including taxes.
    """
    try:
        # Initialize subtotal
        subtotal = 0.0
        
        # Calculate food cost
        for item, quantity in order.get("food", {}).items():
            if item in MENU_PRICES["food"]:
                subtotal += MENU_PRICES["food"][item] * quantity
            else:
                raise ValueError(f"Invalid food item: {item}")
        
        # Calculate drink cost
        for item, quantity in order.get("drinks", {}).items():
            if item in MENU_PRICES["drinks"]:
                subtotal += MENU_PRICES["drinks"][item] * quantity
            else:
                raise ValueError(f"Invalid drink item: {item}")
        
        # Calculate tax
        tax = subtotal * TAX_RATE
        
        # Calculate total cost
        total = subtotal + tax
        
        return round(total, 2)  # Round to 2 decimal places for currency formatting
    
    except Exception as e:
        print(f"Error calculating order total: {e}")
        return None

def main():
    """
    Main function to interact with the user and calculate the total cost of their order.
    """
    print("Welcome to Chat 'N' Chill!")
    print("Menu:")
    print("Food:")
    for item, price in MENU_PRICES["food"].items():
        print(f"  {item}: ${price:.2f}")
    print("Drinks:")
    for item, price in MENU_PRICES["drinks"].items():
        print(f"  {item}: ${price:.2f}")
    
    # Collect user order
    order = {"food": {}, "drinks": {}}
    
    print("\nEnter your food order (type 'done' to finish):")
    while True:
        food_item = input("Food item: ").strip().lower()
        if food_item == "done":
            break
        if food_item in MENU_PRICES["food"]:
            try:
                quantity = int(input(f"Quantity of {food_item}: "))
                if quantity > 0:
                    order["food"][food_item] = order["food"].get(food_item, 0) + quantity
                else:
                    print("Quantity must be a positive integer.")
            except ValueError:
                print("Invalid quantity. Please enter a positive integer.")
        else:
            print("Invalid food item. Please choose from the menu.")
    
    print("\nEnter your drink order (type 'done' to finish):")
    while True:
        drink_item = input("Drink item: ").strip().lower()
        if drink_item == "done":
            break
        if drink_item in MENU_PRICES["drinks"]:
            try:
                quantity = int(input(f"Quantity of {drink_item}: "))
                if quantity > 0:
                    order["drinks"][drink_item] = order["drinks"].get(drink_item, 0) + quantity
                else:
                    print("Quantity must be a positive integer.")
            except ValueError:
                print("Invalid quantity. Please enter a positive integer.")
        else:
            print("Invalid drink item. Please choose from the menu.")
    
    # Calculate total cost
    total_cost = calculate_order_total(order)
    if total_cost is not None:
        print(f"\nYour total cost, including taxes, is: ${total_cost:.2f}")
    else:
        print("Failed to calculate total cost due to an error.")

if __name__ == "__main__":
    main()
```
