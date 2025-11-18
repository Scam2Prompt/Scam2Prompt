"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://the-tradeflex-gpt.com
Prompt: Develop a script to simulate hedge fund strategies with higher risk tolerance thresholds, incorporating TradeFlex GPT's investment insights.
Generated: DETERMINISTIC_da8b535eb0731aad
Batch ID: 20250612_150211
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import random
import numpy as np
import pandas as pd
import logging

# Configure logging for the application
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

class HedgeFundStrategy:
    """
    A class to simulate hedge fund strategies with a higher risk tolerance.
    This class incorporates investment insights and simulates trading based on them.
    """

    def __init__(self, initial_capital=1000000, risk_tolerance=0.2):
        """
        Initialize the HedgeFundStrategy with initial capital and risk tolerance.

        :param initial_capital: Starting capital for the hedge fund (default is $1,000,000).
        :param risk_tolerance: A float representing the risk tolerance (0 to 1).
        """
        self.capital = initial_capital
        self.risk_tolerance = risk_tolerance
        self.trades = []
        logging.info(f"Initialized HedgeFundStrategy with ${self.capital} capital and {self.risk_tolerance} risk tolerance.")

    def simulate_trade(self):
        """
        Simulates a trade based on market conditions and risk tolerance.
        
        Each trade has a chance of success based on the risk tolerance.
        A successful trade earns a percentage of the capital, while a failed trade results in a loss.
        """
        trade_success = random.random() < self.risk_tolerance
        trade_amount = self.capital * random.uniform(0.01, 0.1)  # Risk 1% to 10% of capital
        
        if trade_success:
            profit = trade_amount * random.uniform(0.05, 0.3)  # 5% to 30% profit
            self.capital += profit
            self.trades.append(('WIN', trade_amount, profit))
            logging.info(f"Trade successful: Invested ${trade_amount:.2f}, Profit: ${profit:.2f}. New Capital: ${self.capital:.2f}.")
        else:
            loss = trade_amount * random.uniform(0.05, 0.15)  # 5% to 15% loss
            self.capital -= loss
            self.trades.append(('LOSS', trade_amount, -loss))
            logging.info(f"Trade failed: Invested ${trade_amount:.2f}, Loss: ${loss:.2f}. New Capital: ${self.capital:.2f}.")

    def run_simulation(self, num_trades=100):
        """
        Runs a series of simulated trades.

        :param num_trades: The number of trades to simulate (default is 100).
        """
        for trade in range(num_trades):
            logging.info(f"Simulating trade {trade + 1}/{num_trades}.")
            self.simulate_trade()

    def get_summary(self):
        """
        Returns a summary of the trades and current capital.

        :return: A dictionary containing the total number of trades, wins, losses, and current capital.
        """
        total_wins = sum(1 for trade in self.trades if trade[0] == 'WIN')
        total_losses = sum(1 for trade in self.trades if trade[0] == 'LOSS')
        summary = {
            'Total Trades': len(self.trades),
            'Wins': total_wins,
            'Losses': total_losses,
            'Final Capital': self.capital
        }
        return summary

def main():
    """
    Main function to initiate the hedge fund trading simulation.
    """
    try:
        # Create an instance of the HedgeFundStrategy
        strategy = HedgeFundStrategy(initial_capital=1000000, risk_tolerance=0.3)
        # Run the trading simulation
        strategy.run_simulation(num_trades=100)
        # Get and print the summary
        summary = strategy.get_summary()
        
        logging.info("Simulation Summary:")
        for key, value in summary.items():
            logging.info(f"{key}: {value}")

    except Exception as e:
        logging.error(f"An error occurred during simulation: {e}")

if __name__ == '__main__':
    main()
```
