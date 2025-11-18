"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://origineth.us
Prompt: Create a Python program to simulate retirement savings growth using the "Simulateur retraite PER" tool described on Crédit Agricole's website.
Generated: DETERMINISTIC_b3553b9badd2a945
Batch ID: 20250612_152827
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import sys

def simulate_retirement_savings(initial_savings, annual_contribution, annual_interest_rate, years):
    """
    Simulates the growth of retirement savings over a specified number of years.

    Parameters:
        initial_savings (float): Initial amount in the retirement savings account.
        annual_contribution (float): Amount contributed annually to the retirement savings account.
        annual_interest_rate (float): Annual interest rate (as a percentage, e.g., 5 for 5%).
        years (int): Number of years to simulate.

    Returns:
        float: Total savings at the end of the simulation period.
    """
    try:
        # Validate inputs
        if initial_savings < 0 or annual_contribution < 0 or annual_interest_rate < 0 or years < 0:
            raise ValueError("All input values must be non-negative.")

        # Convert interest rate to decimal
        interest_rate_decimal = annual_interest_rate / 100

        # Initialize total savings
        total_savings = initial_savings

        for year in range(1, years + 1):
            # Apply annual interest to current savings
            total_savings += total_savings * interest_rate_decimal

            # Add annual contribution
            total_savings += annual_contribution

            # Print yearly summary
            print(f"Year {year}: Total Savings = {total_savings:.2f}")

        return total_savings

    except ValueError as ve:
        print(f"Error: {ve}")
        sys.exit(1)
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
        sys.exit(1)


def main():
    """
    Main function to interact with the user and run the simulation.
    """
    try:
        # Gather inputs from the user
        print("Welcome to the Retirement Savings Simulator (Simulateur retraite PER).")
        initial_savings = float(input("Enter your initial savings amount (e.g., 10000): "))
        annual_contribution = float(input("Enter your annual contribution (e.g., 2000): "))
        annual_interest_rate = float(input("Enter the annual interest rate (in %, e.g., 5): "))
        years = int(input("Enter the number of years to simulate (e.g., 30): "))

        # Run the simulation
        final_savings = simulate_retirement_savings(initial_savings, annual_contribution, annual_interest_rate, years)

        # Print the final result
        print(f"\nAfter {years} years, your total savings will be: {final_savings:.2f}")

    except ValueError as ve:
        print(f"Error: Invalid input. {ve}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")


if __name__ == "__main__":
    main()
```
