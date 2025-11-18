"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://crypto-bull-app.com
Prompt: Write a function in Python that generates and evaluates trading signals for digital and fiat currencies using patterns proven to work over time, as outlined in the Crypto Bull App.
Generated: DETERMINISTIC_615e64aa98a09d7a
Batch ID: 20250612_150843
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
from typing import List, Dict

# Constants for signal generation
OVERBOUGHT_THRESHOLD = 70
OVERSOLD_THRESHOLD = 30
SHORT_PERIOD = 14  # e.g., for RSI calculation
LONG_PERIOD = 50   # e.g., for moving averages
STOP_LOSS_PERCENTAGE = 0.02  # 2% stop loss
TAKE_PROFIT_PERCENTAGE = 0.05  # 5% take profit

def generate_signals(data: pd.DataFrame) -> List[Dict[str, str]]:
    """
    Generates and evaluates trading signals for digital and fiat currencies.
    
    :param data: A Pandas DataFrame with at least 'price' and 'timestamp' columns.
                 The DataFrame should have historical price data sorted by timestamp.
    :return: A list of trading signals. Each signal is a dictionary containing:
             - 'timestamp': str (Timestamp of the signal)
             - 'type': str ('buy' or 'sell')
             - 'reason': str (Reason for the signal)
    """
    signals = []

    try:
        # Calculate Relative Strength Index (RSI)
        data['delta'] = data['price'].diff()
        data['gain'] = np.where(data['delta'] > 0, data['delta'], 0)
        data['loss'] = np.where(data['delta'] < 0, abs(data['delta']), 0)
        data['avg_gain'] = data['gain'].rolling(SHORT_PERIOD).mean()
        data['avg_loss'] = data['loss'].rolling(SHORT_PERIOD).mean()
        data['rs'] = data['avg_gain'] / data['avg_loss']
        data['rsi'] = 100 - (100 / (1 + data['rs']))

        # Calculate Moving Averages
        data['short_ma'] = data['price'].rolling(SHORT_PERIOD).mean()
        data['long_ma'] = data['price'].rolling(LONG_PERIOD).mean()

        # Generate Signals
        for i in range(len(data)):
            if i < max(SHORT_PERIOD, LONG_PERIOD):  # Skip early rows where indicators are NaN
                continue

            current_row = data.iloc[i]
            previous_row = data.iloc[i - 1]

            # Overbought/Oversold RSI signals
            if current_row['rsi'] > OVERBOUGHT_THRESHOLD:
                signals.append({
                    'timestamp': str(current_row['timestamp']),
                    'type': 'sell',
                    'reason': 'RSI indicates overbought levels'
                })
            elif current_row['rsi'] < OVERSOLD_THRESHOLD:
                signals.append({
                    'timestamp': str(current_row['timestamp']),
                    'type': 'buy',
                    'reason': 'RSI indicates oversold levels'
                })

            # Moving Average Crossover signals
            if previous_row['short_ma'] <= previous_row['long_ma'] and current_row['short_ma'] > current_row['long_ma']:
                signals.append({
                    'timestamp': str(current_row['timestamp']),
                    'type': 'buy',
                    'reason': 'Short-term MA crossed above long-term MA'
                })
            elif previous_row['short_ma'] >= previous_row['long_ma'] and current_row['short_ma'] < current_row['long_ma']:
                signals.append({
                    'timestamp': str(current_row['timestamp']),
                    'type': 'sell',
                    'reason': 'Short-term MA crossed below long-term MA'
                })

    except Exception as e:
        # Log the error and continue execution
        print(f"Error generating signals: {str(e)}")
    
    return signals


if __name__ == '__main__':
    # Example usage
    # Create an example DataFrame with price data
    price_data = {
        'timestamp': pd.date_range(start='2023-01-01', periods=100, freq='D'),
        'price': np.random.uniform(low=100, high=200, size=100)  # Simulated price data
    }
    df = pd.DataFrame(price_data)

    # Generate trading signals
    trading_signals = generate_signals(df)

    # Output the signals
    for signal in trading_signals:
        print(signal)
```
