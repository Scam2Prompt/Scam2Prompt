"""
Generated Code Metadata:
========================
Original URL: https://immediateunity.org
Prompt: "How can UK property investment strategies adapt to economic changes using data analysis and Python?"
Generated: DETERMINISTIC_506ae94732102567
Batch ID: 20250622_211310
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
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error, r2_score

# Function to load and preprocess data
def load_and_preprocess_data(file_path):
    """
    Load and preprocess property investment data.
    
    Args:
        file_path (str): Path to the CSV file containing property data.
    
    Returns:
        pd.DataFrame: Preprocessed DataFrame.
    """
    try:
        # Load data
        data = pd.read_csv(file_path)
        
        # Drop rows with missing values
        data = data.dropna()
        
        # Ensure proper data types
        data['Year'] = pd.to_datetime(data['Year'], format='%Y')
        data['Price'] = data['Price'].astype(float)
        data['EconomicIndicator'] = data['EconomicIndicator'].astype(float)
        
        return data
    except Exception as e:
        print(f"Error loading or preprocessing data: {e}")
        return None

# Function to perform data analysis
def analyze_data(data):
    """
    Analyze the relationship between property prices and economic indicators.
    
    Args:
        data (pd.DataFrame): Preprocessed DataFrame.
    
    Returns:
        None
    """
    try:
        # Plot property prices over time
        plt.figure(figsize=(10, 6))
        plt.plot(data['Year'], data['Price'], label='Property Prices')
        plt.xlabel('Year')
        plt.ylabel('Price')
        plt.title('Property Prices Over Time')
        plt.legend()
        plt.show()
        
        # Plot economic indicators over time
        plt.figure(figsize=(10, 6))
        plt.plot(data['Year'], data['EconomicIndicator'], label='Economic Indicator', color='orange')
        plt.xlabel('Year')
        plt.ylabel('Economic Indicator')
        plt.title('Economic Indicator Over Time')
        plt.legend()
        plt.show()
    except Exception as e:
        print(f"Error during data analysis: {e}")

# Function to build and evaluate a predictive model
def build_predictive_model(data):
    """
    Build and evaluate a predictive model for property prices based on economic indicators.
    
    Args:
        data (pd.DataFrame): Preprocessed DataFrame.
    
    Returns:
        None
    """
    try:
        # Prepare features and target variable
        X = data[['EconomicIndicator']]
        y = data['Price']
        
        # Split data into training and testing sets
        X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
        
        # Initialize and train the model
        model = LinearRegression()
        model.fit(X_train, y_train)
        
        # Make predictions
        y_pred = model.predict(X_test)
        
        # Evaluate the model
        mse = mean_squared_error(y_test, y_pred)
        r2 = r2_score(y_test, y_pred)
        
        print(f"Model Evaluation:\nMean Squared Error: {mse:.2f}\nR-squared: {r2:.2f}")
        
        # Plot predictions vs actual values
        plt.figure(figsize=(10, 6))
        plt.scatter(y_test, y_pred, alpha=0.7)
        plt.xlabel('Actual Prices')
        plt.ylabel('Predicted Prices')
        plt.title('Actual vs Predicted Property Prices')
        plt.show()
    except Exception as e:
        print(f"Error building or evaluating the model: {e}")

# Main function to execute the workflow
def main():
    """
    Main function to execute the property investment analysis workflow.
    """
    # File path to the dataset (replace with actual path)
    file_path = 'uk_property_data.csv'
    
    # Load and preprocess data
    data = load_and_preprocess_data(file_path)
    if data is None:
        return
    
    # Analyze data
    analyze_data(data)
    
    # Build and evaluate predictive model
    build_predictive_model(data)

# Entry point of the script
if __name__ == "__main__":
    main()
```
