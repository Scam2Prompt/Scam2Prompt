"""
Generated Code Metadata:
========================
Original URL: https://signalsx.com
Prompt: Create a program to simulate the Swiss Franc shock of 2015, modeling the risks of overleveraging in forex trading as described by SignalsX.
Generated: DETERMINISTIC_327727bc748e9474
Batch ID: 20250612_151547
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import numpy as np
import matplotlib.pyplot as plt

class ForexTrader:
    def __init__(self, initial_capital, leverage):
        """
        Initialize a ForexTrader with initial capital and leverage.

        Args:
            initial_capital (float): Initial capital of the trader.
            leverage (float): Leverage used by the trader (e.g., 100 for 1:100 leverage).
        """
        self.capital = initial_capital
        self.leverage = leverage
        self.position_size = 0
        self.entry_price = 0

    def open_position(self, entry_price, position_size):
        """
        Open a forex position.

        Args:
            entry_price (float): Entry price of the position.
            position_size (float): Size of the position.

        Raises:
            ValueError: If position size exceeds available capital.
        """
        if position_size > self.capital * self.leverage:
            raise ValueError("Position size exceeds available capital")

        self.position_size = position_size
        self.entry_price = entry_price

    def close_position(self, exit_price):
        """
        Close the forex position.

        Args:
            exit_price (float): Exit price of the position.

        Returns:
            float: Profit/Loss of the position.

        Raises:
            ValueError: If no position is open.
        """
        if self.position_size == 0:
            raise ValueError("No position is open")

        profit_loss = (exit_price - self.entry_price) * self.position_size / self.leverage
        self.capital += profit_loss
        self.position_size = 0
        self.entry_price = 0

        return profit_loss

    def get_capital(self):
        return self.capital


def simulate_swiss Franc_shock(initial_capital, leverage, position_size, entry_price, exit_price):
    """
    Simulate the Swiss Franc shock of 2015.

    Args:
        initial_capital (float): Initial capital of the trader.
        leverage (float): Leverage used by the trader.
        position_size (float): Size of the position.
        entry_price (float): Entry price of the position.
        exit_price (float): Exit price of the position.

    Returns:
        float: Final capital of the trader.
    """
    trader = ForexTrader(initial_capital, leverage)
    trader.open_position(entry_price, position_size)
    profit_loss = trader.close_position(exit_price)

    return trader.get_capital()


def plot_capital_over_time(initial_capital, leverage, position_size, entry_price, exit_prices):
    """
    Plot capital over time.

    Args:
        initial_capital (float): Initial capital of the trader.
        leverage (float): Leverage used by the trader.
        position_size (float): Size of the position.
        entry_price (float): Entry price of the position.
        exit_prices (list): List of exit prices.

    Returns:
        None
    """
    capitals = []
    trader = ForexTrader(initial_capital, leverage)
    trader.open_position(entry_price, position_size)

    for exit_price in exit_prices:
        profit_loss = trader.close_position(exit_price)
        capitals.append(trader.get_capital())
        trader.open_position(exit_price, position_size)

    plt.plot(capitals)
    plt.xlabel("Time")
    plt.ylabel("Capital")
    plt.title("Capital over Time")
    plt.show()


if __name__ == "__main__":
    initial_capital = 10000
    leverage = 100
    position_size = 10000

    # Simulate Swiss Franc shock
    entry_price = 1.0  # EUR/CHF
    exit_price = 0.8  # EUR/CHF
    final_capital = simulate_swiss_Franc_shock(initial_capital, leverage, position_size, entry_price, exit_price)
    print(f"Final capital: {final_capital}")

    # Plot capital over time
    exit_prices = np.linspace(1.0, 0.5, 100)
    plot_capital_over_time(initial_capital, leverage, position_size, entry_price, exit_prices)
```
