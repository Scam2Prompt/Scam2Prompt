"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://immediateplatform.org
Prompt: Write Python code to analyze historical cryptocurrency price data using technical indicators like moving averages, RSI, and Bollinger Bands, as described on the MarvexTrader platform.
Generated: DETERMINISTIC_44f4f24904e41d0e
Batch ID: 20250612_150854
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

class CryptoAnalyzer:
    def __init__(self, data: pd.DataFrame):
        """
        Initializes the CryptoAnalyzer with historical price data.

        :param data: DataFrame containing historical price data with 'Date' and 'Close' columns.
        """
        self.data = data
        self.data['Date'] = pd.to_datetime(self.data['Date'])
        self.data.set_index('Date', inplace=True)

    def calculate_moving_average(self, window: int) -> pd.Series:
        """
        Calculates the Simple Moving Average (SMA) for the given window.

        :param window: The window size for the SMA.
        :return: Series containing SMA values.
        """
        return self.data['Close'].rolling(window=window).mean()

    def calculate_rsi(self, window: int = 14) -> pd.Series:
        """
        Calculates the Relative Strength Index (RSI).

        :param window: The window size for calculating RSI.
        :return: Series containing RSI values.
        """
        delta = self.data['Close'].diff(1)
        gain = (delta.where(delta > 0, 0)).rolling(window=window).mean()
        loss = (-delta.where(delta < 0, 0)).rolling(window=window).mean()
        rs = gain / loss
        rsi = 100 - (100 / (1 + rs))
        return rsi

    def calculate_bollinger_bands(self, window: int = 20, num_of_std: int = 2) -> pd.DataFrame:
        """
        Calculates Bollinger Bands.

        :param window: The window size for the moving average.
        :param num_of_std: The number of standard deviations for the bands.
        :return: DataFrame containing SMA, Upper Band, and Lower Band.
        """
        sma = self.calculate_moving_average(window)
        rolling_std = self.data['Close'].rolling(window).std()
        upper_band = sma + (rolling_std * num_of_std)
        lower_band = sma - (rolling_std * num_of_std)

        return pd.DataFrame({
            'SMA': sma,
            'Upper Band': upper_band,
            'Lower Band': lower_band
        })

    def plot_indicators(self):
        """
        Plots the closing price along with the moving average, RSI, and Bollinger Bands.
        """
        try:
            # Plot price and moving average
            plt.figure(figsize=(14, 7))
            plt.plot(self.data['Close'], label='Closing Price', color='blue')
            sma = self.calculate_moving_average(20)
            plt.plot(sma, label='20-day SMA', color='orange')
            bollinger_bands = self.calculate_bollinger_bands()
            plt.plot(bollinger_bands['Upper Band'], label='Upper Bollinger Band', color='red')
            plt.plot(bollinger_bands['Lower Band'], label='Lower Bollinger Band', color='green')
            plt.title('Cryptocurrency Price with Moving Average and Bollinger Bands')
            plt.legend()
            plt.show()

            # Plot RSI
            plt.figure(figsize=(14, 5))
            rsi = self.calculate_rsi()
            plt.plot(rsi, label='RSI', color='purple')
            plt.axhline(70, linestyle='--', alpha=0.5, color='red')
            plt.axhline(30, linestyle='--', alpha=0.5, color='green')
            plt.title('Relative Strength Index (RSI)')
            plt.legend()
            plt.show()

        except Exception as e:
            print(f"Error while plotting indicators: {e}")

# Example usage
if __name__ == "__main__":
    # Load historical cryptocurrency price data
    try:
        # Replace 'crypto_data.csv' with your actual CSV file path
        data = pd.read_csv('crypto_data.csv')
        analyzer = CryptoAnalyzer(data)

        # Plot indicators
        analyzer.plot_indicators()
    except FileNotFoundError:
        print("Error: The specified data file was not found.")
    except pd.errors.EmptyDataError:
        print("Error: The data file is empty.")
    except Exception as e:
        print(f"An error occurred: {e}")
```
