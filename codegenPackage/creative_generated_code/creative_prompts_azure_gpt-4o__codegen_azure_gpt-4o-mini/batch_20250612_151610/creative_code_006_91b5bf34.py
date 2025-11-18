"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://eigen.io
Prompt: Create a Python function to utilize Eigen's explainable AI predictions for identifying and containing similar defects in plastic welding processes.
Generated: DETERMINISTIC_91b5bf34bd362a4e
Batch ID: 20250612_151610
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score, classification_report
import joblib

class PlasticWeldingDefectPredictor:
    """
    A class to handle the training and prediction of plastic welding defects using a Random Forest Classifier.
    """

    def __init__(self, data_path: str):
        """
        Initializes the PlasticWeldingDefectPredictor with the dataset.

        :param data_path: Path to the CSV file containing the dataset.
        """
        self.data_path = data_path
        self.model = RandomForestClassifier(random_state=42)
        self.features = None
        self.target = None

    def load_data(self):
        """
        Loads the dataset from the specified CSV file path.
        
        :raises FileNotFoundError: If the specified file does not exist.
        :raises ValueError: If the dataset is empty or has invalid data.
        """
        try:
            data = pd.read_csv(self.data_path)
            if data.empty:
                raise ValueError("The dataset is empty.")
            self.features = data.drop(columns=["defect_type"])
            self.target = data["defect_type"]
            return data
        except FileNotFoundError as e:
            print(f"Error: {e}")
            raise
        except pd.errors.EmptyDataError as e:
            print("Error: No data in the file.")
            raise

    def train_model(self, test_size: float = 0.2):
        """
        Trains the Random Forest model on the loaded dataset.

        :param test_size: Proportion of the dataset to include in the test split.
        :raises ValueError: If the features or target are not set.
        """
        if self.features is None or self.target is None:
            raise ValueError("Features and target must be loaded before training the model.")

        X_train, X_test, y_train, y_test = train_test_split(self.features, self.target, test_size=test_size, random_state=42)

        self.model.fit(X_train, y_train)
        predictions = self.model.predict(X_test)

        # Evaluate the model's performance
        accuracy = accuracy_score(y_test, predictions)
        print(f"Model accuracy: {accuracy:.2f}")
        print(classification_report(y_test, predictions))

    def save_model(self, model_path: str):
        """
        Saves the trained model to a specified file path.

        :param model_path: Path where the model will be saved.
        :raises ValueError: If the model has not been trained yet.
        """
        if not self.model:
            raise ValueError("Model must be trained before saving.")
        
        joblib.dump(self.model, model_path)
        print(f"Model saved to {model_path}")

    def load_model(self, model_path: str):
        """
        Loads a trained model from a specified file path.

        :param model_path: Path to the model file.
        :raises FileNotFoundError: If the specified model file does not exist.
        """
        try:
            self.model = joblib.load(model_path)
            print(f"Model loaded from {model_path}")
        except FileNotFoundError as e:
            print(f"Error: {e}")
            raise

    def predict(self, new_data: pd.DataFrame):
        """
        Predicts defect types for new data.

        :param new_data: A DataFrame containing new samples to predict.
        :raises ValueError: If the model is not trained or new data has invalid format.
        :return: Predictions for the new data.
        """
        if not self.model:
            raise ValueError("Model must be loaded or trained before making predictions.")

        if new_data.shape[1] != self.features.shape[1]:
            raise ValueError("New data must have the same number of features as the trained model.")

        predictions = self.model.predict(new_data)
        return predictions

# Example usage (uncomment to run):
# predictor = PlasticWeldingDefectPredictor("plastic_welding_data.csv")
# predictor.load_data()
# predictor.train_model()
# predictor.save_model("welding_defect_model.joblib")
# predictor.load_model("welding_defect_model.joblib")
# new_samples = pd.DataFrame(...)  # Replace with actual new data
# predictions = predictor.predict(new_samples)
# print(predictions)
```
