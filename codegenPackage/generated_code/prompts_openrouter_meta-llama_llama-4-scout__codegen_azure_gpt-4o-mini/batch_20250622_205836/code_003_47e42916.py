"""
Generated Code Metadata:
========================
Original URL: https://2xether.com
Prompt: Implement a simple trading simulator that uses historical data for ETHT and ETHD to evaluate the performance of a pair trading strategy with a 5% stop-loss, similar to the one described on the webpage.
Generated: DETERMINISTIC_47e42916bfbe9f95
Batch ID: 20250622_205836
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

class PairTradingSimulator:
    def __init__(self, eth_t_data, eth_d_data, stop_loss=0.05):
        """
        Initializes the PairTradingSimulator with historical data for ETHT and ETHD.

        :param eth_t_data: DataFrame containing historical price data for ETHT
        :param eth_d_data: DataFrame containing historical price data for ETHD
        :param stop_loss: Percentage for stop-loss (default is 5%)
        """
        self.eth_t_data = eth_t_data
        self.eth_d_data = eth_d_data
        self.stop_loss = stop_loss
        self.results = []

    def calculate_spread(self):
        """
        Calculates the spread between ETHT and ETHD prices.
        """
        self.eth_t_data['Spread'] = self.eth_t_data['Price'] - self.eth_d_data['Price']

    def simulate_trading(self):
        """
        Simulates the pair trading strategy based on the calculated spread.
        """
        self.calculate_spread()
        position = 0  # 1 for long ETHT, -1 for long ETHD
        entry_price = 0

        for index, row in self.eth_t_data.iterrows():
            spread = row['Spread']
            price_eth_t = row['Price']
            price_eth_d = self.eth_d_data.loc[index, 'Price']

            # Entry conditions
            if spread < -1:  # Buy ETHT, sell ETHD
                if position == 0:
                    position = 1
                    entry_price = price_eth_t
                    self.results.append((index, 'BUY ETHT', entry_price))

            elif spread > 1:  # Sell ETHT, buy ETHD
                if position == 0:
                    position = -1
                    entry_price = price_eth_t
                    self.results.append((index, 'SELL ETHT', entry_price))

            # Stop-loss conditions
            if position == 1 and (price_eth_t < entry_price * (1 - self.stop_loss)):
                self.results.append((index, 'SELL ETHT (Stop-Loss)', price_eth_t))
                position = 0

            elif position == -1 and (price_eth_t > entry_price * (1 + self.stop_loss)):
                self.results.append((index, 'BUY ETHT (Stop-Loss)', price_eth_t))
                position = 0

        # Close any open positions at the end of the data
        if position != 0:
            self.results.append((index, 'CLOSE POSITION', price_eth_t))

    def get_results(self):
        """
        Returns the results of the trading simulation.

        :return: List of results from the trading simulation
        """
        return self.results

    def plot_results(self):
        """
        Plots the results of the trading simulation.
        """
        dates = [result[0] for result in self.results]
        actions = [result[1] for result in self.results]
        prices = [result[2] for result in self.results]

        plt.figure(figsize=(12, 6))
        plt.plot(self.eth_t_data['Date'], self.eth_t_data['Price'], label='ETHT Price', color='blue')
        plt.plot(self.eth_d_data['Date'], self.eth_d_data['Price'], label='ETHD Price', color='orange')

        for i in range(len(dates)):
            plt.annotate(actions[i], (dates[i], prices[i]), textcoords="offset points", xytext=(0,10), ha='center')

        plt.title('Pair Trading Simulation Results')
        plt.xlabel('Date')
        plt.ylabel('Price')
        plt.legend()
        plt.show()

# Example usage
if __name__ == "__main__":
    try:
        # Load historical data for ETHT and ETHD
        eth_t_data = pd.read_csv('eth_t_data.csv', parse_dates=['Date'])
        eth_d_data = pd.read_csv('eth_d_data.csv', parse_dates=['Date'])

        # Ensure both datasets are aligned by date
        eth_t_data.set_index('Date', inplace=True)
        eth_d_data.set_index('Date', inplace=True)
        eth_t_data = eth_t_data.loc[eth_t_data.index.intersection(eth_d_data.index)]
        eth_d_data = eth_d_data.loc[eth_d_data.index.intersection(eth_t_data.index)]

        # Initialize and run the trading simulator
        simulator = PairTradingSimulator(eth_t_data, eth_d_data)
        simulator.simulate_trading()
        results = simulator.get_results()

        # Print results
        for result in results:
            print(result)

        # Plot the results
        simulator.plot_results()

    except FileNotFoundError as e:
        print(f"Error: {e}. Please ensure the CSV files are in the correct path.")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
```
