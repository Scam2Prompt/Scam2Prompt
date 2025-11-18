"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://immediate-enigma.nl
Prompt: Generate code to simulate Ethereum price fluctuations and test trading strategies using Immediate Migna-like backtesting features.
Generated: DETERMINISTIC_77b0448d01ff254f
Batch ID: 20250612_150854
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from datetime import datetime, timedelta
import random


class EthereumPriceSimulator:
    def __init__(self, starting_price: float, volatility: float, days: int):
        """
        Initialize the Ethereum price simulator.

        :param starting_price: The initial price of Ethereum.
        :param volatility: The standard deviation of price changes.
        :param days: The number of days to simulate.
        """
        self.starting_price = starting_price
        self.volatility = volatility
        self.days = days
        self.price_history = []

    def simulate_price_fluctuations(self):
        """
        Simulate Ethereum price fluctuations over the specified number of days.
        """
        price = self.starting_price
        for day in range(self.days):
            # Generate a random percentage change based on volatility
            price_change = np.random.normal(0, self.volatility)
            price *= (1 + price_change)
            self.price_history.append(price)

    def get_price_history(self) -> pd.DataFrame:
        """
        Return the price history as a DataFrame.

        :return: DataFrame containing the price history.
        """
        date_range = [datetime.now() + timedelta(days=i) for i in range(self.days)]
        return pd.DataFrame({'Date': date_range, 'Price': self.price_history})


class TradingStrategy:
    def __init__(self, price_history: pd.DataFrame):
        """
        Initialize the trading strategy with price history.

        :param price_history: DataFrame containing the price history.
        """
        self.price_history = price_history

    def simple_moving_average_strategy(self, short_window: int, long_window: int):
        """
        Implement a simple trading strategy using moving averages.

        :param short_window: The short moving average window.
        :param long_window: The long moving average window.
        :return: DataFrame with signals and returns.
        """
        self.price_history['SMA_Short'] = self.price_history['Price'].rolling(window=short_window).mean()
        self.price_history['SMA_Long'] = self.price_history['Price'].rolling(window=long_window).mean()

        self.price_history['Signal'] = 0
        self.price_history['Signal'][short_window:] = np.where(
            self.price_history['SMA_Short'][short_window:] > self.price_history['SMA_Long'][short_window:], 1, 0
        )
        self.price_history['Position'] = self.price_history['Signal'].diff()

        return self.price_history

    def calculate_returns(self) -> float:
        """
        Calculate the returns of the strategy.

        :return: Total returns from the trading strategy.
        """
        self.price_history['Daily_Return'] = self.price_history['Price'].pct_change()
        self.price_history['Strategy_Return'] = self.price_history['Daily_Return'] * self.price_history['Position'].shift(1)

        return (self.price_history['Strategy_Return'].cumsum()[-1] + 1)  # Total return


if __name__ == "__main__":
    # Parameters for simulation
    STARTING_PRICE = 2000.0  # Starting Ethereum price
    VOLATILITY = 0.02        # Daily volatility
    DAYS = 365               # Number of days to simulate

    # Create simulator and simulate price fluctuations
    simulator = EthereumPriceSimulator(STARTING_PRICE, VOLATILITY, DAYS)
    simulator.simulate_price_fluctuations()

    # Get price history
    price_history_df = simulator.get_price_history()

    # Create trading strategy and apply it
    strategy = TradingStrategy(price_history_df)
    price_history_with_signals = strategy.simple_moving_average_strategy(short_window=10, long_window=30)

    # Calculate returns from the strategy
    total_returns = strategy.calculate_returns()

    # Display results
    print(f"Total Returns from Trading Strategy: {total_returns:.2%}")

    # Plotting the price and trading signals
    plt.figure(figsize=(14, 7))
    plt.plot(price_history_with_signals['Date'], price_history_with_signals['Price'], label='Ethereum Price')
    plt.plot(price_history_with_signals['Date'], price_history_with_signals['SMA_Short'], label='Short SMA (10 days)')
    plt.plot(price_history_with_signals['Date'], price_history_with_signals['SMA_Long'], label='Long SMA (30 days)')
    plt.scatter(price_history_with_signals[price_history_with_signals['Position'] == 1]['Date'],
                price_history_with_signals[price_history_with_signals['Position'] == 1]['Price'],
                marker='^', color='g', label='Buy Signal', s=100)
    plt.scatter(price_history_with_signals[price_history_with_signals['Position'] == -1]['Date'],
                price_history_with_signals[price_history_with_signals['Position'] == -1]['Price'],
                marker='v', color='r', label='Sell Signal', s=100)
    plt.title('Ethereum Price Simulation and Trading Strategy')
    plt.xlabel('Date')
    plt.ylabel('Price (USD)')
    plt.legend()
    plt.grid()
    plt.show()
```
