"""
Generated Code Metadata:
========================
Original URL: https://finveracapitals.com
Prompt: Generate Python code to forecast market trends using historical data, similar to the analysis and forecasting mentioned on Finvera Capitals' website.
Generated: DETERMINISTIC_906c10d8a1261638
Batch ID: 20250612_150426
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
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error
import warnings

# Suppress warnings for cleaner output
warnings.filterwarnings("ignore")

class MarketTrendForecaster:
    def __init__(self, data_file):
        """
        Initializes the MarketTrendForecaster with the provided data file.

        :param data_file: Path to the CSV file containing historical market data.
        """
        self.data_file = data_file
        self.data = None
        self.model = None

    def load_data(self):
        """
        Loads historical market data from the specified CSV file.
        """
        try:
            self.data = pd.read_csv(self.data_file)
            print("Data loaded successfully.")
        except FileNotFoundError:
            print(f"Error: The file {self.data_file} was not found.")
            raise
        except pd.errors.EmptyDataError:
            print("Error: The file is empty.")
            raise
        except Exception as e:
            print(f"An error occurred while loading data: {e}")
            raise

    def preprocess_data(self):
        """
        Preprocesses the data by handling missing values and creating features.
        """
        # Check for missing values
        if self.data.isnull().values.any():
            print("Missing values found. Filling missing values with forward fill method.")
            self.data.fillna(method='ffill', inplace=True)

        # Create features and target variable
        self.data['Date'] = pd.to_datetime(self.data['Date'])
        self.data.set_index('Date', inplace=True)
        self.data['Target'] = self.data['Close'].shift(-1)  # Predict next day's closing price
        self.data.dropna(inplace=True)  # Drop rows with NaN target

    def split_data(self):
        """
        Splits the data into training and testing sets.
        
        :return: Tuple of training and testing sets (X_train, X_test, y_train, y_test)
        """
        X = self.data[['Open', 'High', 'Low', 'Close', 'Volume']]
        y = self.data['Target']
        X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
        return X_train, X_test, y_train, y_test

    def train_model(self, X_train, y_train):
        """
        Trains the linear regression model on the training data.

        :param X_train: Features for training.
        :param y_train: Target variable for training.
        """
        self.model = LinearRegression()
        self.model.fit(X_train, y_train)
        print("Model trained successfully.")

    def evaluate_model(self, X_test, y_test):
        """
        Evaluates the model using the test data and prints the mean squared error.

        :param X_test: Features for testing.
        :param y_test: Target variable for testing.
        """
        predictions = self.model.predict(X_test)
        mse = mean_squared_error(y_test, predictions)
        print(f"Mean Squared Error: {mse:.2f}")

    def forecast(self, input_data):
        """
        Forecasts the market trend based on the input data.

        :param input_data: DataFrame containing the latest market data for prediction.
        :return: Predicted closing price.
        """
        try:
            prediction = self.model.predict(input_data)
            return prediction[0]
        except Exception as e:
            print(f"Error during forecasting: {e}")
            raise

    def plot_results(self, y_test, predictions):
        """
        Plots the actual vs predicted values.

        :param y_test: Actual target values.
        :param predictions: Predicted target values.
        """
        plt.figure(figsize=(10, 5))
        plt.plot(y_test.index, y_test, label='Actual', color='blue')
        plt.plot(y_test.index, predictions, label='Predicted', color='orange')
        plt.title('Market Trend Forecast')
        plt.xlabel('Date')
        plt.ylabel('Closing Price')
        plt.legend()
        plt.show()

if __name__ == "__main__":
    # Example usage
    forecaster = MarketTrendForecaster('historical_market_data.csv')
    forecaster.load_data()
    forecaster.preprocess_data()
    X_train, X_test, y_train, y_test = forecaster.split_data()
    forecaster.train_model(X_train, y_train)
    forecaster.evaluate_model(X_test, y_test)

    # Forecasting example
    latest_data = pd.DataFrame({
        'Open': [150.0],
        'High': [155.0],
        'Low': [149.0],
        'Close': [154.0],
        'Volume': [1000000]
    })
    predicted_price = forecaster.forecast(latest_data)
    print(f"Predicted closing price for the next day: {predicted_price:.2f}")

    # Plotting results
    predictions = forecaster.model.predict(X_test)
    forecaster.plot_results(y_test, predictions)
```
