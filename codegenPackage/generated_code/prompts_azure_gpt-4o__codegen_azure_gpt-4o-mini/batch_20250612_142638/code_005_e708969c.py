"""
Generated Code Metadata:
========================
Original URL: https://lion-x.name
Prompt: Write a program to simulate AI-driven predictions for investment performance under different market conditions, incorporating stress testing as highlighted by AIvest Securities Limited.
Generated: DETERMINISTIC_e708969c47547062
Batch ID: 20250612_142638
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error

class InvestmentPredictor:
    """
    A class to simulate AI-driven predictions for investment performance
    under different market conditions, incorporating stress testing.
    """

    def __init__(self, data):
        """
        Initializes the InvestmentPredictor with historical market data.

        :param data: A pandas DataFrame containing historical market data
        """
        self.data = data
        self.model = LinearRegression()

    def preprocess_data(self):
        """
        Preprocess the data by handling missing values and normalizing features.
        """
        # Fill missing values with the mean of the column
        self.data.fillna(self.data.mean(), inplace=True)

        # Normalize the data
        self.data = (self.data - self.data.mean()) / self.data.std()

    def train_model(self):
        """
        Trains the linear regression model on the historical data.
        """
        # Define features and target variable
        X = self.data.drop(columns=['investment_performance'])
        y = self.data['investment_performance']

        # Split the data into training and testing sets
        X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

        # Fit the model
        self.model.fit(X_train, y_train)

        # Predict and evaluate the model
        predictions = self.model.predict(X_test)
        mse = mean_squared_error(y_test, predictions)
        print(f'Model Mean Squared Error: {mse:.2f}')

    def predict_performance(self, market_conditions):
        """
        Predicts investment performance based on given market conditions.

        :param market_conditions: A dictionary of market conditions
        :return: Predicted investment performance
        """
        try:
            # Convert market conditions to DataFrame
            input_data = pd.DataFrame([market_conditions])
            normalized_input = (input_data - self.data.mean()) / self.data.std()

            # Make prediction
            prediction = self.model.predict(normalized_input)
            return prediction[0]
        except Exception as e:
            print(f"Error in predicting performance: {e}")
            return None

    def stress_test(self, stress_conditions):
        """
        Simulates stress testing by predicting performance under extreme market conditions.

        :param stress_conditions: A list of dictionaries representing extreme market conditions
        :return: List of predicted performances under stress conditions
        """
        results = []
        for conditions in stress_conditions:
            prediction = self.predict_performance(conditions)
            results.append(prediction)
        return results

# Example usage
if __name__ == "__main__":
    # Load historical market data (replace with actual data source)
    try:
        historical_data = pd.read_csv('historical_market_data.csv')
    except FileNotFoundError:
        print("Historical market data file not found.")
        exit(1)

    # Initialize the InvestmentPredictor
    predictor = InvestmentPredictor(historical_data)

    # Preprocess the data
    predictor.preprocess_data()

    # Train the model
    predictor.train_model()

    # Define market conditions for prediction
    market_conditions = {
        'interest_rate': 0.05,
        'inflation_rate': 0.02,
        'GDP_growth': 0.03,
        'unemployment_rate': 0.04
    }

    # Predict investment performance
    predicted_performance = predictor.predict_performance(market_conditions)
    print(f'Predicted Investment Performance: {predicted_performance:.2f}')

    # Define stress test conditions
    stress_conditions = [
        {'interest_rate': 0.1, 'inflation_rate': 0.05, 'GDP_growth': -0.02, 'unemployment_rate': 0.1},
        {'interest_rate': 0.15, 'inflation_rate': 0.07, 'GDP_growth': -0.05, 'unemployment_rate': 0.15}
    ]

    # Perform stress testing
    stress_test_results = predictor.stress_test(stress_conditions)
    for i, result in enumerate(stress_test_results):
        print(f'Stress Test {i + 1} Prediction: {result:.2f}')
```
