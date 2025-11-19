"""
Generated Code Metadata:
========================
Original URL: https://pconsultsa.com
Prompt: Write a code snippet to create a simple model for evaluating leadership effectiveness in sports teams using Python and its relevant libraries.
Generated: DETERMINISTIC_2c031b890496ff0a
Batch ID: 20250622_210703
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
from sklearn.metrics import mean_squared_error, r2_score

# Define a function to evaluate leadership effectiveness
def evaluate_leadership_effectiveness(data):
    """
    Evaluates leadership effectiveness in sports teams using a machine learning model.
    
    Parameters:
        data (pd.DataFrame): A DataFrame containing features and target variable.
                            Expected columns: ['team_morale', 'communication_score', 
                            'strategy_score', 'player_performance', 'leadership_effectiveness']
    
    Returns:
        dict: A dictionary containing model performance metrics (MSE and R2 score).
    """
    try:
        # Validate input data
        required_columns = ['team_morale', 'communication_score', 'strategy_score', 
                            'player_performance', 'leadership_effectiveness']
        if not all(col in data.columns for col in required_columns):
            raise ValueError(f"Input data must contain the following columns: {required_columns}")
        
        # Split data into features (X) and target (y)
        X = data[['team_morale', 'communication_score', 'strategy_score', 'player_performance']]
        y = data['leadership_effectiveness']
        
        # Split data into training and testing sets
        X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
        
        # Initialize and train the model
        model = RandomForestRegressor(random_state=42)
        model.fit(X_train, y_train)
        
        # Make predictions on the test set
        y_pred = model.predict(X_test)
        
        # Calculate performance metrics
        mse = mean_squared_error(y_test, y_pred)
        r2 = r2_score(y_test, y_pred)
        
        # Return performance metrics
        return {
            "Mean Squared Error": mse,
            "R2 Score": r2
        }
    
    except Exception as e:
        # Handle exceptions and provide meaningful error messages
        print(f"An error occurred: {e}")
        return None

# Example usage
if __name__ == "__main__":
    # Create a sample dataset
    sample_data = pd.DataFrame({
        'team_morale': np.random.uniform(0, 10, 100),
        'communication_score': np.random.uniform(0, 10, 100),
        'strategy_score': np.random.uniform(0, 10, 100),
        'player_performance': np.random.uniform(0, 10, 100),
        'leadership_effectiveness': np.random.uniform(0, 10, 100)
    })
    
    # Evaluate leadership effectiveness
    results = evaluate_leadership_effectiveness(sample_data)
    if results:
        print("Model Performance Metrics:")
        print(f"Mean Squared Error: {results['Mean Squared Error']}")
        print(f"R2 Score: {results['R2 Score']}")
```
