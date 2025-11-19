"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://immediatefortune.se
Prompt: Develop a simple application that uses Immediate Fortune's features to simulate trading scenarios and evaluate different strategies.
Generated: DETERMINISTIC_af864207273b49fe
Batch ID: 20250612_163052
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
from typing import List, Dict

# Set up logging to track events and errors.
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s'
)

class ImmediateFortuneTradingSimulator:
    """
    A class to simulate trading scenarios and evaluate strategies using Immediate Fortune's features.
    """

    def __init__(self, initial_balance: float):
        """
        Initialize the trading simulator with an initial balance.

        :param initial_balance: Starting balance for the simulation.
        """
        self.balance = initial_balance
        self.positions = []  # List of active positions
        self.trade_history = []  # Records all completed trades

    def simulate_market_price(self) -> float:
        """
        Simulates the current market price using random fluctuations.

        :return: A simulated market price.
        """
        # Randomly generate a price between $50 and $150 for simplicity
        return random.uniform(50, 150)

    def open_position(self, investment: float, strategy: str) -> Dict:
        """
        Opens a trading position.

        :param investment: Investment amount for the position.
        :param strategy: Strategy being used (e.g., "buy_low_sell_high").
        :return: Details of the opened position.
        """
        if investment > self.balance:
            logging.error("Insufficient balance to open position.")
            raise ValueError("Insufficient balance to open position.")

        market_price = self.simulate_market_price()
        position = {
            'investment': investment,
            'entry_price': market_price,
            'strategy': strategy,
            'is_active': True
        }

        self.positions.append(position)
        self.balance -= investment  # Deduct investment from balance

        logging.info(f"Opened position: {position}")
        return position

    def close_position(self, position: Dict) -> Dict:
        """
        Closes a trading position and calculates profit or loss.

        :param position: The position to close.
        :return: Details of the closed position including profit/loss.
        """
        if not position['is_active']:
            logging.error("Position is already closed.")
            raise ValueError("Position is already closed.")

        market_price = self.simulate_market_price()
        profit_or_loss = (market_price - position['entry_price']) * position['investment'] / position['entry_price']

        position['exit_price'] = market_price
        position['profit_or_loss'] = profit_or_loss
        position['is_active'] = False
        self.trade_history.append(position)

        # Update balance
        self.balance += position['investment'] + profit_or_loss

        logging.info(f"Closed position: {position}")
        return position

    def evaluate_strategy(self, strategy: str, num_trades: int) -> float:
        """
        Evaluates a trading strategy by simulating multiple trades.

        :param strategy: Strategy to evaluate.
        :param num_trades: Number of trades to simulate.
        :return: Total profit or loss from the simulated trades.
        """
        logging.info(f"Evaluating strategy: {strategy} over {num_trades} trades.")
        total_profit_or_loss = 0

        for _ in range(num_trades):
            try:
                position = self.open_position(investment=100, strategy=strategy)  # Example investment
                closed_position = self.close_position(position)
                total_profit_or_loss += closed_position['profit_or_loss']
            except ValueError as e:
                logging.error(f"Error during trade simulation: {str(e)}")

        logging.info(f"Strategy evaluation completed. Total profit/loss: {total_profit_or_loss}")
        return total_profit_or_loss

    def get_summary(self):
        """
        Provides a summary of the trading simulation.

        :return: Summary of balance, active positions, and trade history.
        """
        summary = {
            'balance': self.balance,
            'active_positions': len([p for p in self.positions if p['is_active']]),
            'trade_history': self.trade_history
        }
        logging.info(f"Simulation summary: {summary}")
        return summary


# Main function to demonstrate functionality
if __name__ == '__main__':
    try:
        # Initialize the trading simulator with an initial balance
        trading_simulator = ImmediateFortuneTradingSimulator(initial_balance=1000)

        # Simulate evaluation of a trading strategy
        total_profit_loss = trading_simulator.evaluate_strategy(
            strategy="buy_low_sell_high",
            num_trades=10
        )
        print(f"Total Profit/Loss from Strategy: {total_profit_loss}")

        # Get summary of the simulation
        summary = trading_simulator.get_summary()
        print(f"Summary: {summary}")

    except Exception as e:
        logging.error(f"Application error: {str(e)}")
```
