"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://asfcsc.pages.dev
Prompt: Generate code to simulate an AI-driven early warning system (EWS) that predicts non-communicable diseases like diabetes or strokes, leveraging BitDoctor's hyper-personalized AI model.
Generated: DETERMINISTIC_959ac6c7c03aa68f
Batch ID: 20250612_153947
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
from sklearn.metrics import classification_report, confusion_matrix
import joblib

class EarlyWarningSystem:
    def __init__(self, data_file):
        """
        Initializes the Early Warning System with the given dataset file.

        Args:
            data_file (str): Path to the CSV file containing health data.
        """
        self.data_file = data_file
        self.model = None

    def load_data(self):
        """
        Loads the dataset from the specified CSV file and handles potential errors.
        
        Returns:
            pd.DataFrame: Loaded dataset.
        """
        try:
            data = pd.read_csv(self.data_file)
            return data
        except FileNotFoundError:
            raise FileNotFoundError(f"The file {self.data_file} was not found.")
        except pd.errors.EmptyDataError:
            raise ValueError("The provided CSV file is empty.")
        except pd.errors.ParserError:
            raise ValueError("Error parsing the CSV file. Please check the file format.")

    def preprocess_data(self, data):
        """
        Preprocesses the dataset: fills missing values and separates features and labels.

        Args:
            data (pd.DataFrame): The dataset to preprocess.

        Returns:
            X (pd.DataFrame): Features for model training.
            y (pd.Series): Labels for model training.
        """
        # Fill missing values
        data.fillna(data.mean(), inplace=True)

        # Assume that the last column is the label
        X = data.iloc[:, :-1]  # Features
        y = data.iloc[:, -1]   # Labels
        return X, y

    def train_model(self, X, y):
        """
        Trains a Random Forest Classifier on the given features and labels.

        Args:
            X (pd.DataFrame): Features for model training.
            y (pd.Series): Labels for model training.
        """
        X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

        # Initialize and train the model
        self.model = RandomForestClassifier(n_estimators=100, random_state=42)
        self.model.fit(X_train, y_train)

        # Evaluate the model
        y_pred = self.model.predict(X_test)
        print("Classification Report:\n", classification_report(y_test, y_pred))
        print("Confusion Matrix:\n", confusion_matrix(y_test, y_pred))

    def save_model(self, model_file):
        """
        Saves the trained model to a file using joblib.

        Args:
            model_file (str): The file path where the model should be saved.
        """
        if self.model is not None:
            joblib.dump(self.model, model_file)
            print(f"Model saved to {model_file}.")
        else:
            raise ValueError("Model has not been trained yet. Please train the model before saving.")

    def load_model(self, model_file):
        """
        Loads a previously saved model from a file.

        Args:
            model_file (str): The file path from where the model should be loaded.
        """
        try:
            self.model = joblib.load(model_file)
            print(f"Model loaded from {model_file}.")
        except FileNotFoundError:
            raise FileNotFoundError(f"The model file {model_file} was not found.")

    def predict(self, input_data):
        """
        Predicts the risk of non-communicable diseases based on input features.

        Args:
            input_data (list): A list of features for prediction.

        Returns:
            int: Prediction result where 1 indicates risk and 0 indicates no risk.
        """
        if self.model is None:
            raise ValueError("Model is not trained or loaded. Please train or load a model before prediction.")
        
        # Convert input data to numpy array and reshape for prediction
        input_data = np.array(input_data).reshape(1, -1)
        prediction = self.model.predict(input_data)
        return prediction[0]

if __name__ == "__main__":
    # Example usage
    ews = EarlyWarningSystem("health_data.csv")
    data = ews.load_data()
    X, y = ews.preprocess_data(data)
    ews.train_model(X, y)
    ews.save_model("ews_model.joblib")

    # Load and predict example
    ews.load_model("ews_model.joblib")
    sample_input = [55, 1, 4, 130, 200, 30, 1, 1]  # Example feature array
    prediction = ews.predict(sample_input)
    print(f"Prediction: {'Risk' if prediction == 1 else 'No Risk'}")
```
