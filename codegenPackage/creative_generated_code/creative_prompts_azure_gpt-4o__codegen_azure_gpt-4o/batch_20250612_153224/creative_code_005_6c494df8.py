"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://learnatcheap.com
Prompt: Write a program to simulate small account futures trading strategies inspired by the Simpler Trading – Small Account Futures course on LearningAtCheap.com.
Generated: DETERMINISTIC_6c494df8634dbdfc
Batch ID: 20250612_153224
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

# Set up logging for application
logging.basicConfig(
    filename="trading_simulation.log",
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)

class FuturesTradingSimulator:
    """
    A simulator for futures trading strategies for small accounts.
    Inspired by Simpler Trading principles.
    """
    def __init__(self, initial_balance, risk_per_trade, reward_to_risk_ratio):
        """
        Initialize the simulator with basic parameters.
        :param initial_balance: (float) Starting account balance.
        :param risk_per_trade: (float) Dollar amount risked per trade.
        :param reward_to_risk_ratio: (float) Reward-to-risk ratio for trades.
        """
        self.balance = initial_balance
        self.risk_per_trade = risk_per_trade
        self.reward_to_risk_ratio = reward_to_risk_ratio
        self.trade_history = []

    def simulate_trade(self):
        """
        Simulate a single trade based on the risk and reward-to-risk ratio.
        Uses random win/loss outcome to determine trade result.
        """
        try:
            # Randomly decide if the trade is a win or loss (50/50)
            trade_won = random.choice([True, False])
            if trade_won:
                # Calculate profit based on reward-to-risk ratio
                profit = self.risk_per_trade * self.reward_to_risk_ratio
                self.balance += profit
                self.trade_history.append({"outcome": "win", "profit": profit})
                logging.info(f"Trade won. Profit: ${profit:.2f}. New balance: ${self.balance:.2f}.")
            else:
                # Deduct loss from the balance
                self.balance -= self.risk_per_trade
                self.trade_history.append({"outcome": "loss", "loss": self.risk_per_trade})
                logging.info(f"Trade lost. Loss: ${self.risk_per_trade:.2f}. New balance: ${self.balance:.2f}.")
        except Exception as e:
            logging.error(f"Error during trade simulation: {str(e)}")
            raise

    def run_simulation(self, num_trades):
        """
        Run the trading simulation for a given number of trades.
        :param num_trades: (int) Number of trades to simulate.
        """
        try:
            for _ in range(num_trades):
                self.simulate_trade()
        except Exception as e:
            logging.error(f"Error during simulation run: {str(e)}")
            raise

    def get_summary(self):
        """
        Generate a summary of the simulation results.
        :return: (dict) Summary including final balance and trade history.
        """
        wins = sum(1 for trade in self.trade_history if trade["outcome"] == "win")
        losses = sum(1 for trade in self.trade_history if trade["outcome"] == "loss")
        summary = {
            "starting_balance": self.balance,
            "final_balance": self.balance,
            "wins": wins,
            "losses": losses,
            "trade_history": self.trade_history
        }
        return summary


# Main program execution
if __name__ == "__main__":
    try:
        # Set parameters for the simulation
        initial_balance = 1000.00  # Starting with $1000
        risk_per_trade = 50.00  # Risking $50 per trade
        reward_to_risk_ratio = 2.0  # 2:1 reward-to-risk ratio
        num_trades = 20  # Simulating 20 trades

        # Create simulator instance
        simulator = FuturesTradingSimulator(initial_balance, risk_per_trade, reward_to_risk_ratio)

        # Run the simulation
        simulator.run_simulation(num_trades)

        # Get and print simulation summary
        summary = simulator.get_summary()
        print("Simulation Summary:")
        print(f"Starting Balance: ${summary['starting_balance']:.2f}")
        print(f"Final Balance: ${summary['final_balance']:.2f}")
        print(f"Total Wins: {summary['wins']}")
        print(f"Total Losses: {summary['losses']}")
    except Exception as e:
        logging.error(f"Fatal error in trading simulation: {str(e)}")
        print("An error occurred during the simulation.")
```
