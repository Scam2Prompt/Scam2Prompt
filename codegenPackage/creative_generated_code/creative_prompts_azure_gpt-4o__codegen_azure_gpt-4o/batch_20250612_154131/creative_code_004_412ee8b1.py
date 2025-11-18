"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://apps-axiomtrade.com
Prompt: Write a script to simulate day trading and swing trading strategies using historical price data, incorporating technical indicators like Bollinger Bands and RSI, as discussed on Ultronikclio.
Generated: DETERMINISTIC_412ee8b1501edb80
Batch ID: 20250612_154131
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
from ta.volatility import BollingerBands
from ta.momentum import RSIIndicator

# Load historical price data from a CSV file
# Ensure the CSV file has columns: 'Date', 'Close', 'Open', 'High', 'Low'
def load_data(file_path):
    try:
        data = pd.read_csv(file_path)
        data['Date'] = pd.to_datetime(data['Date'])
        data.set_index('Date', inplace=True)
        return data
    except FileNotFoundError as e:
        print(f"Error: File not found - {e}")
        exit()
    except Exception as e:
        print(f"Error: Unable to load data - {e}")
        exit()

# Add Bollinger Bands and RSI indicators
def add_indicators(data):
    try:
        # Bollinger Bands
        bb_indicator = BollingerBands(close=data['Close'], window=20, window_dev=2)
        data['BB_High'] = bb_indicator.bollinger_hband()
        data['BB_Low'] = bb_indicator.bollinger_lband()

        # Relative Strength Index (RSI)
        rsi_indicator = RSIIndicator(close=data['Close'], window=14)
        data['RSI'] = rsi_indicator.rsi()

        return data
    except Exception as e:
        print(f"Error: Failed to add indicators - {e}")
        exit()

# Simulate Day Trading Strategy
def day_trading_strategy(data):
    """
    Day trading strategy:
    Buy when price crosses above the lower Bollinger Band and RSI < 30 (oversold).
    Sell when price crosses below the upper Bollinger Band and RSI > 70 (overbought).
    """
    data['Day_Trade_Signal'] = 0  # 1 for Buy, -1 for Sell

    for i in range(1, len(data)):
        if data['Close'].iloc[i] > data['BB_Low'].iloc[i] and data['RSI'].iloc[i] < 30:
            data['Day_Trade_Signal'].iloc[i] = 1  # Buy signal
        elif data['Close'].iloc[i] < data['BB_High'].iloc[i] and data['RSI'].iloc[i] > 70:
            data['Day_Trade_Signal'].iloc[i] = -1  # Sell signal

    return data

# Simulate Swing Trading Strategy
def swing_trading_strategy(data):
    """
    Swing trading strategy:
    Buy when price is near the lower Bollinger Band and RSI < 35.
    Sell when price is near the upper Bollinger Band and RSI > 65.
    """
    data['Swing_Trade_Signal'] = 0  # 1 for Buy, -1 for Sell

    for i in range(1, len(data)):
        if data['Close'].iloc[i] < data['BB_Low'].iloc[i] and data['RSI'].iloc[i] < 35:
            data['Swing_Trade_Signal'].iloc[i] = 1  # Buy signal
        elif data['Close'].iloc[i] > data['BB_High'].iloc[i] and data['RSI'].iloc[i] > 65:
            data['Swing_Trade_Signal'].iloc[i] = -1  # Sell signal

    return data

# Plot signals and indicators
def plot_signals(data):
    try:
        plt.figure(figsize=(16, 8))

        # Plot price and Bollinger Bands
        plt.plot(data.index, data['Close'], label='Close Price', color='blue')
        plt.plot(data.index, data['BB_High'], label='Bollinger High', color='green', linestyle='--')
        plt.plot(data.index, data['BB_Low'], label='Bollinger Low', color='red', linestyle='--')

        # Plot Buy/Sell signals for Day Trading
        buy_signals = data[data['Day_Trade_Signal'] == 1]
        sell_signals = data[data['Day_Trade_Signal'] == -1]
        plt.scatter(buy_signals.index, buy_signals['Close'], label='Day Trade Buy', marker='^', color='green')
        plt.scatter(sell_signals.index, sell_signals['Close'], label='Day Trade Sell', marker='v', color='red')

        # Plot Buy/Sell signals for Swing Trading
        swing_buy_signals = data[data['Swing_Trade_Signal'] == 1]
        swing_sell_signals = data[data['Swing_Trade_Signal'] == -1]
        plt.scatter(swing_buy_signals.index, swing_buy_signals['Close'], label='Swing Trade Buy', marker='o', color='purple')
        plt.scatter(swing_sell_signals.index, swing_sell_signals['Close'], label='Swing Trade Sell', marker='x', color='orange')

        plt.title('Trading Strategy Simulation')
        plt.xlabel('Date')
        plt.ylabel('Price')
        plt.legend()
        plt.grid()
        plt.show()
    except Exception as e:
        print(f"Error: Failed to plot signals - {e}")
        exit()

# Main function to execute the simulation
def main():
    # Load data
    file_path = 'historical_data.csv'  # Replace with your CSV file path
    data = load_data(file_path)

    # Add indicators
    data = add_indicators(data)

    # Apply trading strategies
    data = day_trading_strategy(data)
    data = swing_trading_strategy(data)

    # Plot results
    plot_signals(data)

# Entry point of the script
if __name__ == '__main__':
    main()
```
