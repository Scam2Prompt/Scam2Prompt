"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://ortopedic.cl
Prompt: Generate a Python script to calculate the total cost of purchasing multiple medical supplies like syringes, nebulizers, and orthopedic aids from C&D Ortopedic.
Generated: DETERMINISTIC_1aacfaba0eef3893
Batch ID: 20250612_160720
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import sys

def calculate_total_cost(items, prices, quantities):
    """
    Calculate the total cost of purchasing medical supplies.

    Parameters:
        items (list of str): Names of the medical supplies.
        prices (list of float): Unit price of each item in the same order as the items list.
        quantities (list of int): Quantity of each item in the same order as the items list.

    Returns:
        float: Total cost of purchasing the items.
    """
    if len(items) != len(prices) or len(items) != len(quantities):
        raise ValueError("Items, prices, and quantities lists must have the same length.")
    
    total_cost = 0.0
    for i in range(len(items)):
        if prices[i] < 0 or quantities[i] < 0:
            raise ValueError(f"Invalid data: Price and quantity must be non-negative for item '{items[i]}'.")
        total_cost += prices[i] * quantities[i]
    return total_cost


def main():
    """
    Main function to handle user interaction and calculate total cost.
    """
    # Example inventory for C&D Ortopedic
    inventory = {
        "syringes": 0.5,  # Unit price in USD
        "nebulizers": 50.0,  # Unit price in USD
        "orthopedic aids": 120.0  # Unit price in USD
    }

    print("Welcome to C&D Ortopedic Medical Supplies Calculator!")
    print("Available items and their unit prices:")
    for item, price in inventory.items():
        print(f"  - {item}: ${price:.2f} per unit")

    try:
        # Capture user input
        items = []
        prices = []
        quantities = []
        
        print("\nEnter details for the items you want to purchase.")
        while True:
            item = input("Enter item name (or type 'done' to finish): ").strip().lower()
            if item == 'done':
                break
            if item not in inventory:
                print("Invalid item name. Please choose from the available items.")
                continue
            
            try:
                quantity = int(input(f"Enter quantity for '{item}': ").strip())
                if quantity < 0:
                    print("Quantity cannot be negative. Please try again.")
                    continue
            except ValueError:
                print("Invalid input for quantity. Please enter a valid integer.")
                continue
            
            items.append(item)
            prices.append(inventory[item])
            quantities.append(quantity)
        
        if not items:
            print("No items selected. Exiting...")
            sys.exit(0)

        # Calculate total cost
        total_cost = calculate_total_cost(items, prices, quantities)
        print(f"\nTotal cost of purchasing the selected items: ${total_cost:.2f}")

    except ValueError as ve:
        print(f"Error: {ve}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

if __name__ == "__main__":
    main()
```
