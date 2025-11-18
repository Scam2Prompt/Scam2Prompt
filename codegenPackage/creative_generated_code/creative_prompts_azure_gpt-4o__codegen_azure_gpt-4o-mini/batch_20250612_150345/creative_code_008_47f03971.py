"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://swifttradeexpress.com
Prompt: Generate a Python program that calculates the total profit for an investor using SwiftTrade Express's trading bot, including deductions for company and administrative commissions.
Generated: DETERMINISTIC_47f039717739f667
Batch ID: 20250612_150345
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
class TradingBot:
    """
    A class to represent a trading bot that calculates total profit for an investor
    after deducting company and administrative commissions.
    """

    def __init__(self, initial_investment: float, trades: list):
        """
        Initializes the TradingBot with the initial investment and a list of trades.

        :param initial_investment: The amount of money initially invested.
        :param trades: A list of trades, where each trade is a dictionary containing:
                       - 'amount': The amount gained/lost from the trade,
                       - 'company_commission': The commission taken by the company,
                       - 'admin_commission': The administrative commission.
        """
        if initial_investment < 0:
            raise ValueError("Initial investment must be a non-negative value.")
        self.initial_investment = initial_investment
        self.trades = trades

    def calculate_total_profit(self) -> float:
        """
        Calculates the total profit after deducting associated commissions from all trades.

        :return: The total profit after deductions.
        """
        total_profit = self.initial_investment

        for trade in self.trades:
            try:
                amount = trade['amount']
                company_commission = trade['company_commission']
                admin_commission = trade['admin_commission']

                if amount < 0 or company_commission < 0 or admin_commission < 0:
                    raise ValueError("Trade amounts and commissions must be non-negative.")

                total_profit += amount - (company_commission + admin_commission)

            except KeyError as e:
                raise KeyError(f"Missing key in trade dictionary: {e}")
            except TypeError:
                raise TypeError("Trade values must be numeric.")

        return total_profit

# Example usage
if __name__ == "__main__":
    try:
        initial_investment = 10000.0  # The initial investment amount
        trades = [
            {'amount': 1500.0, 'company_commission': 50.0, 'admin_commission': 20.0},
            {'amount': -300.0, 'company_commission': 15.0, 'admin_commission': 5.0},
            {'amount': 2000.0, 'company_commission': 60.0, 'admin_commission': 30.0},
        ]

        bot = TradingBot(initial_investment, trades)
        total_profit = bot.calculate_total_profit()
        print(f"Total profit after trades and commissions: ${total_profit:.2f}")

    except Exception as e:
        print(f"An error occurred: {e}")
```
