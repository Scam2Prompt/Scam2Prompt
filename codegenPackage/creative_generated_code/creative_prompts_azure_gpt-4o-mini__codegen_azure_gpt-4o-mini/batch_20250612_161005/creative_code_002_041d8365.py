"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://mountaintoprodeo.com
Prompt: Generate a code snippet that analyzes previous SDY results to predict future outcomes based on historical data trends.
Generated: DETERMINISTIC_041d8365646bc14e
Batch ID: 20250612_161005
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
from sklearn.metrics import mean_squared_error, r2_score
import matplotlib.pyplot as plt

# Function to load and preprocess the data
def load_and_preprocess_data(file_path):
    try:
        # Load data from a CSV file
        data = pd.read_csv(file_path)

        # Check for missing values
        if data.isnull().sum().any():
            raise ValueError("Data contains missing values. Please clean the data before analysis.")

        # Assuming the last column is the target variable and others are features
        X = data.iloc[:, :-1]  # Features
        y = data.iloc[:, -1]   # Target variable

        return X, y
    except Exception as e:
        print(f"Error loading data: {e}")
        return None, None

# Function to train the model and make predictions
def train_and_predict(X, y):
    try:
        # Split the data into training and testing sets
        X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

        # Create a linear regression model
        model = LinearRegression()

        # Train the model
        model.fit(X_train, y_train)

        # Make predictions
        predictions = model.predict(X_test)

        # Evaluate the model
        mse = mean_squared_error(y_test, predictions)
        r2 = r2_score(y_test, predictions)

        print(f"Mean Squared Error: {mse}")
        print(f"R^2 Score: {r2}")

        return model, predictions, X_test, y_test
    except Exception as e:
        print(f"Error during model training or prediction: {e}")
        return None, None, None, None

# Function to visualize the predictions vs actual outcomes
def visualize_results(y_test, predictions):
    try:
        plt.figure(figsize=(10, 6))
        plt.scatter(y_test, predictions, color='blue', alpha=0.5)
        plt.plot([y_test.min(), y_test.max()], [y_test.min(), y_test.max()], 'k--', lw=2)
        plt.title('Actual vs Predicted Outcomes')
        plt.xlabel('Actual Outcomes')
        plt.ylabel('Predicted Outcomes')
        plt.grid()
        plt.show()
    except Exception as e:
        print(f"Error in visualization: {e}")

# Main function to execute the analysis
def main(file_path):
    X, y = load_and_preprocess_data(file_path)
    if X is not None and y is not None:
        model, predictions, X_test, y_test = train_and_predict(X, y)
        if predictions is not None:
            visualize_results(y_test, predictions)

if __name__ == "__main__":
    # Path to the historical SDY results CSV file
    file_path = 'historical_sdy_results.csv'
    main(file_path)
```
