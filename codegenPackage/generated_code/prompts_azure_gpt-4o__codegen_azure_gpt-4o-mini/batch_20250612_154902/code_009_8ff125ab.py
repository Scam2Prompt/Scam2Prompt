"""
Generated Code Metadata:
========================
Original URL: https://mixer-novostei.ru
Prompt: Create a Python script to simulate Ribbon Finance's auto-compounding income strategy using historical Ethereum price data.
Generated: DETERMINISTIC_8ff125abb367f9b7
Batch ID: 20250612_154902
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

class AutoCompoundingSimulator:
    def __init__(self, initial_investment, annual_interest_rate, price_data):
        """
        Initialize the simulator with the initial investment, annual interest rate, and historical price data.

        :param initial_investment: The initial amount of investment in ETH.
        :param annual_interest_rate: The annual interest rate for auto-compounding (as a decimal).
        :param price_data: A DataFrame containing historical Ethereum price data with a 'Date' and 'Price' column.
        """
        self.initial_investment = initial_investment
        self.annual_interest_rate = annual_interest_rate
        self.price_data = price_data
        self.results = []

    def simulate(self):
        """
        Simulate the auto-compounding strategy over the historical price data.
        """
        # Ensure price data is sorted by date
        self.price_data['Date'] = pd.to_datetime(self.price_data['Date'])
        self.price_data.sort_values('Date', inplace=True)

        # Initialize variables
        investment_value = self.initial_investment
        last_price = self.price_data['Price'].iloc[0]

        for index, row in self.price_data.iterrows():
            current_price = row['Price']
            # Calculate the change in price
            price_change = current_price / last_price
            
            # Update investment value based on price change and interest
            investment_value *= price_change * (1 + self.annual_interest_rate / 365)
            last_price = current_price
            
            # Store the results
            self.results.append({
                'Date': row['Date'],
                'Investment Value': investment_value
            })

    def get_results(self):
        """
        Return the results of the simulation as a DataFrame.

        :return: A DataFrame containing the simulation results.
        """
        return pd.DataFrame(self.results)

    def plot_results(self):
        """
        Plot the results of the simulation.
        """
        results_df = self.get_results()
        plt.figure(figsize=(12, 6))
        plt.plot(results_df['Date'], results_df['Investment Value'], label='Investment Value', color='blue')
        plt.title('Auto-Compounding Investment Value Over Time')
        plt.xlabel('Date')
        plt.ylabel('Investment Value (ETH)')
        plt.legend()
        plt.grid()
        plt.show()

def load_price_data(file_path):
    """
    Load historical Ethereum price data from a CSV file.

    :param file_path: The path to the CSV file containing price data.
    :return: A DataFrame containing the price data.
    """
    try:
        price_data = pd.read_csv(file_path)
        if 'Date' not in price_data.columns or 'Price' not in price_data.columns:
            raise ValueError("CSV must contain 'Date' and 'Price' columns.")
        return price_data
    except Exception as e:
        print(f"Error loading price data: {e}")
        return None

if __name__ == "__main__":
    # Parameters for the simulation
    initial_investment = 1.0  # 1 ETH
    annual_interest_rate = 0.05  # 5% annual interest rate

    # Load historical price data
    price_data = load_price_data('ethereum_price_data.csv')
    
    if price_data is not None:
        # Create the simulator instance
        simulator = AutoCompoundingSimulator(initial_investment, annual_interest_rate, price_data)
        
        # Run the simulation
        simulator.simulate()
        
        # Get and print results
        results_df = simulator.get_results()
        print(results_df)

        # Plot the results
        simulator.plot_results()
```
