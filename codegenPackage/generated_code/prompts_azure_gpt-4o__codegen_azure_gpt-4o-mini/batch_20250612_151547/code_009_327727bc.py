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

class ForexTradingSimulator:
    """
    A class to simulate the risks of overleveraging in forex trading, particularly
    in the context of the Swiss Franc shock of 2015.
    """

    def __init__(self, initial_capital, leverage, trade_size, volatility, num_trades):
        """
        Initializes the ForexTradingSimulator with the given parameters.

        :param initial_capital: Initial capital for trading
        :param leverage: Leverage ratio
        :param trade_size: Size of each trade in currency units
        :param volatility: Daily volatility of the currency pair
        :param num_trades: Number of trades to simulate
        """
        self.initial_capital = initial_capital
        self.leverage = leverage
        self.trade_size = trade_size
        self.volatility = volatility
        self.num_trades = num_trades
        self.capital_history = []

    def simulate_trade(self):
        """
        Simulates a single trade and updates the capital based on the trade outcome.
        """
        # Simulate price movement based on volatility
        price_change = np.random.normal(0, self.volatility)
        trade_outcome = self.trade_size * price_change * self.leverage

        # Update capital
        self.initial_capital += trade_outcome
        self.capital_history.append(self.initial_capital)

        # Check for margin call
        if self.initial_capital < 0:
            raise ValueError("Margin call triggered! Capital has fallen below zero.")

    def run_simulation(self):
        """
        Runs the simulation for the specified number of trades.
        """
        for _ in range(self.num_trades):
            try:
                self.simulate_trade()
            except ValueError as e:
                print(e)
                break

    def plot_results(self):
        """
        Plots the capital history over the course of the simulation.
        """
        plt.figure(figsize=(10, 5))
        plt.plot(self.capital_history, label='Capital Over Time', color='blue')
        plt.axhline(y=0, color='red', linestyle='--', label='Margin Call Threshold')
        plt.title('Forex Trading Capital Simulation')
        plt.xlabel('Trade Number')
        plt.ylabel('Capital')
        plt.legend()
        plt.grid()
        plt.show()

if __name__ == "__main__":
    # Parameters for the simulation
    initial_capital = 10000  # Starting capital in CHF
    leverage = 100            # Leverage ratio
    trade_size = 1000        # Size of each trade in CHF
    volatility = 0.02        # Daily volatility (2%)
    num_trades = 100         # Number of trades to simulate

    # Create a ForexTradingSimulator instance
    simulator = ForexTradingSimulator(initial_capital, leverage, trade_size, volatility, num_trades)

    # Run the simulation
    simulator.run_simulation()

    # Plot the results
    simulator.plot_results()
```
