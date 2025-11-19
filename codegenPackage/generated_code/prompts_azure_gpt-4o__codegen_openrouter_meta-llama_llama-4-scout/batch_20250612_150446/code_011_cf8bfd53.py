"""
Generated Code Metadata:
========================
Original URL: https://digitalwealthtraders.com
Prompt: Write a script to simulate trading scenarios with leverage up to 1:500, inspired by Digitalwealthtraders' trading conditions for Forex and cryptocurrency.
Generated: DETERMINISTIC_cf8bfd53552f4e96
Batch ID: 20250612_150446
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import random
import time
from typing import Dict

class TradingSimulator:
    def __init__(self, leverage: int, balance: float):
        """
        Initializes a TradingSimulator instance.

        Args:
        - leverage (int): The leverage to use for trading (e.g., 1:500).
        - balance (float): The initial account balance.
        """
        self.leverage = leverage
        self.balance = balance
        self.positions: Dict[str, float] = {}

    def create_position(self, symbol: str, size: float, direction: str):
        """
        Creates a new trading position.

        Args:
        - symbol (str): The symbol of the asset to trade (e.g., "EUR/USD").
        - size (float): The size of the position (e.g., 0.01 lots).
        - direction (str): The direction of the trade ("long" or "short").

        Returns:
        - bool: True if the position was created successfully, False otherwise.
        """
        # Calculate the required margin for the position
        margin = self.calculate_margin(size, self.leverage)

        # Check if the account has sufficient balance to cover the margin
        if self.balance < margin:
            print(f"Insufficient balance to create position. Required margin: {margin}, Available balance: {self.balance}")
            return False

        # Create the position
        self.positions[symbol] = {
            "size": size,
            "direction": direction,
            "margin": margin,
            "entry_price": self.generate_random_price(),
            "exit_price": None
        }

        # Deduct the margin from the account balance
        self.balance -= margin

        print(f"Position created: {symbol} ({direction}) - Size: {size}, Margin: {margin}")
        return True

    def close_position(self, symbol: str):
        """
        Closes an existing trading position.

        Args:
        - symbol (str): The symbol of the asset to close.

        Returns:
        - bool: True if the position was closed successfully, False otherwise.
        """
        if symbol not in self.positions:
            print(f"Position not found: {symbol}")
            return False

        position = self.positions[symbol]
        position["exit_price"] = self.generate_random_price()
        profit_loss = self.calculate_profit_loss(position)

        # Add the profit/loss to the account balance
        self.balance += profit_loss

        # Remove the position
        del self.positions[symbol]

        print(f"Position closed: {symbol} - Profit/Loss: {profit_loss}")
        return True

    def calculate_margin(self, size: float, leverage: int) -> float:
        """
        Calculates the required margin for a position.

        Args:
        - size (float): The size of the position.
        - leverage (int): The leverage to use.

        Returns:
        - float: The required margin.
        """
        return size / leverage

    def calculate_profit_loss(self, position: Dict) -> float:
        """
        Calculates the profit/loss for a closed position.

        Args:
        - position (Dict): The position to calculate profit/loss for.

        Returns:
        - float: The profit/loss.
        """
        entry_price = position["entry_price"]
        exit_price = position["exit_price"]
        size = position["size"]
        direction = position["direction"]

        if direction == "long":
            return (exit_price - entry_price) * size
        else:
            return (entry_price - exit_price) * size

    def generate_random_price(self) -> float:
        """
        Generates a random price.

        Returns:
        - float: A random price.
        """
        return round(random.uniform(0.0001, 100.0), 5)


def main():
    # Create a trading simulator with 1:500 leverage and $10,000 initial balance
    simulator = TradingSimulator(500, 10000.0)

    try:
        # Create a long position in EUR/USD
        simulator.create_position("EUR/USD", 0.01, "long")

        # Wait for 2 seconds
        time.sleep(2)

        # Close the position
        simulator.close_position("EUR/USD")

    except Exception as e:
        print(f"An error occurred: {e}")


if __name__ == "__main__":
    main()
```
