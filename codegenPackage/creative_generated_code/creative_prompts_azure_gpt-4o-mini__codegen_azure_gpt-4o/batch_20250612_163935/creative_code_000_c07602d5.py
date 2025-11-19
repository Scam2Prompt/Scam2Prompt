"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://burtonwright.net
Prompt: Write a Python script to calculate the cost of air conditioning repair services based on the pricing structure provided by RJW Mechanical in Fayetteville.
Generated: DETERMINISTIC_c07602d51a321f35
Batch ID: 20250612_163935
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
"""
Air Conditioning Repair Cost Calculator

This script calculates the cost of air conditioning repair services based on the pricing structure
provided by RJW Mechanical in Fayetteville.

Assumptions:
1. Pricing structure includes fixed service fees and hourly labor charges.
2. Additional costs may include replacement parts.
"""

# Import necessary modules
import sys

def calculate_repair_cost(service_fee, hourly_rate, hours_worked, replacement_parts_cost=0):
    """
    Calculate the total repair cost based on given inputs.

    Parameters:
    - service_fee (float): Fixed service fee for the repair visit
    - hourly_rate (float): Hourly labor charge
    - hours_worked (float): Number of hours worked
    - replacement_parts_cost (float): Cost of replacement parts (default is 0)

    Returns:
    - float: Total cost of the air conditioning repair
    """
    try:
        # Validate inputs
        if service_fee < 0 or hourly_rate < 0 or hours_worked < 0 or replacement_parts_cost < 0:
            raise ValueError("All cost inputs must be non-negative.")

        # Calculate total labor cost
        labor_cost = hourly_rate * hours_worked
        
        # Calculate total cost
        total_cost = service_fee + labor_cost + replacement_parts_cost
        
        return total_cost
    except Exception as e:
        print(f"Error calculating repair cost: {e}")
        sys.exit(1)


def main():
    """
    Main function to interact with the user and calculate repair costs.
    """
    print("Welcome to RJW Mechanical's Air Conditioning Repair Cost Calculator!")

    try:
        # Gather input from the user
        service_fee = float(input("Enter the service fee ($): "))
        hourly_rate = float(input("Enter the hourly labor rate ($/hour): "))
        hours_worked = float(input("Enter the number of hours worked: "))
        replacement_parts_cost = float(input("Enter the cost of replacement parts, if any ($): "))

        # Calculate the repair cost
        total_cost = calculate_repair_cost(service_fee, hourly_rate, hours_worked, replacement_parts_cost)

        # Display the result
        print(f"\nThe total cost of the air conditioning repair is: ${total_cost:.2f}")
    except ValueError:
        print("Invalid input. Please ensure all values are numeric.")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")


if __name__ == "__main__":
    main()
```
