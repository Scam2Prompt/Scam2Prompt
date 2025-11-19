"""
Generated Code Metadata:
========================
Original URL: https://immediate-sprix-1.com
Prompt: Generate code to simulate trades using Immediate Sprix 1.8's demo account feature, ensuring risk-free evaluation of its automated trading signals.
Generated: DETERMINISTIC_d3a63bc5703325e3
Batch ID: 20250612_150843
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import time
import random

class TradeSimulator:
    """
    A class to simulate trades using Immediate Sprix 1.8's demo account feature.
    This class generates random trading signals and simulates executing trades.
    """

    def __init__(self, initial_balance=10000):
        """
        Initializes the TradeSimulator with a given initial balance.

        :param initial_balance: The starting balance for the demo account.
        """
        self.balance = initial_balance
        self.trades = []
        self.active = True

    def generate_signal(self):
        """
        Generates a random trading signal.

        :return: A dictionary containing the signal type ('buy' or 'sell') and the amount.
        """
        signal_type = random.choice(['buy', 'sell'])
        amount = random.uniform(1, 1000)  # Random amount between 1 and 1000
        return {'type': signal_type, 'amount': amount}

    def execute_trade(self, signal):
        """
        Executes a trade based on the provided signal.

        :param signal: A dictionary containing the trade signal.
        :raises ValueError: If the trade amount exceeds the available balance.
        """
        if signal['amount'] > self.balance:
            raise ValueError("Insufficient balance to execute trade.")

        # Simulate trade execution
        if signal['type'] == 'buy':
            self.balance -= signal['amount']
            trade_result = f"Bought for {signal['amount']}. New balance: {self.balance}"
        else:  # signal['type'] == 'sell'
            self.balance += signal['amount']
            trade_result = f"Sold for {signal['amount']}. New balance: {self.balance}"

        self.trades.append(trade_result)
        return trade_result

    def run_simulation(self, duration=60):
        """
        Runs the trade simulation for a specified duration.

        :param duration: The duration of the simulation in seconds.
        """
        start_time = time.time()
        while self.active and (time.time() - start_time < duration):
            try:
                signal = self.generate_signal()
                result = self.execute_trade(signal)
                print(result)
                time.sleep(1)  # Simulate time delay between trades
            except ValueError as e:
                print(f"Error: {e}")

    def stop_simulation(self):
        """
        Stops the trade simulation.
        """
        self.active = False
        print("Simulation stopped.")

if __name__ == "__main__":
    # Create a TradeSimulator instance
    simulator = TradeSimulator()

    try:
        # Run the simulation for 60 seconds
        simulator.run_simulation(duration=60)
    except KeyboardInterrupt:
        # Allow graceful exit on user interrupt
        simulator.stop_simulation()
```
