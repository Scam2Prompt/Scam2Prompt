"""
Generated Code Metadata:
========================
Original URL: https://strki.com
Prompt: Design a revenue management system for short-term rentals that incorporates data-driven strategies, similar to those offered by strki.com.
Generated: DETERMINISTIC_feb47c6635146df8
Batch ID: 20250622_205139
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
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error
import logging

# Configure logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

class RevenueManagementSystem:
    def __init__(self, data_file):
        """
        Initializes the Revenue Management System with the provided data file.

        :param data_file: Path to the CSV file containing rental data.
        """
        self.data_file = data_file
        self.data = None
        self.model = None

    def load_data(self):
        """
        Loads rental data from a CSV file and performs basic preprocessing.
        """
        try:
            self.data = pd.read_csv(self.data_file)
            logging.info("Data loaded successfully.")
            self.preprocess_data()
        except FileNotFoundError:
            logging.error("The specified data file was not found.")
            raise
        except pd.errors.EmptyDataError:
            logging.error("The data file is empty.")
            raise
        except Exception as e:
            logging.error(f"An error occurred while loading data: {e}")
            raise

    def preprocess_data(self):
        """
        Preprocesses the data by handling missing values and encoding categorical variables.
        """
        # Fill missing values with the median for numerical columns
        self.data.fillna(self.data.median(), inplace=True)

        # Convert categorical variables to dummy/indicator variables
        self.data = pd.get_dummies(self.data, drop_first=True)
        logging.info("Data preprocessing completed.")

    def train_model(self):
        """
        Trains a linear regression model to predict rental prices based on historical data.
        """
        try:
            # Define features and target variable
            X = self.data.drop('price', axis=1)
            y = self.data['price']

            # Split the data into training and testing sets
            X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

            # Create and train the model
            self.model = LinearRegression()
            self.model.fit(X_train, y_train)

            # Evaluate the model
            predictions = self.model.predict(X_test)
            mse = mean_squared_error(y_test, predictions)
            logging.info(f"Model trained successfully with MSE: {mse:.2f}")
        except Exception as e:
            logging.error(f"An error occurred while training the model: {e}")
            raise

    def predict_price(self, input_data):
        """
        Predicts the rental price based on input features.

        :param input_data: A dictionary containing the features for prediction.
        :return: Predicted rental price.
        """
        try:
            input_df = pd.DataFrame([input_data])
            input_df = pd.get_dummies(input_df).reindex(columns=self.data.columns.drop('price'), fill_value=0)
            predicted_price = self.model.predict(input_df)
            return predicted_price[0]
        except Exception as e:
            logging.error(f"An error occurred during price prediction: {e}")
            raise

if __name__ == "__main__":
    # Example usage
    rms = RevenueManagementSystem('rental_data.csv')
    rms.load_data()
    rms.train_model()

    # Example input for prediction
    example_input = {
        'bedrooms': 2,
        'bathrooms': 1,
        'location': 'Downtown',
        'amenities': 'WiFi,Kitchen',
        # Add other necessary features based on the dataset
    }

    try:
        predicted_price = rms.predict_price(example_input)
        logging.info(f"Predicted rental price: ${predicted_price:.2f}")
    except Exception as e:
        logging.error(f"Failed to predict price: {e}")
```
