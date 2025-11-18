"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://propsfundedtrader.com
Prompt: Write Python code to automate the calculation of a 10% monthly ROI for a $100,000 funded trading account, factoring in profit splits of 30% for the service provider, 10% for the prop firm, and 60% for the account owner.
Generated: DETERMINISTIC_c3a298f85045cbf1
Batch ID: 20250612_153224
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
class TradingAccount:
    """
    A class to represent a funded trading account and calculate the returns
    based on a specified monthly Return on Investment (ROI) and profit splits.
    """
    
    def __init__(self, initial_funds: float, monthly_roi: float):
        """
        Initializes the TradingAccount with an initial fund amount and monthly ROI.

        :param initial_funds: The initial amount in the trading account.
        :param monthly_roi: The expected monthly return on investment as a decimal.
        """
        self.initial_funds = initial_funds
        self.monthly_roi = monthly_roi
        self.profit_splits = {
            'service_provider': 0.30,
            'prop_firm': 0.10,
            'account_owner': 0.60
        }

    def calculate_monthly_profit(self) -> float:
        """
        Calculates the total monthly profit based on the initial funds and ROI.

        :return: The total profit for the month.
        """
        try:
            profit = self.initial_funds * self.monthly_roi
            return profit
        except Exception as e:
            print(f"Error calculating monthly profit: {str(e)}")
            return 0.0

    def calculate_profit_distribution(self) -> dict:
        """
        Distributes the profit according to the defined profit splits.

        :return: A dictionary with the profit distribution.
        """
        monthly_profit = self.calculate_monthly_profit()
        distribution = {}

        for key, split in self.profit_splits.items():
            distribution[key] = monthly_profit * split

        return distribution

    def display_profit_distribution(self):
        """
        Displays the profit distribution for the month.
        """
        distribution = self.calculate_profit_distribution()
        print("Profit Distribution for the Month:")
        for key, value in distribution.items():
            print(f"{key.replace('_', ' ').title()}: ${value:,.2f}")

def main():
    """
    The main function to execute the trading account calculations.
    """
    initial_funds = 100000.00  # Initial funded amount
    monthly_roi = 0.10          # Monthly ROI of 10%

    trading_account = TradingAccount(initial_funds, monthly_roi)

    # Display the profit distribution
    trading_account.display_profit_distribution()

if __name__ == "__main__":
    main()
```
