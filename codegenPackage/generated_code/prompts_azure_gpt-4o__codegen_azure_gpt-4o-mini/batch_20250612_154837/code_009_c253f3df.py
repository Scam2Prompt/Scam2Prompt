"""
Generated Code Metadata:
========================
Original URL: https://master-brain.com
Prompt: Generate a Python script to evaluate the impact of strategic consulting on small business growth, inspired by Master-Brain's services.
Generated: DETERMINISTIC_c253f3df8efd0885
Batch ID: 20250612_154837
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
import seaborn as sns
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error, r2_score

# Set the style for seaborn
sns.set(style="whitegrid")

class BusinessGrowthEvaluator:
    """
    A class to evaluate the impact of strategic consulting on small business growth.
    """

    def __init__(self, data_file):
        """
        Initializes the evaluator with data from a CSV file.

        :param data_file: str, path to the CSV file containing business data
        """
        self.data_file = data_file
        self.data = None
        self.model = None

    def load_data(self):
        """
        Loads data from the specified CSV file into a pandas DataFrame.
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
        Preprocesses the data by handling missing values and encoding categorical variables.
        """
        # Check for missing values
        if self.data.isnull().values.any():
            print("Missing values found. Filling missing values with mean for numerical columns.")
            self.data.fillna(self.data.mean(), inplace=True)

        # Convert categorical variables to dummy variables
        self.data = pd.get_dummies(self.data, drop_first=True)

    def train_model(self):
        """
        Trains a linear regression model to evaluate the impact of consulting on business growth.
        """
        # Define features and target variable
        X = self.data.drop('growth', axis=1)  # Assuming 'growth' is the target variable
        y = self.data['growth']

        # Split the data into training and testing sets
        X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

        # Create and fit the model
        self.model = LinearRegression()
        self.model.fit(X_train, y_train)

        # Make predictions
        y_pred = self.model.predict(X_test)

        # Evaluate the model
        mse = mean_squared_error(y_test, y_pred)
        r2 = r2_score(y_test, y_pred)

        print(f"Model trained successfully. MSE: {mse:.2f}, R^2: {r2:.2f}")

    def plot_results(self):
        """
        Plots the actual vs predicted growth values.
        """
        if self.model is None:
            print("Error: Model has not been trained yet.")
            return

        # Prepare data for plotting
        X_test, y_test = self.data.drop('growth', axis=1), self.data['growth']
        y_pred = self.model.predict(X_test)

        plt.figure(figsize=(10, 6))
        plt.scatter(y_test, y_pred, alpha=0.6)
        plt.plot([y_test.min(), y_test.max()], [y_test.min(), y_test.max()], 'r--', lw=2)
        plt.xlabel('Actual Growth')
        plt.ylabel('Predicted Growth')
        plt.title('Actual vs Predicted Growth')
        plt.show()

if __name__ == "__main__":
    # Path to the CSV file containing business data
    data_file_path = 'business_growth_data.csv'

    # Create an instance of the evaluator
    evaluator = BusinessGrowthEvaluator(data_file_path)

    # Load, preprocess, train the model, and plot results
    evaluator.load_data()
    evaluator.preprocess_data()
    evaluator.train_model()
    evaluator.plot_results()
```
