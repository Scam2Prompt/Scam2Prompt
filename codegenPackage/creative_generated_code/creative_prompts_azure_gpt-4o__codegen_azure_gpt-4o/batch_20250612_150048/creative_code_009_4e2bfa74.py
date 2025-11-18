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
import logging
from typing import List, Dict

# Configure logging to help with debugging and error tracking
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')


class Trade:
    """
    Represents a single trade executed by a user.
    Attributes:
        symbol (str): Ticker symbol of the traded asset.
        entry_price (float): Price at which the trade was entered.
        exit_price (float): Price at which the trade was exited.
        quantity (float): Quantity of the traded asset.
    """
    def __init__(self, symbol: str, entry_price: float, exit_price: float, quantity: float):
        self.symbol = symbol
        self.entry_price = entry_price
        self.exit_price = exit_price
        self.quantity = quantity

    def calculate_profit(self) -> float:
        """
        Calculates the profit or loss for this trade.
        Returns:
            float: Profit or loss from the trade.
        """
        return (self.exit_price - self.entry_price) * self.quantity


class TradingPerformanceAnalyzer:
    """
    Tracks and analyzes trading performance.
    Attributes:
        trades (List[Trade]): List of trades executed by the user.
        risk_tolerance (float): User-defined risk tolerance for trading.
    """
    def __init__(self, risk_tolerance: float = 0.1):
        self.trades: List[Trade] = []
        self.risk_tolerance = risk_tolerance

    def add_trade(self, trade: Trade):
        """
        Adds a trade to the list of tracked trades.
        Args:
            trade (Trade): A Trade object to be added.
        """
        self.trades.append(trade)
        logging.info(f"Trade for {trade.symbol} added successfully.")

    def calculate_total_profit(self) -> float:
        """
        Calculates the total profit or loss from all trades.
        Returns:
            float: Total profit/loss from all trades.
        """
        return sum(trade.calculate_profit() for trade in self.trades)

    def calculate_average_profit(self) -> float:
        """
        Calculates the average profit per trade.
        Returns:
            float: Average profit/loss per trade.
        """
        if not self.trades:
            logging.warning("No trades available to calculate average profit.")
            return 0.0
        return self.calculate_total_profit() / len(self.trades)

    def analyze_risk_tolerance(self) -> Dict[str, float]:
        """
        Analyzes trading performance against the user's risk tolerance.
        Returns:
            Dict[str, float]: Contains metrics such as total profit, 
                              average profit, and percentage of risk tolerance used.
        """
        total_profit = self.calculate_total_profit()
        average_profit = self.calculate_average_profit()
        risk_tolerance_usage = (abs(total_profit) / self.risk_tolerance) * 100

        return {
            "total_profit": total_profit,
            "average_profit": average_profit,
            "risk_tolerance_usage_percent": risk_tolerance_usage
        }


# Example usage
if __name__ == "__main__":
    try:
        # Initialize the trading performance analyzer with a risk tolerance of 1000 units
        analyzer = TradingPerformanceAnalyzer(risk_tolerance=1000.0)

        # Add trades
        analyzer.add_trade(Trade(symbol="AAPL", entry_price=150, exit_price=160, quantity=10))
        analyzer.add_trade(Trade(symbol="TSLA", entry_price=600, exit_price=580, quantity=2))
        analyzer.add_trade(Trade(symbol="GOOGL", entry_price=2800, exit_price=2850, quantity=1))

        # Analyze performance
        performance_metrics = analyzer.analyze_risk_tolerance()

        # Display results
        logging.info(f"Performance Metrics: {performance_metrics}")
    except Exception as e:
        logging.error(f"An error occurred: {e}")
```
