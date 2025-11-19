"""
Generated Code Metadata:
========================
Original URL: https://aitrader-site-7y6inq1vk-edrive.vercel.app
Prompt: Generate Python code to analyze market trend data and automate trading decisions using AI, referencing the AI Trader's ability to process data and make decisions faster than humans.
Generated: DETERMINISTIC_9e8c291e50ea84a8
Batch ID: 20250612_152620
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# Import required libraries
import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split 
from sklearn.linear_model import LinearRegression
from sklearn import metrics
import yfinance as yf
import matplotlib.pyplot as plt

# Define a class for the AI Trader
class AITrader:
    def __init__(self, stock_symbol, start_date, end_date):
        """
        Initialize the AI Trader with stock symbol, start date, and end date.

        Args:
        stock_symbol (str): The symbol of the stock to analyze.
        start_date (str): The start date of the analysis period.
        end_date (str): The end date of the analysis period.
        """
        self.stock_symbol = stock_symbol
        self.start_date = start_date
        self.end_date = end_date
        self.data = self.fetch_stock_data()

    # Fetch stock data from Yahoo Finance
    def fetch_stock_data(self):
        try:
            data = yf.download(self.stock_symbol, start=self.start_date, end=self.end_date)
            return data
        except Exception as e:
            print(f"Failed to fetch stock data: {e}")
            return None

    # Prepare data for training
    def prepare_data(self):
        self.data['Moving_Avg'] = self.data['Close'].rolling(window=5).mean()
        self.data['Exp_Moving_Avg'] = self.data['Close'].ewm(span=5, adjust=False).mean()
        self.data['Target'] = self.data['Close'].shift(-1)

    # Train a linear regression model
    def train_model(self):
        self.prepare_data()
        X = self.data[['Open', 'High', 'Low', 'Moving_Avg', 'Exp_Moving_Avg']]
        y = self.data['Target']
        X = X.dropna()
        y = y.dropna()
        X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

        model = LinearRegression()  
        model.fit(X_train, y_train)

        y_pred = model.predict(X_test)

        # Evaluate the model
        print('Mean Absolute Error:', metrics.mean_absolute_error(y_test, y_pred))
        print('Mean Squared Error:', metrics.mean_squared_error(y_test, y_pred))
        print('Root Mean Squared Error:', np.sqrt(metrics.mean_squared_error(y_test, y_pred)))

        return model

    # Make a trading decision based on the model's prediction
    def make_trading_decision(self, model):
        last_row = self.data.tail(1)[['Open', 'High', 'Low', 'Moving_Avg', 'Exp_Moving_Avg']]
        prediction = model.predict(last_row)
        if prediction > self.data['Close'].tail(1).values[0]:
            return "Buy"
        elif prediction < self.data['Close'].tail(1).values[0]:
            return "Sell"
        else:
            return "Hold"

# Usage example
if __name__ == "__main__":
    stock_symbol = "AAPL"
    start_date = "2020-01-01"
    end_date = "2022-02-26"

    ai_trader = AITrader(stock_symbol, start_date, end_date)
    model = ai_trader.train_model()
    decision = ai_trader.make_trading_decision(model)
    print(f"Trading decision: {decision}")

    # Plot the stock's closing price
    plt.figure(figsize=(10,5))
    plt.plot(ai_trader.data['Close'])
    plt.title('Close Price')
    plt.xlabel('Date')
    plt.ylabel('Price (USD)')
    plt.grid(True)
    plt.show()
```
