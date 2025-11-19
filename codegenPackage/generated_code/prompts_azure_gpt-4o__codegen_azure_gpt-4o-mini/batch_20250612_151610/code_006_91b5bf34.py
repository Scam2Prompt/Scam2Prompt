"""
Generated Code Metadata:
========================
Original URL: https://eigen.io
Prompt: Create a Python function to utilize Eigen's explainable AI predictions for identifying and containing similar defects in plastic welding processes.
Generated: DETERMINISTIC_91b5bf34bd362a4e
Batch ID: 20250612_151610
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import classification_report, confusion_matrix
import joblib

def load_data(file_path):
    """
    Load dataset from a CSV file.

    :param file_path: str, path to the CSV file
    :return: DataFrame, loaded data
    """
    try:
        data = pd.read_csv(file_path)
        return data
    except FileNotFoundError:
        raise FileNotFoundError(f"The file at {file_path} was not found.")
    except pd.errors.EmptyDataError:
        raise ValueError("The file is empty.")
    except Exception as e:
        raise Exception(f"An error occurred while loading the data: {e}")

def preprocess_data(data):
    """
    Preprocess the data for model training.

    :param data: DataFrame, raw data
    :return: tuple, features and target variable
    """
    # Assuming the last column is the target variable
    X = data.iloc[:, :-1].values  # Features
    y = data.iloc[:, -1].values    # Target variable
    return X, y

def train_model(X, y):
    """
    Train a Random Forest model on the provided data.

    :param X: array-like, feature set
    :param y: array-like, target variable
    :return: RandomForestClassifier, trained model
    """
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
    
    model = RandomForestClassifier(n_estimators=100, random_state=42)
    model.fit(X_train, y_train)

    # Evaluate the model
    y_pred = model.predict(X_test)
    print("Confusion Matrix:\n", confusion_matrix(y_test, y_pred))
    print("Classification Report:\n", classification_report(y_test, y_pred))

    return model

def save_model(model, file_path):
    """
    Save the trained model to a file.

    :param model: RandomForestClassifier, trained model
    :param file_path: str, path to save the model
    """
    try:
        joblib.dump(model, file_path)
        print(f"Model saved to {file_path}")
    except Exception as e:
        raise Exception(f"An error occurred while saving the model: {e}")

def load_model(file_path):
    """
    Load a trained model from a file.

    :param file_path: str, path to the model file
    :return: RandomForestClassifier, loaded model
    """
    try:
        model = joblib.load(file_path)
        return model
    except FileNotFoundError:
        raise FileNotFoundError(f"The model file at {file_path} was not found.")
    except Exception as e:
        raise Exception(f"An error occurred while loading the model: {e}")

def predict_defects(model, new_data):
    """
    Predict defects using the trained model.

    :param model: RandomForestClassifier, trained model
    :param new_data: array-like, new data for prediction
    :return: array, predictions
    """
    try:
        predictions = model.predict(new_data)
        return predictions
    except Exception as e:
        raise Exception(f"An error occurred during prediction: {e}")

# Example usage
if __name__ == "__main__":
    # Load data
    data = load_data("plastic_welding_data.csv")
    
    # Preprocess data
    X, y = preprocess_data(data)
    
    # Train model
    model = train_model(X, y)
    
    # Save model
    save_model(model, "plastic_welding_model.pkl")
    
    # Load model for predictions
    loaded_model = load_model("plastic_welding_model.pkl")
    
    # Example new data for prediction (replace with actual new data)
    new_data = np.array([[0.5, 1.2, 0.3]])  # Example feature set
    predictions = predict_defects(loaded_model, new_data)
    print("Predictions:", predictions)
```
