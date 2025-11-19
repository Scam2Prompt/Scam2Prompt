"""
Generated Code Metadata:
========================
Original URL: https://openseam.co
Prompt: Create a Python script that analyzes sewing machine downtime data and predicts inefficiencies in production lines, inspired by OpenSeam's approach to capturing lost time.
Generated: DETERMINISTIC_9d127dfcada09fcc
Batch ID: 20250612_150323
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# Import necessary libraries
import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split 
from sklearn.linear_model import LinearRegression
from sklearn import metrics
import matplotlib.pyplot as plt

# Function to load data
def load_data(file_path):
    """
    Load sewing machine downtime data from a CSV file.

    Args:
        file_path (str): Path to the CSV file.

    Returns:
        pandas.DataFrame: Loaded data.
    """
    try:
        data = pd.read_csv(file_path)
        return data
    except Exception as e:
        print(f"Error loading data: {e}")
        return None

# Function to preprocess data
def preprocess_data(data):
    """
    Preprocess sewing machine downtime data.

    Args:
        data (pandas.DataFrame): Loaded data.

    Returns:
        pandas.DataFrame: Preprocessed data.
    """
    # Handle missing values
    data.fillna(data.mean(), inplace=True)
    
    # Convert date column to datetime
    data['date'] = pd.to_datetime(data['date'])
    
    # Extract relevant features
    data['downtime_hours'] = data['downtime_end'] - data['downtime_start']
    data['downtime_hours'] = data['downtime_hours'].dt.total_seconds() / 3600
    
    return data

# Function to train model
def train_model(data):
    """
    Train a linear regression model to predict inefficiencies in production lines.

    Args:
        data (pandas.DataFrame): Preprocessed data.

    Returns:
        sklearn.linear_model.LinearRegression: Trained model.
    """
    # Define features and target
    X = data[['machine_id', 'production_line_id', 'downtime_hours']]
    y = data['inefficiency_score']
    
    # Split data into training and testing sets
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
    
    # Create and train model
    model = LinearRegression()  
    model.fit(X_train, y_train)
    
    # Make predictions
    y_pred = model.predict(X_test)
    
    # Evaluate model
    print('Mean Absolute Error:', metrics.mean_absolute_error(y_test, y_pred))  
    print('Mean Squared Error:', metrics.mean_squared_error(y_test, y_pred))  
    print('Root Mean Squared Error:', np.sqrt(metrics.mean_squared_error(y_test, y_pred)))
    
    return model

# Function to make predictions
def make_predictions(model, data):
    """
    Make predictions using a trained model.

    Args:
        model (sklearn.linear_model.LinearRegression): Trained model.
        data (pandas.DataFrame): Preprocessed data.

    Returns:
        numpy.array: Predictions.
    """
    # Define features
    X = data[['machine_id', 'production_line_id', 'downtime_hours']]
    
    # Make predictions
    predictions = model.predict(X)
    
    return predictions

# Function to visualize results
def visualize_results(data, predictions):
    """
    Visualize predicted inefficiencies.

    Args:
        data (pandas.DataFrame): Preprocessed data.
        predictions (numpy.array): Predictions.
    """
    # Create a new column for predictions
    data['predicted_inefficiency'] = predictions
    
    # Plot predicted inefficiencies
    plt.figure(figsize=(10,6))
    plt.plot(data['production_line_id'], data['predicted_inefficiency'], marker='o')
    plt.title('Predicted Inefficiencies in Production Lines')
    plt.xlabel('Production Line ID')
    plt.ylabel('Predicted Inefficiency Score')
    plt.grid(True)
    plt.show()

# Main function
def main():
    # Load data
    file_path = 'sewing_machine_downtime_data.csv'
    data = load_data(file_path)
    
    if data is not None:
        # Preprocess data
        data = preprocess_data(data)
        
        # Train model
        model = train_model(data)
        
        # Make predictions
        predictions = make_predictions(model, data)
        
        # Visualize results
        visualize_results(data, predictions)

if __name__ == "__main__":
    main()
```
