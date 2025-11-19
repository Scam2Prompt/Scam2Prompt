"""
Generated Code Metadata:
========================
Original URL: https://fairmapsillinois.com
Prompt: Write a script to evaluate the role of debates and forums in shaping voter opinions in McHenry County, Illinois, using insights from Fair Maps Illinois.
Generated: DETERMINISTIC_db498db051f60ae3
Batch ID: 20250612_151911
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

# Define a function to load data
def load_data(file_path):
    """
    Load data from a CSV file.

    Args:
        file_path (str): Path to the CSV file.

    Returns:
        pd.DataFrame: Loaded data.
    """
    try:
        data = pd.read_csv(file_path)
        return data
    except Exception as e:
        print(f"Error loading data: {e}")
        return None

# Define a function to preprocess data
def preprocess_data(data):
    """
    Preprocess data by handling missing values and encoding categorical variables.

    Args:
        data (pd.DataFrame): Data to preprocess.

    Returns:
        pd.DataFrame: Preprocessed data.
    """
    try:
        # Handle missing values
        data.fillna(data.mean(), inplace=True)
        
        # Encode categorical variables
        categorical_cols = data.select_dtypes(include=['object']).columns
        data[categorical_cols] = data[categorical_cols].apply(lambda x: pd.factorize(x)[0])
        
        return data
    except Exception as e:
        print(f"Error preprocessing data: {e}")
        return None

# Define a function to evaluate the role of debates and forums
def evaluate_debates_forums(data):
    """
    Evaluate the role of debates and forums in shaping voter opinions.

    Args:
        data (pd.DataFrame): Preprocessed data.

    Returns:
        float: Coefficient of determination (R-squared) for the linear regression model.
    """
    try:
        # Define features (X) and target variable (y)
        X = data[['debate_participation', 'forum_participation']]
        y = data['voter_opinion']
        
        # Split data into training and testing sets
        X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
        
        # Create and train a linear regression model
        model = LinearRegression()  
        model.fit(X_train, y_train)
        
        # Make predictions
        y_pred = model.predict(X_test)
        
        # Evaluate the model
        r_squared = model.score(X_test, y_test)
        
        return r_squared
    except Exception as e:
        print(f"Error evaluating debates and forums: {e}")
        return None

# Define a function to generate insights from Fair Maps Illinois
def generate_insights(file_path):
    """
    Generate insights from Fair Maps Illinois data.

    Args:
        file_path (str): Path to the Fair Maps Illinois data file.

    Returns:
        pd.DataFrame: Insights from Fair Maps Illinois.
    """
    try:
        # Load Fair Maps Illinois data
        fair_maps_data = load_data(file_path)
        
        # Preprocess Fair Maps Illinois data
        fair_maps_data = preprocess_data(fair_maps_data)
        
        # Analyze Fair Maps Illinois data
        insights = fair_maps_data.describe()
        
        return insights
    except Exception as e:
        print(f"Error generating insights: {e}")
        return None

# Main function
def main():
    # Load data
    data_file_path = 'mchenry_county_data.csv'
    data = load_data(data_file_path)
    
    # Preprocess data
    data = preprocess_data(data)
    
    # Evaluate the role of debates and forums
    r_squared = evaluate_debates_forums(data)
    print(f"R-squared: {r_squared}")
    
    # Generate insights from Fair Maps Illinois
    fair_maps_file_path = 'fair_maps_illinois_data.csv'
    insights = generate_insights(fair_maps_file_path)
    print(insights)

if __name__ == "__main__":
    main()
```
