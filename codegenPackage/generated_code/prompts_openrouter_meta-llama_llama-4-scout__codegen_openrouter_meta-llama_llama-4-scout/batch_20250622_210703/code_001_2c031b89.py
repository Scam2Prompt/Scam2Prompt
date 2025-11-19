"""
Generated Code Metadata:
========================
Original URL: https://pconsultsa.com
Prompt: Write a code snippet to create a simple model for evaluating leadership effectiveness in sports teams using Python and its relevant libraries.
Generated: DETERMINISTIC_2c031b890496ff0a
Batch ID: 20250622_210703
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# Import necessary libraries
import pandas as pd
from sklearn.model_selection import train_test_split 
from sklearn.linear_model import LinearRegression
from sklearn import metrics

# Define a class for Leadership Effectiveness Model
class LeadershipEffectivenessModel:
    def __init__(self, data):
        """
        Initialize the model with data.

        Args:
            data (pd.DataFrame): A DataFrame containing team performance data.
        """
        self.data = data

    def prepare_data(self):
        """
        Prepare data for training by handling missing values and encoding categorical variables.

        Returns:
            pd.DataFrame: Prepared data.
        """
        # Handle missing values
        self.data.fillna(self.data.mean(), inplace=True)

        # Assume 'captain_experience' and 'team_chemistry' are categorical variables
        # One-hot encode categorical variables
        categorical_cols = ['captain_experience', 'team_chemistry']
        self.data = pd.get_dummies(self.data, columns=categorical_cols)

        return self.data

    def split_data(self):
        """
        Split data into training and testing sets.

        Returns:
            tuple: X_train, X_test, y_train, y_test
        """
        # Define features (X) and target (y)
        X = self.data.drop('leadership_effectiveness', axis=1)
        y = self.data['leadership_effectiveness']

        # Split data into training and testing sets
        X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

        return X_train, X_test, y_train, y_test

    def train_model(self, X_train, y_train):
        """
        Train a linear regression model.

        Args:
            X_train (pd.DataFrame): Training features.
            y_train (pd.Series): Training target.

        Returns:
            LinearRegression: Trained model.
        """
        # Create and train a linear regression model
        model = LinearRegression()  
        model.fit(X_train, y_train)

        return model

    def evaluate_model(self, model, X_test, y_test):
        """
        Evaluate the model's performance.

        Args:
            model (LinearRegression): Trained model.
            X_test (pd.DataFrame): Testing features.
            y_test (pd.Series): Testing target.

        Returns:
            dict: Evaluation metrics.
        """
        # Make predictions
        y_pred = model.predict(X_test)

        # Evaluate the model
        mae = metrics.mean_absolute_error(y_test, y_pred)
        mse = metrics.mean_squared_error(y_test, y_pred)
        rmse = mse ** 0.5
        r2 = metrics.r2_score(y_test, y_pred)

        return {
            'MAE': mae,
            'MSE': mse,
            'RMSE': rmse,
            'R2': r2
        }

# Example usage
if __name__ == "__main__":
    # Sample data
    data = pd.DataFrame({
        'captain_experience': [5, 3, 4, 6, 7],
        'team_chemistry': ['good', 'bad', 'good', 'good', 'bad'],
        'communication': [8, 6, 7, 9, 5],
        'strategy': [7, 5, 6, 8, 4],
        'leadership_effectiveness': [8.5, 6.2, 7.5, 9.0, 5.8]
    })

    # Create an instance of the model
    model = LeadershipEffectivenessModel(data)

    # Prepare data
    data = model.prepare_data()

    # Split data
    X_train, X_test, y_train, y_test = model.split_data()

    # Train the model
    trained_model = model.train_model(X_train, y_train)

    # Evaluate the model
    metrics = model.evaluate_model(trained_model, X_test, y_test)

    # Print evaluation metrics
    print("Model Evaluation Metrics:")
    for metric, value in metrics.items():
        print(f"{metric}: {value:.2f}")
```
