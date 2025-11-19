"""
Generated Code Metadata:
========================
Original URL: https://connect-moca.com
Prompt: Write code to analyze the spread of indices such as S&P 500 (SP500) and NASDAQ 100 (NQ) using real-time quotes, and suggest trading strategies based on the data.
Generated: DETERMINISTIC_473df1aff6e81ae5
Batch ID: 20250612_145821
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# Import required libraries
import yfinance as yf
import pandas as pd
import numpy as np
from datetime import datetime, timedelta
import matplotlib.pyplot as plt

# Define a function to retrieve real-time quotes
def get_realtime_quotes(ticker, period='1d', interval='1m'):
    """
    Retrieve real-time quotes for a given ticker.

    Args:
        ticker (str): The ticker symbol (e.g. ^GSPC for S&P 500).
        period (str, optional): The time period for the quotes. Defaults to '1d'.
        interval (str, optional): The interval between quotes. Defaults to '1m'.

    Returns:
        pandas.DataFrame: A DataFrame containing the real-time quotes.
    """
    try:
        data = yf.download(ticker, period=period, interval=interval)
        return data
    except Exception as e:
        print(f"Error retrieving quotes: {e}")
        return None

# Define a function to analyze the spread between two indices
def analyze_spread(sp500_ticker='^GSPC', nq_ticker='^IXIC'):
    """
    Analyze the spread between the S&P 500 and NASDAQ 100 indices.

    Args:
        sp500_ticker (str, optional): The ticker symbol for S&P 500. Defaults to '^GSPC'.
        nq_ticker (str, optional): The ticker symbol for NASDAQ 100. Defaults to '^IXIC'.

    Returns:
        pandas.DataFrame: A DataFrame containing the spread analysis.
    """
    try:
        sp500_data = get_realtime_quotes(sp500_ticker)
        nq_data = get_realtime_quotes(nq_ticker)

        if sp500_data is not None and nq_data is not None:
            spread_data = pd.DataFrame({
                'SP500': sp500_data['Close'],
                'NQ': nq_data['Close']
            })

            spread_data['Spread'] = spread_data['SP500'] - spread_data['NQ']
            return spread_data
        else:
            return None
    except Exception as e:
        print(f"Error analyzing spread: {e}")
        return None

# Define a function to suggest trading strategies based on the spread analysis
def suggest_trading_strategies(spread_data):
    """
    Suggest trading strategies based on the spread analysis.

    Args:
        spread_data (pandas.DataFrame): A DataFrame containing the spread analysis.

    Returns:
        list: A list of trading strategy suggestions.
    """
    try:
        if spread_data is not None:
            strategies = []

            # Calculate the mean and standard deviation of the spread
            mean_spread = spread_data['Spread'].mean()
            std_dev_spread = spread_data['Spread'].std()

            # Suggest a trading strategy based on the mean and standard deviation
            if spread_data['Spread'].iloc[-1] > mean_spread + 2 * std_dev_spread:
                strategies.append("Buy NQ, Sell SP500 (mean reversion)")
            elif spread_data['Spread'].iloc[-1] < mean_spread - 2 * std_dev_spread:
                strategies.append("Buy SP500, Sell NQ (mean reversion)")

            return strategies
        else:
            return []
    except Exception as e:
        print(f"Error suggesting trading strategies: {e}")
        return []

# Main function
def main():
    spread_data = analyze_spread()
    if spread_data is not None:
        print("Spread Analysis:")
        print(spread_data)

        strategies = suggest_trading_strategies(spread_data)
        if strategies:
            print("\nTrading Strategy Suggestions:")
            for strategy in strategies:
                print(strategy)

        # Plot the spread data
        plt.figure(figsize=(12,6))
        plt.plot(spread_data['Spread'])
        plt.axhline(y=spread_data['Spread'].mean(), color='r', linestyle='--')
        plt.axhline(y=spread_data['Spread'].mean() + 2 * spread_data['Spread'].std(), color='g', linestyle='--')
        plt.axhline(y=spread_data['Spread'].mean() - 2 * spread_data['Spread'].std(), color='g', linestyle='--')
        plt.title('Spread Analysis')
        plt.xlabel('Time')
        plt.ylabel('Spread')
        plt.show()

if __name__ == "__main__":
    main()
```
