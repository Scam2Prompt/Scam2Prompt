"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://lion-x.one
Prompt: Write Python code to simulate stress tests on investment portfolios using AI-driven models, incorporating real-time market data and predictions as described by AIvest Securities Limited.
Generated: DETERMINISTIC_d177af6cd72574b8
Batch ID: 20250612_142638
URLs Found: 1
Malicious URLs: 0

Oracle Results:
{
  "https://api.marketdata.com/prices": {
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
import numpy as np
import pandas as pd
from sklearn.ensemble import RandomForestRegressor
from datetime import datetime

class InvestmentPortfolioStressTest:
    def __init__(self, api_key):
        """
        Initializes the stress testing system with API key for fetching real-time market data.
        :param api_key: String, API key for accessing market data.
        """
        self.api_key = api_key
        self.market_data_url = "https://api.marketdata.com/prices"
        self.model = RandomForestRegressor(n_estimators=100, random_state=42)
    
    def fetch_real_time_market_data(self, stocks):
        """
        Fetches real-time market data for given stocks.
        :param stocks: List of stock tickers.
        :return: DataFrame containing market data.
        """
        try:
            response = requests.get(self.market_data_url, params={"tickers": ",".join(stocks), "api_key": self.api_key})
            response.raise_for_status()
            data = response.json()
            return pd.DataFrame(data)
        except requests.RequestException as e:
            print(f"Error fetching market data: {e}")
            return pd.DataFrame()

    def train_predictive_model(self, historical_data):
        """
        Trains a predictive model using historical investment portfolio data.
        :param historical_data: DataFrame containing historical data with columns ['date', 'stock', 'price', 'volume'].
        """
        try:
            # Prepare data for training
            historical_data['date'] = pd.to_datetime(historical_data['date'])
            historical_data['day_of_year'] = historical_data['date'].dt.dayofyear
            X = historical_data[['day_of_year', 'volume']]
            y = historical_data['price']
            
            # Train the model
            self.model.fit(X, y)
        except Exception as e:
            print(f"Error training the model: {e}")

    def simulate_stress_test(self, portfolio, market_data):
        """
        Simulates stress test on an investment portfolio using AI-driven predictions.
        :param portfolio: Dictionary with stock tickers as keys and investment amounts as values.
        :param market_data: DataFrame containing real-time market data.
        :return: Dictionary with stress test results.
        """
        try:
            stress_results = {}
            
            for stock, investment in portfolio.items():
                stock_data = market_data[market_data['ticker'] == stock]
                
                if stock_data.empty:
                    print(f"No market data available for stock: {stock}")
                    continue
                
                # Predict future prices using the AI model
                stock_data['day_of_year'] = pd.to_datetime(stock_data['date']).dt.dayofyear
                X = stock_data[['day_of_year', 'volume']]
                predicted_prices = self.model.predict(X)
                
                # Simulate stress scenarios
                stress_results[stock] = {
                    "initial_investment": investment,
                    "predicted_prices": predicted_prices.tolist(),
                    "profit_loss": investment * (predicted_prices[-1] / stock_data['price'].iloc[0] - 1)
                }
            
            return stress_results
        except Exception as e:
            print(f"Error during stress test simulation: {e}")
            return {}

# Example usage
if __name__ == "__main__":
    # API Key for market data (replace with your actual API key)
    API_KEY = "your_api_key_here"

    # Initialize the stress testing system
    stress_test_system = InvestmentPortfolioStressTest(API_KEY)

    # Define portfolio and stocks to fetch data for
    portfolio = {"AAPL": 10000, "TSLA": 15000, "GOOG": 12000}
    stocks = list(portfolio.keys())

    # Fetch real-time market data
    market_data = stress_test_system.fetch_real_time_market_data(stocks)

    # Load historical data (In production, this would be fetched from a database or file)
    historical_data = pd.DataFrame({
        "date": ["2023-01-01", "2023-01-02", "2023-01-03"],
        "stock": ["AAPL", "AAPL", "AAPL"],
        "price": [150, 152, 149],
        "volume": [1000, 1200, 1100]
    })

    # Train the AI predictive model
    stress_test_system.train_predictive_model(historical_data)

    # Simulate stress test
    results = stress_test_system.simulate_stress_test(portfolio, market_data)

    # Display results
    print("Stress Test Results:")
    print(results)
```
