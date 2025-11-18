"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://uniaircargo.id
Prompt: Create a Python script to calculate cargo insurance premiums based on Uniair Cargo’s insurance brokerage services.
Generated: DETERMINISTIC_7d2562ec29ed4b30
Batch ID: 20250612_153954
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
"""
Cargo Insurance Premium Calculator

This script calculates the insurance premiums for cargo based on Uniair Cargo's
insurance brokerage services. The formula for calculating premiums is based on
the declared cargo value and the specified rate percentage.
"""

import sys

def calculate_insurance_premium(cargo_value, rate_percentage):
    """
    Calculates the insurance premium based on cargo value and rate percentage.

    Parameters:
        cargo_value (float): The declared value of the cargo (in USD).
        rate_percentage (float): The rate percentage (as a percentage, e.g., 1.5 for 1.5%).

    Returns:
        float: The calculated insurance premium.

    Raises:
        ValueError: If cargo_value or rate_percentage is negative.
    """
    if cargo_value < 0:
        raise ValueError("Cargo value cannot be negative.")
    if rate_percentage < 0:
        raise ValueError("Rate percentage cannot be negative.")

    # Formula to calculate insurance premium
    premium = cargo_value * (rate_percentage / 100)
    return premium

def prompt_user_input():
    """
    Prompts the user for input and calculates the insurance premium.

    Returns:
        None
    """
    try:
        # Gather input from the user
        cargo_value = float(input("Enter the cargo value (in USD): "))
        rate_percentage = float(input("Enter the rate percentage (e.g., enter 1.5 for 1.5%): "))

        # Calculate the premium
        premium = calculate_insurance_premium(cargo_value, rate_percentage)

        # Display the result
        print(f"The insurance premium for your cargo is: ${premium:.2f}")
    except ValueError as e:
        # Handle invalid input
        print(f"Error: {e}")
    except Exception as e:
        # Handle unexpected errors
        print(f"An unexpected error occurred: {e}")
        sys.exit(1)

if __name__ == "__main__":
    """
    Main entry point of the script. Prompts the user for input and calculates
    the insurance premium.
    """
    print("Welcome to Uniair Cargo Insurance Premium Calculator")
    prompt_user_input()
```
