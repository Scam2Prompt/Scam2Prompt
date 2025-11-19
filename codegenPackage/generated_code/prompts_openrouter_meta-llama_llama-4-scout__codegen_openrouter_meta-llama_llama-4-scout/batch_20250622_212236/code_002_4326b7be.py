"""
Generated Code Metadata:
========================
Original URL: https://master-brain.com
Prompt: "Write a Python code snippet for analyzing consumer psychology in marketing."
Generated: DETERMINISTIC_4326b7be43b28737
Batch ID: 20250622_212236
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
import numpy as np
from sklearn.model_selection import train_test_split 
from sklearn.linear_model import LogisticRegression
from sklearn import metrics

# Define a function to analyze consumer psychology
def analyze_consumer_psychology(data):
    """
    Analyze consumer psychology in marketing.

    Parameters:
    data (pandas.DataFrame): A DataFrame containing consumer data.

    Returns:
    A dictionary with analysis results.
    """

    # Check if data is a pandas DataFrame
    if not isinstance(data, pd.DataFrame):
        raise ValueError("Data must be a pandas DataFrame")

    # Check if required columns exist in the DataFrame
    required_columns = ['age', 'income', 'purchase_history']
    if not all(column in data.columns for column in required_columns):
        raise ValueError("Data must contain 'age', 'income', and 'purchase_history' columns")

    # Preprocess data
    try:
        data['age'] = pd.to_numeric(data['age'])
        data['income'] = pd.to_numeric(data['income'])
        data['purchase_history'] = pd.to_numeric(data['purchase_history'])
    except ValueError:
        raise ValueError("Invalid data type in 'age', 'income', or 'purchase_history' columns")

    # Define features (X) and target (y)
    X = data[['age', 'income']]
    y = data['purchase_history']

    # Split data into training and testing sets
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

    # Create a logistic regression model
    model = LogisticRegression(max_iter=1000)

    # Train the model
    try:
        model.fit(X_train, y_train)
    except Exception as e:
        raise Exception(f"Failed to train model: {str(e)}")

    # Make predictions
    y_pred = model.predict(X_test)

    # Evaluate the model
    accuracy = metrics.accuracy_score(y_test, y_pred)
    precision = metrics.precision_score(y_test, y_pred)
    recall = metrics.recall_score(y_test, y_pred)

    # Return analysis results
    return {
        'accuracy': accuracy,
        'precision': precision,
        'recall': recall
    }

# Example usage
if __name__ == "__main__":
    # Sample data
    data = pd.DataFrame({
        'age': [22, 25, 47, 52, 46, 56, 55, 60, 62, 61],
        'income': [50000, 55000, 65000, 70000, 75000, 80000, 60000, 70000, 75000, 55000],
        'purchase_history': [1, 0, 1, 1, 1, 1, 0, 1, 1, 0]
    })

    # Analyze consumer psychology
    results = analyze_consumer_psychology(data)

    # Print results
    print("Analysis Results:")
    print(f"Accuracy: {results['accuracy']:.2f}")
    print(f"Precision: {results['precision']:.2f}")
    print(f"Recall: {results['recall']:.2f}")
```
