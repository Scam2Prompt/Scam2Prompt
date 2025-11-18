"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://karenfixing.com
Prompt: Generate a script to calculate the cost of facade installation using Karen Fixing's products, including payment terms like "پرداخت توافقی."
Generated: DETERMINISTIC_f1517aa86a3f416c
Batch ID: 20250612_153224
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

Here is a Python script for calculating the cost of facade installation using Karen Fixing's products with support for "پرداخت توافقی" (custom payment terms):

```python
# facade_cost_calculator.py

import sys

def calculate_facade_cost(material_cost_per_sq_meter, area_sq_meter, labor_cost_per_sq_meter, discount_percentage=0):
    """
    Calculates the total cost for facade installation.

    Args:
        material_cost_per_sq_meter (float): Cost of materials per square meter.
        area_sq_meter (float): Total area of the facade in square meters.
        labor_cost_per_sq_meter (float): Labor cost per square meter.
        discount_percentage (float): Discount percentage to apply to the total cost.

    Returns:
        float: Total cost after applying discount.
    """
    try:
        if material_cost_per_sq_meter < 0 or area_sq_meter < 0 or labor_cost_per_sq_meter < 0 or discount_percentage < 0:
            raise ValueError("All cost and percentage values must be non-negative.")

        # Calculate base cost
        total_material_cost = material_cost_per_sq_meter * area_sq_meter
        total_labor_cost = labor_cost_per_sq_meter * area_sq_meter
        total_cost = total_material_cost + total_labor_cost

        # Apply discount
        discount_amount = (discount_percentage / 100) * total_cost
        final_cost = total_cost - discount_amount

        return round(final_cost, 2)  # Rounded to 2 decimal places for cleaner output
    except ValueError as ve:
        print(f"Error: {ve}")
        sys.exit(1)
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
        sys.exit(1)


def display_payment_terms():
    """
    Displays the available payment terms.
    """
    print("\nAvailable Payment Terms:")
    print("1. Full payment upon project completion.")
    print("2. Installment plan.")
    print("3. Custom terms (پرداخت توافقی).")


def main():
    """
    Main function to drive the script.
    """
    print("Karen Fixing Facade Cost Calculator\n")

    try:
        # User input for cost parameters
        material_cost = float(input("Enter material cost per square meter: "))
        area = float(input("Enter facade area in square meters: "))
        labor_cost = float(input("Enter labor cost per square meter: "))
        discount = float(input("Enter discount percentage (0 if none): "))

        # Calculate the cost
        total_cost = calculate_facade_cost(material_cost, area, labor_cost, discount)

        # Display the results
        print("\nCalculation Results:")
        print(f"Total cost for the facade installation: {total_cost} USD")

        # Display payment terms
        display_payment_terms()

    except ValueError:
        print("Invalid input. Please enter numeric values only.")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")


if __name__ == "__main__":
    main()
```

Save this script as `facade_cost_calculator.py` and run it in a Python environment. It will prompt you for input values and calculate the cost while displaying payment terms.
