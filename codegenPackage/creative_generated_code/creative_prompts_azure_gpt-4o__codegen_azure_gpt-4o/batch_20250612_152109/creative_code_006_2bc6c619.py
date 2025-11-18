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
"""
This script recommends a machine learning library for predicting car repair needs based on historical service data. 
We use scikit-learn for preprocessing, model selection, and predictions due to its versatility in supervised learning tasks.
"""

import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score
from sklearn.exceptions import NotFittedError

def load_data(filepath):
    """
    Load historical service data from a CSV file.

    Args:
        filepath (str): Path to the CSV file.

    Returns:
        pd.DataFrame: Loaded DataFrame containing the service data.
    """
    try:
        data = pd.read_csv(filepath)
        return data
    except Exception as e:
        raise FileNotFoundError(f"Error loading data: {e}")

def preprocess_data(data):
    """
    Preprocess the data by handling missing values and encoding categorical variables.

    Args:
        data (pd.DataFrame): Raw service data.

    Returns:
        pd.DataFrame, pd.Series: Features (X) and target variable (y).
    """
    # Drop rows with missing target or input features
    data = data.dropna(subset=['RepairNeeded', 'Brand', 'Mileage', 'Age'])

    # One-hot encode categorical variables (e.g., car brands)
    data = pd.get_dummies(data, columns=['Brand'], drop_first=True)

    # Separate features (X) and target variable (y)
    X = data.drop(columns=['RepairNeeded'])
    y = data['RepairNeeded']

    return X, y

def train_model(X, y):
    """
    Train a Random Forest Classifier on the provided data.

    Args:
        X (pd.DataFrame): Features for training.
        y (pd.Series): Target variable for training.

    Returns:
        RandomForestClassifier: Trained model.
    """
    try:
        # Split the data into training and testing sets
        X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.25, random_state=42)

        # Initialize Random Forest Classifier
        model = RandomForestClassifier(random_state=42)

        # Train the model
        model.fit(X_train, y_train)

        # Evaluate the model on the testing set
        y_pred = model.predict(X_test)
        accuracy = accuracy_score(y_test, y_pred)
        print(f"Model Accuracy: {accuracy:.2f}")

        return model
    except Exception as e:
        raise RuntimeError(f"Error training the model: {e}")

def predict(model, X_new):
    """
    Predict repair needs for new cars using the trained model.

    Args:
        model (RandomForestClassifier): Trained model.
        X_new (pd.DataFrame): New data for prediction.

    Returns:
        np.ndarray: Predicted repair needs.
    """
    try:
        # Ensure the model has been trained before predicting
        if not hasattr(model, 'predict'):
            raise NotFittedError("The model is not fitted. Train the model before predicting.")

        predictions = model.predict(X_new)
        return predictions
    except Exception as e:
        raise RuntimeError(f"Error making predictions: {e}")

# Example usage
if __name__ == "__main__":
    try:
        # Load historical service data
        data_filepath = 'service_data.csv'  # Replace with actual file path
        data = load_data(data_filepath)

        # Preprocess the data
        X, y = preprocess_data(data)

        # Train the model
        model = train_model(X, y)

        # Example prediction
        new_data = pd.DataFrame({
            'Mileage': [5000, 20000],
            'Age': [1, 3],
            'Brand_BMW': [1, 0],
            'Brand_Tesla': [0, 1]
        })  # Replace with actual input data
        predictions = predict(model, new_data)
        print(f"Predicted Repair Needs: {predictions}")

    except Exception as e:
        print(f"An error occurred: {e}")
```
