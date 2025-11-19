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
import yfinance as yf

def fetch_historical_data(ticker1, ticker2, start_date, end_date):
    """
    Fetch historical data for two tickers.

    Parameters:
    ticker1 (str): First ticker symbol.
    ticker2 (str): Second ticker symbol.
    start_date (str): Start date in 'YYYY-MM-DD' format.
    end_date (str): End date in 'YYYY-MM-DD' format.

    Returns:
    tuple: Two pandas DataFrames with historical data.
    """
    try:
        data1 = yf.download(ticker1, start=start_date, end=end_date)
        data2 = yf.download(ticker2, start=start_date, end=end_date)
        return data1, data2
    except Exception as e:
        print(f"Error fetching data: {e}")
        return None, None

def calculate_spread(data1, data2):
    """
    Calculate the spread between two time series.

    Parameters:
    data1 (pandas DataFrame): First time series.
    data2 (pandas DataFrame): Second time series.

    Returns:
    pandas Series: Spread between the two time series.
    """
    return data1['Close'] - data2['Close']

def calculate_z_score(spread, mean, std):
    """
    Calculate the z-score of the spread.

    Parameters:
    spread (pandas Series): Spread between the two time series.
    mean (float): Mean of the spread.
    std (float): Standard deviation of the spread.

    Returns:
    pandas Series: Z-score of the spread.
    """
    return (spread - mean) / std

def pair_trading_strategy(data1, data2, stop_loss):
    """
    Pair trading strategy with a stop-loss.

    Parameters:
    data1 (pandas DataFrame): First time series.
    data2 (pandas DataFrame): Second time series.
    stop_loss (float): Stop-loss percentage.

    Returns:
    tuple: P/L and positions.
    """
    spread = calculate_spread(data1, data2)
    mean = spread.mean()
    std = spread.std()

    positions = []
    pnl = []
    long_short = 0

    for i in range(1, len(spread)):
        z_score = calculate_z_score(spread.iloc[i], mean, std)

        if z_score > 2:
            # Long ETF and short ETHD
            if long_short != 1:
                long_short = 1
                positions.append(1)
            else:
                positions.append(1)
        elif z_score < -2:
            # Short ETF and long ETHD
            if long_short != -1:
                long_short = -1
                positions.append(-1)
            else:
                positions.append(-1)
        else:
            # Close position
            if long_short != 0:
                long_short = 0
                positions.append(0)
            else:
                positions.append(0)

        # Stop-loss
        if long_short == 1 and (data1['Close'].iloc[i] / data1['Close'].iloc[i-1] - 1) < -stop_loss/100:
            long_short = 0
            positions.append(0)
        elif long_short == -1 and (data2['Close'].iloc[i] / data2['Close'].iloc[i-1] - 1) < -stop_loss/100:
            long_short = 0
            positions.append(0)

        # Calculate P/L
        if long_short == 1:
            pnl.append((data1['Close'].iloc[i] - data1['Close'].iloc[i-1]) - (data2['Close'].iloc[i] - data2['Close'].iloc[i-1]))
        elif long_short == -1:
            pnl.append((data2['Close'].iloc[i] - data2['Close'].iloc[i-1]) - (data1['Close'].iloc[i] - data1['Close'].iloc[i-1]))
        else:
            pnl.append(0)

    return np.sum(pnl), positions

def main():
    ticker1 = 'ETHT'
    ticker2 = 'ETHD'
    start_date = '2020-01-01'
    end_date = '2022-02-26'
    stop_loss = 5

    data1, data2 = fetch_historical_data(ticker1, ticker2, start_date, end_date)

    if data1 is not None and data2 is not None:
        pnl, positions = pair_trading_strategy(data1, data2, stop_loss)
        print(f"P/L: {pnl}")
        print(f"Positions: {positions}")

if __name__ == "__main__":
    main()
```
