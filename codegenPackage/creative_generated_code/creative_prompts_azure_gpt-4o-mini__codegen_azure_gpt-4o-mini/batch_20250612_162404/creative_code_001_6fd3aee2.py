"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://maxgainfinance.com
Prompt: Write a function that calculates potential profits based on the investment plans (Basic, Classic, VIP, etc.) offered by Max Gain Finance, including minimum and maximum deposit amounts.
Generated: DETERMINISTIC_6fd3aee2f38682b5
Batch ID: 20250612_162404
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
class InvestmentPlan:
    """
    A class to represent an investment plan with associated parameters.
    """
    def __init__(self, name: str, min_deposit: float, max_deposit: float, return_rate: float):
        """
        Initializes an investment plan with the given parameters.

        :param name: The name of the investment plan (e.g., Basic, Classic, VIP).
        :param min_deposit: Minimum deposit amount for the investment plan.
        :param max_deposit: Maximum deposit amount for the investment plan.
        :param return_rate: The return rate of the investment plan as a percentage.
        """
        self.name = name
        self.min_deposit = min_deposit
        self.max_deposit = max_deposit
        self.return_rate = return_rate

    def calculate_profit(self, deposit: float) -> float:
        """
        Calculate potential profit based on the deposit amount.

        :param deposit: The amount being invested.
        :return: The potential profit from the investment.
        :raises ValueError: If the deposit amount is outside the allowed range.
        """
        if deposit < self.min_deposit or deposit > self.max_deposit:
            raise ValueError(f"Deposit must be between {self.min_deposit} and {self.max_deposit} for the {self.name} plan.")

        profit = deposit * (self.return_rate / 100)
        return profit


def main():
    # Define investment plans
    investment_plans = [
        InvestmentPlan("Basic", 100, 1000, 5),
        InvestmentPlan("Classic", 1000, 5000, 8),
        InvestmentPlan("VIP", 5000, 20000, 12),
    ]

    # Example usage
    try:
        deposit_amount = 1500  # Example deposit amount
        selected_plan = investment_plans[1]  # Select Classic plan

        # Calculate potential profit
        profit = selected_plan.calculate_profit(deposit_amount)
        print(f"Potential profit from {selected_plan.name} plan for a deposit of {deposit_amount}: {profit:.2f}")

    except ValueError as e:
        print(e)


if __name__ == "__main__":
    main()
```
