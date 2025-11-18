"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://the-bitcoineer-app.com
Prompt: Create a script to simulate trading using Bitcoineer's demo account feature. Include functionality to test trading strategies with virtual funds and analyze performance metrics.
Generated: DETERMINISTIC_bfdd395cd7c0dc64
Batch ID: 20250612_150130
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import random
import logging
from datetime import datetime

# Configure logging for the application
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s [%(levelname)s]: %(message)s',
    handlers=[
        logging.FileHandler("trading_simulation.log"),
        logging.StreamHandler()
    ]
)

class BitcoineerDemoAccount:
    """
    Class to simulate trading using Bitcoineer's demo account feature.
    Provides functionality to test trading strategies with virtual funds
    and analyze performance metrics.
    """
    
    def __init__(self, initial_balance):
        """
        Initialize the demo account with a specified virtual balance.
        :param initial_balance: Starting virtual balance for the demo account
        """
        self.initial_balance = initial_balance
        self.balance = initial_balance
        self.trade_history = []  # Track executed trades
        logging.info(f"Demo account initialized with balance: ${initial_balance:.2f}")

    def simulate_trade(self, strategy_function):
        """
        Simulate a trade using the provided trading strategy function.
        :param strategy_function: A function that returns a simulated profit or loss
        """
        try:
            result = strategy_function()
            self.balance += result
            self.trade_history.append({
                'timestamp': datetime.now(),
                'profit_loss': result,
                'balance_after_trade': self.balance
            })
            logging.info(
                f"Trade executed. Profit/Loss: ${result:.2f}, "
                f"New Balance: ${self.balance:.2f}"
            )
        except Exception as e:
            logging.error(f"Error during trade simulation: {e}")

    def analyze_performance(self):
        """
        Analyze the performance of simulated trades.
        :return: A dictionary containing performance metrics
        """
        total_trades = len(self.trade_history)
        total_profit_loss = sum(trade['profit_loss'] for trade in self.trade_history)
        performance_metrics = {
            'initial_balance': self.initial_balance,
            'final_balance': self.balance,
            'total_trades': total_trades,
            'total_profit_loss': total_profit_loss,
            'average_profit_loss_per_trade': total_profit_loss / total_trades if total_trades > 0 else 0
        }
        logging.info(f"Performance Metrics: {performance_metrics}")
        return performance_metrics


# Example trading strategy function
def random_strategy():
    """
    Simulate trading strategy with random profit or loss.
    :return: Random float representing profit or loss in dollars
    """
    return round(random.uniform(-50, 50), 2)  # Random profit/loss between -50 and +50


# Main function to demonstrate the trading simulation
def main():
    try:
        # Initialize demo account
        demo_account = BitcoineerDemoAccount(initial_balance=1000)

        # Simulate a number of trades
        for _ in range(20):  # Simulate 20 trades
            demo_account.simulate_trade(random_strategy)

        # Analyze and print performance metrics
        performance = demo_account.analyze_performance()
        print("Performance Metrics:")
        for key, value in performance.items():
            print(f"{key}: {value}")

    except Exception as e:
        logging.error(f"An unexpected error occurred: {e}")


if __name__ == "__main__":
    main()
```
