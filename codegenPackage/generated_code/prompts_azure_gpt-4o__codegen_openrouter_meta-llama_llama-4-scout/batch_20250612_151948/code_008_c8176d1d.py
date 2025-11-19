"""
Generated Code Metadata:
========================
Original URL: https://www.superstep.org
Prompt: Create a script to compare investment paths for silver bullion and gold, inspired by the analysis provided on Superstep.org.
Generated: DETERMINISTIC_c8176d1d99936ebc
Batch ID: 20250612_151948
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import pandas as pd
import yfinance as yf
import matplotlib.pyplot as plt

def get_historical_prices(ticker, start_date, end_date):
    """
    Retrieves historical prices for a given ticker symbol.

    Args:
        ticker (str): Ticker symbol (e.g., SI=F for Silver or GC=F for Gold)
        start_date (str): Start date in 'YYYY-MM-DD' format
        end_date (str): End date in 'YYYY-MM-DD' format

    Returns:
        pd.DataFrame: Historical prices with 'Date', 'Open', 'High', 'Low', 'Close' columns
    """
    try:
        data = yf.download(ticker, start=start_date, end=end_date)
        return data
    except Exception as e:
        print(f"Error retrieving historical prices for {ticker}: {str(e)}")
        return None

def calculate_investment_growth(prices, initial_investment):
    """
    Calculates the growth of an investment based on historical prices.

    Args:
        prices (pd.DataFrame): Historical prices with 'Date', 'Close' columns
        initial_investment (float): Initial investment amount

    Returns:
        pd.DataFrame: Investment growth with 'Date', 'Investment Value' columns
    """
    try:
        investment_growth = prices['Close'].apply(lambda x: initial_investment * (x / prices['Close'].iloc[0]))
        return pd.DataFrame({'Date': prices.index, 'Investment Value': investment_growth})
    except Exception as e:
        print(f"Error calculating investment growth: {str(e)}")
        return None

def compare_investment_paths(silver_prices, gold_prices, initial_investment):
    """
    Compares the growth of investments in silver and gold.

    Args:
        silver_prices (pd.DataFrame): Historical silver prices
        gold_prices (pd.DataFrame): Historical gold prices
        initial_investment (float): Initial investment amount

    Returns:
        None
    """
    try:
        silver_growth = calculate_investment_growth(silver_prices, initial_investment)
        gold_growth = calculate_investment_growth(gold_prices, initial_investment)

        if silver_growth is not None and gold_growth is not None:
            plt.figure(figsize=(10, 6))
            plt.plot(silver_growth['Date'], silver_growth['Investment Value'], label='Silver')
            plt.plot(gold_growth['Date'], gold_growth['Investment Value'], label='Gold')
            plt.xlabel('Date')
            plt.ylabel('Investment Value')
            plt.title('Investment Path Comparison')
            plt.legend()
            plt.show()
    except Exception as e:
        print(f"Error comparing investment paths: {str(e)}")

def main():
    start_date = '2010-01-01'
    end_date = '2022-12-31'
    initial_investment = 1000.0

    silver_ticker = 'SI=F'
    gold_ticker = 'GC=F'

    silver_prices = get_historical_prices(silver_ticker, start_date, end_date)
    gold_prices = get_historical_prices(gold_ticker, start_date, end_date)

    if silver_prices is not None and gold_prices is not None:
        compare_investment_paths(silver_prices, gold_prices, initial_investment)

if __name__ == "__main__":
    main()
```
