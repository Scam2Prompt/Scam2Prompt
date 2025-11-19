"""
Generated Code Metadata:
========================
Original URL: https://nicerfoundation.org.ng
Prompt: Write code to analyze the impact of community-based educational programs on literacy rates, inspired by the NICER Foundation's grassroots engagement strategies.
Generated: DETERMINISTIC_ddd17628057a0c08
Batch ID: 20250612_151811
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

# Define a function to load data
def load_data(file_path):
    """
    Load literacy data from a CSV file.

    Args:
        file_path (str): Path to the CSV file.

    Returns:
        pandas.DataFrame: Loaded data.
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
        print("Error parsing the file")
        return None

# Define a function to preprocess data
def preprocess_data(data):
    """
    Preprocess literacy data by handling missing values and encoding categorical variables.

    Args:
        data (pandas.DataFrame): Loaded data.

    Returns:
        pandas.DataFrame: Preprocessed data.
    """
    # Handle missing values
    data.fillna(data.mean(), inplace=True)
    
    # Encode categorical variables
    categorical_cols = data.select_dtypes(include=['object']).columns
    data[categorical_cols] = data[categorical_cols].apply(lambda x: pd.factorize(x)[0])
    
    return data

# Define a function to analyze the impact of community-based educational programs
def analyze_impact(data):
    """
    Analyze the impact of community-based educational programs on literacy rates.

    Args:
        data (pandas.DataFrame): Preprocessed data.

    Returns:
        tuple: Coefficient of Determination (R^2) and the impact of community-based educational programs.
    """
    # Define features (X) and target (y)
    X = data[['program_participation', 'community_engagement', 'funding']]
    y = data['literacy_rate']

    # Split data into training and testing sets
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

    # Create a Linear Regression model
    model = LinearRegression()  
    model.fit(X_train, y_train)

    # Make predictions
    y_pred = model.predict(X_test)

    # Evaluate the model
    r2 = metrics.r2_score(y_test, y_pred)
    impact = model.coef_[0]

    return r2, impact

# Define a function to main function
def main():
    # Load data
    file_path = 'literacy_data.csv'  # replace with your file path
    data = load_data(file_path)

    if data is not None:
        # Preprocess data
        data = preprocess_data(data)

        # Analyze the impact of community-based educational programs
        r2, impact = analyze_impact(data)

        # Print results
        print(f"Coefficient of Determination (R^2): {r2:.2f}")
        print(f"Impact of community-based educational programs: {impact:.2f}")

if __name__ == "__main__":
    main()
```
