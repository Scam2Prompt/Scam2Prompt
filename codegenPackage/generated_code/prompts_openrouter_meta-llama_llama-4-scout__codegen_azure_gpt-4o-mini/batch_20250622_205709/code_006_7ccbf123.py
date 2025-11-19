"""
Generated Code Metadata:
========================
Original URL: https://pranaisland.com
Prompt: Develop a recommendation engine for an e-commerce site selling stackable jewelry, using machine learning algorithms and product features like material, price, and elemental theme.
Generated: DETERMINISTIC_7ccbf123ff5a073c
Batch ID: 20250622_205709
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score, classification_report
import joblib

# Load the dataset
def load_data(file_path):
    """
    Load the dataset from a CSV file.

    :param file_path: str - Path to the CSV file containing product data.
    :return: DataFrame - Loaded product data.
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
    Preprocess the data by encoding categorical features and handling missing values.

    :param data: DataFrame - Raw product data.
    :return: DataFrame - Preprocessed product data.
    """
    # Handle missing values
    data.fillna(method='ffill', inplace=True)

    # Encode categorical features
    data = pd.get_dummies(data, columns=['material', 'elemental_theme'], drop_first=True)
    
    return data

# Train the recommendation model
def train_model(data):
    """
    Train a Random Forest Classifier on the product data.

    :param data: DataFrame - Preprocessed product data.
    :return: RandomForestClassifier - Trained model.
    """
    # Define features and target
    X = data.drop('recommended', axis=1)  # Features
    y = data['recommended']  # Target variable

    # Split the data into training and testing sets
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

    # Initialize and train the model
    model = RandomForestClassifier(n_estimators=100, random_state=42)
    model.fit(X_train, y_train)

    # Evaluate the model
    y_pred = model.predict(X_test)
    print(f"Accuracy: {accuracy_score(y_test, y_pred)}")
    print(classification_report(y_test, y_pred))

    return model

# Save the trained model
def save_model(model, file_path):
    """
    Save the trained model to a file.

    :param model: RandomForestClassifier - Trained model to save.
    :param file_path: str - Path to save the model.
    """
    try:
        joblib.dump(model, file_path)
        print(f"Model saved to {file_path}")
    except Exception as e:
        print(f"Error saving model: {e}")
        raise

# Load and preprocess data, train model, and save it
if __name__ == "__main__":
    # Define file paths
    data_file_path = 'stackable_jewelry_data.csv'
    model_file_path = 'recommendation_model.pkl'

    # Load data
    data = load_data(data_file_path)

    # Preprocess data
    processed_data = preprocess_data(data)

    # Train model
    recommendation_model = train_model(processed_data)

    # Save the trained model
    save_model(recommendation_model, model_file_path)
```
