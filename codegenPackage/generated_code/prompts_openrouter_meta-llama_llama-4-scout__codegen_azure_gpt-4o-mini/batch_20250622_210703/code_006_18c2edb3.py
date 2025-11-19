"""
Generated Code Metadata:
========================
Original URL: https://guapaaltejer.com
Prompt: Develop a machine learning model to recommend knitting or crochet patterns based on a user's skill level, yarn preferences, and project type.
Generated: DETERMINISTIC_18c2edb3fa117d15
Batch ID: 20250622_210703
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
from sklearn.metrics import classification_report, accuracy_score
import joblib

# Load dataset
def load_data(file_path):
    """
    Load the dataset from a CSV file.

    :param file_path: str, path to the CSV file
    :return: DataFrame, loaded data
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
def preprocess_data(data):
    """
    Preprocess the data for the model.

    :param data: DataFrame, raw data
    :return: DataFrame, processed data
    """
    # Convert categorical variables to numerical
    data = pd.get_dummies(data, columns=['skill_level', 'yarn_preference', 'project_type'], drop_first=True)
    return data

# Train the model
def train_model(X, y):
    """
    Train a Random Forest model.

    :param X: DataFrame, features
    :param y: Series, target variable
    :return: RandomForestClassifier, trained model
    """
    model = RandomForestClassifier(n_estimators=100, random_state=42)
    model.fit(X, y)
    return model

# Evaluate the model
def evaluate_model(model, X_test, y_test):
    """
    Evaluate the trained model.

    :param model: RandomForestClassifier, trained model
    :param X_test: DataFrame, test features
    :param y_test: Series, test target variable
    """
    predictions = model.predict(X_test)
    print("Accuracy:", accuracy_score(y_test, predictions))
    print(classification_report(y_test, predictions))

# Save the model
def save_model(model, file_name):
    """
    Save the trained model to a file.

    :param model: RandomForestClassifier, trained model
    :param file_name: str, name of the file to save the model
    """
    joblib.dump(model, file_name)

# Main function
def main():
    # Load and preprocess data
    data = load_data('knitting_patterns.csv')
    processed_data = preprocess_data(data)

    # Split data into features and target
    X = processed_data.drop('pattern', axis=1)  # Assuming 'pattern' is the target column
    y = processed_data['pattern']

    # Split data into training and testing sets
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

    # Train the model
    model = train_model(X_train, y_train)

    # Evaluate the model
    evaluate_model(model, X_test, y_test)

    # Save the model
    save_model(model, 'knitting_pattern_recommender.pkl')

if __name__ == "__main__":
    main()
```
