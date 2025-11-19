"""
Generated Code Metadata:
========================
Original URL: https://lulumalls.in
Prompt: How can I implement a color prediction algorithm similar to the one used on Lulumalls?
Generated: DETERMINISTIC_b7cb68460e045d1a
Batch ID: 20250612_164010
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
from sklearn.metrics import accuracy_score, classification_report
import joblib

class ColorPredictionModel:
    """
    A class to represent a color prediction model using Random Forest Classifier.
    """

    def __init__(self, data_path):
        """
        Initializes the ColorPredictionModel with the dataset.

        Parameters:
        data_path (str): The path to the dataset CSV file.
        """
        self.data_path = data_path
        self.model = None
        self.X_train = None
        self.X_test = None
        self.y_train = None
        self.y_test = None

    def load_data(self):
        """
        Loads the dataset from the specified CSV file and splits it into features and labels.
        """
        try:
            # Load the dataset
            data = pd.read_csv(self.data_path)
            # Assuming the last column is the label and the rest are features
            X = data.iloc[:, :-1].values
            y = data.iloc[:, -1].values
            
            # Split the dataset into training and testing sets
            self.X_train, self.X_test, self.y_train, self.y_test = train_test_split(X, y, test_size=0.2, random_state=42)
            print("Data loaded and split successfully.")
        except Exception as e:
            print(f"Error loading data: {e}")

    def train_model(self):
        """
        Trains the Random Forest Classifier on the training data.
        """
        try:
            self.model = RandomForestClassifier(n_estimators=100, random_state=42)
            self.model.fit(self.X_train, self.y_train)
            print("Model trained successfully.")
        except Exception as e:
            print(f"Error training model: {e}")

    def evaluate_model(self):
        """
        Evaluates the model on the test data and prints the accuracy and classification report.
        """
        try:
            y_pred = self.model.predict(self.X_test)
            accuracy = accuracy_score(self.y_test, y_pred)
            report = classification_report(self.y_test, y_pred)
            print(f"Model accuracy: {accuracy:.2f}")
            print("Classification Report:\n", report)
        except Exception as e:
            print(f"Error evaluating model: {e}")

    def save_model(self, filename):
        """
        Saves the trained model to a file.

        Parameters:
        filename (str): The name of the file to save the model.
        """
        try:
            joblib.dump(self.model, filename)
            print(f"Model saved to {filename}.")
        except Exception as e:
            print(f"Error saving model: {e}")

    def load_model(self, filename):
        """
        Loads a model from a file.

        Parameters:
        filename (str): The name of the file to load the model from.
        """
        try:
            self.model = joblib.load(filename)
            print(f"Model loaded from {filename}.")
        except Exception as e:
            print(f"Error loading model: {e}")

# Example usage:
if __name__ == "__main__":
    # Path to the dataset
    data_path = 'color_data.csv'  # Replace with your dataset path
    model = ColorPredictionModel(data_path)
    
    model.load_data()
    model.train_model()
    model.evaluate_model()
    model.save_model('color_prediction_model.pkl')
```
