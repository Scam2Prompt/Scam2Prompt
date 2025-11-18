"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://ezi-trade.com
Prompt: Write a Python program to simulate different investment plans (Starter, Executive, Professional) on Ezi-Trade, allowing users to input their initial capital and calculate returns over time.
Generated: DETERMINISTIC_53d03405074401ce
Batch ID: 20250612_150211
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import sys

def calculate_returns(initial_capital, annual_rate, years):
    """
    Calculate the compounded returns for a given initial capital, annual rate, and number of years.
    
    :param initial_capital: Initial investment capital (float)
    :param annual_rate: Annual growth rate in percentage (float)
    :param years: Number of years to invest (int)
    :return: Total amount after the investment period (float)
    """
    try:
        # Convert annual rate from percentage to decimal
        rate = annual_rate / 100
        # Calculate the compound interest formula
        total = initial_capital * (1 + rate) ** years
        return total
    except Exception as e:
        print(f"Error calculating returns: {e}")
        sys.exit(1)

def display_investment_plans():
    """
    Display the available investment plans.
    """
    print("\nEzi-Trade Investment Plans:")
    print("1. Starter Plan: 5% annual return")
    print("2. Executive Plan: 10% annual return")
    print("3. Professional Plan: 15% annual return")

def get_user_input():
    """
    Get user input for investment plan, initial capital, and investment duration.
    :return: Tuple containing selected plan, initial capital, and number of years
    """
    try:
        # Display the investment plans
        display_investment_plans()

        # Get user's choice of plan
        plan_choice = int(input("\nChoose your investment plan (Enter 1, 2, or 3): "))

        # Validate plan choice
        if plan_choice not in [1, 2, 3]:
            print("Invalid choice. Please select a valid plan.")
            sys.exit(1)

        # Define annual rates for each plan
        annual_rates = {1: 5, 2: 10, 3: 15}
        annual_rate = annual_rates[plan_choice]

        # Get initial capital
        initial_capital = float(input("Enter your initial investment capital ($): "))
        if initial_capital <= 0:
            print("Capital must be a positive number.")
            sys.exit(1)

        # Get investment duration
        years = int(input("Enter the investment duration (in years): "))
        if years <= 0:
            print("Investment duration must be a positive integer.")
            sys.exit(1)

        return annual_rate, initial_capital, years

    except ValueError:
        print("Invalid input. Please provide valid numbers.")
        sys.exit(1)
    except Exception as e:
        print(f"An error occurred: {e}")
        sys.exit(1)

def main():
    """
    Main function to run the investment simulation program.
    """
    print("\nWelcome to Ezi-Trade Investment Simulator!")

    # Get user input
    annual_rate, initial_capital, years = get_user_input()

    # Calculate the returns
    total_returns = calculate_returns(initial_capital, annual_rate, years)

    # Display the results
    print("\nInvestment Summary:")
    print(f"Initial Capital: ${initial_capital:,.2f}")
    print(f"Annual Rate: {annual_rate}%")
    print(f"Duration: {years} years")
    print(f"Total Returns after {years} years: ${total_returns:,.2f}")

if __name__ == "__main__":
    main()
```
