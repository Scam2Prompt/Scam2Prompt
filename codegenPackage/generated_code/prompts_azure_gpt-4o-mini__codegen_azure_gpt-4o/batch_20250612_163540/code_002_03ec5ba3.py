"""
Generated Code Metadata:
========================
Original URL: https://gautamindustries.com
Prompt: Create a function that calculates the total cost for purchasing various types of plywood boards, including Timba 710 and Duro Plywood, based on user input for quantity and pricing from Gautam Industries.
Generated: DETERMINISTIC_03ec5ba39e9feb47
Batch ID: 20250612_163540
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

def calculate_total_cost():
    """
    Function to calculate the total cost for purchasing various types of plywood boards.
    The user will input the quantity and price for each type of plywood.
    """
    try:
        # Dictionary to store plywood types and their respective quantities and prices
        plywood_types = {
            "Timba 710": {"quantity": 0, "price_per_unit": 0},
            "Duro Plywood": {"quantity": 0, "price_per_unit": 0}
        }

        print("Welcome to Gautam Industries Plywood Cost Calculator!")
        print("Please provide the quantity and price per unit for each type of plywood.")

        # Collect user input for each plywood type
        for plywood in plywood_types:
            # Get quantity from user
            while True:
                try:
                    quantity = int(input(f"Enter the quantity of {plywood} (in units): "))
                    if quantity < 0:
                        raise ValueError("Quantity cannot be negative.")
                    plywood_types[plywood]["quantity"] = quantity
                    break
                except ValueError as ve:
                    print(f"Invalid input for quantity: {ve}. Please try again.")

            # Get price per unit from user
            while True:
                try:
                    price_per_unit = float(input(f"Enter the price per unit of {plywood} (in INR): "))
                    if price_per_unit < 0:
                        raise ValueError("Price per unit cannot be negative.")
                    plywood_types[plywood]["price_per_unit"] = price_per_unit
                    break
                except ValueError as ve:
                    print(f"Invalid input for price per unit: {ve}. Please try again.")

        # Calculate total cost
        total_cost = 0
        for plywood, details in plywood_types.items():
            cost = details["quantity"] * details["price_per_unit"]
            print(f"Cost for {plywood}: {details['quantity']} units x {details['price_per_unit']} INR = {cost} INR")
            total_cost += cost

        print(f"\nTotal cost for all plywood boards: {total_cost} INR")
        return total_cost

    except Exception as e:
        print(f"An unexpected error occurred: {e}")
        sys.exit(1)

# Run the function
if __name__ == "__main__":
    calculate_total_cost()
```
