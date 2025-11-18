"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://mybitcoinqrcode.com
Prompt: Write code to analyze the performance of a crypto strategy, including Bitcoin, using historical data and calculate returns over 1 month, 1 year, and year-to-date (YTD).
Generated: DETERMINISTIC_3cd0caa76bebd3a0
Batch ID: 20250612_151847
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
from datetime import datetime, timedelta

class CryptoPerformanceAnalyzer:
    """
    A class to analyze the performance of a cryptocurrency strategy, specifically Bitcoin,
    using historical price data.
    """

    def __init__(self, data_file):
        """
        Initialize the analyzer with historical price data.

        :param data_file: Path to the CSV file containing historical price data.
        """
        self.data = self.load_data(data_file)
        self.data['Date'] = pd.to_datetime(self.data['Date'])
        self.data.set_index('Date', inplace=True)

    def load_data(self, data_file):
        """
        Load historical price data from a CSV file.

        :param data_file: Path to the CSV file.
        :return: Pandas DataFrame containing the price data.
        """
        try:
            data = pd.read_csv(data_file)
            return data
        except FileNotFoundError:
            raise FileNotFoundError("The specified data file was not found.")
        except pd.errors.EmptyDataError:
            raise ValueError("The data file is empty.")
        except Exception as e:
            raise RuntimeError(f"An error occurred while loading data: {e}")

    def calculate_returns(self):
        """
        Calculate the returns over 1 month, 1 year, and year-to-date (YTD).
        
        :return: A dictionary containing the returns for different periods.
        """
        latest_date = self.data.index[-1]
        one_month_ago = latest_date - pd.DateOffset(months=1)
        one_year_ago = latest_date - pd.DateOffset(years=1)
        year_start = datetime(latest_date.year, 1, 1)

        try:
            # Get prices for the relevant periods
            price_latest = self.data.loc[latest_date, 'Close']
            price_1m = self.data.loc[one_month_ago, 'Close']
            price_1y = self.data.loc[one_year_ago, 'Close']
            price_ytd = self.data.loc[year_start:latest_date]['Close'].iloc[0]

            # Calculate returns
            returns = {
                '1M': (price_latest - price_1m) / price_1m * 100,
                '1Y': (price_latest - price_1y) / price_1y * 100,
                'YTD': (price_latest - price_ytd) / price_ytd * 100,
            }
            return returns
        except KeyError as e:
            raise KeyError(f"Missing data for key: {e}")
        except Exception as e:
            raise RuntimeError(f"An error occurred while calculating returns: {e}")

    def plot_performance(self):
        """
        Plot the historical price data.
        """
        plt.figure(figsize=(12, 6))
        plt.plot(self.data.index, self.data['Close'], label='Bitcoin Price', color='blue')
        plt.title('Bitcoin Historical Price')
        plt.xlabel('Date')
        plt.ylabel('Price (USD)')
        plt.legend()
        plt.grid()
        plt.show()

if __name__ == "__main__":
    # Replace 'path_to_your_data.csv' with the actual path to your historical data file.
    analyzer = CryptoPerformanceAnalyzer('path_to_your_data.csv')
    
    # Calculate returns
    returns = analyzer.calculate_returns()
    print("Returns over different periods:")
    print(f"1 Month: {returns['1M']:.2f}%")
    print(f"1 Year: {returns['1Y']:.2f}%")
    print(f"Year-To-Date: {returns['YTD']:.2f}%")
    
    # Plot performance
    analyzer.plot_performance()
```

**Note**: Ensure that your CSV file has at least two columns: "Date" (in YYYY-MM-DD format) and "Close" (for the closing price of Bitcoin). Adjust the file path in the `CryptoPerformanceAnalyzer` instantiation.
