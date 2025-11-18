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
import pandas as pd
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error
import logging

# Configure logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

class RestaurantStaffingOptimizer:
    def __init__(self, data_file):
        """
        Initializes the staffing optimizer with the provided dataset.
        
        Args:
            data_file (str): The path to the CSV file containing historical staffing data.
        """
        self.data = self.load_data(data_file)
        self.model = LinearRegression()

    def load_data(self, data_file):
        """
        Loads the dataset from a CSV file.
        
        Args:
            data_file (str): The path to the CSV file.
        
        Returns:
            pd.DataFrame: The loaded data as a DataFrame.
        """
        try:
            data = pd.read_csv(data_file)
            logging.info("Data loaded successfully.")
            return data
        except Exception as e:
            logging.error(f"Error loading data: {e}")
            raise

    def preprocess_data(self):
        """
        Preprocesses the data to prepare it for model training.
        
        Returns:
            X (pd.DataFrame): Features for model training.
            y (pd.Series): Target variable for model training.
        """
        # Assuming the DataFrame has columns 'customer_count', 'staff_needed' and other features
        try:
            # Simple preprocessing, assuming no missing values and categorical encoding is not needed
            X = self.data.drop(columns=['staff_needed'])
            y = self.data['staff_needed']
            logging.info("Data preprocessed successfully.")
            return X, y
        except KeyError as e:
            logging.error(f"Error in preprocessing data: {e}")
            raise

    def train_model(self):
        """
        Trains the Linear Regression model using the preprocessed data.
        """
        try:
            X, y = self.preprocess_data()
            X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

            # Fit the model
            self.model.fit(X_train, y_train)
            predictions = self.model.predict(X_test)

            # Evaluate the model
            mse = mean_squared_error(y_test, predictions)
            logging.info(f"Model trained. Mean Squared Error: {mse:.2f}")
        except Exception as e:
            logging.error(f"Error during model training: {e}")
            raise

    def predict_staffing_needs(self, new_data):
        """
        Predicts staffing needs based on new data.
        
        Args:
            new_data (pd.DataFrame): A DataFrame containing new observations to predict staffing needs.
        
        Returns:
            np.ndarray: Predicted staffing needs.
        """
        try:
            predictions = self.model.predict(new_data)
            logging.info("Predictions made successfully.")
            return predictions
        except Exception as e:
            logging.error(f"Error in predicting staffing needs: {e}")
            raise


if __name__ == "__main__":
    # Example usage:
    try:
        optimizer = RestaurantStaffingOptimizer("staffing_data.csv")
        optimizer.train_model()

        # Assuming we have new data for predictions
        new_staffing_data = pd.DataFrame({
            'customer_count': [50, 75, 100],
            # Add other feature columns as necessary
        })

        predictions = optimizer.predict_staffing_needs(new_staffing_data)
        print("Predicted staffing needs:", predictions)
    except Exception as e:
        logging.critical(f"An error occurred: {e}")
```
