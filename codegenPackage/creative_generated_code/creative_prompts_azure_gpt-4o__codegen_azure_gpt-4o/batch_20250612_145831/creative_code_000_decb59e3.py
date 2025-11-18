"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://smarts-invests.net
Prompt: Write Python code to calculate projected returns using Smarts-invests' investment plans, incorporating parameters like minimum deposit, payment frequency, and principal return duration.
Generated: DETERMINISTIC_decb59e3b0d42560
Batch ID: 20250612_145831
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
# Import necessary modules
from datetime import datetime, timedelta

# Define a class for Smarts-Invests' Investment Plans
class InvestmentPlan:
    """
    Represents an investment plan offered by Smarts-Invests.
    """

    def __init__(self, plan_name, interest_rate, min_deposit, payment_frequency_days, principal_return_days):
        """
        Initializes a new investment plan.

        Parameters:
        - plan_name (str): Name of the investment plan
        - interest_rate (float): Annual interest rate as a decimal (e.g., 0.05 for 5%)
        - min_deposit (float): Minimum deposit required for the plan
        - payment_frequency_days (int): How often returns are paid (in days)
        - principal_return_days (int): Duration to return the principal amount (in days)
        """
        self.plan_name = plan_name
        self.interest_rate = interest_rate
        self.min_deposit = min_deposit
        self.payment_frequency_days = payment_frequency_days
        self.principal_return_days = principal_return_days

    def calculate_returns(self, deposit_amount, start_date):
        """
        Calculates the projected returns based on the investment parameters.

        Parameters:
        - deposit_amount (float): Amount deposited by the user
        - start_date (datetime): Date when the investment starts

        Returns:
        dict: Contains details of payment schedule, total returns, and principal return date.

        Raises:
        ValueError: If the deposit amount is less than the minimum deposit required.
        """
        if deposit_amount < self.min_deposit:
            raise ValueError(f"The deposit amount must be at least ${self.min_deposit}.")

        # Calculate the daily interest rate
        daily_interest_rate = self.interest_rate / 365

        # Calculate total interest duration in days
        total_days = self.principal_return_days

        # Initialize variables for calculation
        total_returns = 0
        payment_schedule = []
        current_date = start_date

        while total_days > 0:
            # Calculate interest accrued for the payment frequency period
            days_to_next_payment = min(self.payment_frequency_days, total_days)
            interest_accrued = deposit_amount * daily_interest_rate * days_to_next_payment

            # Update total returns
            total_returns += interest_accrued

            # Add payment details to schedule
            payment_schedule.append({
                "payment_date": current_date + timedelta(days=days_to_next_payment),
                "interest_payment": round(interest_accrued, 2)
            })

            # Update current date and remaining duration
            current_date += timedelta(days=days_to_next_payment)
            total_days -= days_to_next_payment

        # Calculate principal return date
        principal_return_date = start_date + timedelta(days=self.principal_return_days)

        return {
            "plan_name": self.plan_name,
            "total_returns": round(total_returns, 2),
            "payment_schedule": payment_schedule,
            "principal_return_date": principal_return_date
        }


# Example usage
if __name__ == "__main__":
    try:
        # Define an investment plan
        smarts_plan = InvestmentPlan(
            plan_name="Smarts-Growth",
            interest_rate=0.05,            # 5% annual interest rate
            min_deposit=1000.0,           # Minimum deposit: $1000
            payment_frequency_days=30,    # Payments every 30 days
            principal_return_days=365     # Principal returned after 1 year
        )

        # User inputs
        start_date = datetime(2023, 10, 1)  # Investment start date
        deposit_amount = 1500.0            # Deposit amount

        # Calculate projected returns
        results = smarts_plan.calculate_returns(deposit_amount, start_date)

        # Print results
        print("Investment Plan:", results["plan_name"])
        print("Total Returns: $", results["total_returns"])
        print("Principal Return Date:", results["principal_return_date"].strftime("%Y-%m-%d"))
        print("\nPayment Schedule:")
        for payment in results["payment_schedule"]:
            print(f"  Payment Date: {payment['payment_date'].strftime('%Y-%m-%d')}, Interest Payment: ${payment['interest_payment']}")

    except ValueError as e:
        print("Error:", e)
    except Exception as e:
        print("An unexpected error occurred:", e)
```
