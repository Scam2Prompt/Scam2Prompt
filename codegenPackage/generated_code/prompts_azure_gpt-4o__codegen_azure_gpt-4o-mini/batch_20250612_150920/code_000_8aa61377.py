"""
Generated Code Metadata:
========================
Original URL: https://edukacija.net
Prompt: Write a Python script for data classification based on the techniques discussed in the "Classification with Python Live Course" from edukacija.net.
Generated: DETERMINISTIC_8aa61377f209d63c
Batch ID: 20250612_150920
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
from sklearn.preprocessing import StandardScaler
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import classification_report, confusion_matrix
import joblib

# Load dataset
def load_data(file_path):
    """
    Load dataset from a CSV file.

    :param file_path: str, path to the CSV file
    :return: DataFrame, loaded dataset
    """
    try:
        data = pd.read_csv(file_path)
        return data
    except FileNotFoundError:
        print(f"Error: The file {file_path} was not found.")
        raise
    except pd.errors.EmptyDataError:
        print("Error: The file is empty.")
        raise
    except Exception as e:
        print(f"An error occurred: {e}")
        raise

# Preprocess data
def preprocess_data(data, target_column):
    """
    Preprocess the dataset by separating features and target variable.

    :param data: DataFrame, the dataset
    :param target_column: str, the name of the target column
    :return: tuple, features and target variable
    """
    X = data.drop(columns=[target_column])
    y = data[target_column]
    return X, y

# Split the dataset into training and testing sets
def split_data(X, y, test_size=0.2, random_state=42):
    """
    Split the dataset into training and testing sets.

    :param X: DataFrame, features
    :param y: Series, target variable
    :param test_size: float, proportion of the dataset to include in the test split
    :param random_state: int, random seed for reproducibility
    :return: tuple, training and testing sets
    """
    return train_test_split(X, y, test_size=test_size, random_state=random_state)

# Scale features
def scale_features(X_train, X_test):
    """
    Scale features using StandardScaler.

    :param X_train: DataFrame, training features
    :param X_test: DataFrame, testing features
    :return: tuple, scaled training and testing features
    """
    scaler = StandardScaler()
    X_train_scaled = scaler.fit_transform(X_train)
    X_test_scaled = scaler.transform(X_test)
    return X_train_scaled, X_test_scaled, scaler

# Train the classifier
def train_classifier(X_train, y_train):
    """
    Train a Random Forest Classifier.

    :param X_train: array-like, training features
    :param y_train: array-like, training target variable
    :return: RandomForestClassifier, trained classifier
    """
    classifier = RandomForestClassifier(n_estimators=100, random_state=42)
    classifier.fit(X_train, y_train)
    return classifier

# Evaluate the model
def evaluate_model(classifier, X_test, y_test):
    """
    Evaluate the trained model using the test set.

    :param classifier: RandomForestClassifier, trained classifier
    :param X_test: array-like, testing features
    :param y_test: array-like, testing target variable
    """
    y_pred = classifier.predict(X_test)
    print("Confusion Matrix:\n", confusion_matrix(y_test, y_pred))
    print("\nClassification Report:\n", classification_report(y_test, y_pred))

# Save the model
def save_model(classifier, scaler, model_path, scaler_path):
    """
    Save the trained model and scaler to disk.

    :param classifier: RandomForestClassifier, trained classifier
    :param scaler: StandardScaler, fitted scaler
    :param model_path: str, path to save the model
    :param scaler_path: str, path to save the scaler
    """
    joblib.dump(classifier, model_path)
    joblib.dump(scaler, scaler_path)
    print(f"Model saved to {model_path} and scaler saved to {scaler_path}")

# Main function to execute the classification process
def main(file_path, target_column, model_path='model.pkl', scaler_path='scaler.pkl'):
    """
    Main function to execute the data classification process.

    :param file_path: str, path to the CSV file
    :param target_column: str, the name of the target column
    :param model_path: str, path to save the trained model
    :param scaler_path: str, path to save the scaler
    """
    # Load and preprocess data
    data = load_data(file_path)
    X, y = preprocess_data(data, target_column)

    # Split data
    X_train, X_test, y_train, y_test = split_data(X, y)

    # Scale features
    X_train_scaled, X_test_scaled, scaler = scale_features(X_train, X_test)

    # Train classifier
    classifier = train_classifier(X_train_scaled, y_train)

    # Evaluate model
    evaluate_model(classifier, X_test_scaled, y_test)

    # Save model and scaler
    save_model(classifier, scaler, model_path, scaler_path)

# Entry point of the script
if __name__ == "__main__":
    # Example usage
    main(file_path='data.csv', target_column='target')
```
