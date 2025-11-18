"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://digitalwealthtraders.com
Prompt: Create a program to simulate an investment plan with parameters like minimum deposit, duration, and fixed interest rates, as outlined in Digitalwealthtraders' Bronze, Silver, Gold, and Platinum plans.
Generated: DETERMINISTIC_2b72c67896f0f1f9
Batch ID: 20250612_150446
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import sys


class InvestmentPlan:
    """
    A class to represent an investment plan.

    Attributes:
        name (str): Name of the investment plan.
        min_deposit (float): Minimum deposit required for this investment plan.
        interest_rate (float): Fixed annual interest rate (in percentage).
        duration_months (int): Duration of the investment in months.
    """
    def __init__(self, name, min_deposit, interest_rate, duration_months):
        self.name = name
        self.min_deposit = min_deposit
        self.interest_rate = interest_rate
        self.duration_months = duration_months

    def calculate_return(self, deposit):
        """
        Calculate the total return based on the deposit and fixed interest rate.
        
        Args:
            deposit (float): The investment amount.

        Returns:
            float: The total return on investment after the duration.
        """
        if deposit < self.min_deposit:
            raise ValueError(
                f"Deposit amount must be at least {self.min_deposit} for the {self.name} plan."
            )
        # Convert annual interest rate to monthly
        monthly_interest_rate = self.interest_rate / 100 / 12
        # Compound interest formula: A = P(1 + r)^n
        total_return = deposit * (1 + monthly_interest_rate) ** self.duration_months
        return total_return


def main():
    try:
        # Define the investment plans
        plans = [
            InvestmentPlan("Bronze", min_deposit=100, interest_rate=5, duration_months=12),
            InvestmentPlan("Silver", min_deposit=1000, interest_rate=8, duration_months=24),
            InvestmentPlan("Gold", min_deposit=5000, interest_rate=10, duration_months=36),
            InvestmentPlan("Platinum", min_deposit=20000, interest_rate=15, duration_months=60),
        ]

        # Display available plans
        print("Available Investment Plans:")
        for i, plan in enumerate(plans, start=1):
            print(f"{i}. {plan.name} Plan - Minimum Deposit: ${plan.min_deposit}, "
                  f"Interest Rate: {plan.interest_rate}%, Duration: {plan.duration_months} months")

        # Get user's choice of investment plan
        choice = int(input("\nSelect a plan by entering the corresponding number (1-4): "))
        if choice < 1 or choice > len(plans):
            raise ValueError("Invalid choice. Please select a valid plan number.")

        selected_plan = plans[choice - 1]

        # Get deposit amount
        deposit = float(input(f"Enter your deposit amount for the {selected_plan.name} Plan: $"))

        # Calculate and display the total return
        total_return = selected_plan.calculate_return(deposit)
        print(f"\nAfter {selected_plan.duration_months} months, your total return on the "
              f"{selected_plan.name} Plan will be: ${total_return:,.2f}")

    except ValueError as ve:
        # Handle invalid inputs
        print(f"Error: {ve}")
    except Exception as e:
        # Handle unexpected errors
        print(f"An unexpected error occurred: {e}")
    finally:
        print("\nThank you for using the Investment Plan Simulator!")


# Entry point for the program
if __name__ == "__main__":
    main()
```
