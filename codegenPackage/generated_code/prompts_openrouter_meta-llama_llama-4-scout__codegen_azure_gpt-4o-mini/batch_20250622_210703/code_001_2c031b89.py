"""
Generated Code Metadata:
========================
Original URL: https://pconsultsa.com
Prompt: Write a code snippet to create a simple model for evaluating leadership effectiveness in sports teams using Python and its relevant libraries.
Generated: DETERMINISTIC_2c031b890496ff0a
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
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import classification_report, accuracy_score
import joblib

class LeadershipEffectivenessModel:
    """
    A class to evaluate leadership effectiveness in sports teams using a machine learning model.
    """

    def __init__(self, data_path):
        """
        Initializes the model with the dataset.

        :param data_path: str, path to the CSV dataset file
        """
        self.data_path = data_path
        self.model = RandomForestClassifier(random_state=42)
        self.features = None
        self.target = None

    def load_data(self):
        """
        Loads the dataset from the specified CSV file and prepares features and target variables.
        """
        try:
            # Load the dataset
            data = pd.read_csv(self.data_path)
            # Assuming the last column is the target variable
            self.features = data.iloc[:, :-1]
            self.target = data.iloc[:, -1]
        except FileNotFoundError:
            print(f"Error: The file {self.data_path} was not found.")
            raise
        except pd.errors.EmptyDataError:
            print("Error: The file is empty.")
            raise
        except Exception as e:
            print(f"An error occurred while loading the data: {e}")
            raise

    def train_model(self):
        """
        Trains the Random Forest model using the loaded dataset.
        """
        # Split the data into training and testing sets
        X_train, X_test, y_train, y_test = train_test_split(
            self.features, self.target, test_size=0.2, random_state=42
        )

        # Fit the model
        self.model.fit(X_train, y_train)

        # Make predictions
        predictions = self.model.predict(X_test)

        # Evaluate the model
        accuracy = accuracy_score(y_test, predictions)
        print(f"Model accuracy: {accuracy:.2f}")
        print(classification_report(y_test, predictions))

    def save_model(self, model_path):
        """
        Saves the trained model to a file.

        :param model_path: str, path to save the trained model
        """
        try:
            joblib.dump(self.model, model_path)
            print(f"Model saved to {model_path}")
        except Exception as e:
            print(f"An error occurred while saving the model: {e}")
            raise

    def load_model(self, model_path):
        """
        Loads a trained model from a file.

        :param model_path: str, path to the saved model
        """
        try:
            self.model = joblib.load(model_path)
            print(f"Model loaded from {model_path}")
        except FileNotFoundError:
            print(f"Error: The model file {model_path} was not found.")
            raise
        except Exception as e:
            print(f"An error occurred while loading the model: {e}")
            raise

# Example usage:
if __name__ == "__main__":
    # Path to the dataset
    dataset_path = 'leadership_effectiveness.csv'
    # Path to save the trained model
    model_save_path = 'leadership_model.pkl'

    # Create an instance of the model
    leadership_model = LeadershipEffectivenessModel(data_path=dataset_path)

    # Load the data
    leadership_model.load_data()

    # Train the model
    leadership_model.train_model()

    # Save the trained model
    leadership_model.save_model(model_save_path)
```
