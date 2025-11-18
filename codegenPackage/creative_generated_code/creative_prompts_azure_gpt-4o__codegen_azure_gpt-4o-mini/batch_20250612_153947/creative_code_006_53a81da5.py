"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://asfcsc.pages.dev
Prompt: Create a Python script that analyzes health data and predicts disease risks up to 6 months in advance, inspired by BitDoctor's AI-driven preventive care system.
Generated: DETERMINISTIC_53a81da5cf1c5a44
Batch ID: 20250612_153947
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import classification_report, confusion_matrix
import joblib

# Set random seed for reproducibility
np.random.seed(42)

class HealthDataAnalyzer:
    def __init__(self, data_path):
        """
        Initializes the HealthDataAnalyzer with the path to the health data CSV file.
        
        :param data_path: str, path to the CSV file containing health data
        """
        self.data_path = data_path
        self.model = None
        self.X_train = None
        self.X_test = None
        self.y_train = None
        self.y_test = None

    def load_data(self):
        """Loads health data from a CSV file into a pandas DataFrame."""
        try:
            self.data = pd.read_csv(self.data_path)
            print(f"Data loaded successfully from {self.data_path}")
        except FileNotFoundError:
            print(f"Error: File not found at {self.data_path}")
            raise
        except pd.errors.EmptyDataError:
            print("Error: No data found in the file.")
            raise
        except Exception as e:
            print(f"An unexpected error occurred: {e}")
            raise

    def preprocess_data(self):
        """Preprocesses the health data for analysis."""
        # Placeholder for preprocessing steps (e.g., handling missing values, encoding categorical variables)
        # For now, we will drop any rows with missing values
        self.data.dropna(inplace=True)

        # Assume the last column is the target variable
        X = self.data.iloc[:, :-1]
        y = self.data.iloc[:, -1]

        # Split the data into training and testing sets
        self.X_train, self.X_test, self.y_train, self.y_test = train_test_split(X, y, test_size=0.2, random_state=42)
        print("Data preprocessed and split into training and testing sets.")

    def train_model(self):
        """Trains a Random Forest classifier on the training data."""
        self.model = RandomForestClassifier(n_estimators=100, random_state=42)
        self.model.fit(self.X_train, self.y_train)
        print("Model trained successfully.")

    def evaluate_model(self):
        """Evaluates the trained model on the test data and prints the performance metrics."""
        if self.model is None:
            print("Error: Model has not been trained yet.")
            return

        predictions = self.model.predict(self.X_test)
        print("Model evaluation:")
        print(classification_report(self.y_test, predictions))
        print("Confusion Matrix:")
        print(confusion_matrix(self.y_test, predictions))

    def save_model(self, model_path):
        """Saves the trained model to a file."""
        if self.model is None:
            print("Error: Model has not been trained yet.")
            return
        
        joblib.dump(self.model, model_path)
        print(f"Model saved to {model_path}")

    def load_model(self, model_path):
        """Loads a trained model from a file."""
        try:
            self.model = joblib.load(model_path)
            print(f"Model loaded successfully from {model_path}")
        except FileNotFoundError:
            print(f"Error: Model file not found at {model_path}")
            raise
        except Exception as e:
            print(f"An unexpected error occurred while loading the model: {e}")
            raise

if __name__ == "__main__":
    # Path to the health data CSV file
    data_path = "health_data.csv"  # Update this path as necessary
    model_path = "health_model.pkl"  # Path to save/load the model

    analyzer = HealthDataAnalyzer(data_path)
    
    # Load, preprocess, train, and evaluate the model
    analyzer.load_data()
    analyzer.preprocess_data()
    analyzer.train_model()
    analyzer.evaluate_model()
    
    # Save the trained model
    analyzer.save_model(model_path)
```
