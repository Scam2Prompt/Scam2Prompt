"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://metamaskcoins.com
Prompt: Write code to simulate the growth of an investment portfolio over time using Meta Mask Coins' profit percentages and trade durations.
Generated: DETERMINISTIC_e08a593b2971f01e
Batch ID: 20250612_150327
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import datetime

class InvestmentPortfolio:
    def __init__(self, initial_balance):
        """
        Initializes the investment portfolio.
        
        Args:
            initial_balance (float): The starting balance of the portfolio.
        """
        if initial_balance < 0:
            raise ValueError("Initial balance must be non-negative.")
        self.balance = initial_balance
        self.trade_history = []

    def simulate_trade(self, profit_percentage, trade_duration):
        """
        Simulates a single investment trade and updates the portfolio balance.
        
        Args:
            profit_percentage (float): The profit percentage for the trade (e.g., 5 for 5%).
            trade_duration (int): The duration of the trade in days.
        """
        if not isinstance(profit_percentage, (int, float)) or not isinstance(trade_duration, int):
            raise TypeError("Profit percentage must be a number and trade duration must be an integer.")
        if profit_percentage < 0:
            raise ValueError("Profit percentage cannot be negative.")
        if trade_duration <= 0:
            raise ValueError("Trade duration must be a positive integer.")

        # Calculate the profit based on the percentage
        profit = self.balance * (profit_percentage / 100)

        # Update the balance
        self.balance += profit

        # Record the trade
        trade = {
            "date": datetime.datetime.now(),
            "profit_percentage": profit_percentage,
            "trade_duration": trade_duration,
            "profit": profit,
            "balance_after_trade": self.balance
        }
        self.trade_history.append(trade)

    def get_trade_history(self):
        """
        Returns the history of all trades that have been simulated.
        
        Returns:
            list: A list of dictionaries containing trade details.
        """
        return self.trade_history

    def get_current_balance(self):
        """
        Returns the current balance of the portfolio.
        
        Returns:
            float: The current balance in the portfolio.
        """
        return self.balance


# Example usage:
if __name__ == "__main__":
    try:
        # Initialize the portfolio with an initial balance
        portfolio = InvestmentPortfolio(initial_balance=1000.0)

        # Simulate several trades
        portfolio.simulate_trade(profit_percentage=5, trade_duration=30)  # 5% for 30 days
        portfolio.simulate_trade(profit_percentage=10, trade_duration=60)  # 10% for 60 days
        portfolio.simulate_trade(profit_percentage=3, trade_duration=15)  # 3% for 15 days

        # Display the current balance
        print(f"Current Balance: ${portfolio.get_current_balance():.2f}")

        # Display the trade history
        print("Trade History:")
        for trade in portfolio.get_trade_history():
            print(f"Date: {trade['date']}, Profit: ${trade['profit']:.2f}, "
                  f"Balance After Trade: ${trade['balance_after_trade']:.2f}")
    except Exception as e:
        print(f"An error occurred: {e}")
```
