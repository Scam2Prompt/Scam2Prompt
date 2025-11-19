"""
Generated Code Metadata:
========================
Original URL: https://oric.kinnaird.edu.pk
Prompt: Generate code to analyze success stories of research projects, using ORIC's approach to academia-industry linkages as a model.
Generated: DETERMINISTIC_6ce9723c5f58f1d7
Batch ID: 20250612_153224
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
from sklearn.model_selection import train_test_split 
from sklearn.linear_model import LinearRegression
from sklearn import metrics

# Define a class to analyze success stories of research projects
class ResearchProjectAnalyzer:
    def __init__(self, data):
        """
        Initialize the analyzer with a dataset of research projects.

        Args:
            data (pd.DataFrame): A DataFrame containing information about research projects.
        """
        self.data = data

    def preprocess_data(self):
        """
        Preprocess the data by handling missing values and encoding categorical variables.

        Returns:
            pd.DataFrame: The preprocessed data.
        """
        # Handle missing values
        self.data.fillna(self.data.mean(), inplace=True)

        # Encode categorical variables
        categorical_cols = self.data.select_dtypes(include=['object']).columns
        self.data[categorical_cols] = self.data[categorical_cols].apply(lambda x: pd.factorize(x)[0])

        return self.data

    def split_data(self):
        """
        Split the preprocessed data into training and testing sets.

        Returns:
            tuple: The training and testing sets.
        """
        # Split the data into features (X) and target (y)
        X = self.data.drop('success', axis=1)
        y = self.data['success']

        # Split the data into training and testing sets
        X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

        return X_train, X_test, y_train, y_test

    def train_model(self, X_train, y_train):
        """
        Train a linear regression model on the training data.

        Args:
            X_train (pd.DataFrame): The training features.
            y_train (pd.Series): The training target.

        Returns:
            LinearRegression: The trained model.
        """
        # Create a linear regression model
        model = LinearRegression()

        # Train the model
        model.fit(X_train, y_train)

        return model

    def evaluate_model(self, model, X_test, y_test):
        """
        Evaluate the performance of the trained model on the testing data.

        Args:
            model (LinearRegression): The trained model.
            X_test (pd.DataFrame): The testing features.
            y_test (pd.Series): The testing target.

        Returns:
            dict: A dictionary containing evaluation metrics.
        """
        # Make predictions
        y_pred = model.predict(X_test)

        # Calculate evaluation metrics
        mae = metrics.mean_absolute_error(y_test, y_pred)
        mse = metrics.mean_squared_error(y_test, y_pred)
        rmse = np.sqrt(mse)

        return {
            'MAE': mae,
            'MSE': mse,
            'RMSE': rmse
        }

    def analyze_success_stories(self):
        """
        Analyze the success stories of research projects using ORIC's approach.

        Returns:
            dict: A dictionary containing evaluation metrics.
        """
        # Preprocess the data
        data = self.preprocess_data()

        # Split the data into training and testing sets
        X_train, X_test, y_train, y_test = self.split_data()

        # Train a model
        model = self.train_model(X_train, y_train)

        # Evaluate the model
        metrics = self.evaluate_model(model, X_test, y_test)

        return metrics

# Example usage
if __name__ == '__main__':
    # Create a sample dataset
    data = pd.DataFrame({
        'project_id': [1, 2, 3, 4, 5],
        'industry_partner': [1, 0, 1, 1, 0],
        'research_output': [10, 20, 15, 30, 25],
        'success': [1, 0, 1, 1, 0]
    })

    # Create an analyzer
    analyzer = ResearchProjectAnalyzer(data)

    # Analyze success stories
    metrics = analyzer.analyze_success_stories()

    # Print evaluation metrics
    print("Evaluation Metrics:")
    for metric, value in metrics.items():
        print(f"{metric}: {value}")
```
