"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://rapidresponder.net
Prompt: Write a program that evaluates the legitimacy of investment programs using data analysis techniques, as mentioned in Rapid Responder's information-gathering services.
Generated: DETERMINISTIC_76d7d231f94131d8
Batch ID: 20250612_152924
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
from sklearn.metrics import classification_report, accuracy_score
import logging

# Configure logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

class InvestmentProgramEvaluator:
    def __init__(self, data_path: str):
        """
        Initializes the InvestmentProgramEvaluator with the provided data path.

        :param data_path: Path to the CSV file containing investment program data.
        """
        self.data_path = data_path
        self.model = None
        self.features = None
        self.target = None
        self.X_train = None
        self.X_test = None
        self.y_train = None
        self.y_test = None

    def load_data(self):
        """
        Loads the investment data from a CSV file and handles potential errors.
        
        :return: DataFrame containing the investment data.
        """
        try:
            data = pd.read_csv(self.data_path)
            logging.info("Data loaded successfully.")
            return data
        except FileNotFoundError:
            logging.error("The specified data file was not found.")
            raise
        except pd.errors.EmptyDataError:
            logging.error("No data found in the file.")
            raise
        except Exception as e:
            logging.error(f"An error occurred while loading data: {e}")
            raise

    def preprocess_data(self, data: pd.DataFrame):
        """
        Preprocesses the data by separating features and target variable.
        
        :param data: DataFrame containing the investment data.
        """
        try:
            # Assuming the last column is the target variable
            self.features = data.iloc[:, :-1]
            self.target = data.iloc[:, -1]

            # Handle categorical features (if any) and missing values
            self.features.fillna(self.features.mean(), inplace=True)  # Simple imputation
            self.features = pd.get_dummies(self.features)

            logging.info("Data preprocessing completed.")
        except Exception as e:
            logging.error(f"An error occurred during preprocessing: {e}")
            raise

    def split_data(self):
        """
        Splits the data into training and testing sets.
        """
        try:
            self.X_train, self.X_test, self.y_train, self.y_test = train_test_split(
                self.features, self.target, test_size=0.2, random_state=42
            )
            logging.info("Data has been split into training and testing sets.")
        except Exception as e:
            logging.error(f"An error occurred while splitting data: {e}")
            raise

    def train_model(self):
        """
        Trains a Random Forest Classifier on the training data.
        """
        try:
            self.model = RandomForestClassifier(n_estimators=100, random_state=42)
            self.model.fit(self.X_train, self.y_train)
            logging.info("Model training completed.")
        except Exception as e:
            logging.error(f"An error occurred during model training: {e}")
            raise

    def evaluate_model(self):
        """
        Evaluates the trained model using the test data and prints the classification report.
        """
        try:
            predictions = self.model.predict(self.X_test)
            accuracy = accuracy_score(self.y_test, predictions)
            logging.info(f"Model accuracy: {accuracy:.2f}")
            print(classification_report(self.y_test, predictions))
        except Exception as e:
            logging.error(f"An error occurred during model evaluation: {e}")
            raise

if __name__ == "__main__":
    # Path to the dataset
    DATA_PATH = "investment_data.csv"

    evaluator = InvestmentProgramEvaluator(DATA_PATH)

    # Load, preprocess, split, train, and evaluate the model
    data = evaluator.load_data()
    evaluator.preprocess_data(data)
    evaluator.split_data()
    evaluator.train_model()
    evaluator.evaluate_model()
```
