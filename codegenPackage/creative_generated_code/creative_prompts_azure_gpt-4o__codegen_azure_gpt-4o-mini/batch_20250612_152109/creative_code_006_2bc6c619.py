"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://mechanics.ae
Prompt: Recommend a machine learning library for predicting car repair needs based on historical service data, focusing on luxury car brands like Audi, BMW, and Tesla.
Generated: DETERMINISTIC_2bc6c619c35f1b67
Batch ID: 20250612_152109
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import classification_report, confusion_matrix
import joblib
import logging

# Set up logging for debugging purposes
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

def load_data(file_path):
    """
    Load historical service data from a CSV file.
    
    Parameters:
        file_path (str): Path to the CSV file containing service data.

    Returns:
        pd.DataFrame: DataFrame containing the loaded service data.
    """
    try:
        data = pd.read_csv(file_path)
        logging.info("Data loaded successfully from %s", file_path)
        return data
    except Exception as e:
        logging.error("Error loading data: %s", e)
        raise

def preprocess_data(data):
    """
    Preprocess the data for training the model.
    
    Parameters:
        data (pd.DataFrame): Raw service data.

    Returns:
        X (pd.DataFrame): Features for model training.
        y (pd.Series): Target variable for model training.
    """
    try:
        # Drop rows with missing values
        data.dropna(inplace=True)
        
        # Filter for luxury car brands
        luxury_brands = ['Audi', 'BMW', 'Tesla']
        data = data[data['brand'].isin(luxury_brands)]
        
        # Encode categorical variables
        data = pd.get_dummies(data, columns=['service_type', 'brand'], drop_first=True)
        
        # Define feature set and target variable
        X = data.drop('repair_needed', axis=1)  # Features
        y = data['repair_needed']                 # Target variable
        
        logging.info("Data preprocessed successfully")
        return X, y
    except Exception as e:
        logging.error("Error in preprocessing data: %s", e)
        raise

def train_model(X, y):
    """
    Train the Random Forest model on the provided features and target variable.
    
    Parameters:
        X (pd.DataFrame): Features for model training.
        y (pd.Series): Target variable for model training.

    Returns:
        model: Trained machine learning model.
    """
    try:
        # Split the data into training and testing sets
        X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
        
        # Initialize the Random Forest Classifier
        model = RandomForestClassifier(n_estimators=100, random_state=42)
        model.fit(X_train, y_train)  # Train the model
        
        # Predictions and evaluation
        predictions = model.predict(X_test)
        print(classification_report(y_test, predictions))
        print(confusion_matrix(y_test, predictions))
        
        logging.info("Model trained successfully")
        return model
    except Exception as e:
        logging.error("Error during model training: %s", e)
        raise

def save_model(model, filename):
    """
    Save the trained model to a file.
    
    Parameters:
        model: Trained machine learning model.
        filename (str): Filename to save the model.
    """
    try:
        joblib.dump(model, filename)
        logging.info("Model saved successfully to %s", filename)
    except Exception as e:
        logging.error("Error saving model: %s", e)
        raise

if __name__ == "__main__":
    # Example usage
    try:
        data_file = "historical_service_data.csv"  # Path to the historical service data
        data = load_data(data_file)
        X, y = preprocess_data(data)
        model = train_model(X, y)
        save_model(model, "car_repair_predictor_model.joblib")
    except Exception as e:
        logging.critical("An error occurred in the main workflow: %s", e)
```
