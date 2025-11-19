"""
Generated Code Metadata:
========================
Original URL: https://generalearnings.com
Prompt: Design a system to manage risk and ensure satisfactory returns for investors, similar to General Earnings' risk management approach.
Generated: DETERMINISTIC_a2d8d26ce82fe39d
Batch ID: 20250622_212015
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
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import classification_report, confusion_matrix
import logging

# Configure logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

class RiskManagementSystem:
    def __init__(self, data):
        """
        Initializes the Risk Management System with the provided dataset.

        :param data: A pandas DataFrame containing historical investment data.
        """
        self.data = data
        self.model = None

    def preprocess_data(self):
        """
        Preprocess the data by handling missing values and encoding categorical variables.
        """
        logging.info("Starting data preprocessing...")
        # Fill missing values with the mean for numerical columns
        self.data.fillna(self.data.mean(), inplace=True)

        # Convert categorical variables to dummy variables
        self.data = pd.get_dummies(self.data, drop_first=True)
        logging.info("Data preprocessing completed.")

    def split_data(self, target_column):
        """
        Splits the data into training and testing sets.

        :param target_column: The name of the target column for prediction.
        :return: Tuple of training and testing data.
        """
        logging.info("Splitting data into training and testing sets...")
        X = self.data.drop(target_column, axis=1)
        y = self.data[target_column]
        X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
        logging.info("Data split completed.")
        return X_train, X_test, y_train, y_test

    def train_model(self, X_train, y_train):
        """
        Trains a Random Forest Classifier on the training data.

        :param X_train: Features for training.
        :param y_train: Target variable for training.
        """
        logging.info("Training the model...")
        self.model = RandomForestClassifier(n_estimators=100, random_state=42)
        self.model.fit(X_train, y_train)
        logging.info("Model training completed.")

    def evaluate_model(self, X_test, y_test):
        """
        Evaluates the trained model on the test data.

        :param X_test: Features for testing.
        :param y_test: Target variable for testing.
        """
        logging.info("Evaluating the model...")
        predictions = self.model.predict(X_test)
        logging.info("Model evaluation completed.")
        print(confusion_matrix(y_test, predictions))
        print(classification_report(y_test, predictions))

    def run(self, target_column):
        """
        Executes the risk management system workflow.

        :param target_column: The name of the target column for prediction.
        """
        try:
            self.preprocess_data()
            X_train, X_test, y_train, y_test = self.split_data(target_column)
            self.train_model(X_train, y_train)
            self.evaluate_model(X_test, y_test)
        except Exception as e:
            logging.error(f"An error occurred: {e}")

# Example usage
if __name__ == "__main__":
    # Load your dataset here
    # For demonstration, we will create a dummy DataFrame
    data = pd.DataFrame({
        'investment_amount': np.random.rand(100) * 10000,
        'risk_factor': np.random.choice(['low', 'medium', 'high'], 100),
        'return': np.random.choice([0, 1], 100)  # 0 = loss, 1 = gain
    })

    # Initialize the risk management system
    rms = RiskManagementSystem(data)

    # Run the system with 'return' as the target column
    rms.run(target_column='return')
```
