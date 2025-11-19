"""
Generated Code Metadata:
========================
Original URL: https://adygeya.propiski-net.ru
Prompt: Write a Python script to calculate the costs of temporary registration for multiple individuals in Adygea, considering the prices starting from 4,000 rubles for a 3-month period.
Generated: DETERMINISTIC_6b316b1cfad56765
Batch ID: 20250622_210216
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
"""
Script to calculate the costs of temporary registration for multiple individuals in Adygea.
The base price is 4,000 rubles for a 3-month period.
"""

# Import necessary modules
import sys

def calculate_registration_costs(individuals, base_price=4000, period_months=3):
    """
    Calculate the total registration costs for multiple individuals.

    Args:
        individuals (int): Number of individuals requiring registration.
        base_price (int): Base price for a 3-month registration period (default: 4000 rubles).
        period_months (int): Duration of the registration period in months (default: 3 months).

    Returns:
        int: Total cost for the registration.
    """
    if individuals <= 0:
        raise ValueError("Number of individuals must be greater than zero.")
    if base_price <= 0:
        raise ValueError("Base price must be greater than zero.")
    if period_months <= 0:
        raise ValueError("Registration period must be greater than zero.")

    # Calculate total cost
    total_cost = individuals * base_price
    return total_cost

def main():
    """
    Main function to handle user input and calculate registration costs.
    """
    try:
        # Prompt user for input
        print("Welcome to the Adygea Temporary Registration Cost Calculator!")
        individuals = int(input("Enter the number of individuals requiring registration: "))
        
        # Calculate costs
        total_cost = calculate_registration_costs(individuals)
        print(f"The total cost for registering {individuals} individuals is: {total_cost} rubles.")
    
    except ValueError as ve:
        print(f"Input error: {ve}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
    finally:
        print("Thank you for using the calculator!")

# Entry point for the script
if __name__ == "__main__":
    main()
```
