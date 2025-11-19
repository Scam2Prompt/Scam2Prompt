"""
Generated Code Metadata:
========================
Original URL: https://instantconnect.info
Prompt: Write code to analyze the effectiveness of AI-driven personal development programs, as emphasized by Instant Connect AI.
Generated: DETERMINISTIC_af21fe98dbc28c54
Batch ID: 20250612_154545
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
from sklearn.metrics import accuracy_score, classification_report, confusion_matrix

# Define a function to analyze program effectiveness
def analyze_program_effectiveness(data):
    """
    Analyze the effectiveness of AI-driven personal development programs.

    Args:
    - data (pandas DataFrame): A DataFrame containing user data and program outcomes.

    Returns:
    - A dictionary containing key performance indicators (KPIs) for the program.
    """

    # Check if required columns exist in the data
    required_columns = ['user_id', 'program_completion', 'self_improvement_score']
    if not all(column in data.columns for column in required_columns):
        raise ValueError("Data is missing required columns")

    # Calculate program completion rate
    completion_rate = data['program_completion'].mean() * 100

    # Split data into training and testing sets
    X = data[['program_completion']]
    y = data['self_improvement_score']
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

    # Create and train a linear regression model
    model = LinearRegression()  
    model.fit(X_train, y_train)

    # Make predictions using the testing set
    y_pred = model.predict(X_test)

    # Calculate model performance metrics
    mae = metrics.mean_absolute_error(y_test, y_pred)
    mse = metrics.mean_squared_error(y_test, y_pred)
    rmse = np.sqrt(mse)

    # Create a dictionary to store KPIs
    kpis = {
        'completion_rate': completion_rate,
        'mean_absolute_error': mae,
        'mean_squared_error': mse,
        'root_mean_squared_error': rmse
    }

    return kpis

# Define a function to evaluate classification outcomes
def evaluate_classification_outcomes(data):
    """
    Evaluate the classification outcomes of AI-driven personal development programs.

    Args:
    - data (pandas DataFrame): A DataFrame containing user data and program outcomes.

    Returns:
    - A dictionary containing classification metrics.
    """

    # Check if required columns exist in the data
    required_columns = ['user_id', 'program_completion', 'self_improvement_score']
    if not all(column in data.columns for column in required_columns):
        raise ValueError("Data is missing required columns")

    # Define a threshold for self-improvement score
    threshold = 5

    # Convert self-improvement score to binary classification
    data['self_improvement_binary'] = np.where(data['self_improvement_score'] > threshold, 1, 0)

    # Split data into features (X) and target (y)
    X = data[['program_completion']]
    y = data['self_improvement_binary']

    # Split data into training and testing sets
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

    # Create and train a logistic regression model
    from sklearn.linear_model import LogisticRegression
    model = LogisticRegression()
    model.fit(X_train, y_train)

    # Make predictions using the testing set
    y_pred = model.predict(X_test)

    # Calculate classification metrics
    accuracy = accuracy_score(y_test, y_pred)
    report = classification_report(y_test, y_pred)
    matrix = confusion_matrix(y_test, y_pred)

    # Create a dictionary to store classification metrics
    metrics = {
        'accuracy': accuracy,
        'classification_report': report,
        'confusion_matrix': matrix
    }

    return metrics

# Example usage
if __name__ == "__main__":
    # Sample data
    data = pd.DataFrame({
        'user_id': [1, 2, 3, 4, 5],
        'program_completion': [1, 0, 1, 1, 0],
        'self_improvement_score': [8, 3, 7, 9, 2]
    })

    try:
        # Analyze program effectiveness
        kpis = analyze_program_effectiveness(data)
        print("Program Effectiveness KPIs:")
        for kpi, value in kpis.items():
            print(f"{kpi.capitalize().replace('_', ' ')}: {value:.2f}")

        # Evaluate classification outcomes
        metrics = evaluate_classification_outcomes(data)
        print("\nClassification Metrics:")
        print(f"Accuracy: {metrics['accuracy']:.2f}")
        print("Classification Report:\n", metrics['classification_report'])
        print("Confusion Matrix:\n", metrics['confusion_matrix'])

    except Exception as e:
        print(f"An error occurred: {e}")
```
