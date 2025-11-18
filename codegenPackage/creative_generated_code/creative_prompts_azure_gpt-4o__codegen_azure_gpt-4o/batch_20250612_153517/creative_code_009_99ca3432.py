"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://childnepal.org
Prompt: Recommend a machine learning library for predicting the impact of future initiatives based on Child Nepal's historical milestones and impact data.
Generated: DETERMINISTIC_99ca3432cf49d63b
Batch ID: 20250612_153517
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
"""
This script recommends a machine learning library for predicting the impact of future initiatives
based on historical milestones and impact data from Child Nepal. We use scikit-learn due to its 
ease of use, wide adoption, extensive documentation, and robust support for regression and classification tasks.
"""

# Import necessary libraries
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import mean_squared_error

def predict_initiative_impact(data_file_path):
    """
    Predicts the impact of future initiatives based on historical data.

    Args:
        data_file_path (str): Path to the CSV file containing historical milestones and impact data.

    Returns:
        None: Prints the Mean Squared Error and feature importance of the prediction model.
    """
    try:
        # Load historical data into a DataFrame
        data = pd.read_csv(data_file_path)
        
        # Ensure the file contains necessary columns
        if 'Milestone_Features' not in data.columns or 'Impact_Score' not in data.columns:
            raise ValueError("Input data must contain 'Milestone_Features' and 'Impact_Score' columns.")
        
        # Split the data into features (X) and target variable (y)
        X = data.drop(columns=['Impact_Score'])
        y = data['Impact_Score']
        
        # Split into training and testing sets
        X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
        
        # Create and train a Random Forest model
        model = RandomForestRegressor(random_state=42)
        model.fit(X_train, y_train)
        
        # Evaluate the model on the testing data
        y_pred = model.predict(X_test)
        mse = mean_squared_error(y_test, y_pred)
        
        # Print the model's performance
        print(f"Mean Squared Error of the prediction model: {mse:.2f}")
        
        # Feature importance for better understanding
        feature_importance = model.feature_importances_
        print("Feature Importance (in descending order):")
        for feature, importance in sorted(zip(X.columns, feature_importance), key=lambda x: x[1], reverse=True):
            print(f"{feature}: {importance:.4f}")
    
    except FileNotFoundError:
        print("Error: The specified data file path does not exist.")
    except ValueError as ve:
        print(f"Error: {ve}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

# Example usage
# Replace 'your_data.csv' with the path to the actual data file in CSV format
predict_initiative_impact('your_data.csv')
```
