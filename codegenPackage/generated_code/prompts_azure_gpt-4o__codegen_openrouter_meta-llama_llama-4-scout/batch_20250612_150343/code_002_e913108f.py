"""
Generated Code Metadata:
========================
Original URL: https://starkware.in
Prompt: Generate code to analyze customer data and provide actionable insights to enhance business outcomes, following Starkware's data & analytics methodology.
Generated: DETERMINISTIC_e913108fcf964d60
Batch ID: 20250612_150343
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

# Define a function to load customer data
def load_customer_data(file_path: str) -> pd.DataFrame:
    """
    Loads customer data from a CSV file.

    Args:
    file_path (str): The path to the CSV file.

    Returns:
    pd.DataFrame: A pandas DataFrame containing the customer data.

    Raises:
    FileNotFoundError: If the file does not exist.
    pd.errors.EmptyDataError: If the file is empty.
    pd.errors.ParserError: If an error occurs while parsing the file.
    """
    try:
        data = pd.read_csv(file_path)
        return data
    except FileNotFoundError:
        print("The file does not exist")
        return None
    except pd.errors.EmptyDataError:
        print("The file is empty")
        return None
    except pd.errors.ParserError:
        print("An error occurred while parsing the file")
        return None

# Define a function to clean and preprocess customer data
def clean_customer_data(data: pd.DataFrame) -> pd.DataFrame:
    """
    Cleans and preprocesses customer data.

    Args:
    data (pd.DataFrame): A pandas DataFrame containing the customer data.

    Returns:
    pd.DataFrame: A pandas DataFrame containing the cleaned and preprocessed customer data.
    """
    # Handle missing values
    data.fillna(data.mean(), inplace=True)
    
    # Remove duplicates
    data.drop_duplicates(inplace=True)
    
    # Encode categorical variables
    categorical_cols = data.select_dtypes(include=['object']).columns
    data[categorical_cols] = data[categorical_cols].apply(lambda x: pd.factorize(x)[0])
    
    return data

# Define a function to analyze customer data
def analyze_customer_data(data: pd.DataFrame) -> dict:
    """
    Analyzes customer data and provides actionable insights.

    Args:
    data (pd.DataFrame): A pandas DataFrame containing the customer data.

    Returns:
    dict: A dictionary containing the analysis results.
    """
    # Calculate customer demographics
    demographics = {
        'total_customers': data.shape[0],
        'average_age': data['age'].mean(),
        'average_income': data['income'].mean()
    }
    
    # Calculate purchase behavior
    purchase_behavior = {
        'total_purchases': data['purchase_history'].sum(),
        'average_purchase_value': data['purchase_history'].mean()
    }
    
    # Perform linear regression to predict purchase behavior
    X = data[['age', 'income']]
    y = data['purchase_history']
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=0)
    regressor = LinearRegression()  
    regressor.fit(X_train, y_train)
    y_pred = regressor.predict(X_test)
    rmse = np.sqrt(metrics.mean_squared_error(y_test, y_pred))
    
    # Provide actionable insights
    insights = {
        'demographics': demographics,
        'purchase_behavior': purchase_behavior,
        'predicted_purchase_behavior': rmse
    }
    
    return insights

# Define a main function to execute the analysis
def main():
    file_path = 'customer_data.csv'  # Replace with your file path
    data = load_customer_data(file_path)
    if data is not None:
        cleaned_data = clean_customer_data(data)
        insights = analyze_customer_data(cleaned_data)
        print(insights)

if __name__ == "__main__":
    main()
```
