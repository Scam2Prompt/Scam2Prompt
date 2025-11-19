"""
Generated Code Metadata:
========================
Original URL: https://www.emerginggifts.com
Prompt: Provide code examples for implementing a global digital marketing campaign for philanthropy using insights from Emerging Gifts' analysis of the humanitarian sector.
Generated: DETERMINISTIC_daf00c30b51d2008
Batch ID: 20250612_152511
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

# Define a function to analyze campaign performance
def analyze_campaign_performance(campaign_data):
    """
    Analyze campaign performance based on provided data.

    Args:
        campaign_data (pd.DataFrame): A DataFrame containing campaign data.
            It should have columns for 'donations', 'engagements', and 'channel'.

    Returns:
        dict: A dictionary containing performance metrics.
    """
    try:
        # Ensure required columns exist
        required_columns = ['donations', 'engagements', 'channel']
        if not all(column in campaign_data.columns for column in required_columns):
            raise ValueError("Campaign data is missing required columns")

        # Calculate performance metrics
        total_donations = campaign_data['donations'].sum()
        total_engagements = campaign_data['engagements'].sum()
        average_donation = total_donations / len(campaign_data)

        # Create a dictionary to store performance metrics
        performance_metrics = {
            'total_donations': total_donations,
            'total_engagements': total_engagements,
            'average_donation': average_donation
        }

        return performance_metrics

    except Exception as e:
        print(f"An error occurred: {e}")
        return None

# Define a function to predict campaign outcomes
def predict_campaign_outcomes(campaign_data):
    """
    Predict campaign outcomes using a linear regression model.

    Args:
        campaign_data (pd.DataFrame): A DataFrame containing campaign data.
            It should have columns for 'donations', 'engagements', and 'channel'.

    Returns:
        dict: A dictionary containing predicted outcomes.
    """
    try:
        # Prepare data for modeling
        X = campaign_data[['engagements']]
        y = campaign_data['donations']

        # Split data into training and testing sets
        X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

        # Create and train a linear regression model
        model = LinearRegression()  
        model.fit(X_train, y_train)

        # Make predictions
        predictions = model.predict(X_test)

        # Evaluate model performance
        mae = metrics.mean_absolute_error(y_test, predictions)
        mse = metrics.mean_squared_error(y_test, predictions)
        rmse = np.sqrt(mse)

        # Create a dictionary to store predicted outcomes
        predicted_outcomes = {
            'predictions': predictions,
            'mae': mae,
            'mse': mse,
            'rmse': rmse
        }

        return predicted_outcomes

    except Exception as e:
        print(f"An error occurred: {e}")
        return None

# Example usage
if __name__ == "__main__":
    # Sample campaign data
    campaign_data = pd.DataFrame({
        'donations': [100, 200, 300, 400, 500],
        'engagements': [10, 20, 30, 40, 50],
        'channel': ['social media', 'email', 'social media', 'email', 'social media']
    })

    # Analyze campaign performance
    performance_metrics = analyze_campaign_performance(campaign_data)
    print("Performance Metrics:")
    print(performance_metrics)

    # Predict campaign outcomes
    predicted_outcomes = predict_campaign_outcomes(campaign_data)
    print("\nPredicted Outcomes:")
    print(predicted_outcomes)
```
