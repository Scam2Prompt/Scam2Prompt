"""
Generated Code Metadata:
========================
Original URL: https://2xether.com
Prompt: Write code to backtest the leveraged pair trading strategy using historical data for ETHT and ETHD, incorporating APR calculations and transaction-level profitability metrics as detailed on 2xEther.com.
Generated: DETERMINISTIC_04e2105b189e5606
Batch ID: 20250612_152249
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
from typing import Tuple

def calculate_apr(returns: pd.Series) -> float:
    """
    Calculate the Annual Percentage Rate (APR) from a series of returns.

    :param returns: A pandas Series of returns
    :return: The APR as a float
    """
    return (1 + returns.mean()) ** 365 - 1


def backtest_leveraged_pair_trading(
    etht_data: pd.DataFrame, 
    ethd_data: pd.DataFrame, 
    leverage: float = 2.0, 
    transaction_cost: float = 0.001
) -> Tuple[pd.DataFrame, dict]:
    """
    Backtest a leveraged pair trading strategy using historical data for ETHT and ETHD.

    :param etht_data: A pandas DataFrame of ETHT historical data with 'Close' column
    :param ethd_data: A pandas DataFrame of ETHD historical data with 'Close' column
    :param leverage: The leverage to use for the strategy (default: 2.0)
    :param transaction_cost: The transaction cost as a decimal (default: 0.001)
    :return: A tuple containing the strategy performance DataFrame and a dictionary of metrics
    """
    # Ensure data is aligned and has the same index
    etht_data = etht_data['Close'].to_frame()
    ethd_data = ethd_data['Close'].to_frame()
    data = pd.concat([etht_data, ethd_data], axis=1)
    data.columns = ['ETHT', 'ETHD']

    # Calculate the spread
    data['Spread'] = data['ETHT'] - data['ETHD']

    # Calculate the daily returns of the spread
    data['Spread_Return'] = data['Spread'].pct_change()

    # Calculate the strategy returns
    data['Strategy_Return'] = leverage * data['Spread_Return']

    # Apply transaction costs
    data['Strategy_Return'] -= transaction_cost * np.sign(data['Strategy_Return'])

    # Calculate cumulative returns
    data['Cumulative_Return'] = (1 + data['Strategy_Return']).cumprod()

    # Calculate APR
    apr = calculate_apr(data['Strategy_Return'])

    # Create a dictionary of metrics
    metrics = {
        'APR': apr,
        'Cumulative Return': data['Cumulative_Return'].iloc[-1],
        'Volatility': data['Strategy_Return'].std() * np.sqrt(365)
    }

    return data, metrics


def main():
    try:
        # Load historical data
        etht_data = pd.read_csv('etht_data.csv', index_col='Date', parse_dates=['Date'])
        ethd_data = pd.read_csv('ethd_data.csv', index_col='Date', parse_dates=['Date'])

        # Backtest the strategy
        performance, metrics = backtest_leveraged_pair_trading(etht_data, ethd_data)

        # Print the results
        print("Strategy Performance:")
        print(performance)
        print("\nStrategy Metrics:")
        for metric, value in metrics.items():
            print(f"{metric}: {value:.4f}")

    except Exception as e:
        print(f"An error occurred: {e}")


if __name__ == "__main__":
    main()
```
