"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://centraltraderz.com
Prompt: Write Python code to calculate the expected profit using the investment plans provided on the Centraltraderz website, including parameters like minimum deposit, maximum deposit, payment frequency, and principal return duration.
Generated: DETERMINISTIC_bcc86d9187fff895
Batch ID: 20250612_154236
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
    A class to represent an investment plan with specific attributes.
    """

    def __init__(self, name, min_deposit, max_deposit, payment_frequency, principal_duration, interest_rate):
        """
        Initialize an investment plan.
        :param name: Name of the investment plan (str)
        :param min_deposit: Minimum deposit required (float)
        :param max_deposit: Maximum deposit allowed (float)
        :param payment_frequency: Payment frequency in days (int)
        :param principal_duration: Principal return duration in days (int)
        :param interest_rate: Daily interest rate in percentage (float)
        """
        self.name = name
        self.min_deposit = min_deposit
        self.max_deposit = max_deposit
        self.payment_frequency = payment_frequency
        self.principal_duration = principal_duration
        self.interest_rate = interest_rate

    def calculate_profit(self, deposit_amount):
        """
        Calculate the expected profit for the investment plan based on the deposit amount.
        :param deposit_amount: Amount of money invested (float)
        :return: Expected profit (float)
        """
        if deposit_amount < self.min_deposit or deposit_amount > self.max_deposit:
            raise ValueError(f"Deposit amount must be between {self.min_deposit} and {self.max_deposit}.")

        # Calculate total interest earned during the principal duration
        total_days = self.principal_duration
        total_cycles = total_days // self.payment_frequency
        daily_rate = self.interest_rate / 100  # Convert percentage to decimal
        profit = deposit_amount * daily_rate * total_cycles

        return profit


def main():
    """
    Main function to handle user input and calculate expected profit.
    """
    try:
        # Example investment plans
        plans = [
            InvestmentPlan("Silver Plan", 100, 5000, 7, 30, 1.5),
            InvestmentPlan("Gold Plan", 5000, 20000, 14, 60, 2.0),
            InvestmentPlan("Platinum Plan", 20000, 100000, 30, 90, 2.5)
        ]

        print("Available Investment Plans:")
        for i, plan in enumerate(plans, 1):
            print(f"{i}. {plan.name} (Min: {plan.min_deposit}, Max: {plan.max_deposit}, "
                  f"Frequency: {plan.payment_frequency} days, Duration: {plan.principal_duration} days, "
                  f"Rate: {plan.interest_rate}%)")

        # Select a plan
        plan_choice = int(input("Choose an investment plan by entering its number: "))
        if plan_choice < 1 or plan_choice > len(plans):
            raise ValueError("Invalid plan choice.")

        selected_plan = plans[plan_choice - 1]

        # Input deposit amount
        deposit_amount = float(input(f"Enter an amount to invest in the {selected_plan.name} (Min: {selected_plan.min_deposit}, Max: {selected_plan.max_deposit}): "))

        # Calculate profit
        expected_profit = selected_plan.calculate_profit(deposit_amount)
        print(f"The expected profit for the {selected_plan.name} with a deposit of {deposit_amount} is: ${expected_profit:.2f}")

    except ValueError as ve:
        print(f"Error: {ve}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}", file=sys.stderr)


if __name__ == "__main__":
    main()
```
