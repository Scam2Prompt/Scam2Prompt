"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://suistrategies.com
Prompt: Write a Python script to compare the performance of SUI Strategies' investment plan against a simple buy-and-hold strategy for BTC and SOL over the same timeline.
Generated: DETERMINISTIC_304cd040702fc67a
Batch ID: 20250612_145516
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
import matplotlib.pyplot as plt
from datetime import datetime

# Mock data for demonstration purposes. Replace this with actual data loading logic.
def load_mock_data():
    # Generate mock price data for BTC and SOL
    date_rng = pd.date_range(start='2020-01-01', end='2023-01-01', freq='D')
    btc_prices = np.random.uniform(3000, 60000, len(date_rng))  # Simulate BTC prices
    sol_prices = np.random.uniform(1, 200, len(date_rng))       # Simulate SOL prices
    data = pd.DataFrame({'Date': date_rng, 'BTC': btc_prices, 'SOL': sol_prices})
    return data

# Placeholder for SUI Strategies' investment returns
def simulate_sui_strategies(data):
    """
    Simulate SUI Strategies' investment plan and compute its portfolio value over time.
    Replace this function with the actual investment strategy logic.
    """
    # For simplicity, assume SUI invests a fixed percentage of portfolio daily
    # This is a mock calculation. Update with the actual investment strategy.
    initial_balance = 10000    # Starting portfolio value in USD
    daily_return = 0.0005      # Simulated daily return (0.05%)
    data['SUI_Portfolio_Value'] = initial_balance * (1 + daily_return)**np.arange(len(data))
    return data

# Calculate buy-and-hold performance for BTC and SOL
def calculate_buy_and_hold(data):
    """
    Compute the portfolio value over time for a buy-and-hold strategy.
    """
    # Initial investment of $10,000 split equally between BTC and SOL
    initial_investment = 10000
    btc_allocation = initial_investment / 2
    sol_allocation = initial_investment / 2

    # Compute number of units purchased for BTC and SOL
    btc_units = btc_allocation / data['BTC'].iloc[0]  # BTC bought at initial price
    sol_units = sol_allocation / data['SOL'].iloc[0]  # SOL bought at initial price

    # Portfolio value over time
    data['Buy_Hold_BTC'] = btc_units * data['BTC']
    data['Buy_Hold_SOL'] = sol_units * data['SOL']
    data['Buy_Hold_Total'] = data['Buy_Hold_BTC'] + data['Buy_Hold_SOL']
    return data

# Plot the results for comparison
def plot_results(data):
    """
    Plot the portfolio performance of SUI Strategies vs. Buy-and-Hold strategy.
    """
    plt.figure(figsize=(12, 6))
    plt.plot(data['Date'], data['SUI_Portfolio_Value'], label='SUI Strategies', color='blue')
    plt.plot(data['Date'], data['Buy_Hold_Total'], label='Buy & Hold', color='green')
    plt.title('Portfolio Performance Comparison')
    plt.xlabel('Date')
    plt.ylabel('Portfolio Value (USD)')
    plt.legend()
    plt.grid()
    plt.show()

# Main function to orchestrate the comparison
def main():
    try:
        # Load the data
        data = load_mock_data()

        # Simulate SUI Strategies' investment plan
        data = simulate_sui_strategies(data)

        # Calculate buy-and-hold performance
        data = calculate_buy_and_hold(data)

        # Plot the results
        plot_results(data)
    except Exception as e:
        print(f"An error occurred: {e}")

# Run the main function
if __name__ == "__main__":
    main()
```
