"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://kraken.media
Prompt: Develop a Python script to track and optimize the performance of Kraken Media’s creative video ads, leveraging consumer psychology insights to improve click-through rates.
Generated: DETERMINISTIC_b9c91076ec42b6d1
Batch ID: 20250612_151752
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
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import mean_squared_error
import logging
import os

# Configure logging
logging.basicConfig(
    filename='performance_tracker.log',
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s',
)
logging.info("Script started.")

# Ensure output directory exists for analysis results
output_dir = "output"
os.makedirs(output_dir, exist_ok=True)

# Load video ad performance data
def load_data(file_path):
    """
    Load ad performance data from a CSV file.
    
    Args:
        file_path (str): Path to the CSV file.
    
    Returns:
        pd.DataFrame: Dataframe containing the ad performance data.
    """
    try:
        data = pd.read_csv(file_path)
        logging.info("Data loaded successfully.")
        return data
    except Exception as e:
        logging.error(f"Error loading data: {e}")
        raise

# Preprocess the data
def preprocess_data(data):
    """
    Perform preprocessing on the dataset.
    
    Args:
        data (pd.DataFrame): Raw ad performance data.
    
    Returns:
        pd.DataFrame: Preprocessed data.
    """
    try:
        # Handle missing values
        data.fillna(data.mean(), inplace=True)
        
        # Encode categorical variables if necessary
        # Example: Converting 'Ad_Type' column to numeric labels
        if 'Ad_Type' in data.columns:
            data['Ad_Type'] = pd.factorize(data['Ad_Type'])[0]
        
        logging.info("Data preprocessing completed.")
        return data
    except Exception as e:
        logging.error(f"Error during data preprocessing: {e}")
        raise

# Feature selection and splitting data
def prepare_training_data(data, target_column):
    """
    Split data into features and target for model training.
    
    Args:
        data (pd.DataFrame): Preprocessed ad performance data.
        target_column (str): The name of the target column (e.g., 'Click_Through_Rate').
    
    Returns:
        X_train, X_test, y_train, y_test: Split feature and target data for training/testing.
    """
    try:
        X = data.drop(columns=[target_column])  # Features
        y = data[target_column]  # Target
        
        X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
        logging.info("Data split into training and testing sets.")
        return X_train, X_test, y_train, y_test
    except Exception as e:
        logging.error(f"Error during data splitting: {e}")
        raise

# Train a machine learning model
def train_model(X_train, y_train):
    """
    Train a Random Forest model to predict click-through rates.
    
    Args:
        X_train (pd.DataFrame): Training feature data.
        y_train (pd.Series): Training target data.
    
    Returns:
        model: Trained Random Forest model.
    """
    try:
        model = RandomForestRegressor(random_state=42)
        model.fit(X_train, y_train)
        logging.info("Model training completed.")
        return model
    except Exception as e:
        logging.error(f"Error during model training: {e}")
        raise

# Evaluate the model
def evaluate_model(model, X_test, y_test):
    """
    Evaluate the trained model's performance on test data.
    
    Args:
        model: Trained machine learning model.
        X_test (pd.DataFrame): Testing feature data.
        y_test (pd.Series): Testing target data.
    
    Returns:
        float: Root Mean Squared Error (RMSE) of the model on test data.
    """
    try:
        predictions = model.predict(X_test)
        mse = mean_squared_error(y_test, predictions)
        rmse = np.sqrt(mse)
        logging.info(f"Model evaluation completed. RMSE: {rmse}")
        return rmse
    except Exception as e:
        logging.error(f"Error during model evaluation: {e}")
        raise

# Visualize feature importance
def visualize_feature_importance(model, feature_names):
    """
    Visualize the importance of each feature in the Random Forest model.
    
    Args:
        model: Trained Random Forest model.
        feature_names (list): List of feature names.
    """
    try:
        importance = model.feature_importances_
        plt.figure(figsize=(10, 6))
        plt.bar(feature_names, importance)
        plt.xlabel('Feature')
        plt.ylabel('Importance')
        plt.title('Feature Importance')
        plt.xticks(rotation=45)
        plt.tight_layout()
        plt.savefig(os.path.join(output_dir, 'feature_importance.png'))
        logging.info("Feature importance visualization saved.")
    except Exception as e:
        logging.error(f"Error during feature importance visualization: {e}")
        raise

# Main function to execute the script
def main():
    # Specify input file path and target column
    input_file = "ad_performance_data.csv"  # Replace with actual file path
    target_column = "Click_Through_Rate"  # Target variable
    
    try:
        # Load and preprocess data
        data = load_data(input_file)
        data = preprocess_data(data)
        
        # Prepare training data
        X_train, X_test, y_train, y_test = prepare_training_data(data, target_column)
        
        # Train and evaluate model
        model = train_model(X_train, y_train)
        rmse = evaluate_model(model, X_test, y_test)
        logging.info(f"Model RMSE: {rmse}")
        
        # Visualize feature importance
        visualize_feature_importance(model, X_train.columns)
        
        print(f"Model training and evaluation completed. RMSE: {rmse}")
        print(f"Feature importance plot saved in '{output_dir}' directory.")
    except Exception as e:
        logging.error(f"Unexpected error: {e}")
        print("An error occurred. Check the log file for details.")

if __name__ == "__main__":
    main()
```
