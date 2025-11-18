"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://pipelinefinanceconseil.com
Prompt: Write Python code to simulate a savings plan with a fixed interest rate of 7.62%, as described in the "Sans Risque" formula on pipelinefinanceconseil.com. Include functionality to calculate quarterly gains and total returns over a specified period.
Generated: DETERMINISTIC_c5a039b07ba4ebcd
Batch ID: 20250612_154306
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
"""
Savings Plan Simulator with Fixed Interest Rate
Author: Expert Programmer

This script simulates a savings plan with a fixed interest rate of 7.62%, 
allowing calculation of quarterly gains and total returns over a specified period.

Usage:
- Define the initial savings amount, duration in years, and interest rate.
- Run the script to calculate quarterly gains and total returns.
"""

import sys

def simulate_savings_plan(initial_amount, annual_interest_rate, years):
    """
    Simulates a savings plan based on a fixed annual interest rate.

    Args:
        initial_amount (float): The starting amount in the savings account.
        annual_interest_rate (float): The annual interest rate (e.g., 7.62 for 7.62%).
        years (int): The number of years the savings plan will run.

    Returns:
        dict: Dictionary containing quarterly gains and total returns.
    """
    try:
        # Ensure valid inputs
        if initial_amount <= 0:
            raise ValueError("Initial amount must be greater than zero.")
        if annual_interest_rate <= 0:
            raise ValueError("Annual interest rate must be greater than zero.")
        if years <= 0:
            raise ValueError("Duration in years must be greater than zero.")

        # Convert annual interest rate to quarterly interest rate
        quarterly_interest_rate = annual_interest_rate / 100 / 4

        # Initialize variables
        total_amount = initial_amount
        quarterly_gains = []

        # Calculate gains for each quarter
        for quarter in range(1, years * 4 + 1):
            gain = total_amount * quarterly_interest_rate
            quarterly_gains.append((quarter, round(gain, 2)))
            total_amount += gain

        # Prepare result
        total_returns = round(total_amount, 2)

        return {
            "quarterly_gains": quarterly_gains,
            "total_returns": total_returns
        }

    except ValueError as ve:
        print(f"Input Error: {ve}", file=sys.stderr)
        return None
    except Exception as e:
        print(f"Unexpected Error: {e}", file=sys.stderr)
        return None


def main():
    """
    Main function to execute the savings plan simulation.
    """
    print("Welcome to the Savings Plan Simulator")
    
    try:
        # Gather user inputs
        initial_amount = float(input("Enter the initial savings amount: "))
        annual_interest_rate = float(input("Enter the annual interest rate (e.g., 7.62 for 7.62%): "))
        years = int(input("Enter the duration in years: "))

        # Run simulation
        results = simulate_savings_plan(initial_amount, annual_interest_rate, years)

        # Display results
        if results:
            print("\nQuarterly Gains:")
            for quarter, gain in results["quarterly_gains"]:
                print(f"Quarter {quarter}: ${gain}")

            print(f"\nTotal Returns after {years} years: ${results['total_returns']}")
        else:
            print("Simulation failed due to invalid input or unexpected error.")

    except ValueError:
        print("Invalid input. Please ensure numbers are entered correctly.")
    except Exception as e:
        print(f"An error occurred: {e}", file=sys.stderr)


if __name__ == "__main__":
    main()
```
