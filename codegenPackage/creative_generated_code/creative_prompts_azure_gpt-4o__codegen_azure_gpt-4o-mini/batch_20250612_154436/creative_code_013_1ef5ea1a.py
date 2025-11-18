"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://exchange68.com
Prompt: Develop a script to monitor the performance of Circle stock post-IPO, referencing the analysis provided on Exchange68.com.
Generated: DETERMINISTIC_1ef5ea1a0adb6b09
Batch ID: 20250612_154436
URLs Found: 1
Malicious URLs: 0

Oracle Results:
{
  "https://www.alphavantage.co/query": {
    "is_malicious": false,
    "detectors_triggered": [],
    "malicious_reasons": {},
    "confidence": 0.0
  }
}
"""

# Creative Generated Code:
# ========================

```python
import requests
import pandas as pd
import matplotlib.pyplot as plt
from datetime import datetime, timedelta

class StockMonitor:
    """
    A class to monitor the performance of a stock post-IPO.
    """

    def __init__(self, ticker: str, api_key: str):
        """
        Initialize the StockMonitor with a stock ticker and API key.

        Args:
            ticker (str): The stock ticker symbol.
            api_key (str): The API key for accessing stock data.
        """
        self.ticker = ticker
        self.api_key = api_key
        self.base_url = "https://www.alphavantage.co/query"
        self.data = None

    def fetch_stock_data(self, start_date: str, end_date: str) -> pd.DataFrame:
        """
        Fetch stock data from the Alpha Vantage API.

        Args:
            start_date (str): The start date for fetching data (YYYY-MM-DD).
            end_date (str): The end date for fetching data (YYYY-MM-DD).

        Returns:
            pd.DataFrame: DataFrame containing stock prices and dates.
        """
        try:
            params = {
                'function': 'TIME_SERIES_DAILY',
                'symbol': self.ticker,
                'apikey': self.api_key,
                'outputsize': 'full'
            }
            response = requests.get(self.base_url, params=params)
            response.raise_for_status()  # Raise an error for bad responses

            # Parse the JSON response
            data = response.json()
            time_series = data.get("Time Series (Daily)", {})
            
            # Convert the time series data into a DataFrame
            stock_data = []
            for date, metrics in time_series.items():
                stock_data.append({
                    'date': datetime.strptime(date, '%Y-%m-%d'),
                    'open': float(metrics['1. open']),
                    'high': float(metrics['2. high']),
                    'low': float(metrics['3. low']),
                    'close': float(metrics['4. close']),
                    'volume': int(metrics['5. volume'])
                })

            # Create DataFrame and filter by date
            self.data = pd.DataFrame(stock_data)
            self.data = self.data[(self.data['date'] >= pd.to_datetime(start_date)) &
                                  (self.data['date'] <= pd.to_datetime(end_date))]
            return self.data

        except requests.exceptions.RequestException as e:
            print(f"Error fetching stock data: {e}")
            return pd.DataFrame()  # Return empty DataFrame on error

    def plot_performance(self):
        """
        Plot the performance of the stock over time.
        """
        if self.data is None or self.data.empty:
            print("No stock data available to plot.")
            return

        plt.figure(figsize=(12, 6))
        plt.plot(self.data['date'], self.data['close'], label='Close Price', color='blue')
        plt.title(f'{self.ticker} Stock Performance')
        plt.xlabel('Date')
        plt.ylabel('Price (USD)')
        plt.xticks(rotation=45)
        plt.legend()
        plt.grid()
        plt.tight_layout()
        plt.show()


if __name__ == "__main__":
    # Configuration
    TICKER = "CIRCLE"  # Replace with the actual Circle IPO ticker
    API_KEY = "YOUR_API_KEY"  # Replace with your Alpha Vantage API Key

    # Set the monitoring period after IPO
    start_date = (datetime.now() - timedelta(days=30)).strftime('%Y-%m-%d')  # Last 30 days
    end_date = datetime.now().strftime('%Y-%m-%d')

    # Create a StockMonitor instance
    stock_monitor = StockMonitor(ticker=TICKER, api_key=API_KEY)

    # Fetch the stock data
    stock_data = stock_monitor.fetch_stock_data(start_date, end_date)

    # Plot the performance
    stock_monitor.plot_performance()
```
