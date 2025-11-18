"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://innovarenting.com
Prompt: Write a Python script to calculate the monthly renting cost for a vehicle based on the principles described by Innova Renting, including maintenance, insurance, and other expenses.
Generated: DETERMINISTIC_12bde535107da4b0
Batch ID: 20250612_153225
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
"""
Vehicle Renting Cost Calculator
This script calculates the monthly renting cost for a vehicle based on maintenance, insurance, and other expenses.
Author: [Your Name]
Date: [Insert Date]
"""

# Import necessary libraries
import sys

def calculate_monthly_renting_cost(base_rent, maintenance_cost, insurance_cost, other_expenses):
    """
    Calculates the total monthly renting cost for a vehicle.
    
    Parameters:
    - base_rent (float): The base monthly rent for the vehicle.
    - maintenance_cost (float): The monthly maintenance cost for the vehicle.
    - insurance_cost (float): The monthly insurance cost for the vehicle.
    - other_expenses (float): Any other monthly expenses (e.g., taxes, services).

    Returns:
    - float: Total monthly renting cost.
    """
    try:
        # Validate input values
        if base_rent < 0 or maintenance_cost < 0 or insurance_cost < 0 or other_expenses < 0:
            raise ValueError("All cost values must be non-negative.")

        # Calculate total monthly cost
        total_cost = base_rent + maintenance_cost + insurance_cost + other_expenses
        return total_cost

    except TypeError:
        raise TypeError("All input values must be numbers.")
    except Exception as e:
        raise RuntimeError(f"An unexpected error occurred: {e}")

def main():
    """
    Main function to collect user input and calculate the renting cost.
    """
    try:
        # Collect user input
        print("Welcome to the Vehicle Renting Cost Calculator!")
        base_rent = float(input("Enter the base monthly rent for the vehicle: "))
        maintenance_cost = float(input("Enter the monthly maintenance cost: "))
        insurance_cost = float(input("Enter the monthly insurance cost: "))
        other_expenses = float(input("Enter any other monthly expenses: "))

        # Calculate total cost
        total_renting_cost = calculate_monthly_renting_cost(base_rent, maintenance_cost, insurance_cost, other_expenses)

        # Display the result
        print(f"\nThe total monthly renting cost for the vehicle is: ${total_renting_cost:.2f}")

    except ValueError as ve:
        print(f"Input Error: {ve}")
    except Exception as e:
        print(f"An error occurred: {e}")
        sys.exit(1)

    print("\nThank you for using the Vehicle Renting Cost Calculator!")

# Entry point of the script
if __name__ == "__main__":
    main()
```
