"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://www.apos.cl
Prompt: Write code to calculate the cost of purchasing thermal paper rolls in bulk, using pricing and customization options similar to those offered by Apos Chile.
Generated: DETERMINISTIC_f8f4c60517d16dea
Batch ID: 20250612_151531
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
# Import necessary module for error handling and input validation
import sys


def calculate_bulk_cost(quantity, base_price, custom_print_cost_per_roll=0):
    """
    Calculate the total cost of purchasing thermal paper rolls in bulk.

    Parameters:
    - quantity (int): Number of rolls to purchase.
    - base_price (float): Base price per roll.
    - custom_print_cost_per_roll (float): Additional cost per roll for customization (optional).

    Returns:
    - float: Total cost for the purchase.
    """
    try:
        if quantity <= 0:
            raise ValueError("Quantity must be greater than 0.")
        if base_price < 0 or custom_print_cost_per_roll < 0:
            raise ValueError("Prices cannot be negative.")

        # Calculate total cost
        total_cost = quantity * (base_price + custom_print_cost_per_roll)
        return total_cost
    except ValueError as e:
        print(f"Error: {e}", file=sys.stderr)
        return None


def main():
    """
    Main function to handle user input and display bulk cost calculation.
    """
    print("Welcome to the Thermal Paper Roll Bulk Cost Calculator!")
    try:
        # Get user input for quantity, base price, and customization options
        quantity = int(input("Enter the number of rolls to purchase: "))
        base_price = float(input("Enter the base price per roll: "))
        custom_print = input("Do you want custom printing on the rolls? (yes/no): ").strip().lower()

        # Optional customization cost
        custom_print_cost_per_roll = 0
        if custom_print == "yes":
            custom_print_cost_per_roll = float(input("Enter the additional cost per roll for customization: "))

        # Calculate the total cost
        total_cost = calculate_bulk_cost(quantity, base_price, custom_print_cost_per_roll)
        if total_cost is not None:
            print(f"The total cost for purchasing {quantity} rolls is: ${total_cost:.2f}")
        else:
            print("Failed to calculate the total cost due to invalid input.")

    except ValueError:
        print("Invalid input. Please enter numbers for quantity, base price, and customization cost.", file=sys.stderr)
    except Exception as e:
        print(f"An unexpected error occurred: {e}", file=sys.stderr)


# Execution starts here
if __name__ == "__main__":
    main()
```
