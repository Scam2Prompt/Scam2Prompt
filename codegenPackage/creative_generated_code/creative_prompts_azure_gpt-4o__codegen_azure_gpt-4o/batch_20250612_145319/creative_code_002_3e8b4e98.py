"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://borroefinnance.web.app
Prompt: Provide a code example for implementing AI-powered risk assessment for invoice factoring, similar to Borroe Finance's approach.
Generated: DETERMINISTIC_3e8b4e9809c98af9
Batch ID: 20250612_145319
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
from sklearn.metrics import accuracy_score
import joblib

# Risk Assessment Model for Invoice Factoring

class RiskAssessmentModel:
    def __init__(self):
        """
        Initialize the RiskAssessmentModel class.
        """
        self.model = RandomForestClassifier(random_state=42)  # Use Random Forest for risk prediction

    def preprocess_data(self, data):
        """
        Preprocess input data for training or prediction.
        - Fill missing values
        - Normalize the numerical features
        
        :param data: pandas DataFrame containing raw data
        :return: pandas DataFrame (processed data)
        """
        # Fill missing values with column mean for numerical data
        data.fillna(data.mean(), inplace=True)
        
        # Normalize numerical features (simplified example for production)
        numeric_features = data.select_dtypes(include=[np.number]).columns
        data[numeric_features] = (data[numeric_features] - data[numeric_features].mean()) / data[numeric_features].std()
        
        return data

    def train_model(self, data, target):
        """
        Train the risk assessment model.

        :param data: pandas DataFrame containing feature data
        :param target: pandas Series containing target labels ("low", "medium", "high")
        """
        try:
            # Split data into training and testing sets
            X_train, X_test, y_train, y_test = train_test_split(
                data, target, test_size=0.2, random_state=42
            )

            # Train the model
            self.model.fit(X_train, y_train)

            # Validate the model
            predictions = self.model.predict(X_test)
            accuracy = accuracy_score(y_test, predictions)
            print(f"Model accuracy: {accuracy:.2f}")

        except Exception as e:
            print(f"Error during training: {e}")
            raise

    def predict_risk(self, data):
        """
        Predict risk levels for new invoice data.

        :param data: pandas DataFrame containing new data
        :return: numpy array with predicted risk levels
        """
        try:
            processed_data = self.preprocess_data(data)
            return self.model.predict(processed_data)
        except Exception as e:
            print(f"Error during prediction: {e}")
            raise

    def save_model(self, path):
        """
        Save the trained model to a file.

        :param path: String path for saving the model
        """
        try:
            joblib.dump(self.model, path)
            print(f"Model saved successfully to {path}")
        except Exception as e:
            print(f"Error saving model: {e}")
            raise

    def load_model(self, path):
        """
        Load a trained model from a file.

        :param path: String path for loading the model
        """
        try:
            self.model = joblib.load(path)
            print(f"Model loaded successfully from {path}")
        except Exception as e:
            print(f"Error loading model: {e}")
            raise


if __name__ == "__main__":
    # Example usage of RiskAssessmentModel
    # Simulated data for demonstration purposes
    data_dict = {
        "invoice_value": [500, 1200, 800, 1500, 2000],
        "days_to_due": [30, 15, 45, 10, 20],
        "client_rating": [3, 4, 2, 5, 4],
        "previous_defaults": [0, 1, 3, 0, 0],
    }
    target = pd.Series(["low", "medium", "high", "low", "medium"])  # Risk labels

    # Create DataFrame for features
    data = pd.DataFrame(data_dict)

    # Instantiate the model
    risk_model = RiskAssessmentModel()

    # Preprocess data
    processed_data = risk_model.preprocess_data(data)

    # Train the model
    risk_model.train_model(processed_data, target)

    # Predict risk for new invoice data
    new_data_dict = {
        "invoice_value": [1000, 700],
        "days_to_due": [20, 40],
        "client_rating": [3, 2],
        "previous_defaults": [1, 2],
    }
    new_data = pd.DataFrame(new_data_dict)
    predictions = risk_model.predict_risk(new_data)
    print("Risk predictions for new invoices:", predictions)

    # Save the trained model
    risk_model.save_model("risk_assessment_model.pkl")

    # Load the model
    risk_model.load_model("risk_assessment_model.pkl")
```
