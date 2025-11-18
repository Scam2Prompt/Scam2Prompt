"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://orgairways.top
Prompt: Create a Python script to calculate the total cost of selected items in the Velodrome Shop's "Track Essentials Kit" category and simulate a checkout process.
Generated: DETERMINISTIC_ceb6bce736d41720
Batch ID: 20250612_154021
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import sys

def display_items(items):
    """
    Display the available items and their prices in the Track Essentials Kit category.
    """
    print("Welcome to Velodrome Shop - Track Essentials Kit")
    print("Available items:")
    for item_id, details in items.items():
        print(f"{item_id}. {details['name']} - ${details['price']:.2f}")

def get_user_selection(items):
    """
    Prompt the user to select items by entering their corresponding IDs.
    Returns a dictionary of selected items and their quantities.
    """
    print("\nEnter the item IDs you wish to purchase (comma-separated, e.g., 1,2,3).")
    print("Type 'done' to finish selection.")
    
    selected_items = {}
    while True:
        user_input = input("Your selection: ").strip()
        if user_input.lower() == 'done':
            break
        
        try:
            item_ids = [int(id.strip()) for id in user_input.split(",")]
            for item_id in item_ids:
                if item_id not in items:
                    print(f"Invalid item ID: {item_id}. Please select valid IDs only.")
                else:
                    if item_id not in selected_items:
                        selected_items[item_id] = 1
                    else:
                        selected_items[item_id] += 1
        except ValueError:
            print("Invalid input. Please enter valid item IDs.")
    
    return selected_items

def calculate_total_cost(selected_items, items):
    """
    Calculate the total cost of selected items.
    """
    total_cost = 0.0
    for item_id, quantity in selected_items.items():
        total_cost += items[item_id]['price'] * quantity
    return total_cost

def display_checkout_summary(selected_items, items, total_cost):
    """
    Display a summary of the checkout process, including selected items and total cost.
    """
    print("\nCheckout Summary:")
    print("Items Purchased:")
    for item_id, quantity in selected_items.items():
        item_name = items[item_id]['name']
        item_price = items[item_id]['price']
        print(f"{item_name} (x{quantity}) - ${item_price:.2f} each")
    print(f"\nTotal Cost: ${total_cost:.2f}")

def main():
    """
    Main function to simulate the checkout process in Velodrome Shop.
    """
    # Predefined items in the "Track Essentials Kit" category
    items = {
        1: {"name": "Track Helmet", "price": 129.99},
        2: {"name": "Cycling Gloves", "price": 39.99},
        3: {"name": "Speed Suit", "price": 199.99},
        4: {"name": "Track Shoes", "price": 149.99},
        5: {"name": "Bike Pump", "price": 49.99}
    }

    try:
        # Display available items
        display_items(items)

        # Get user selection
        selected_items = get_user_selection(items)

        if not selected_items:
            print("\nNo items were selected. Exiting the checkout process.")
            sys.exit(0)

        # Calculate total cost
        total_cost = calculate_total_cost(selected_items, items)

        # Display checkout summary
        display_checkout_summary(selected_items, items, total_cost)
        
        print("\nThank you for shopping at Velodrome Shop!")

    except Exception as e:
        print(f"An unexpected error occurred: {e}")
        sys.exit(1)

# Entry point for the script
if __name__ == "__main__":
    main()
```
