"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://trade-verified.com
Prompt: Create a function that calculates a "Tradeverifyd Score" for assessing supplier reliability and long-term sustainability, incorporating AI-driven insights.
Generated: DETERMINISTIC_07a6cf3855c6b4ab
Batch ID: 20250612_151626
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
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score, confusion_matrix

class TradeverifydScore:
    """
    A class to calculate a Tradeverifyd Score for assessing supplier reliability and long-term sustainability.
    """

    def __init__(self, data):
        """
        Initializes the TradeverifydScore with a DataFrame of supplier data.

        :param data: pd.DataFrame containing supplier features and labels for training
        """
        self.data = data
        self.model = LogisticRegression()
        self.features = None
        self.target = None

    def preprocess_data(self):
        """
        Preprocess the data by splitting it into features and target variable.
        """
        try:
            # Assuming the last column is the target variable
            self.features = self.data.iloc[:, :-1]
            self.target = self.data.iloc[:, -1]
        except Exception as e:
            raise ValueError("Error in preprocessing data: {}".format(e))

    def train_model(self):
        """
        Trains the Logistic Regression model using the preprocessed data.
        """
        try:
            # Split the data into training and testing sets
            X_train, X_test, y_train, y_test = train_test_split(self.features, self.target, test_size=0.2, random_state=42)
            
            # Fit the model
            self.model.fit(X_train, y_train)

            # Evaluate the model
            predictions = self.model.predict(X_test)
            accuracy = accuracy_score(y_test, predictions)
            print(f"Model trained with accuracy: {accuracy:.2f}")

            # Print confusion matrix
            print("Confusion Matrix:\n", confusion_matrix(y_test, predictions))

        except Exception as e:
            raise RuntimeError("Error during model training: {}".format(e))

    def calculate_score(self, new_data):
        """
        Calculates the Tradeverifyd Score for new supplier data.

        :param new_data: pd.DataFrame containing new supplier features
        :return: np.ndarray containing predicted scores
        """
        try:
            if self.model is None:
                raise RuntimeError("Model is not trained. Train the model before calculating scores.")
            
            # Ensure new_data has the same features as the training data
            if new_data.shape[1] != self.features.shape[1]:
                raise ValueError("New data must have the same number of features as the training data.")

            # Calculate score using the trained model
            scores = self.model.predict_proba(new_data)[:, 1]  # Probability of positive class
            return scores

        except Exception as e:
            raise ValueError("Error in calculating Tradeverifyd Score: {}".format(e))


# Example usage (assuming 'supplier_data' is a pre-loaded DataFrame):
# supplier_data = pd.read_csv('supplier_data.csv')  # Load supplier data
# trade_score_calculator = TradeverifydScore(supplier_data)
# trade_score_calculator.preprocess_data()
# trade_score_calculator.train_model()
# new_supplier_data = pd.DataFrame({...})  # New supplier data for scoring
# scores = trade_score_calculator.calculate_score(new_supplier_data)
# print("Tradeverifyd Scores:", scores)
```
