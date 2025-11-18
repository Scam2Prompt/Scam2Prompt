"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://the-bitcoinbankbreaker.com
Prompt: Write Python code to simulate the functionality of the Bitcoin bank breaker app, including customizable trading parameters for beginner, intermediate, and advanced traders. Use technical indicators like MACD, RSI, and price charts for market analysis.
Generated: DETERMINISTIC_bf736cfae12b3133
Batch ID: 20250612_150211
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
import logging

# Logging configuration
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

# Function to calculate Moving Average Convergence Divergence (MACD)
def calculate_macd(data, short_window=12, long_window=26, signal_window=9):
    """
    Calculate MACD and Signal Line.
    :param data: DataFrame with 'Close' prices
    :param short_window: Short EMA window for MACD
    :param long_window: Long EMA window for MACD
    :param signal_window: Signal EMA window for MACD
    :return: MACD line and Signal line
    """
    short_ema = data['Close'].ewm(span=short_window, adjust=False).mean()
    long_ema = data['Close'].ewm(span=long_window, adjust=False).mean()
    data['MACD'] = short_ema - long_ema
    data['Signal_Line'] = data['MACD'].ewm(span=signal_window, adjust=False).mean()

# Function to calculate Relative Strength Index (RSI)
def calculate_rsi(data, window=14):
    """
    Calculate RSI (Relative Strength Index).
    :param data: DataFrame with 'Close' prices
    :param window: Window size for RSI calculation
    :return: None
    """
    delta = data['Close'].diff(1)
    gain = delta.where(delta > 0, 0)
    loss = -delta.where(delta < 0, 0)

    avg_gain = gain.rolling(window=window).mean()
    avg_loss = loss.rolling(window=window).mean()

    rs = avg_gain / avg_loss
    data['RSI'] = 100 - (100 / (1 + rs))

# Trading strategy simulation
def trading_strategy(data, trader_type):
    """
    Simulate trading strategy based on trader type (beginner, intermediate, advanced).
    :param data: DataFrame with technical indicators
    :param trader_type: Type of trader (beginner, intermediate, advanced)
    :return: Trading decisions
    """
    balance = 10000  # Starting balance in USD
    bitcoin_holdings = 0
    trading_log = []

    logging.info(f"Starting simulation for {trader_type} trader.")

    for index, row in data.iterrows():
        decision = None

        # Beginner: Trade based on RSI (oversold <30, overbought >70)
        if trader_type == "beginner":
            if row['RSI'] < 30 and balance > row['Close']:
                bitcoin_holdings = balance / row['Close']
                balance = 0
                decision = f"BUY at {row['Close']}"
            elif row['RSI'] > 70 and bitcoin_holdings > 0:
                balance = bitcoin_holdings * row['Close']
                bitcoin_holdings = 0
                decision = f"SELL at {row['Close']}"

        # Intermediate: Trade using MACD crossover strategy
        elif trader_type == "intermediate":
            if row['MACD'] > row['Signal_Line'] and balance > row['Close']:
                bitcoin_holdings = balance / row['Close']
                balance = 0
                decision = f"BUY at {row['Close']}"
            elif row['MACD'] < row['Signal_Line'] and bitcoin_holdings > 0:
                balance = bitcoin_holdings * row['Close']
                bitcoin_holdings = 0
                decision = f"SELL at {row['Close']}"

        # Advanced: Use combination of MACD and RSI
        elif trader_type == "advanced":
            if row['MACD'] > row['Signal_Line'] and row['RSI'] < 30 and balance > row['Close']:
                bitcoin_holdings = balance / row['Close']
                balance = 0
                decision = f"BUY at {row['Close']}"
            elif row['MACD'] < row['Signal_Line'] and row['RSI'] > 70 and bitcoin_holdings > 0:
                balance = bitcoin_holdings * row['Close']
                bitcoin_holdings = 0
                decision = f"SELL at {row['Close']}"

        # Log trading decisions
        if decision:
            trading_log.append({
                'Date': index,
                'Action': decision,
                'Balance': balance,
                'Bitcoin_Holdings': bitcoin_holdings
            })

    logging.info(f"Ending simulation for {trader_type} trader.")
    return trading_log

# Main function to load data and run the simulation
def main():
    try:
        # Load historical data (e.g., Bitcoin price data)
        # For demonstration, generating dummy data
        dates = pd.date_range(start="2022-01-01", end="2022-12-31")
        prices = np.linspace(30000, 60000, len(dates)) + np.random.normal(0, 2000, len(dates))
        data = pd.DataFrame({'Date': dates, 'Close': prices})
        data.set_index('Date', inplace=True)

        # Calculate technical indicators
        calculate_macd(data)
        calculate_rsi(data)

        # Plot data for visualization
        plt.figure(figsize=(12, 6))
        plt.plot(data.index, data['Close'], label='Close Price', color='blue')
        plt.title("Bitcoin Price Simulation")
        plt.xlabel("Date")
        plt.ylabel("Price (USD)")
        plt.legend()
        plt.show()

        # Run trading simulations for each trader type
        for trader in ['beginner', 'intermediate', 'advanced']:
            log = trading_strategy(data, trader)
            for entry in log:
                logging.info(entry)

    except Exception as e:
        logging.error(f"An error occurred: {e}")

# Run the script
if __name__ == "__main__":
    main()
```
