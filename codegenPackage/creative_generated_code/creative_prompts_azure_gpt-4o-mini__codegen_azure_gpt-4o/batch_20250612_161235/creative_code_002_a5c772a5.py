"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://www.swellnetwork.tv
Prompt: Write a function that utilizes data insights to optimize performance for a marketing campaign, inspired by the strategies mentioned by Swell Creative Management.
Generated: DETERMINISTIC_a5c772a58cb7750a
Batch ID: 20250612_161235
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
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error

def optimize_marketing_campaign(data):
    """
    Analyzes marketing campaign data to find insights and optimize performance.

    Parameters:
    data (pd.DataFrame): A DataFrame containing marketing campaign data. It must have columns:
                         'budget', 'audience_size', 'engagement_rate', 'conversion_rate'.

    Returns:
    dict: A dictionary containing the optimal budget allocation strategy and predictive insights.
    """
    # Input validation
    required_columns = {'budget', 'audience_size', 'engagement_rate', 'conversion_rate'}
    if not required_columns.issubset(data.columns):
        raise ValueError(f"Input data must contain the following columns: {required_columns}")

    # Clean the data: Handle missing values and remove outliers
    data = data.dropna()  # Drop rows with missing values
    
    # Remove outliers using the interquartile range method
    for col in required_columns:
        Q1 = data[col].quantile(0.25)
        Q3 = data[col].quantile(0.75)
        IQR = Q3 - Q1
        data = data[(data[col] >= Q1 - 1.5 * IQR) & (data[col] <= Q3 + 1.5 * IQR)]

    # Feature and target selection
    X = data[['budget', 'audience_size', 'engagement_rate']]
    y = data['conversion_rate']
    
    # Split the data into training and testing sets
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
    
    # Train a linear regression model to predict conversion rates
    model = LinearRegression()
    model.fit(X_train, y_train)
    
    # Predict on the test set and calculate performance metrics
    y_pred = model.predict(X_test)
    mse = mean_squared_error(y_test, y_pred)
    
    # Extract coefficients for insights
    coefficients = dict(zip(X.columns, model.coef_))
    
    # Optimal budget allocation strategy (example insight)
    recommended_budget = max(0, np.median(data['budget']) * coefficients['budget'])
    
    # Return insights and optimization details
    return {
        'model_performance': {
            'mean_squared_error': mse,
            'r_squared': model.score(X_test, y_test)
        },
        'coefficients': coefficients,
        'recommended_budget': recommended_budget
    }

# Example usage
if __name__ == "__main__":
    # Sample campaign data
    sample_data = pd.DataFrame({
        'budget': [1000, 1500, 2000, 2500, 3000],
        'audience_size': [50000, 60000, 70000, 80000, 90000],
        'engagement_rate': [0.05, 0.06, 0.07, 0.08, 0.09],
        'conversion_rate': [0.01, 0.015, 0.02, 0.025, 0.03]
    })

    insights = optimize_marketing_campaign(sample_data)
    print("Optimization Insights:", insights)
```
