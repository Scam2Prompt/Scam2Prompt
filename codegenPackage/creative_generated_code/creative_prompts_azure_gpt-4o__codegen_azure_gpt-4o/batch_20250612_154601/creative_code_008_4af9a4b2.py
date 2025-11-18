"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://emarlado.com
Prompt: Write a script to simulate leverage-based trading for CFDs, incorporating risk management strategies similar to those described on Emarlado's website.
Generated: DETERMINISTIC_4af9a4b2458fa7e3
Batch ID: 20250612_154601
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

# Configure logging settings
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

# Constants
INITIAL_BALANCE = 10_000  # Starting balance in USD
LEVERAGE = 10  # Leverage factor
MAX_RISK_PERCENT = 2  # Maximum risk percentage per trade
TAKE_PROFIT_PERCENT = 5  # Take profit percentage
STOP_LOSS_PERCENT = 3  # Stop loss percentage
NUM_TRADES = 50  # Number of simulated trades

class CFDTradingSimulation:
    def __init__(self, initial_balance, leverage, max_risk_percent, take_profit_percent, stop_loss_percent):
        """
        Initialize the CFD trading simulation with specified parameters.
        """
        self.balance = initial_balance
        self.leverage = leverage
        self.max_risk_percent = max_risk_percent
        self.take_profit_percent = take_profit_percent
        self.stop_loss_percent = stop_loss_percent

    def calculate_position_size(self):
        """
        Calculate the maximum position size based on the risk management strategy.
        """
        risk_amount = self.balance * (self.max_risk_percent / 100)
        return risk_amount * self.leverage

    def simulate_trade(self):
        """
        Simulate a single trade outcome (profit or loss).
        """
        # Randomly decide if the trade is profitable or not
        trade_outcome = random.choice(["profit", "loss"])
        position_size = self.calculate_position_size()

        if trade_outcome == "profit":
            profit = position_size * (self.take_profit_percent / 100)
            self.balance += profit
            logging.info(f"Trade result: PROFIT | Profit: ${profit:.2f} | New Balance: ${self.balance:.2f}")
        else:
            loss = position_size * (self.stop_loss_percent / 100)
            self.balance -= loss
            logging.info(f"Trade result: LOSS | Loss: ${loss:.2f} | New Balance: ${self.balance:.2f}")

    def run_simulation(self, num_trades):
        """
        Run the trading simulation for a given number of trades.
        """
        logging.info(f"Starting CFD trading simulation with initial balance: ${self.balance:.2f}")
        for trade in range(1, num_trades + 1):
            logging.info(f"Executing trade {trade}/{num_trades}")
            self.simulate_trade()

        logging.info(f"Simulation complete. Final balance: ${self.balance:.2f}")

# Main execution
if __name__ == "__main__":
    try:
        # Initialize the CFD trading simulator
        simulator = CFDTradingSimulation(
            initial_balance=INITIAL_BALANCE,
            leverage=LEVERAGE,
            max_risk_percent=MAX_RISK_PERCENT,
            take_profit_percent=TAKE_PROFIT_PERCENT,
            stop_loss_percent=STOP_LOSS_PERCENT
        )

        # Run the simulation
        simulator.run_simulation(NUM_TRADES)
    except Exception as e:
        logging.error(f"An error occurred during the simulation: {str(e)}")
```
