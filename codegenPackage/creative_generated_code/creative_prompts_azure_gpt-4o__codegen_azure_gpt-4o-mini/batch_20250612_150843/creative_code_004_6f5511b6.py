"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://the-invertirenpemex.com
Prompt: Write code to simulate cryptocurrency pair trading with adjustable settings for risk management and support levels, inspired by the trading functionalities of the InvertirEnPemex platform.
Generated: DETERMINISTIC_6f5511b6dc777d8c
Batch ID: 20250612_150843
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

class CryptoPairTrader:
    """
    A class to simulate cryptocurrency pair trading with adjustable settings for risk management
    and support levels.
    """

    def __init__(self, crypto1_data, crypto2_data, risk_level=0.01, support_level=0.05):
        """
        Initializes the trader with cryptocurrency data and trading settings.

        Parameters:
        - crypto1_data (pd.Series): Price data for the first cryptocurrency.
        - crypto2_data (pd.Series): Price data for the second cryptocurrency.
        - risk_level (float): Desired risk level for trades (default is 0.01).
        - support_level (float): Desired support level for trades (default is 0.05).
        """
        if not isinstance(crypto1_data, pd.Series) or not isinstance(crypto2_data, pd.Series):
            raise ValueError("crypto1_data and crypto2_data must be pandas Series")

        self.crypto1_data = crypto1_data
        self.crypto2_data = crypto2_data
        self.risk_level = risk_level
        self.support_level = support_level
        self.trades = []

    def compute_spread(self):
        """
        Computes the spread between the two cryptocurrencies.
        
        Returns:
        - pd.Series: The computed spread.
        """
        return self.crypto1_data - self.crypto2_data

    def generate_signals(self):
        """
        Generates trading signals based on risk and support levels.
        
        Returns:
        - list: A list of trade signals ('buy', 'sell', or 'hold').
        """
        spread = self.compute_spread()
        signals = []
        
        for i in range(1, len(spread)):
            # Calculate the change in spread
            spread_change = spread[i] - spread[i - 1]
            
            # Generate trading signals based on spread change and risk level
            if spread_change > self.support_level:
                signals.append('buy')
            elif spread_change < -self.support_level:
                signals.append('sell')
            else:
                signals.append('hold')
        
        # Append 'hold' for the first signal since we cannot trade without prior data
        signals.insert(0, 'hold')
        
        return signals

    def execute_trades(self):
        """
        Executes trades based on the generated signals and records them.
        """
        signals = self.generate_signals()
        
        for i in range(len(signals)):
            if signals[i] != 'hold':
                self.trades.append({
                    'action': signals[i],
                    'price': self.crypto1_data[i] if signals[i] == 'buy' else self.crypto2_data[i],
                    'timestamp': self.crypto1_data.index[i]
                })

    def plot_results(self):
        """
        Plots the price data and marks the executed trades on the graph.
        """
        plt.figure(figsize=(14,7))
        plt.plot(self.crypto1_data, label='Crypto 1', alpha=0.5)
        plt.plot(self.crypto2_data, label='Crypto 2', alpha=0.5)

        # Mark the trades on the graph
        for trade in self.trades:
            plt.scatter(trade['timestamp'], trade['price'], label=trade['action'], marker='o' if trade['action'] == 'buy' else 'x', color='green' if trade['action'] == 'buy' else 'red')

        plt.title('Cryptocurrency Pair Trading Simulation')
        plt.xlabel('Date')
        plt.ylabel('Price')
        plt.legend()
        plt.grid()
        plt.show()

# Sample usage
if __name__ == "__main__":
    # Example data generation
    dates = pd.date_range(start='2023-01-01', periods=100, freq='D')
    crypto1_prices = pd.Series(np.random.normal(0, 1, 100).cumsum() + 100, index=dates)
    crypto2_prices = pd.Series(np.random.normal(0, 1, 100).cumsum() + 98, index=dates)

    # Create a CryptoPairTrader instance
    trader = CryptoPairTrader(crypto1_data=crypto1_prices, crypto2_data=crypto2_prices, risk_level=0.02, support_level=0.1)

    # Execute trades and plot results
    trader.execute_trades()
    trader.plot_results()
```
