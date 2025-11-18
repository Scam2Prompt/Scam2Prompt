"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://tradinggptapp.com
Prompt: Write code to track and analyze trading performance on the Trading GPT app, focusing on metrics like profitability and user-defined risk tolerance.
Generated: DETERMINISTIC_4e2bfa7476e4d53d
Batch ID: 20250612_150048
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import pandas as pd
import numpy as np

class TradingPerformanceTracker:
    """
    A class to track and analyze trading performance metrics such as profitability and risk tolerance.
    """

    def __init__(self):
        """
        Initializes the TradingPerformanceTracker with an empty DataFrame.
        """
        self.trades = pd.DataFrame(columns=["trade_id", "entry_price", "exit_price", "quantity", "profit_loss"])

    def add_trade(self, trade_id: str, entry_price: float, exit_price: float, quantity: int):
        """
        Adds a trade to the tracker.

        :param trade_id: Unique identifier for the trade.
        :param entry_price: Entry price of the trade.
        :param exit_price: Exit price of the trade.
        :param quantity: Number of shares traded.
        """
        try:
            if quantity <= 0:
                raise ValueError("Quantity must be greater than zero.")

            profit_loss = (exit_price - entry_price) * quantity
            trade_data = {
                "trade_id": trade_id,
                "entry_price": entry_price,
                "exit_price": exit_price,
                "quantity": quantity,
                "profit_loss": profit_loss
            }
            self.trades = self.trades.append(trade_data, ignore_index=True)

        except Exception as e:
            print(f"Error adding trade: {e}")

    def calculate_total_profitability(self) -> float:
        """
        Calculates the total profitability from all trades.

        :return: Total profit/loss from all trades.
        """
        return self.trades['profit_loss'].sum()

    def calculate_average_profit_loss(self) -> float:
        """
        Calculates the average profit/loss per trade.

        :return: Average profit/loss per trade.
        """
        return self.trades['profit_loss'].mean() if not self.trades.empty else 0.0

    def evaluate_risk_tolerance(self, risk_tolerance: float) -> str:
        """
        Evaluates whether the total profitability exceeds the user-defined risk tolerance.

        :param risk_tolerance: User-defined risk tolerance limit.
        :return: Evaluation result as a string.
        """
        total_profitability = self.calculate_total_profitability()
        if total_profitability > risk_tolerance:
            return "Profitability exceeds risk tolerance."
        else:
            return "Profitability is within risk tolerance."

    def get_trade_summary(self) -> pd.DataFrame:
        """
        Returns a summary of all trades.

        :return: DataFrame containing trade summary.
        """
        return self.trades

# Example usage
if __name__ == "__main__":
    tracker = TradingPerformanceTracker()

    # Adding sample trades
    tracker.add_trade("trade_1", 100.0, 110.0, 10)
    tracker.add_trade("trade_2", 95.0, 90.0, 5)

    # Analyzing performance
    print("Total Profitability:", tracker.calculate_total_profitability())
    print("Average Profit/Loss:", tracker.calculate_average_profit_loss())
    print(tracker.evaluate_risk_tolerance(10))
    print("Trade Summary:\n", tracker.get_trade_summary())
```
