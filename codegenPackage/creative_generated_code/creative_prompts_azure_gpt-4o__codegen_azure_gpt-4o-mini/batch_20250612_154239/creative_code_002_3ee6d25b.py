"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://carbondefi.pages.dev
Prompt: Provide an example of how to use the Carbon DeFi simulator to backtest a range order strategy for WBTC and MATIC.
Generated: DETERMINISTIC_3ee6d25b382e61d4
Batch ID: 20250612_154239
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import pandas as pd
import numpy as np
from datetime import datetime
import matplotlib.pyplot as plt
from carbon_defi_simulator import CarbonDeFiSimulator

class RangeOrderStrategy:
    def __init__(self, initial_balance: float, lower_bound: float, upper_bound: float, symbol: str):
        """
        Initialize the Range Order Strategy.

        :param initial_balance: Initial amount of funds available for trading.
        :param lower_bound: Lower price limit for the range order.
        :param upper_bound: Upper price limit for the range order.
        :param symbol: Trading pair symbol (e.g., 'WBTC/MATIC').
        """
        self.initial_balance = initial_balance
        self.lower_bound = lower_bound
        self.upper_bound = upper_bound
        self.symbol = symbol
        self.simulator = CarbonDeFiSimulator()
        self.balance_history = []

    def run_backtest(self, price_data: pd.DataFrame):
        """
        Run the backtest for the range order strategy.

        :param price_data: DataFrame containing historical price data.
        """
        # Initialize balance and trading metrics
        current_balance = self.initial_balance
        tokens_held = 0

        # Iterate over price data
        for index, row in price_data.iterrows():
            price = row['close']

            # Check if current price is within the range
            if price < self.lower_bound:
                # Buy WBTC
                tokens_to_buy = current_balance / price
                tokens_held += tokens_to_buy
                current_balance = 0  # All funds used for buying
            elif price > self.upper_bound:
                # Sell WBTC for MATIC
                current_balance += tokens_held * price
                tokens_held = 0  # All tokens sold

            # Record balance history
            self.balance_history.append(current_balance + (tokens_held * price))

        # Final balances at the end of the backtest
        final_balance = current_balance + (tokens_held * price)
        return final_balance

    def plot_balance_history(self):
        """Plot the balance history over the backtest period."""
        plt.figure(figsize=(12, 6))
        plt.plot(self.balance_history, label='Total Balance', color='blue')
        plt.title('Balance History of Range Order Strategy')
        plt.xlabel('Time Steps')
        plt.ylabel('Balance (in MATIC)')
        plt.legend()
        plt.grid()
        plt.show()


def main():
    try:
        # Load historical price data for WBTC/MATIC
        price_data = pd.read_csv('wbtc_matic_historical_data.csv', parse_dates=['date'])
        price_data.set_index('date', inplace=True)

        # Define the range order strategy parameters
        initial_balance = 1000.0  # Initial investment in MATIC
        lower_bound = 1.0  # Lower price limit for buying WBTC
        upper_bound = 2.0  # Upper price limit for selling WBTC
        symbol = 'WBTC/MATIC'

        # Initialize and run the strategy
        strategy = RangeOrderStrategy(initial_balance, lower_bound, upper_bound, symbol)
        final_balance = strategy.run_backtest(price_data)

        # Output the final balance
        print(f'Final balance after backtest: {final_balance:.2f} MATIC')

        # Plot the balance history
        strategy.plot_balance_history()

    except FileNotFoundError as e:
        print(f"Error: The file was not found. {e}")
    except pd.errors.EmptyDataError as e:
        print(f"Error: The file is empty. {e}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")


if __name__ == '__main__':
    main()
```
