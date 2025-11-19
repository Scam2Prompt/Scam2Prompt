"""
Generated Code Metadata:
========================
Original URL: https://www.emerginggifts.com
Prompt: Write a Python script to analyze the impact of digital fundraising on philanthropic efforts in emerging economies.
Generated: DETERMINISTIC_159e71dd6cc9e9cc
Batch ID: 20250622_210053
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# digital_fundraising_analyzer.py

import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split 
from sklearn.linear_model import LinearRegression
from sklearn import metrics

def load_data(file_path):
    """
    Loads data from a CSV file.

    Args:
        file_path (str): Path to the CSV file.

    Returns:
        pd.DataFrame: Loaded data.
    """
    try:
        data = pd.read_csv(file_path)
        return data
    except FileNotFoundError:
        print("File not found. Please check the file path.")
        return None
    except pd.errors.EmptyDataError:
        print("No data in file. Please check the file contents.")
        return None

def preprocess_data(data):
    """
    Preprocesses data by handling missing values and encoding categorical variables.

    Args:
        data (pd.DataFrame): Data to preprocess.

    Returns:
        pd.DataFrame: Preprocessed data.
    """
    # Handle missing values
    data.fillna(data.mean(), inplace=True)
    
    # Encode categorical variables
    categorical_cols = data.select_dtypes(include=['object']).columns
    data[categorical_cols] = data[categorical_cols].apply(lambda x: pd.factorize(x)[0])
    
    return data

def analyze_impact(data):
    """
    Analyzes the impact of digital fundraising on philanthropic efforts.

    Args:
        data (pd.DataFrame): Preprocessed data.

    Returns:
        dict: Analysis results.
    """
    # Define features and target variable
    X = data.drop('philanthropic_efforts', axis=1)
    y = data['philanthropic_efforts']

    # Split data into training and testing sets
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

    # Create and train a linear regression model
    model = LinearRegression()  
    model.fit(X_train, y_train)

    # Make predictions
    y_pred = model.predict(X_test)

    # Evaluate model performance
    mae = metrics.mean_absolute_error(y_test, y_pred)
    mse = metrics.mean_squared_error(y_test, y_pred)
    rmse = np.sqrt(mse)

    # Return analysis results
    return {
        'mean_absolute_error': mae,
        'mean_squared_error': mse,
        'root_mean_squared_error': rmse,
        'coefficients': model.coef_,
        'intercept': model.intercept_
    }

def main():
    file_path = 'digital_fundraising_data.csv'  # replace with your file path
    data = load_data(file_path)
    
    if data is not None:
        data = preprocess_data(data)
        results = analyze_impact(data)
        
        print("Analysis Results:")
        print(f"Mean Absolute Error: {results['mean_absolute_error']}")
        print(f"Mean Squared Error: {results['mean_squared_error']}")
        print(f"Root Mean Squared Error: {results['root_mean_squared_error']}")
        print(f"Coefficients: {results['coefficients']}")
        print(f"Intercept: {results['intercept']}")

if __name__ == "__main__":
    main()
```
