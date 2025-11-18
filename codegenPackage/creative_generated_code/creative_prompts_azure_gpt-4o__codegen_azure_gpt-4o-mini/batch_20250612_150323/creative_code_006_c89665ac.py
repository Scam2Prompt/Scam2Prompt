"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://openseam.co
Prompt: Develop a machine learning model to predict worker fatigue and proficiency based on time-series data collected from sewing stations, following OpenSeam's focus on upskilling and reskilling.
Generated: DETERMINISTIC_c89665ac26f760cc
Batch ID: 20250612_150323
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
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import classification_report, confusion_matrix
from sklearn.preprocessing import StandardScaler
from sklearn.pipeline import Pipeline
from sklearn.impute import SimpleImputer
import joblib

# Load the dataset
def load_data(file_path):
    """
    Load time-series data from a CSV file.
    
    Parameters:
        file_path (str): Path to the CSV file.
    
    Returns:
        pd.DataFrame: Loaded data.
    """
    try:
        data = pd.read_csv(file_path)
        return data
    except Exception as e:
        print(f"Error loading data: {e}")
        raise

# Preprocess the data
def preprocess_data(data):
    """
    Preprocess the dataset by handling missing values and scaling features.
    
    Parameters:
        data (pd.DataFrame): Raw data to preprocess.
    
    Returns:
        pd.DataFrame: Processed data ready for modeling.
    """
    # Impute missing values and scale features
    imputer = SimpleImputer(strategy='mean')
    scaler = StandardScaler()
    
    # Assume the last column is the target variable and rest are features
    X = data.iloc[:, :-1]
    y = data.iloc[:, -1]

    # Transform features
    X_imputed = imputer.fit_transform(X)
    X_scaled = scaler.fit_transform(X_imputed)
    
    return pd.DataFrame(X_scaled), y

# Train the model
def train_model(X, y):
    """
    Train a RandomForestClassifier on the dataset.
    
    Parameters:
        X (pd.DataFrame): Features for training.
        y (pd.Series): Target variable for training.
    
    Returns:
        RandomForestClassifier: Trained model.
    """
    # Split the dataset into training and testing sets
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

    # Initialize the model
    model = RandomForestClassifier(n_estimators=100, random_state=42)

    # Fit the model
    model.fit(X_train, y_train)

    # Evaluate the model
    y_pred = model.predict(X_test)
    print("Confusion Matrix:\n", confusion_matrix(y_test, y_pred))
    print("Classification Report:\n", classification_report(y_test, y_pred))

    return model

# Save the trained model
def save_model(model, file_path):
    """
    Save the trained model to a file.
    
    Parameters:
        model (RandomForestClassifier): The trained model.
        file_path (str): Path to save the model.
    """
    try:
        joblib.dump(model, file_path)
        print(f"Model saved to {file_path}")
    except Exception as e:
        print(f"Error saving model: {e}")
        raise

# Main function to execute the workflow
def main(file_path, model_save_path):
    """
    Main function to load data, preprocess it, train a model, and save the model.
    
    Parameters:
        file_path (str): Path to the CSV file containing the data.
        model_save_path (str): Path to save the trained model.
    """
    # Load the data
    data = load_data(file_path)
    
    # Preprocess the data
    X, y = preprocess_data(data)
    
    # Train the model
    model = train_model(X, y)
    
    # Save the trained model
    save_model(model, model_save_path)

# Example usage (to be replaced with actual file paths)
if __name__ == "__main__":
    main("sewing_station_data.csv", "fatigue_proficiency_model.pkl")
```
