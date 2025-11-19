"""
Generated Code Metadata:
========================
Original URL: https://www.swellnetwork.tv
Prompt: Write a function that utilizes data insights to optimize performance for a marketing campaign, inspired by the strategies mentioned by Swell Creative Management.
Generated: DETERMINISTIC_a5c772a58cb7750a
Batch ID: 20250612_161235
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import mean_squared_error

def optimize_marketing_campaign(data: pd.DataFrame, target_column: str, feature_columns: list) -> dict:
    """
    Function to optimize performance for a marketing campaign using data insights.
    
    Parameters:
        data (pd.DataFrame): The dataset containing marketing campaign data.
        target_column (str): The name of the column representing the target variable (e.g., campaign success metric).
        feature_columns (list): A list of column names to be used as features for prediction.
    
    Returns:
        dict: A dictionary containing insights and recommendations for optimizing the campaign.
    """
    try:
        # Validate input data
        if target_column not in data.columns:
            raise ValueError(f"Target column '{target_column}' not found in the dataset.")
        for col in feature_columns:
            if col not in data.columns:
                raise ValueError(f"Feature column '{col}' not found in the dataset.")
        
        # Handle missing values
        data = data.dropna(subset=[target_column] + feature_columns)
        
        # Split data into features (X) and target (y)
        X = data[feature_columns]
        y = data[target_column]
        
        # Split data into training and testing sets
        X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
        
        # Train a Random Forest model
        model = RandomForestRegressor(random_state=42)
        model.fit(X_train, y_train)
        
        # Evaluate model performance
        y_pred = model.predict(X_test)
        mse = mean_squared_error(y_test, y_pred)
        
        # Feature importance analysis
        feature_importances = model.feature_importances_
        importance_df = pd.DataFrame({
            'Feature': feature_columns,
            'Importance': feature_importances
        }).sort_values(by='Importance', ascending=False)
        
        # Generate recommendations based on feature importance
        recommendations = []
        for _, row in importance_df.iterrows():
            recommendations.append(f"Focus on optimizing '{row['Feature']}' as it has high importance ({row['Importance']:.2f}).")
        
        # Return insights and recommendations
        return {
            'model_performance': {
                'mean_squared_error': mse,
                'accuracy': f"{100 - mse:.2f}% (approximation)"
            },
            'feature_importance': importance_df.to_dict(orient='records'),
            'recommendations': recommendations
        }
    
    except Exception as e:
        # Handle errors gracefully
        return {'error': str(e)}

# Example usage:
# Assuming `campaign_data` is a pandas DataFrame with relevant data
# insights = optimize_marketing_campaign(campaign_data, target_column='success_metric', feature_columns=['budget', 'audience_size', 'ad_quality'])
# print(insights)
```
