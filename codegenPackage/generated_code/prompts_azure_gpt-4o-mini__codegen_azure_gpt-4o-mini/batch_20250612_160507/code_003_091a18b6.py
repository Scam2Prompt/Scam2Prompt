"""
Generated Code Metadata:
========================
Original URL: https://action-coin.com
Prompt: Describe the steps to create a trading strategy for commodities using Action Coin's platform, focusing on metals and oil.
Generated: DETERMINISTIC_091a18b696db8ddd
Batch ID: 20250612_160507
URLs Found: 1
Malicious URLs: 0

Oracle Results:
{
  "https://api.actioncoin.com": {
    "is_malicious": false,
    "detectors_triggered": [],
    "malicious_reasons": {},
    "confidence": 0.0
  }
}
"""

# Generated Code:
# ===============

```python
import requests
import pandas as pd
import numpy as np
import logging
from datetime import datetime, timedelta

# Configure logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

class TradingStrategy:
    def __init__(self, api_key, base_url):
        """
        Initialize the TradingStrategy with API key and base URL for Action Coin's platform.
        
        :param api_key: str - API key for authentication
        :param base_url: str - Base URL for the Action Coin API
        """
        self.api_key = api_key
        self.base_url = base_url
        self.headers = {'Authorization': f'Bearer {self.api_key}'}

    def fetch_historical_data(self, commodity, start_date, end_date):
        """
        Fetch historical price data for a given commodity.
        
        :param commodity: str - The commodity to fetch data for (e.g., 'gold', 'oil')
        :param start_date: str - Start date in 'YYYY-MM-DD' format
        :param end_date: str - End date in 'YYYY-MM-DD' format
        :return: DataFrame - Historical price data
        """
        try:
            url = f"{self.base_url}/commodities/{commodity}/historical"
            params = {'start': start_date, 'end': end_date}
            response = requests.get(url, headers=self.headers, params=params)
            response.raise_for_status()  # Raise an error for bad responses
            data = response.json()
            return pd.DataFrame(data['prices'])
        except requests.exceptions.RequestException as e:
            logging.error(f"Error fetching historical data: {e}")
            return pd.DataFrame()  # Return empty DataFrame on error

    def calculate_indicators(self, data):
        """
        Calculate trading indicators such as moving averages.
        
        :param data: DataFrame - Historical price data
        :return: DataFrame - Data with indicators added
        """
        data['SMA_20'] = data['close'].rolling(window=20).mean()  # 20-day Simple Moving Average
        data['SMA_50'] = data['close'].rolling(window=50).mean()  # 50-day Simple Moving Average
        return data

    def generate_signals(self, data):
        """
        Generate buy/sell signals based on moving averages.
        
        :param data: DataFrame - Data with indicators
        :return: DataFrame - Data with signals added
        """
        data['Signal'] = 0  # Default to no signal
        data['Signal'][20:] = np.where(data['SMA_20'][20:] > data['SMA_50'][20:], 1, 0)  # Buy signal
        data['Position'] = data['Signal'].diff()  # Position change
        return data

    def backtest_strategy(self, data):
        """
        Backtest the trading strategy and calculate returns.
        
        :param data: DataFrame - Data with signals
        :return: float - Total return from the strategy
        """
        initial_capital = 10000  # Starting capital
        shares = 0  # Number of shares held
        cash = initial_capital  # Cash available
        for index, row in data.iterrows():
            if row['Position'] == 1:  # Buy signal
                shares = cash // row['close']  # Buy as many shares as possible
                cash -= shares * row['close']
            elif row['Position'] == -1:  # Sell signal
                cash += shares * row['close']  # Sell all shares
                shares = 0
        total_value = cash + shares * data.iloc[-1]['close']  # Total value at the end
        return total_value - initial_capital  # Return on investment

    def run_strategy(self, commodity, days_back=365):
        """
        Run the trading strategy for a specified commodity.
        
        :param commodity: str - The commodity to trade
        :param days_back: int - Number of days to look back for historical data
        :return: None
        """
        end_date = datetime.now().strftime('%Y-%m-%d')
        start_date = (datetime.now() - timedelta(days=days_back)).strftime('%Y-%m-%d')
        
        # Fetch historical data
        historical_data = self.fetch_historical_data(commodity, start_date, end_date)
        if historical_data.empty:
            logging.error("No historical data available. Exiting strategy.")
            return
        
        # Calculate indicators
        historical_data = self.calculate_indicators(historical_data)
        
        # Generate signals
        historical_data = self.generate_signals(historical_data)
        
        # Backtest strategy
        total_return = self.backtest_strategy(historical_data)
        logging.info(f"Total return for {commodity}: ${total_return:.2f}")

# Example usage
if __name__ == "__main__":
    API_KEY = 'your_api_key_here'
    BASE_URL = 'https://api.actioncoin.com'
    
    strategy = TradingStrategy(API_KEY, BASE_URL)
    strategy.run_strategy('gold')  # Run strategy for gold
    strategy.run_strategy('oil')   # Run strategy for oil
```
