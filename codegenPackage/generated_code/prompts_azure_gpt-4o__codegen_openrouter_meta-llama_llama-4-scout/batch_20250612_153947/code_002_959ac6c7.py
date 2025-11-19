"""
Generated Code Metadata:
========================
Original URL: https://asfcsc.pages.dev
Prompt: Generate code to simulate an AI-driven early warning system (EWS) that predicts non-communicable diseases like diabetes or strokes, leveraging BitDoctor's hyper-personalized AI model.
Generated: DETERMINISTIC_959ac6c7c03aa68f
Batch ID: 20250612_153947
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# Import required libraries
import pandas as pd
from sklearn.model_selection import train_test_split 
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score, classification_report, confusion_matrix
import numpy as np

# Define a class for the Early Warning System
class EarlyWarningSystem:
    def __init__(self, data):
        """
        Initialize the Early Warning System with a dataset.

        Args:
        - data (pandas.DataFrame): A DataFrame containing the dataset.
        """
        self.data = data

    def preprocess_data(self):
        """
        Preprocess the data by handling missing values and encoding categorical variables.

        Returns:
        - preprocessed_data (pandas.DataFrame): The preprocessed dataset.
        """
        # Handle missing values
        self.data.fillna(self.data.mean(), inplace=True)

        # Encode categorical variables
        categorical_cols = self.data.select_dtypes(include=['object']).columns
        self.data[categorical_cols] = self.data[categorical_cols].apply(lambda x: pd.factorize(x)[0])

        return self.data

    def split_data(self):
        """
        Split the preprocessed data into training and testing sets.

        Returns:
        - X_train (pandas.DataFrame): The training features.
        - X_test (pandas.DataFrame): The testing features.
        - y_train (pandas.Series): The training target variable.
        - y_test (pandas.Series): The testing target variable.
        """
        # Define the feature columns and target column
        feature_cols = self.data.columns[:-1]
        target_col = self.data.columns[-1]

        # Split the data into training and testing sets
        X = self.data[feature_cols]
        y = self.data[target_col]
        X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

        return X_train, X_test, y_train, y_test

    def train_model(self, X_train, y_train):
        """
        Train a random forest classifier model on the training data.

        Args:
        - X_train (pandas.DataFrame): The training features.
        - y_train (pandas.Series): The training target variable.

        Returns:
        - model (sklearn.ensemble.RandomForestClassifier): The trained model.
        """
        # Train a random forest classifier model
        model = RandomForestClassifier(n_estimators=100, random_state=42)
        model.fit(X_train, y_train)

        return model

    def evaluate_model(self, model, X_test, y_test):
        """
        Evaluate the performance of the trained model on the testing data.

        Args:
        - model (sklearn.ensemble.RandomForestClassifier): The trained model.
        - X_test (pandas.DataFrame): The testing features.
        - y_test (pandas.Series): The testing target variable.

        Returns:
        - accuracy (float): The accuracy of the model.
        - report (str): The classification report.
        - matrix (numpy.ndarray): The confusion matrix.
        """
        # Make predictions on the testing data
        y_pred = model.predict(X_test)

        # Evaluate the model's performance
        accuracy = accuracy_score(y_test, y_pred)
        report = classification_report(y_test, y_pred)
        matrix = confusion_matrix(y_test, y_pred)

        return accuracy, report, matrix

    def predict(self, model, data):
        """
        Make predictions on new, unseen data using the trained model.

        Args:
        - model (sklearn.ensemble.RandomForestClassifier): The trained model.
        - data (pandas.DataFrame): The new data to make predictions on.

        Returns:
        - predictions (numpy.ndarray): The predicted probabilities.
        """
        # Make predictions on the new data
        predictions = model.predict_proba(data)

        return predictions

# Example usage
if __name__ == "__main__":
    # Generate sample data
    np.random.seed(42)
    data = pd.DataFrame({
        'age': np.random.randint(18, 100, size=1000),
        'bmi': np.random.uniform(15, 40, size=1000),
        'blood_pressure': np.random.randint(90, 140, size=1000),
        'diabetes': np.random.randint(0, 2, size=1000)
    })

    # Create an instance of the Early Warning System
    ews = EarlyWarningSystem(data)

    try:
        # Preprocess the data
        preprocessed_data = ews.preprocess_data()

        # Split the data into training and testing sets
        X_train, X_test, y_train, y_test = ews.split_data()

        # Train a model
        model = ews.train_model(X_train, y_train)

        # Evaluate the model's performance
        accuracy, report, matrix = ews.evaluate_model(model, X_test, y_test)
        print(f"Model Accuracy: {accuracy:.3f}")
        print("Classification Report:\n", report)
        print("Confusion Matrix:\n", matrix)

        # Make predictions on new data
        new_data = pd.DataFrame({
            'age': [50],
            'bmi': [30],
            'blood_pressure': [120]
        })
        predictions = ews.predict(model, new_data)
        print("Predicted Probabilities:\n", predictions)

    except Exception as e:
        print("An error occurred: ", str(e))
```
