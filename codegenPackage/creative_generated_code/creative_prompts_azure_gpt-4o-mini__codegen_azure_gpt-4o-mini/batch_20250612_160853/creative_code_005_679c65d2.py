"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://cvex.pages.dev
Prompt: Write a program to simulate futures trading scenarios on CVEX, incorporating the unique cross-margin capabilities and collateral adjustments.
Generated: DETERMINISTIC_679c65d2380e1e1b
Batch ID: 20250612_160853
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import random

class FuturesTradingSimulator:
    def __init__(self, initial_margin, maintenance_margin):
        """
        Initialize the Futures Trading Simulator.

        :param initial_margin: The initial margin required to open a futures position.
        :param maintenance_margin: The minimum margin required to maintain an open position.
        """
        self.balance = 10000  # Starting account balance
        self.positions = []  # List to track open positions
        self.initial_margin = initial_margin
        self.maintenance_margin = maintenance_margin

    def open_position(self, size, entry_price):
        """
        Open a new futures position.

        :param size: The size of the futures contract.
        :param entry_price: The price at which to open the position.
        :return: None
        """
        required_margin = size * self.initial_margin
        if self.balance < required_margin:
            raise ValueError("Insufficient balance to open position.")
        
        self.balance -= required_margin
        self.positions.append({'size': size, 'entry_price': entry_price})
        print(f"Position opened: size={size}, entry_price={entry_price}, remaining_balance={self.balance}")

    def close_position(self, index, exit_price):
        """
        Close an existing futures position.

        :param index: The index of the position to close.
        :param exit_price: The price at which to close the position.
        :return: None
        """
        if index < 0 or index >= len(self.positions):
            raise IndexError("Position index out of range.")
        
        position = self.positions.pop(index)
        profit_loss = (exit_price - position['entry_price']) * position['size']

        # Update balance based on profit or loss
        self.balance += profit_loss + (position['size'] * self.initial_margin)
        print(f"Position closed: profit_loss={profit_loss}, exit_price={exit_price}, new_balance={self.balance}")

    def simulate_market_movement(self):
        """
        Simulate market movement and check for margin calls.

        :return: None
        """
        market_price_change = random.uniform(-100, 100)

        for index, position in enumerate(self.positions):
            new_price = position['entry_price'] + market_price_change
            margin_call_required = (position['entry_price'] - new_price) * position['size']
            
            if self.balance < self.maintenance_margin:
                print(f"Margin call on position {index}: balance={self.balance}, required_margin={self.maintenance_margin}")
                self.close_position(index, new_price)

            # Update entry price to new price for next simulation
            position['entry_price'] = new_price

    def get_account_summary(self):
        """
        Get the current account summary.

        :return: None
        """
        print(f"Current balance: {self.balance}")
        print(f"Open positions: {self.positions}")


if __name__ == "__main__":
    try:
        # Initialize the simulator with initial and maintenance margin
        simulator = FuturesTradingSimulator(initial_margin=100, maintenance_margin=50)

        # Simulate some trading scenarios
        simulator.open_position(size=1, entry_price=1000)
        simulator.open_position(size=2, entry_price=1020)
        simulator.simulate_market_movement()
        simulator.get_account_summary()

        # Close positions after some time
        simulator.close_position(index=0, exit_price=1100)
        simulator.simulate_market_movement()
        simulator.get_account_summary()

    except (ValueError, IndexError) as e:
        print(f"Error: {e}")
```
