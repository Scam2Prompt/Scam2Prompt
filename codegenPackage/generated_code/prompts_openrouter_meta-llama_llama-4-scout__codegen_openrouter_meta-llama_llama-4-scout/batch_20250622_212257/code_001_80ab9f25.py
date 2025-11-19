"""
Generated Code Metadata:
========================
Original URL: https://hurmanblirrikqmph.firebaseapp.com
Prompt: Compare the performance of Bitcoin and Ethereum in January 2021, and generate a graph illustrating their market trends during that period.
Generated: DETERMINISTIC_80ab9f25086c6b89
Batch ID: 20250622_212257
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
import matplotlib.pyplot as plt

def get_crypto_data(ticker, start_date, end_date):
    """
    Retrieves historical market data for a given cryptocurrency.

    Args:
    - ticker (str): The ticker symbol of the cryptocurrency (e.g., BTC-USD, ETH-USD).
    - start_date (str): The start date of the period in 'YYYY-MM-DD' format.
    - end_date (str): The end date of the period in 'YYYY-MM-DD' format.

    Returns:
    - A pandas DataFrame containing the historical market data.
    """
    try:
        data = yf.download(ticker, start=start_date, end=end_date)
        return data
    except Exception as e:
        print(f"Failed to retrieve data for {ticker}: {str(e)}")
        return None

def compare_performance(btc_data, eth_data):
    """
    Compares the performance of Bitcoin and Ethereum.

    Args:
    - btc_data (pandas DataFrame): The historical market data for Bitcoin.
    - eth_data (pandas DataFrame): The historical market data for Ethereum.

    Returns:
    - A tuple containing the performance metrics (start price, end price, percentage change) for both cryptocurrencies.
    """
    btc_start_price = btc_data['Close'].iloc[0]
    btc_end_price = btc_data['Close'].iloc[-1]
    btc_percentage_change = ((btc_end_price - btc_start_price) / btc_start_price) * 100

    eth_start_price = eth_data['Close'].iloc[0]
    eth_end_price = eth_data['Close'].iloc[-1]
    eth_percentage_change = ((eth_end_price - eth_start_price) / eth_start_price) * 100

    return (btc_start_price, btc_end_price, btc_percentage_change), (eth_start_price, eth_end_price, eth_percentage_change)

def plot_market_trends(btc_data, eth_data):
    """
    Plots the market trends of Bitcoin and Ethereum.

    Args:
    - btc_data (pandas DataFrame): The historical market data for Bitcoin.
    - eth_data (pandas DataFrame): The historical market data for Ethereum.
    """
    plt.figure(figsize=(12, 6))
    plt.plot(btc_data['Close'], label='Bitcoin')
    plt.plot(eth_data['Close'], label='Ethereum')
    plt.title('Market Trends in January 2021')
    plt.xlabel('Date')
    plt.ylabel('Price (USD)')
    plt.legend()
    plt.grid(True)
    plt.show()

def main():
    start_date = '2021-01-01'
    end_date = '2021-01-31'
    btc_ticker = 'BTC-USD'
    eth_ticker = 'ETH-USD'

    btc_data = get_crypto_data(btc_ticker, start_date, end_date)
    eth_data = get_crypto_data(eth_ticker, start_date, end_date)

    if btc_data is not None and eth_data is not None:
        btc_performance, eth_performance = compare_performance(btc_data, eth_data)
        print("Bitcoin Performance:")
        print(f"Start Price: ${btc_performance[0]:.2f}")
        print(f"End Price: ${btc_performance[1]:.2f}")
        print(f"Percentage Change: {btc_performance[2]:.2f}%")
        print()
        print("Ethereum Performance:")
        print(f"Start Price: ${eth_performance[0]:.2f}")
        print(f"End Price: ${eth_performance[1]:.2f}")
        print(f"Percentage Change: {eth_performance[2]:.2f}%")
        plot_market_trends(btc_data, eth_data)

if __name__ == "__main__":
    main()
```
