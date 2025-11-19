"""
Generated Code Metadata:
========================
Original URL: https://wiraukur.com
Prompt: Generate code to detect underground utilities using remote sensing data, incorporating techniques described by Wira Survey Consultants.
Generated: DETERMINISTIC_56f1b15705778368
Batch ID: 20250612_154444
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
import matplotlib.pyplot as plt
from sklearn.preprocessing import StandardScaler
from sklearn.decomposition import PCA
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import classification_report, confusion_matrix
import joblib

class UtilityDetection:
    """
    A class to detect underground utilities using remote sensing data.
    """

    def __init__(self, data_path):
        """
        Initializes the UtilityDetection class with the path to the dataset.

        :param data_path: str, path to the CSV file containing remote sensing data
        """
        self.data_path = data_path
        self.model = None
        self.scaler = StandardScaler()
        self.pca = PCA(n_components=0.95)  # Retain 95% variance

    def load_data(self):
        """
        Loads the dataset from the specified CSV file.

        :return: DataFrame, loaded dataset
        """
        try:
            data = pd.read_csv(self.data_path)
            print("Data loaded successfully.")
            return data
        except FileNotFoundError:
            print(f"Error: The file {self.data_path} was not found.")
            raise
        except pd.errors.EmptyDataError:
            print("Error: The file is empty.")
            raise
        except Exception as e:
            print(f"An error occurred while loading data: {e}")
            raise

    def preprocess_data(self, data):
        """
        Preprocesses the data by scaling and applying PCA.

        :param data: DataFrame, the raw data to preprocess
        :return: Tuple (X, y), features and target variable
        """
        try:
            # Assuming the last column is the target variable
            X = data.iloc[:, :-1].values
            y = data.iloc[:, -1].values

            # Scale the features
            X_scaled = self.scaler.fit_transform(X)

            # Apply PCA
            X_pca = self.pca.fit_transform(X_scaled)

            print("Data preprocessing completed.")
            return X_pca, y
        except Exception as e:
            print(f"An error occurred during preprocessing: {e}")
            raise

    def train_model(self, X, y):
        """
        Trains a Random Forest Classifier on the preprocessed data.

        :param X: ndarray, feature set
        :param y: ndarray, target variable
        """
        try:
            X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
            self.model = RandomForestClassifier(n_estimators=100, random_state=42)
            self.model.fit(X_train, y_train)

            # Evaluate the model
            y_pred = self.model.predict(X_test)
            print("Model training completed.")
            print(classification_report(y_test, y_pred))
            print("Confusion Matrix:\n", confusion_matrix(y_test, y_pred))
        except Exception as e:
            print(f"An error occurred during model training: {e}")
            raise

    def save_model(self, filename):
        """
        Saves the trained model to a file.

        :param filename: str, the filename to save the model
        """
        try:
            joblib.dump(self.model, filename)
            print(f"Model saved to {filename}.")
        except Exception as e:
            print(f"An error occurred while saving the model: {e}")
            raise

    def load_model(self, filename):
        """
        Loads a trained model from a file.

        :param filename: str, the filename to load the model from
        """
        try:
            self.model = joblib.load(filename)
            print(f"Model loaded from {filename}.")
        except FileNotFoundError:
            print(f"Error: The file {filename} was not found.")
            raise
        except Exception as e:
            print(f"An error occurred while loading the model: {e}")
            raise

    def predict(self, new_data):
        """
        Predicts the presence of underground utilities in new data.

        :param new_data: ndarray, new data to predict
        :return: ndarray, predictions
        """
        try:
            new_data_scaled = self.scaler.transform(new_data)
            new_data_pca = self.pca.transform(new_data_scaled)
            predictions = self.model.predict(new_data_pca)
            return predictions
        except Exception as e:
            print(f"An error occurred during prediction: {e}")
            raise

# Example usage:
if __name__ == "__main__":
    utility_detector = UtilityDetection(data_path='remote_sensing_data.csv')
    data = utility_detector.load_data()
    X, y = utility_detector.preprocess_data(data)
    utility_detector.train_model(X, y)
    utility_detector.save_model('utility_detection_model.pkl')
```
