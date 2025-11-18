"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://cropscoinspro.com
Prompt: Create a program that simulates live trading for forex and bitcoin, allowing users to view real-time trades and profit growth, as highlighted on the Cropscoinspro platform.
Generated: DETERMINISTIC_03d99dbf4e91619d
Batch ID: 20250612_150426
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import time
import random
from datetime import datetime

class LiveTradingSimulator:
    """
    A class to simulate live trading for forex and bitcoin.
    Users can view real-time trades and profit growth.
    """

    def __init__(self):
        # Initialize trading pairs and starting balance
        self.trading_pairs = ['EUR/USD', 'USD/JPY', 'BTC/USD']
        self.balance = 10000.0  # Initial starting balance in USD
        self.trade_history = []

    def simulate_trade(self):
        """
        Simulates a single trade with a random trading pair, profit/loss, and timestamp.
        """
        pair = random.choice(self.trading_pairs)
        profit_loss = round(random.uniform(-50, 100), 2)  # Random profit/loss per trade
        timestamp = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        
        # Update balance with profit/loss
        self.balance += profit_loss

        # Record the trade details
        trade = {
            'timestamp': timestamp,
            'pair': pair,
            'profit_loss': profit_loss,
            'balance': round(self.balance, 2)
        }
        self.trade_history.append(trade)

        # Return the trade for display purposes
        return trade

    def display_trade(self, trade):
        """
        Displays the details of a single trade.
        """
        print(f"[{trade['timestamp']}] Trading Pair: {trade['pair']}, "
              f"Profit/Loss: ${trade['profit_loss']}, "
              f"Balance: ${trade['balance']}")

    def run_simulation(self, duration=30, trade_interval=2):
        """
        Runs the live trading simulation for a specified duration.
        
        :param duration: How long to run the simulation (in seconds).
        :param trade_interval: Time interval between trades (in seconds).
        """
        print("Starting Live Trading Simulation...")
        start_time = time.time()
        try:
            while time.time() - start_time < duration:
                trade = self.simulate_trade()
                self.display_trade(trade)
                time.sleep(trade_interval)
        except KeyboardInterrupt:
            print("\nSimulation interrupted by user.")
        finally:
            print("\nLive Trading Simulation Ended.")
            print(f"Final Balance: ${round(self.balance, 2)}")
            print("Trade History:")
            for trade in self.trade_history:
                print(trade)


if __name__ == "__main__":
    # Create an instance of the simulator
    simulator = LiveTradingSimulator()

    # Run the simulator for 30 seconds with trades occurring every 2 seconds
    simulator.run_simulation(duration=30, trade_interval=2)
```
