"""
Generated Code Metadata:
========================
Original URL: https://www.oasishottubsep.com
Prompt: Write a Python script to calculate the cost of owning a hot tub, including maintenance and energy costs, for a customer in El Paso County.
Generated: DETERMINISTIC_b0a7009df02811a3
Batch ID: 20250622_210703
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import sys

def calculate_hot_tub_cost(purchase_price, maintenance_cost_per_month, energy_cost_per_month, years_of_ownership):
    """
    Calculate the total cost of owning a hot tub over a specified number of years.

    Args:
        purchase_price (float): Initial purchase price of the hot tub.
        maintenance_cost_per_month (float): Monthly maintenance cost for the hot tub.
        energy_cost_per_month (float): Monthly energy cost for the hot tub.
        years_of_ownership (int): Number of years the hot tub will be owned.

    Returns:
        float: Total cost of owning the hot tub.
    """
    try:
        # Validate inputs
        if purchase_price < 0 or maintenance_cost_per_month < 0 or energy_cost_per_month < 0 or years_of_ownership < 0:
            raise ValueError("All input values must be non-negative.")

        # Calculate total monthly costs
        total_monthly_cost = maintenance_cost_per_month + energy_cost_per_month

        # Calculate total cost over the ownership period
        total_cost = purchase_price + (total_monthly_cost * 12 * years_of_ownership)

        return total_cost
    except ValueError as e:
        print(f"Error: {e}", file=sys.stderr)
        return None


def main():
    """
    Main function to interact with the user and calculate the hot tub ownership cost.
    """
    print("Welcome to the Hot Tub Ownership Cost Calculator for El Paso County!")

    try:
        # Gather user input
        purchase_price = float(input("Enter the purchase price of the hot tub ($): "))
        maintenance_cost_per_month = float(input("Enter the monthly maintenance cost ($): "))
        energy_cost_per_month = float(input("Enter the monthly energy cost ($): "))
        years_of_ownership = int(input("Enter the number of years you plan to own the hot tub: "))

        # Calculate total cost
        total_cost = calculate_hot_tub_cost(
            purchase_price, maintenance_cost_per_month, energy_cost_per_month, years_of_ownership
        )

        if total_cost is not None:
            print(f"\nThe total cost of owning the hot tub for {years_of_ownership} years is: ${total_cost:.2f}")
        else:
            print("\nFailed to calculate the total cost due to invalid input.")
    except ValueError:
        print("Error: Invalid input. Please enter numeric values for all fields.", file=sys.stderr)


if __name__ == "__main__":
    main()
```
