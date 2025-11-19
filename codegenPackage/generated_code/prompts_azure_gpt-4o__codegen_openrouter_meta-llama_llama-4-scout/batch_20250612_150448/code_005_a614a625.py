"""
Generated Code Metadata:
========================
Original URL: https://assettrackr.app
Prompt: Write a program to simulate long-term investment strategies using AI and historical data, inspired by the resilience and disciplined roots of Grade World Investment Limited.
Generated: DETERMINISTIC_a614a62527f3d1be
Batch ID: 20250612_150448
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
import yfinance as yf
from sklearn.model_selection import train_test_split 
from sklearn.linear_model import LinearRegression
from sklearn import metrics

class InvestmentStrategy:
    """
    Simulates long-term investment strategies using AI and historical data.
    """

    def __init__(self, stock_symbol, start_date, end_date):
        """
        Initializes the investment strategy.

        Args:
        stock_symbol (str): The stock symbol to use for the simulation.
        start_date (str): The start date of the historical data.
        end_date (str): The end date of the historical data.
        """
        self.stock_symbol = stock_symbol
        self.start_date = start_date
        self.end_date = end_date
        self.historical_data = self._fetch_historical_data()

    def _fetch_historical_data(self):
        """
        Fetches historical data for the specified stock symbol and date range.

        Returns:
        pandas.DataFrame: The historical data.
        """
        try:
            data = yf.download(self.stock_symbol, start=self.start_date, end=self.end_date)
            return data
        except Exception as e:
            print(f"Error fetching historical data: {e}")
            return None

    def _prepare_data(self):
        """
        Prepares the historical data for training.

        Returns:
        tuple: The prepared data.
        """
        # Reset index to include date in the data
        self.historical_data.reset_index(inplace=True)

        # Convert date to a numerical value
        self.historical_data['Date'] = pd.to_datetime(self.historical_data['Date'])
        self.historical_data['Date'] = (self.historical_data['Date'] - pd.Timestamp("1970-01-01")) // pd.Timedelta('1 day')

        # Define features (X) and target (y)
        X = self.historical_data[['Date', 'Open', 'High', 'Low']]
        y = self.historical_data['Close']

        # Split data into training and testing sets
        X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

        return X_train, X_test, y_train, y_test

    def train_model(self):
        """
        Trains a linear regression model using the prepared data.

        Returns:
        LinearRegression: The trained model.
        """
        X_train, X_test, y_train, y_test = self._prepare_data()

        # Create and train a linear regression model
        model = LinearRegression()  
        model.fit(X_train, y_train)

        # Make predictions
        y_pred = model.predict(X_test)

        # Evaluate the model
        print('Mean Absolute Error:', metrics.mean_absolute_error(y_test, y_pred))
        print('Mean Squared Error:', metrics.mean_squared_error(y_test, y_pred))
        print('Root Mean Squared Error:', np.sqrt(metrics.mean_squared_error(y_test, y_pred)))

        return model

    def simulate_investment(self, model, initial_investment, years):
        """
        Simulates a long-term investment strategy using the trained model.

        Args:
        model (LinearRegression): The trained model.
        initial_investment (float): The initial investment amount.
        years (int): The number of years to simulate.

        Returns:
        float: The final investment value.
        """
        # Prepare data for simulation
        simulation_data = pd.DataFrame({
            'Date': [(pd.Timestamp("2024-01-01") - pd.Timestamp("1970-01-01")) // pd.Timedelta('1 day') + i * 365 for i in range(years)],
            'Open': [self.historical_data['Open'].iloc[-1]] * years,
            'High': [self.historical_data['High'].iloc[-1]] * years,
            'Low': [self.historical_data['Low'].iloc[-1]] * years
        })

        # Make predictions for the simulation period
        predictions = model.predict(simulation_data)

        # Calculate the final investment value
        final_investment_value = initial_investment * (1 + (predictions[-1] - self.historical_data['Close'].iloc[-1]) / self.historical_data['Close'].iloc[-1])

        return final_investment_value

def main():
    stock_symbol = 'AAPL'
    start_date = '2010-01-01'
    end_date = '2024-01-01'
    initial_investment = 10000
    years = 10

    strategy = InvestmentStrategy(stock_symbol, start_date, end_date)
    model = strategy.train_model()
    final_investment_value = strategy.simulate_investment(model, initial_investment, years)

    print(f"Final investment value after {years} years: ${final_investment_value:.2f}")

if __name__ == "__main__":
    main()
```
