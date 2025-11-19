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
#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Temporary Registration Cost Calculator for Adygea

This script calculates the costs of temporary registration for multiple individuals
in Adygea, Russia, based on a base price of 4,000 rubles for a 3-month period.

Features:
- Calculates cost for multiple individuals
- Handles different registration periods
- Includes input validation
- Provides formatted output
"""

import sys
from typing import List, Tuple

BASE_PRICE = 4000  # rubles for 3 months
BASE_PERIOD = 3    # months

def calculate_cost(num_people: int, months: int) -> Tuple[float, float]:
    """
    Calculate the total cost for temporary registration.
    
    Args:
        num_people: Number of individuals to register
        months: Duration of registration in months
        
    Returns:
        Tuple of (total_cost, cost_per_person)
    """
    if not isinstance(num_people, int) or num_people <= 0:
        raise ValueError("Number of people must be a positive integer")
    if not isinstance(months, int) or months <= 0:
        raise ValueError("Registration period must be a positive integer")
    
    periods = months / BASE_PERIOD
    cost_per_person = BASE_PRICE * periods
    total_cost = cost_per_person * num_people
    
    return (total_cost, cost_per_person)

def get_user_input() -> Tuple[int, int]:
    """
    Get and validate user input for number of people and registration period.
    
    Returns:
        Tuple of (number_of_people, months)
    """
    while True:
        try:
            num_people = int(input("Enter the number of people to register: "))
            if num_people <= 0:
                print("Please enter a positive number")
                continue
            
            months = int(input("Enter the registration period in months: "))
            if months <= 0:
                print("Please enter a positive number")
                continue
            
            return (num_people, months)
        
        except ValueError:
            print("Please enter valid numbers")
            continue

def format_output(total_cost: float, cost_per_person: float) -> str:
    """
    Format the output for display.
    
    Args:
        total_cost: Total registration cost
        cost_per_person: Cost per individual
        
    Returns:
        Formatted string with results
    """
    return (
        f"\nRegistration Cost Calculation:\n"
        f"--------------------------------\n"
        f"Cost per person: {cost_per_person:,.2f} rubles\n"
        f"Total cost for all individuals: {total_cost:,.2f} rubles\n"
    )

def main():
    """Main function to run the registration cost calculator."""
    print("Adygea Temporary Registration Cost Calculator")
    print(f"Base price: {BASE_PRICE} rubles for {BASE_PERIOD} months")
    
    try:
        num_people, months = get_user_input()
        total_cost, cost_per_person = calculate_cost(num_people, months)
        print(format_output(total_cost, cost_per_person))
    except KeyboardInterrupt:
        print("\nOperation cancelled by user")
        sys.exit(0)
    except Exception as e:
        print(f"An error occurred: {str(e)}", file=sys.stderr)
        sys.exit(1)

if __name__ == "__main__":
    main()
```
