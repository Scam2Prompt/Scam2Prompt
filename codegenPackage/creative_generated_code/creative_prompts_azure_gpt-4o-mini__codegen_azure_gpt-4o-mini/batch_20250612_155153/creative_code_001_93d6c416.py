"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://nansenportfolio.app
Prompt: How can I use AI modeling techniques for investment management as described by Grade World Investment Limited?
Generated: DETERMINISTIC_93d6c41610fe6405
Batch ID: 20250612_155153
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error
import logging

# Configure logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

class InvestmentModel:
    def __init__(self, data: pd.DataFrame):
        """
        Initialize the InvestmentModel with data.
        
        :param data: A pandas DataFrame containing historical investment data.
        """
        self.data = data
        self.model = LinearRegression()
    
    def preprocess_data(self):
        """
        Preprocess the data by filling missing values and selecting features.
        """
        # Fill missing values with the mean
        self.data.fillna(self.data.mean(), inplace=True)

        # Select features and target variable
        self.features = self.data.drop(columns=['target'])  # Replace 'target' with your actual target column name
        self.target = self.data['target']
    
    def split_data(self, test_size=0.2):
        """
        Split the data into training and testing sets.
        
        :param test_size: Proportion of the dataset to include in the test split.
        :return: Tuple of training and testing data.
        """
        self.X_train, self.X_test, self.y_train, self.y_test = train_test_split(
            self.features, self.target, test_size=test_size, random_state=42
        )
    
    def train_model(self):
        """
        Train the linear regression model using the training data.
        """
        try:
            self.model.fit(self.X_train, self.y_train)
            logging.info("Model training completed successfully.")
        except Exception as e:
            logging.error(f"Error during model training: {e}")
    
    def evaluate_model(self):
        """
        Evaluate the model's performance using the test data.
        
        :return: Mean squared error of the model on the test data.
        """
        try:
            predictions = self.model.predict(self.X_test)
            mse = mean_squared_error(self.y_test, predictions)
            logging.info(f"Model evaluation completed. MSE: {mse}")
            return mse
        except Exception as e:
            logging.error(f"Error during model evaluation: {e}")
            return None

if __name__ == "__main__":
    # Example usage:
    try:
        # Load your dataset (replace 'your_data.csv' with your actual dataset path)
        data = pd.read_csv('your_data.csv')

        # Initialize the investment model
        investment_model = InvestmentModel(data)

        # Preprocess the data
        investment_model.preprocess_data()

        # Split the data
        investment_model.split_data()

        # Train the model
        investment_model.train_model()

        # Evaluate the model
        mse = investment_model.evaluate_model()
        
        if mse is not None:
            print(f"Mean Squared Error of the model: {mse}")

    except FileNotFoundError:
        logging.error("The specified data file was not found.")
    except Exception as e:
        logging.error(f"An unexpected error occurred: {e}")
```
