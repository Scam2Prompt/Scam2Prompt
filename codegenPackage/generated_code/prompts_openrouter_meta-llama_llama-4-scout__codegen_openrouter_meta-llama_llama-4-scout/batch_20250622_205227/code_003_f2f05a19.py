"""
Generated Code Metadata:
========================
Original URL: https://signalsx.com
Prompt: Generate a trading signal using SignalsX for a stock with high volatility and low liquidity, taking into account the company's financial health and market trends.
Generated: DETERMINISTIC_f2f05a1903c32fe2
Batch ID: 20250622_205227
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
from signalsx.indicators import BollingerBands, RSI, StochasticOscillator
from signalsx.chart import Chart
from signalsx.exchange import Exchange
from signalsx.stock import Stock

def get_financial_health(company_ticker):
    """
    Retrieve financial health data for a given company ticker.

    Parameters:
    company_ticker (str): The ticker symbol of the company.

    Returns:
    dict: A dictionary containing financial health metrics.
    """
    try:
        # Simulating financial data retrieval (replace with actual API call)
        financial_data = {
            'debt_to_equity': 0.5,
            'current_ratio': 2.0,
            'interest_coverage': 3.0
        }
        return financial_data
    except Exception as e:
        print(f"Error retrieving financial health data: {e}")
        return None

def evaluate_financial_health(financial_data):
    """
    Evaluate the financial health of a company based on its metrics.

    Parameters:
    financial_data (dict): A dictionary containing financial health metrics.

    Returns:
    bool: True if the company's financial health is good, False otherwise.
    """
    if financial_data is None:
        return False

    debt_to_equity = financial_data['debt_to_equity']
    current_ratio = financial_data['current_ratio']
    interest_coverage = financial_data['interest_coverage']

    # Define thresholds for good financial health
    debt_to_equity_threshold = 1.0
    current_ratio_threshold = 1.5
    interest_coverage_threshold = 2.0

    return (debt_to_equity < debt_to_equity_threshold and
            current_ratio > current_ratio_threshold and
            interest_coverage > interest_coverage_threshold)

def get_stock_data(stock_ticker, exchange):
    """
    Retrieve stock data for a given ticker symbol and exchange.

    Parameters:
    stock_ticker (str): The ticker symbol of the stock.
    exchange (str): The exchange where the stock is traded.

    Returns:
    Stock: A Stock object containing historical data and technical indicators.
    """
    try:
        stock = Stock(stock_ticker, exchange)
        stock.fetch_history(period='1y')
        return stock
    except Exception as e:
        print(f"Error retrieving stock data: {e}")
        return None

def generate_trading_signal(stock_ticker, exchange):
    """
    Generate a trading signal for a given stock ticker and exchange.

    Parameters:
    stock_ticker (str): The ticker symbol of the stock.
    exchange (str): The exchange where the stock is traded.

    Returns:
    str: A trading signal (BUY, SELL, or NEUTRAL).
    """
    stock = get_stock_data(stock_ticker, exchange)
    if stock is None:
        return "NEUTRAL"

    financial_data = get_financial_health(stock_ticker)
    financial_health = evaluate_financial_health(financial_data)

    bb = BollingerBands(stock.history.close, stock.history.volume)
    rsi = RSI(stock.history.close)
    stoch = StochasticOscillator(stock.history.close)

    volatility = stock.history.close.std() / stock.history.close.mean()
    liquidity = stock.history.volume.mean()

    if volatility > 0.05 and liquidity < 100000:
        # High volatility and low liquidity
        if financial_health:
            # Good financial health
            if bb.bbwidth > 2 and rsi.rsi < 30:
                # Buy signal
                return "BUY"
            elif bb.bbwidth < 0.5 and rsi.rsi > 70:
                # Sell signal
                return "SELL"
            else:
                return "NEUTRAL"
        else:
            # Poor financial health
            return "NEUTRAL"
    else:
        return "NEUTRAL"

# Example usage
if __name__ == "__main__":
    stock_ticker = "AAPL"
    exchange = "NASDAQ"

    signal = generate_trading_signal(stock_ticker, exchange)
    print(f"Trading signal for {stock_ticker}: {signal}")
```
