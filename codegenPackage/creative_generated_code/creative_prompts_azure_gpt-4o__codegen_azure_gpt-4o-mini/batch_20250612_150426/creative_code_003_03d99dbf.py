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
import random
import time
import threading
from datetime import datetime

class Trade:
    """Class representing a single trade."""
    def __init__(self, asset, amount, price):
        self.asset = asset  # Asset being traded (Forex or Bitcoin)
        self.amount = amount  # Amount of asset traded
        self.price = price  # Price at which the asset was traded
        self.timestamp = datetime.now()  # Timestamp of the trade

    def __str__(self):
        return f"[{self.timestamp}] {self.amount} {self.asset} @ {self.price}"

class TradingSimulator:
    """Class to simulate trading for Forex and Bitcoin."""
    def __init__(self):
        self.trades = []  # List to store trades
        self.running = True  # Flag to control the simulation loop
        self.profit = 0.0  # Total profit from trades

    def generate_trade(self):
        """Simulate a new trade by generating random data."""
        asset = random.choice(['Forex', 'Bitcoin'])  # Randomly choose asset type
        amount = round(random.uniform(0.01, 1.0), 2)  # Random trade amount
        price = round(random.uniform(1000, 50000), 2) if asset == 'Bitcoin' else round(random.uniform(0.5, 2.0), 2)  # Random price for asset

        # Create a Trade instance and append it to trades list
        trade = Trade(asset, amount, price)
        self.trades.append(trade)

        # Update profit (simple model: assume profit = amount * price, for demo purposes)
        self.update_profit(amount * price)

        # Print the trade
        print(trade)

    def update_profit(self, profit):
        """Update the total profit from trades."""
        self.profit += profit

    def start_trading(self):
        """Start the trading simulation."""
        print("Starting the trading simulation...")

        while self.running:
            try:
                self.generate_trade()  # Generate a new trade
                time.sleep(1)  # Simulate a delay between trades
            except Exception as e:
                print(f"Error during trading simulation: {e}")

    def stop_trading(self):
        """Stop the trading simulation."""
        self.running = False
        print("Trading simulation stopped.")
        print(f"Total profit: {self.profit}")

def main():
    """Main function to run the Trading Simulator."""
    simulator = TradingSimulator()

    # Start trading in a separate thread
    trading_thread = threading.Thread(target=simulator.start_trading)
    trading_thread.start()

    try:
        while True:
            user_input = input("Type 'stop' to end the simulation: ")
            if user_input.lower() == 'stop':
                simulator.stop_trading()
                break
    except KeyboardInterrupt:
        simulator.stop_trading()

if __name__ == "__main__":
    main()
```
