"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://acextradex.ltd
Prompt: Develop a script that simulates the investment process on Acex Tradex, allowing users to select an investment plan and calculate their returns over time.
Generated: DETERMINISTIC_56ccd4c42ea81c4b
Batch ID: 20250612_164236
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import sys

def display_investment_plans():
    """
    Displays investment plans available for users.
    """
    print("\nAvailable Investment Plans:")
    print("1. Conservative Plan: 5% annual return")
    print("2. Balanced Plan: 10% annual return")
    print("3. Aggressive Plan: 20% annual return")


def calculate_returns(principal, annual_rate, years):
    """
    Calculates investment returns over time using compound interest formula.

    Args:
        principal (float): Initial investment amount.
        annual_rate (float): Annual rate of return (as a percentage).
        years (int): Number of years the investment is held.

    Returns:
        float: Final amount after investment period.
    """
    try:
        # Compound interest formula: A = P * (1 + r)^t
        return principal * (1 + annual_rate / 100) ** years
    except Exception as e:
        print(f"Error calculating returns: {e}")
        sys.exit(1)


def main():
    """
    Main function to simulate the investment process.
    """
    print("Welcome to Acex Tradex Investment Simulator!")

    # Display investment plans
    display_investment_plans()

    try:
        # User chooses an investment plan
        plan_choice = int(input("\nSelect an investment plan (1, 2, or 3): "))
        if plan_choice not in [1, 2, 3]:
            raise ValueError("Invalid choice. Please select a valid plan.")

        # Map plan choice to annual return rate
        annual_rate_map = {1: 5, 2: 10, 3: 20}
        annual_rate = annual_rate_map[plan_choice]

        # User inputs investment details
        principal = float(input("Enter the initial investment amount ($): "))
        if principal <= 0:
            raise ValueError("Investment amount must be greater than zero.")
        
        years = int(input("Enter the number of years for the investment: "))
        if years <= 0:
            raise ValueError("Investment duration must be greater than zero.")

        # Calculate returns
        final_amount = calculate_returns(principal, annual_rate, years)
        
        # Display results
        print("\nInvestment Details:")
        print(f"Initial Amount: ${principal:,.2f}")
        print(f"Annual Rate of Return: {annual_rate}%")
        print(f"Investment Duration: {years} years")
        print(f"Final Amount after {years} years: ${final_amount:,.2f}")

    except ValueError as ve:
        print(f"Input error: {ve}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")


if __name__ == "__main__":
    main()
```
