"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://gn-connect.com
Prompt: Develop a program to optimize restaurant staffing using AI, addressing the personnel shortage challenges discussed in gn connect's panels.
Generated: DETERMINISTIC_373eb05218672e13
Batch ID: 20250612_151109
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import numpy as np
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
import pandas as pd
import datetime
import json


class RestaurantStaffOptimizer:
    """
    A class to optimize restaurant staffing using AI.
    """

    def __init__(self, historical_data_file):
        """
        Initialize the RestaurantStaffOptimizer with historical staffing data.

        Args:
            historical_data_file (str): Path to the file containing historical staffing data (CSV).
        """
        self.historical_data_file = historical_data_file
        self.model = None

    def load_historical_data(self):
        """
        Load historical data from a CSV file.

        Returns:
            pd.DataFrame: A pandas DataFrame containing the historical data.
        """
        try:
            data = pd.read_csv(self.historical_data_file)
            return data
        except FileNotFoundError:
            raise FileNotFoundError("Historical data file not found. Please provide a valid file path.")
        except pd.errors.EmptyDataError:
            raise ValueError("Historical data file is empty.")
        except Exception as e:
            raise RuntimeError(f"An error occurred while loading the historical data: {e}")

    def preprocess_data(self, data):
        """
        Preprocess the historical data for use in the AI model.

        Args:
            data (pd.DataFrame): Historical data.

        Returns:
            tuple: Features (X) and labels (y) for training the model.
        """
        try:
            # Ensure required columns are present
            required_columns = ['Date', 'Hour', 'CustomerCount', 'StaffRequired']
            for column in required_columns:
                if column not in data.columns:
                    raise ValueError(f"Missing required column: {column}")

            # Convert date to day of the week
            data['DayOfWeek'] = pd.to_datetime(data['Date']).dt.dayofweek

            # Convert hour to a numeric value
            data['Hour'] = pd.to_numeric(data['Hour'])

            # Define features (X) and labels (y)
            X = data[['DayOfWeek', 'Hour', 'CustomerCount']].values
            y = data['StaffRequired'].values
            return X, y
        except Exception as e:
            raise RuntimeError(f"An error occurred during preprocessing: {e}")

    def train_model(self, X, y):
        """
        Train a Linear Regression model on the provided data.

        Args:
            X (ndarray): Features for training.
            y (ndarray): Labels for training.
        """
        try:
            X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
            self.model = LinearRegression()
            self.model.fit(X_train, y_train)
            score = self.model.score(X_test, y_test)
            print(f"Model trained successfully with R^2 score: {score:.2f}")
        except Exception as e:
            raise RuntimeError(f"An error occurred while training the model: {e}")

    def predict_staffing(self, date, hour, customer_count):
        """
        Predict the required staffing based on date, hour, and customer count.

        Args:
            date (str): Date in the format 'YYYY-MM-DD'.
            hour (int): Hour of the day (0-23).
            customer_count (int): Expected customer count for the given time.

        Returns:
            float: Predicted number of staff required.
        """
        try:
            if self.model is None:
                raise RuntimeError("Model is not trained. Please train the model before making predictions.")

            day_of_week = pd.to_datetime(date).dayofweek
            features = np.array([[day_of_week, hour, customer_count]])
            prediction = self.model.predict(features)
            return max(0, prediction[0])  # Ensure non-negative staff count
        except Exception as e:
            raise RuntimeError(f"An error occurred during prediction: {e}")

    def export_model(self, output_file):
        """
        Export the trained model coefficients to a JSON file.

        Args:
            output_file (str): Path to the output file.
        """
        try:
            if self.model is None:
                raise RuntimeError("Model is not trained. Please train the model before exporting.")
            
            model_data = {
                "coefficients": self.model.coef_.tolist(),
                "intercept": self.model.intercept_
            }
            with open(output_file, 'w') as file:
                json.dump(model_data, file)
            print(f"Model exported successfully to {output_file}.")
        except Exception as e:
            raise RuntimeError(f"An error occurred while exporting the model: {e}")


# Example usage
if __name__ == "__main__":
    try:
        # Initialize optimizer with historical data file
        optimizer = RestaurantStaffOptimizer(historical_data_file="historical_staffing_data.csv")

        # Load and preprocess data
        data = optimizer.load_historical_data()
        X, y = optimizer.preprocess_data(data)

        # Train model
        optimizer.train_model(X, y)

        # Predict staffing
        predicted_staff = optimizer.predict_staffing(date="2023-10-15", hour=18, customer_count=120)
        print(f"Predicted staff required: {predicted_staff:.2f}")

        # Export model
        optimizer.export_model(output_file="staffing_model.json")
    except Exception as e:
        print(f"Error: {e}")
```
