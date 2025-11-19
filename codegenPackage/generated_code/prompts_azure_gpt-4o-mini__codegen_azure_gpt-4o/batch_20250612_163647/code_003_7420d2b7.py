"""
Generated Code Metadata:
========================
Original URL: https://pipelinefinanceconseil.com
Prompt: Develop a script that models the impact of quarterly withdrawals on a savings plan with a variable average rate of 9.24%, reflecting the features of Pipeline Finance Conseil.
Generated: DETERMINISTIC_7420d2b7251b9fb9
Batch ID: 20250612_163647
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import math

def calculate_savings_with_withdrawals(initial_balance, quarterly_withdrawal, annual_rate, years):
    """
    Models the impact of quarterly withdrawals on a savings plan.

    Parameters:
        initial_balance (float): The starting balance in the savings account.
        quarterly_withdrawal (float): The amount withdrawn at the end of each quarter.
        annual_rate (float): The annual interest rate (as a percentage, e.g., 9.24 for 9.24%).
        years (int): The number of years to model.

    Returns:
        list: A list of tuples containing the quarter number and the balance at the end of that quarter.
    """
    # Convert annual rate to quarterly rate
    quarterly_rate = annual_rate / 100 / 4

    # Initialize variables
    balance = initial_balance
    results = []

    # Calculate the total number of quarters
    total_quarters = years * 4

    for quarter in range(1, total_quarters + 1):
        # Apply interest for the quarter
        balance += balance * quarterly_rate

        # Deduct the quarterly withdrawal
        balance -= quarterly_withdrawal

        # Ensure balance does not go negative
        if balance < 0:
            balance = 0

        # Store the result for this quarter
        results.append((quarter, round(balance, 2)))

        # Stop if balance reaches zero
        if balance == 0:
            break

    return results


def main():
    """
    Main function to execute the savings plan model.
    """
    try:
        # Input parameters
        initial_balance = float(input("Enter the initial balance in the savings account: "))
        quarterly_withdrawal = float(input("Enter the quarterly withdrawal amount: "))
        annual_rate = float(input("Enter the annual interest rate (e.g., 9.24 for 9.24%): "))
        years = int(input("Enter the number of years to model: "))

        # Validate inputs
        if initial_balance < 0 or quarterly_withdrawal < 0 or annual_rate < 0 or years <= 0:
            raise ValueError("All inputs must be positive numbers, and years must be greater than zero.")

        # Calculate savings plan
        results = calculate_savings_with_withdrawals(initial_balance, quarterly_withdrawal, annual_rate, years)

        # Display results
        print("\nQuarterly Savings Plan Results:")
        print("Quarter | Balance")
        print("------------------")
        for quarter, balance in results:
            print(f"{quarter:7} | ${balance:,.2f}")

    except ValueError as ve:
        print(f"Input Error: {ve}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")


if __name__ == "__main__":
    main()
```
