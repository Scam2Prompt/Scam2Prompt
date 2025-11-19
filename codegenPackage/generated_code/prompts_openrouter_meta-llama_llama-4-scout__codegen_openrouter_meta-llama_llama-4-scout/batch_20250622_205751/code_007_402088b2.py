"""
Generated Code Metadata:
========================
Original URL: https://skifoundation.org
Prompt: Develop a code snippet to analyze data on program outcomes and impact for an organization like SKI Foundation.
Generated: DETERMINISTIC_402088b210b85a15
Batch ID: 20250622_205751
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
from sklearn.linear_model import LinearRegression
from sklearn import metrics

# Define a function to analyze program outcomes and impact
def analyze_program_outcomes(data):
    """
    Analyze data on program outcomes and impact.

    Parameters:
    data (pandas.DataFrame): A DataFrame containing program outcome data.

    Returns:
    dict: A dictionary containing analysis results.
    """

    # Check if data is not empty
    if data.empty:
        raise ValueError("Data is empty")

    # Ensure required columns exist in the data
    required_columns = ['program_name', 'outcome_measure', 'impact_value']
    if not all(column in data.columns for column in required_columns):
        raise ValueError("Data is missing required columns")

    # Group data by program and calculate mean impact
    program_impacts = data.groupby('program_name')['impact_value'].mean().reset_index()

    # Sort program impacts in descending order
    program_impacts = program_impacts.sort_values(by='impact_value', ascending=False)

    # Perform linear regression to model program outcomes
    try:
        X = data[['program_name']]  # Convert program_name to numeric values
        X = pd.get_dummies(X, columns=['program_name'])
        y = data['impact_value']

        X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=0)

        regressor = LinearRegression()  
        regressor.fit(X_train, y_train)

        y_pred = regressor.predict(X_test)

        # Evaluate model performance
        mae = metrics.mean_absolute_error(y_test, y_pred)
        mse = metrics.mean_squared_error(y_test, y_pred)
        rmse = np.sqrt(metrics.mean_squared_error(y_test, y_pred))

        analysis_results = {
            'program_impacts': program_impacts,
            'model_performance': {
                'mean_absolute_error': mae,
                'mean_squared_error': mse,
                'root_mean_squared_error': rmse
            }
        }

        return analysis_results

    except Exception as e:
        raise Exception(f"An error occurred during analysis: {str(e)}")

# Example usage
if __name__ == "__main__":
    # Sample data
    data = pd.DataFrame({
        'program_name': ['Program A', 'Program B', 'Program A', 'Program C', 'Program B', 'Program C'],
        'outcome_measure': ['Measure 1', 'Measure 2', 'Measure 1', 'Measure 3', 'Measure 2', 'Measure 3'],
        'impact_value': [10, 20, 15, 30, 25, 35]
    })

    try:
        analysis_results = analyze_program_outcomes(data)
        print("Program Impacts:")
        print(analysis_results['program_impacts'])
        print("\nModel Performance:")
        print(f"Mean Absolute Error: {analysis_results['model_performance']['mean_absolute_error']}")
        print(f"Mean Squared Error: {analysis_results['model_performance']['mean_squared_error']}")
        print(f"Root Mean Squared Error: {analysis_results['model_performance']['root_mean_squared_error']}")

    except Exception as e:
        print(f"An error occurred: {str(e)}")
```
