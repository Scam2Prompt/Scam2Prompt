"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://metamaskcoins.com
Prompt: Write a code snippet that calculates potential profits based on the trading plans offered by Meta Mask Coins, including different deposit ranges and profit percentages.
Generated: DETERMINISTIC_38dc242eec8170ee
Batch ID: 20250612_135129
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
class TradingPlan:
    """
    A class to represent a trading plan for calculating potential profits.
    """

    def __init__(self, deposit_range: tuple, profit_percentage: float):
        """
        Initialize a trading plan with a deposit range and profit percentage.

        :param deposit_range: A tuple containing the minimum and maximum deposit amounts (min, max).
        :param profit_percentage: The percentage of profit to be calculated.
        """
        self.deposit_range = deposit_range
        self.profit_percentage = profit_percentage

    def calculate_profit(self, deposit_amount: float) -> float:
        """
        Calculate the potential profit based on the given deposit amount.

        :param deposit_amount: The amount of money deposited for trading.
        :return: The calculated profit.
        :raises ValueError: If the deposit amount is outside the defined deposit range.
        """
        min_deposit, max_deposit = self.deposit_range

        if deposit_amount < min_deposit or deposit_amount > max_deposit:
            raise ValueError(f"Deposit amount must be between {min_deposit} and {max_deposit}, inclusive.")

        profit = deposit_amount * (self.profit_percentage / 100)
        return profit


def main():
    """
    Main function to demonstrate the calculation of potential profits.
    """
    # Example trading plans
    plans = [
        TradingPlan((100, 1000), 10),  # 10% profit for deposits between $100 and $1000
        TradingPlan((1000, 5000), 15),  # 15% profit for deposits between $1000 and $5000
        TradingPlan((5000, 10000), 20),  # 20% profit for deposits between $5000 and $10000
    ]

    # Example deposit amounts to calculate profits
    deposits = [150, 1200, 8000, 50]  # Includes an out-of-range deposit amount for testing

    for deposit in deposits:
        print(f"Calculating profit for deposit amount: ${deposit}")
        for plan in plans:
            try:
                profit = plan.calculate_profit(deposit)
                print(f"  Plan with deposit range {plan.deposit_range} and profit percentage {plan.profit_percentage}%: Profit = ${profit:.2f}")
            except ValueError as e:
                print(f"  {e}")

if __name__ == "__main__":
    main()
```
