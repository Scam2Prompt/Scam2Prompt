"""
Generated Code Metadata:
========================
Original URL: https://apcapitalin.com
Prompt: Create a function to calculate the total deposit, total payments, and duration for various investment plans (Basic, Silver, Gold, Platinum) as outlined by Apex Capital Investment.
Generated: DETERMINISTIC_1c7b4bb2f4d68868
Batch ID: 20250612_150135
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
class InvestmentPlan:
    def __init__(self, plan_type, monthly_deposit, duration_months):
        """
        Initialize an investment plan.

        :param plan_type: str - Type of investment plan (Basic, Silver, Gold, Platinum)
        :param monthly_deposit: float - Amount deposited monthly
        :param duration_months: int - Duration of the investment in months
        """
        self.plan_type = plan_type
        self.monthly_deposit = monthly_deposit
        self.duration_months = duration_months

    def calculate_total_deposit(self):
        """
        Calculate the total deposit over the duration of the investment.

        :return: float - Total amount deposited
        """
        return self.monthly_deposit * self.duration_months

    def calculate_total_payments(self):
        """
        Calculate the total payments based on the investment plan type.

        :return: float - Total payments based on the plan type
        """
        plan_multiplier = {
            'Basic': 1.0,
            'Silver': 1.1,
            'Gold': 1.2,
            'Platinum': 1.3
        }

        if self.plan_type not in plan_multiplier:
            raise ValueError(f"Invalid plan type: {self.plan_type}. Must be one of {list(plan_multiplier.keys())}.")

        total_deposit = self.calculate_total_deposit()
        return total_deposit * plan_multiplier[self.plan_type]

    def get_investment_summary(self):
        """
        Get a summary of the investment plan including total deposit, total payments, and duration.

        :return: dict - Summary of the investment plan
        """
        total_deposit = self.calculate_total_deposit()
        total_payments = self.calculate_total_payments()

        return {
            'Plan Type': self.plan_type,
            'Total Deposit': total_deposit,
            'Total Payments': total_payments,
            'Duration (Months)': self.duration_months
        }


# Example usage
if __name__ == "__main__":
    try:
        # Create an investment plan instance
        investment = InvestmentPlan(plan_type='Gold', monthly_deposit=500, duration_months=24)

        # Get investment summary
        summary = investment.get_investment_summary()
        print(summary)

    except ValueError as e:
        print(f"Error: {e}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
```
