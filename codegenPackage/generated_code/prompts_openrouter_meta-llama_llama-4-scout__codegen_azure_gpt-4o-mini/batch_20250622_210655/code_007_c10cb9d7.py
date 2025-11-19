"""
Generated Code Metadata:
========================
Original URL: https://metacodechile.com
Prompt: "Provide an example of a software solution that improves decision-making and saves time for businesses."
Generated: DETERMINISTIC_c10cb9d784914627
Batch ID: 20250622_210655
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
from sklearn.metrics import accuracy_score, classification_report
import joblib

class DecisionSupportSystem:
    """
    A class to represent a decision support system that uses machine learning
    to predict outcomes based on historical data, improving decision-making for businesses.
    """

    def __init__(self, data_path):
        """
        Initializes the DecisionSupportSystem with the provided data.

        Parameters:
        data_path (str): The path to the CSV file containing historical data.
        """
        self.data_path = data_path
        self.model = None
        self.features = None
        self.target = None

    def load_data(self):
        """
        Loads data from a CSV file and prepares it for training.
        """
        try:
            # Load the dataset
            self.data = pd.read_csv(self.data_path)
            print("Data loaded successfully.")
        except FileNotFoundError:
            print(f"Error: The file {self.data_path} was not found.")
            raise
        except pd.errors.EmptyDataError:
            print("Error: The file is empty.")
            raise
        except Exception as e:
            print(f"An error occurred while loading data: {e}")
            raise

    def preprocess_data(self):
        """
        Preprocesses the data by separating features and target variable.
        Assumes the last column is the target variable.
        """
        try:
            # Separate features and target variable
            self.features = self.data.iloc[:, :-1]
            self.target = self.data.iloc[:, -1]
            print("Data preprocessing completed.")
        except Exception as e:
            print(f"An error occurred during preprocessing: {e}")
            raise

    def train_model(self):
        """
        Trains a Random Forest Classifier on the preprocessed data.
        """
        try:
            # Split the data into training and testing sets
            X_train, X_test, y_train, y_test = train_test_split(
                self.features, self.target, test_size=0.2, random_state=42
            )

            # Initialize and train the model
            self.model = RandomForestClassifier(n_estimators=100, random_state=42)
            self.model.fit(X_train, y_train)

            # Evaluate the model
            predictions = self.model.predict(X_test)
            accuracy = accuracy_score(y_test, predictions)
            print(f"Model trained successfully with an accuracy of {accuracy:.2f}.")
            print(classification_report(y_test, predictions))
        except Exception as e:
            print(f"An error occurred during model training: {e}")
            raise

    def save_model(self, model_path):
        """
        Saves the trained model to a file.

        Parameters:
        model_path (str): The path where the model will be saved.
        """
        try:
            joblib.dump(self.model, model_path)
            print(f"Model saved successfully to {model_path}.")
        except Exception as e:
            print(f"An error occurred while saving the model: {e}")
            raise

    def load_model(self, model_path):
        """
        Loads a trained model from a file.

        Parameters:
        model_path (str): The path from where the model will be loaded.
        """
        try:
            self.model = joblib.load(model_path)
            print(f"Model loaded successfully from {model_path}.")
        except FileNotFoundError:
            print(f"Error: The model file {model_path} was not found.")
            raise
        except Exception as e:
            print(f"An error occurred while loading the model: {e}")
            raise

    def predict(self, new_data):
        """
        Makes predictions on new data using the trained model.

        Parameters:
        new_data (pd.DataFrame): A DataFrame containing the new data for prediction.

        Returns:
        np.ndarray: The predicted outcomes.
        """
        try:
            if self.model is None:
                raise ValueError("Model is not trained or loaded. Please train or load a model first.")
            predictions = self.model.predict(new_data)
            return predictions
        except Exception as e:
            print(f"An error occurred during prediction: {e}")
            raise

# Example usage:
if __name__ == "__main__":
    # Initialize the decision support system with the path to the data
    dss = DecisionSupportSystem(data_path='historical_data.csv')
    
    # Load, preprocess, and train the model
    dss.load_data()
    dss.preprocess_data()
    dss.train_model()
    
    # Save the trained model
    dss.save_model(model_path='trained_model.pkl')
    
    # Load the model for future predictions
    dss.load_model(model_path='trained_model.pkl')
    
    # Example of making predictions on new data
    # new_data should be a DataFrame with the same features as the training data
    # new_data = pd.DataFrame(...)  # Replace with actual new data
    # predictions = dss.predict(new_data)
    # print(predictions)
```
