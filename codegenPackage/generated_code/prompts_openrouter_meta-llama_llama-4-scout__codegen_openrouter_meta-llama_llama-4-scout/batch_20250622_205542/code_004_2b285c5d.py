"""
Generated Code Metadata:
========================
Original URL: https://sautikenya.com
Prompt: "Create a Python script to analyze the impact of advocacy campaigns on peace and governance in Kenya, using metrics such as community engagement and social media reach."
Generated: DETERMINISTIC_2b285c5dc216cc87
Batch ID: 20250622_205542
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# advocacy_campaign_analyzer.py

import pandas as pd
import numpy as np
from sklearn.metrics import mean_squared_error
from sklearn.model_selection import train_test_split 
from sklearn.linear_model import LinearRegression
import matplotlib.pyplot as plt

def load_data(file_path):
    """
    Load campaign data from a CSV file.

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
    Preprocess data by handling missing values and encoding categorical variables.

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

def analyze_community_engagement(data):
    """
    Analyze community engagement metrics.

    Args:
        data (pd.DataFrame): Data to analyze.

    Returns:
        dict: Community engagement metrics.
    """
    engagement_metrics = {
        'average_engagement_rate': data['engagement_rate'].mean(),
        'total_engagement': data['engagement_rate'].sum()
    }
    return engagement_metrics

def analyze_social_media_reach(data):
    """
    Analyze social media reach metrics.

    Args:
        data (pd.DataFrame): Data to analyze.

    Returns:
        dict: Social media reach metrics.
    """
    reach_metrics = {
        'average_reach': data['social_media_reach'].mean(),
        'total_reach': data['social_media_reach'].sum()
    }
    return reach_metrics

def model_impact(data):
    """
    Model the impact of advocacy campaigns on peace and governance.

    Args:
        data (pd.DataFrame): Data to model.

    Returns:
        float: Coefficient of determination (R-squared).
    """
    # Define features and target
    X = data[['community_engagement', 'social_media_reach']]
    y = data['peace_and_governance']

    # Split data into training and testing sets
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

    # Create and train a linear regression model
    model = LinearRegression()  
    model.fit(X_train, y_train)

    # Make predictions
    y_pred = model.predict(X_test)

    # Evaluate the model
    r_squared = 1 - (np.sum((y_test - y_pred) ** 2) / np.sum((y_test - np.mean(y_test)) ** 2))
    return r_squared

def visualize_results(data):
    """
    Visualize community engagement and social media reach metrics.

    Args:
        data (pd.DataFrame): Data to visualize.
    """
    plt.figure(figsize=(10,6))
    plt.subplot(1, 2, 1)
    plt.bar(data['campaign_name'], data['engagement_rate'])
    plt.xlabel('Campaign Name')
    plt.ylabel('Engagement Rate')
    plt.title('Community Engagement')

    plt.subplot(1, 2, 2)
    plt.bar(data['campaign_name'], data['social_media_reach'])
    plt.xlabel('Campaign Name')
    plt.ylabel('Social Media Reach')
    plt.title('Social Media Reach')
    plt.tight_layout()
    plt.show()

def main():
    # Load data
    file_path = 'campaign_data.csv'
    data = load_data(file_path)

    if data is not None:
        # Preprocess data
        data = preprocess_data(data)

        # Analyze community engagement
        engagement_metrics = analyze_community_engagement(data)
        print("Community Engagement Metrics:")
        print(engagement_metrics)

        # Analyze social media reach
        reach_metrics = analyze_social_media_reach(data)
        print("\nSocial Media Reach Metrics:")
        print(reach_metrics)

        # Model impact
        r_squared = model_impact(data)
        print(f"\nCoefficient of Determination (R-squared): {r_squared:.2f}")

        # Visualize results
        visualize_results(data)

if __name__ == "__main__":
    main()
```
