"""
Generated Code Metadata:
========================
Original URL: https://apnhardware.co.th
Prompt: "Write a Python code to calculate the total cost of ordering stainless steel screws and nuts from a wholesale supplier like APN Hardware."
Generated: DETERMINISTIC_89334c5aeba8ab24
Batch ID: 20250622_205919
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# Import necessary modules
import sys

def calculate_total_cost(screw_price, nut_price, screw_quantity, nut_quantity):
    """
    Calculate the total cost of screws and nuts.

    Parameters:
        screw_price (float): Price per screw.
        nut_price (float): Price per nut.
        screw_quantity (int): Quantity of screws ordered.
        nut_quantity (int): Quantity of nuts ordered.

    Returns:
        float: Total cost of the order.
    """
    try:
        # Validate inputs
        if screw_price < 0 or nut_price < 0:
            raise ValueError("Prices must be non-negative.")
        if screw_quantity < 0 or nut_quantity < 0:
            raise ValueError("Quantities must be non-negative.")

        # Calculate total cost
        total_cost = (screw_price * screw_quantity) + (nut_price * nut_quantity)
        return total_cost

    except ValueError as ve:
        print(f"Input Error: {ve}", file=sys.stderr)
        return None
    except Exception as e:
        print(f"An unexpected error occurred: {e}", file=sys.stderr)
        return None

def main():
    """
    Main function to interact with the user and calculate the total cost.
    """
    print("Welcome to the Stainless Steel Screws and Nuts Cost Calculator!")
    
    try:
        # Get user inputs
        screw_price = float(input("Enter the price per screw: "))
        nut_price = float(input("Enter the price per nut: "))
        screw_quantity = int(input("Enter the quantity of screws: "))
        nut_quantity = int(input("Enter the quantity of nuts: "))

        # Calculate total cost
        total_cost = calculate_total_cost(screw_price, nut_price, screw_quantity, nut_quantity)

        if total_cost is not None:
            print(f"The total cost of your order is: ${total_cost:.2f}")
        else:
            print("Failed to calculate the total cost due to input errors.")

    except ValueError:
        print("Invalid input. Please enter numeric values for prices and quantities.", file=sys.stderr)
    except Exception as e:
        print(f"An unexpected error occurred: {e}", file=sys.stderr)

# Entry point of the program
if __name__ == "__main__":
    main()
```
