"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://fairmapsillinois.com
Prompt: Write a Python script that analyzes the impact of campaign spending on election outcomes in McHenry County, Illinois, as discussed on Fair Maps Illinois.
Generated: DETERMINISTIC_bdd1eb4da1978304
Batch ID: 20250612_155253
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
from sklearn.metrics import mean_squared_error

# Set visualisation style
sns.set(style="whitegrid")

def load_data(spending_file, outcomes_file):
    """
    Load campaign spending and election outcome data from CSV files.

    Parameters:
    spending_file (str): Path to the campaign spending data CSV.
    outcomes_file (str): Path to the election outcomes data CSV.

    Returns:
    pd.DataFrame, pd.DataFrame: DataFrames containing the spending and outcome data.
    """
    try:
        spending_data = pd.read_csv(spending_file)
        outcomes_data = pd.read_csv(outcomes_file)
        return spending_data, outcomes_data
    except FileNotFoundError as e:
        print(f"Error: {e}")
        raise
    except pd.errors.EmptyDataError as e:
        print("Error: One of the CSV files is empty.")
        raise
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
        raise

def preprocess_data(spending_data, outcomes_data):
    """
    Preprocess the data by merging it on common columns and handling missing values.

    Parameters:
    spending_data (pd.DataFrame): DataFrame containing campaign spending data.
    outcomes_data (pd.DataFrame): DataFrame containing election outcomes data.

    Returns:
    pd.DataFrame: Merged and cleaned DataFrame.
    """
    try:
        merged_data = pd.merge(spending_data, outcomes_data, on='district_id')
        # Fill missing values with zeros
        merged_data.fillna(0, inplace=True)
        return merged_data
    except Exception as e:
        print(f"Error during data preprocessing: {e}")
        raise

def analyze_data(data):
    """
    Perform analysis on the cleaned data and visualize the results.

    Parameters:
    data (pd.DataFrame): The cleaned DataFrame containing spending and outcomes.
    """
    try:
        # Plotting spending vs. outcomes
        plt.figure(figsize=(10, 6))
        sns.scatterplot(x='campaign_spending', y='vote_percentage', data=data)
        plt.title('Campaign Spending vs. Vote Percentage')
        plt.xlabel('Campaign Spending ($)')
        plt.ylabel('Vote Percentage (%)')
        plt.show()

        # Linear regression model to analyze impact
        X = data[['campaign_spending']]
        y = data['vote_percentage']
        X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

        model = LinearRegression()
        model.fit(X_train, y_train)

        # Predictions and evaluation
        predictions = model.predict(X_test)
        mse = mean_squared_error(y_test, predictions)
        print(f"Mean Squared Error of the model: {mse}")

        # Reporting the coefficients
        print(f"Coefficient of campaign spending: {model.coef_[0]}")
    except Exception as e:
        print(f"Error during analysis: {e}")
        raise

def main():
    """
    Main function to execute the campaign spending analysis.
    """
    # File paths for the data
    spending_file = 'mc_henry_campaign_spending.csv'
    outcomes_file = 'mc_henry_election_outcomes.csv'

    # Load data
    spending_data, outcomes_data = load_data(spending_file, outcomes_file)

    # Preprocess data
    cleaned_data = preprocess_data(spending_data, outcomes_data)

    # Analyze and visualize the data
    analyze_data(cleaned_data)

if __name__ == "__main__":
    main()
```

**Note:**
Make sure to replace the file paths `mc_henry_campaign_spending.csv` and `mc_henry_election_outcomes.csv` with the actual paths to your data files before running the script.
