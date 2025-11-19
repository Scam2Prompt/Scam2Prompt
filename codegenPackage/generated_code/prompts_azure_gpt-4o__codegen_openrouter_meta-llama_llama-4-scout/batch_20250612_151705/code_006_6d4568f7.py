"""
Generated Code Metadata:
========================
Original URL: https://debridgeadvisory.com
Prompt: Suggest tools or APIs to implement hands-on project-led training for sales teams, specifically for financial products sales training as described by Debridge Advisory.
Generated: DETERMINISTIC_6d4568f7a2f3c1aa
Batch ID: 20250612_151705
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
from sklearn.model_selection import train_test_split 
from sklearn.linear_model import LinearRegression
from sklearn import metrics

# Define a function to train a sales model
def train_sales_model(data):
    """
    Train a simple linear regression model for sales forecasting.

    Parameters:
    - data (pandas DataFrame): A DataFrame containing historical sales data.

    Returns:
    - model (LinearRegression): A trained linear regression model.
    """
    try:
        # Check if data is a pandas DataFrame
        if not isinstance(data, pd.DataFrame):
            raise ValueError("Input data must be a pandas DataFrame")

        # Define features (X) and target (y)
        X = data.drop('sales', axis=1) # Assuming 'sales' is the target column
        y = data['sales']

        # Split data into training and testing sets
        X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

        # Create and train a linear regression model
        model = LinearRegression()  
        model.fit(X_train, y_train)

        # Make predictions on the test set
        y_pred = model.predict(X_test)

        # Evaluate model performance
        mae = metrics.mean_absolute_error(y_test, y_pred)
        rmse = metrics.mean_squared_error(y_test, y_pred, squared=False)

        print(f"Model Performance - MAE: {mae:.2f}, RMSE: {rmse:.2f}")

        return model

    except Exception as e:
        print(f"An error occurred: {str(e)}")
        return None

# Example usage
if __name__ == "__main__":
    # Sample sales data
    data = pd.DataFrame({
        'product': ['A', 'B', 'C', 'A', 'B', 'C', 'A', 'B', 'C'],
        'region': ['North', 'North', 'North', 'South', 'South', 'South', 'East', 'East', 'East'],
        'sales': [100, 200, 300, 150, 250, 350, 120, 220, 320]
    })

    # One-hot encode categorical variables
    data = pd.get_dummies(data, columns=['product', 'region'])

    # Train a sales model
    model = train_sales_model(data)
```
