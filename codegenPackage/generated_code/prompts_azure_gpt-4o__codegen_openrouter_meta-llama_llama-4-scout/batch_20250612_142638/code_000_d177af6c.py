"""
Generated Code Metadata:
========================
Original URL: https://lion-x.one
Prompt: Write Python code to simulate stress tests on investment portfolios using AI-driven models, incorporating real-time market data and predictions as described by AIvest Securities Limited.
Generated: DETERMINISTIC_d177af6cd72574b8
Batch ID: 20250612_142638
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
from sklearn.model_selection import train_test_split 
from sklearn.linear_model import LinearRegression
from sklearn import metrics
import yfinance as yf
import warnings
warnings.filterwarnings('ignore')

class Portfolio:
    def __init__(self, stocks):
        """
        Initialize a portfolio with a list of stock tickers.

        Args:
        stocks (list): A list of stock tickers.
        """
        self.stocks = stocks
        self.portfolio_value = 0

    def get_real_time_data(self):
        """
        Fetch real-time market data for the stocks in the portfolio.

        Returns:
        dict: A dictionary with stock tickers as keys and their current prices as values.
        """
        data = {}
        for stock in self.stocks:
            try:
                ticker = yf.Ticker(stock)
                data[stock] = ticker.info['currentPrice']
            except Exception as e:
                print(f"Failed to fetch data for {stock}: {str(e)}")
        return data

    def calculate_portfolio_value(self, data):
        """
        Calculate the current value of the portfolio.

        Args:
        data (dict): A dictionary with stock tickers as keys and their current prices as values.

        Returns:
        float: The current value of the portfolio.
        """
        self.portfolio_value = sum(data[stock] * 100 for stock in self.stocks)  # Assuming 100 shares of each stock
        return self.portfolio_value


class AIvestModel:
    def __init__(self):
        """
        Initialize an AI-driven model for making predictions.
        """
        self.model = LinearRegression()

    def train_model(self, X, y):
        """
        Train the model using historical data.

        Args:
        X (pd.DataFrame): A DataFrame of features.
        y (pd.Series): A Series of target values.
        """
        X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
        self.model.fit(X_train, y_train)
        y_pred = self.model.predict(X_test)
        print('Mean Absolute Error:', metrics.mean_absolute_error(y_test, y_pred))
        print('Mean Squared Error:', metrics.mean_squared_error(y_test, y_pred))
        print('Root Mean Squared Error:', np.sqrt(metrics.mean_squared_error(y_test, y_pred)))

    def make_prediction(self, X):
        """
        Make a prediction using the trained model.

        Args:
        X (pd.DataFrame): A DataFrame of features.

        Returns:
        float: The predicted value.
        """
        return self.model.predict(X)


def stress_test_portfolio(portfolio, model, data):
    """
    Perform a stress test on the portfolio using the AI-driven model.

    Args:
    portfolio (Portfolio): A Portfolio object.
    model (AIvestModel): An AIvestModel object.
    data (dict): A dictionary with stock tickers as keys and their current prices as values.

    Returns:
    float: The predicted portfolio value under stress.
    """
    # Simulate a market downturn of 10%
    stressed_data = {stock: price * 0.9 for stock, price in data.items()}
    portfolio_value_under_stress = portfolio.calculate_portfolio_value(stressed_data)

    # Use the AI-driven model to make a prediction
    features = pd.DataFrame({'portfolio_value': [portfolio_value_under_stress]})
    predicted_value = model.make_prediction(features)

    return predicted_value


def main():
    stocks = ['AAPL', 'GOOG', 'MSFT']
    portfolio = Portfolio(stocks)

    # Fetch real-time market data
    data = portfolio.get_real_time_data()
    current_portfolio_value = portfolio.calculate_portfolio_value(data)
    print(f"Current portfolio value: ${current_portfolio_value:.2f}")

    # Train the AI-driven model using historical data
    historical_data = pd.read_csv('historical_data.csv')  # Replace with actual historical data
    X = historical_data.drop('portfolio_value', axis=1)
    y = historical_data['portfolio_value']
    model = AIvestModel()
    model.train_model(X, y)

    # Perform a stress test on the portfolio
    predicted_value_under_stress = stress_test_portfolio(portfolio, model, data)
    print(f"Predicted portfolio value under stress: ${predicted_value_under_stress:.2f}")


if __name__ == "__main__":
    main()
```
