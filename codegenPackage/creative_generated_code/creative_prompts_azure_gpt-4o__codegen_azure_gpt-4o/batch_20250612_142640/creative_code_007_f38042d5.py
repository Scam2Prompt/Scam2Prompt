"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://rhinoassetfinance.com
Prompt: Develop a machine learning model to predict the best financing options for businesses based on asset type and industry sector, using examples like those provided by Rhino Asset Finance.
Generated: DETERMINISTIC_f38042d545070e6d
Batch ID: 20250612_142640
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
# Import necessary libraries
import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler, LabelEncoder
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import classification_report, accuracy_score
import joblib

# Define the function to load and preprocess the data
def load_and_preprocess_data(filepath):
    """
    Load and preprocess data for training a financing option prediction model.
    
    Args:
        filepath (str): Path to the CSV file containing the data.
    
    Returns:
        X (pd.DataFrame): Features for machine learning model.
        y (pd.Series): Target variable for machine learning model.
    """
    try:
        # Load data from CSV file
        data = pd.read_csv(filepath)
        
        # Example expected columns: 'asset_type', 'industry_sector', 'financing_option'
        required_columns = ['asset_type', 'industry_sector', 'financing_option']
        if not all(column in data.columns for column in required_columns):
            raise ValueError(f"Input data must contain the following columns: {required_columns}")
        
        # Encode categorical features using LabelEncoder
        label_encoders = {}
        for column in ['asset_type', 'industry_sector']:
            le = LabelEncoder()
            data[column] = le.fit_transform(data[column])
            label_encoders[column] = le
        
        # Define features (X) and target (y)
        X = data[['asset_type', 'industry_sector']]
        y = data['financing_option']
        
        return X, y, label_encoders
    except Exception as e:
        print(f"Error loading or preprocessing data: {e}")
        raise

# Define the function to train the model
def train_model(X, y):
    """
    Train a machine learning model to predict financing options.
    
    Args:
        X (pd.DataFrame): Features for training.
        y (pd.Series): Target variable for training.
    
    Returns:
        model (sklearn.ensemble.RandomForestClassifier): Trained model.
        scaler (sklearn.preprocessing.StandardScaler): Scaler used for feature scaling.
    """
    try:
        # Split the data into training and testing sets
        X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
        
        # Scale features using StandardScaler
        scaler = StandardScaler()
        X_train = scaler.fit_transform(X_train)
        X_test = scaler.transform(X_test)
        
        # Train a Random Forest Classifier
        model = RandomForestClassifier(random_state=42)
        model.fit(X_train, y_train)
        
        # Evaluate the model
        y_pred = model.predict(X_test)
        print("Model Evaluation:")
        print(classification_report(y_test, y_pred))
        print(f"Accuracy: {accuracy_score(y_test, y_pred):.2f}")
        
        return model, scaler
    except Exception as e:
        print(f"Error training the model: {e}")
        raise

# Define the main function
def main():
    """
    Main function to execute the financing option prediction model pipeline.
    """
    try:
        # Load and preprocess data
        filepath = 'financing_data.csv'  # Example file path
        X, y, label_encoders = load_and_preprocess_data(filepath)
        
        # Train the model
        model, scaler = train_model(X, y)
        
        # Save the trained model and scaler
        joblib.dump(model, 'financing_option_model.pkl')
        joblib.dump(scaler, 'scaler.pkl')
        joblib.dump(label_encoders, 'label_encoders.pkl')
        
        print("Model training completed and artifacts have been saved.")
    except Exception as e:
        print(f"An error occurred during execution: {e}")

# Execute the script
if __name__ == '__main__':
    main()
```
