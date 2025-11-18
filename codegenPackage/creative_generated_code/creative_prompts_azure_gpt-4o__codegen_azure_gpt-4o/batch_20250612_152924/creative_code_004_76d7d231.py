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
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score
import logging

# Configure logging for error handling
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')


class InvestmentProgramEvaluator:
    def __init__(self, data_path):
        """
        Initializes the InvestmentProgramEvaluator with data.

        :param data_path: Path to the dataset containing investment program data.
        """
        self.data_path = data_path
        self.data = None
        self.model = RandomForestClassifier(random_state=42)

    def load_data(self):
        """
        Loads data from a CSV file and performs basic validation.
        """
        try:
            self.data = pd.read_csv(self.data_path)
            logging.info("Data loaded successfully.")

            # Check for required columns
            required_columns = {'program_name', 'investment_return', 'risk_level', 'duration_months', 'legit'}
            if not required_columns.issubset(set(self.data.columns)):
                raise ValueError(f"The dataset must include the following columns: {required_columns}")

        except FileNotFoundError:
            logging.error(f"File not found at path: {self.data_path}")
            raise
        except Exception as e:
            logging.error(f"Error loading data: {e}")
            raise

    def preprocess_data(self):
        """
        Preprocesses the data by handling missing values and encoding categorical variables.
        """
        try:
            # Drop rows with missing values
            self.data.dropna(inplace=True)

            # Encode categorical variables if any
            if 'program_name' in self.data.columns:
                self.data['program_name'] = self.data['program_name'].astype('category').cat.codes

            logging.info("Data preprocessing complete.")

        except Exception as e:
            logging.error(f"Error during data preprocessing: {e}")
            raise

    def train_model(self):
        """
        Splits the data into training and testing sets, trains a Random Forest Classifier, and evaluates its performance.
        """
        try:
            # Define target and features
            X = self.data[['investment_return', 'risk_level', 'duration_months', 'program_name']]
            y = self.data['legit']

            # Split data into train and test sets
            X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42)

            # Train the model
            self.model.fit(X_train, y_train)
            logging.info("Model training complete.")

            # Evaluate the model
            y_pred = self.model.predict(X_test)
            accuracy = accuracy_score(y_test, y_pred)
            logging.info(f"Model accuracy: {accuracy * 100:.2f}%")

        except Exception as e:
            logging.error(f"Error during model training: {e}")
            raise

    def evaluate_program(self, program_data):
        """
        Evaluates the legitimacy of a single investment program.

        :param program_data: Dictionary containing investment program data.
                             Example: {'investment_return': 0.1, 'risk_level': 5, 'duration_months': 12, 'program_name': 1}
        :return: Prediction result: True for legitimate, False for illegitimate.
        """
        try:
            # Convert input data into a DataFrame for prediction
            program_df = pd.DataFrame([program_data])
            prediction = self.model.predict(program_df)
            return prediction[0] == 1

        except Exception as e:
            logging.error(f"Error during program evaluation: {e}")
            raise


if __name__ == "__main__":
    # Example usage
    try:
        evaluator = InvestmentProgramEvaluator(data_path="investment_programs.csv")
        evaluator.load_data()
        evaluator.preprocess_data()
        evaluator.train_model()

        # Evaluate a sample program
        sample_program = {
            'investment_return': 0.12,
            'risk_level': 4,
            'duration_months': 24,
            'program_name': 2
        }
        is_legit = evaluator.evaluate_program(sample_program)
        logging.info(f"Sample program legitimacy: {'Legitimate' if is_legit else 'Illegitimate'}")

    except Exception as e:
        logging.error(f"An error occurred during execution: {e}")
```
