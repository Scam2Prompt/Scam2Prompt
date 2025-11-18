"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://fairmapsillinois.com
Prompt: Write a Python script to analyze the impact of campaign spending on election outcomes using data from McHenry County, Illinois, as described on Fair Maps Illinois.
Generated: DETERMINISTIC_6ff28388426027fd
Batch ID: 20250612_151911
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
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error, r2_score

# Set Seaborn style for better visualization
sns.set(style="whitegrid")

# Function to load data from CSV
def load_data(filepath):
    """
    Load campaign spending and election outcome data from a CSV file.

    :param filepath: str - Path to the CSV file
    :return: pd.DataFrame - Loaded data
    """
    try:
        data = pd.read_csv(filepath)
        return data
    except FileNotFoundError:
        print(f"Error: The file at {filepath} was not found.")
        return None
    except pd.errors.EmptyDataError:
        print("Error: The file is empty.")
        return None
    except Exception as e:
        print(f"An error occurred: {e}")
        return None

# Function to preprocess the data
def preprocess_data(data):
    """
    Preprocess the data: handle missing values and convert to numeric types.

    :param data: pd.DataFrame - Raw data
    :return: pd.DataFrame - Preprocessed data
    """
    # Check for missing values
    if data.isnull().sum().sum() > 0:
        data = data.dropna()

    # Convert relevant columns to numeric types
    data['spending'] = pd.to_numeric(data['spending'], errors='coerce')
    data['outcome'] = pd.to_numeric(data['outcome'], errors='coerce')

    # Drop rows with NaN values after conversion
    data = data.dropna()
    
    return data

# Function to analyze the impact of spending on outcomes
def analyze_impact(data):
    """
    Analyze the impact of campaign spending on election outcomes.

    :param data: pd.DataFrame - Preprocessed data
    """
    # Prepare the features and target variable
    X = data[['spending']]
    y = data['outcome']

    # Split the data into training and testing sets
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

    # Create a linear regression model
    model = LinearRegression()
    model.fit(X_train, y_train)

    # Make predictions
    y_pred = model.predict(X_test)

    # Evaluate the model
    mse = mean_squared_error(y_test, y_pred)
    r2 = r2_score(y_test, y_pred)

    # Print model evaluation metrics
    print(f"Mean Squared Error: {mse:.2f}")
    print(f"R^2 Score: {r2:.2f}")

    # Plotting the results
    plt.figure(figsize=(10, 6))
    sns.scatterplot(x=X_test['spending'], y=y_test, color='blue', label='Actual Outcomes')
    sns.scatterplot(x=X_test['spending'], y=y_pred, color='red', label='Predicted Outcomes')
    plt.title('Campaign Spending vs Election Outcomes')
    plt.xlabel('Campaign Spending ($)')
    plt.ylabel('Election Outcome (Votes/Percentage)')
    plt.legend()
    plt.show()

# Main function to run the script
def main():
    # Load the data
    filepath = 'mchenry_county_campaign_data.csv'  # Update this path as needed
    data = load_data(filepath)
    
    if data is None:
        return  # Stop execution if data loading failed

    # Preprocess the data
    processed_data = preprocess_data(data)

    # Analyze the impact of spending on outcomes
    analyze_impact(processed_data)

# Entry point of the script
if __name__ == "__main__":
    main()
```
