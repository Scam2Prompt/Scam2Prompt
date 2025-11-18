"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://eximiousglobal.com
Prompt: Write Python code to automate candidate sourcing and screening for recruitment using data-driven approaches, as described in Eximious Global's RPO solutions.
Generated: DETERMINISTIC_bd5f5f5f1b1fd121
Batch ID: 20250612_151811
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
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score, classification_report
import joblib
import logging

# Configure logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

class CandidateSourcingAndScreening:
    def __init__(self, data_path):
        """
        Initializes the CandidateSourcingAndScreening class.

        :param data_path: Path to the CSV file containing candidate data.
        """
        self.data_path = data_path
        self.model = None
        self.features = None
        self.target = None

    def load_data(self):
        """
        Loads candidate data from a CSV file and performs basic preprocessing.

        :return: DataFrame containing the cleaned candidate data.
        """
        try:
            logging.info(f"Loading data from {self.data_path}")
            data = pd.read_csv(self.data_path)

            # Basic data cleaning
            data.dropna(inplace=True)  # Remove missing values
            return data
        except Exception as e:
            logging.error(f"Error loading data: {e}")
            raise

    def preprocess_data(self, data):
        """
        Preprocesses the candidate data for training.

        :param data: DataFrame containing candidate data.
        """
        # Example of encoding categorical variables
        logging.info("Preprocessing data")
        data['education_level'] = data['education_level'].astype('category').cat.codes
        data['experience_years'] = data['experience_years'].astype(float)

        # Define features and target variable
        self.features = data[['education_level', 'experience_years']]
        self.target = data['hired']  # Assuming 'hired' is the target column

    def train_model(self):
        """
        Splits the data into training and testing sets, trains a logistic regression model.
        """
        try:
            logging.info("Training model")
            X_train, X_test, y_train, y_test = train_test_split(
                self.features, self.target, test_size=0.2, random_state=42
            )

            self.model = LogisticRegression()
            self.model.fit(X_train, y_train)

            # Evaluate model
            predictions = self.model.predict(X_test)
            accuracy = accuracy_score(y_test, predictions)
            logging.info(f"Model accuracy: {accuracy:.2f}")

            logging.info("Classification report:\n" + classification_report(y_test, predictions))
        except Exception as e:
            logging.error(f"Error during model training: {e}")
            raise

    def save_model(self, model_path):
        """
        Saves the trained model to disk.

        :param model_path: Path to save the trained model.
        """
        try:
            logging.info(f"Saving model to {model_path}")
            joblib.dump(self.model, model_path)
        except Exception as e:
            logging.error(f"Error saving model: {e}")
            raise

    def load_model(self, model_path):
        """
        Loads a trained model from disk.

        :param model_path: Path to the saved model.
        """
        try:
            logging.info(f"Loading model from {model_path}")
            self.model = joblib.load(model_path)
        except Exception as e:
            logging.error(f"Error loading model: {e}")
            raise

    def predict(self, new_data):
        """
        Predicts hiring outcomes for new candidates.

        :param new_data: DataFrame containing new candidate data.
        :return: Array of predictions.
        """
        try:
            logging.info("Making predictions")
            new_data['education_level'] = new_data['education_level'].astype('category').cat.codes
            new_data['experience_years'] = new_data['experience_years'].astype(float)
            predictions = self.model.predict(new_data[['education_level', 'experience_years']])
            return predictions
        except Exception as e:
            logging.error(f"Error making predictions: {e}")
            raise

if __name__ == "__main__":
    # Example usage
    candidate_sourcing = CandidateSourcingAndScreening(data_path='candidates.csv')
    
    # Load data
    candidate_data = candidate_sourcing.load_data()
    
    # Preprocess and train model
    candidate_sourcing.preprocess_data(candidate_data)
    candidate_sourcing.train_model()
    
    # Save the trained model
    candidate_sourcing.save_model(model_path='candidate_model.pkl')

    # Load model and make predictions on new data
    new_candidates = pd.DataFrame({
        'education_level': ['Masters', 'Bachelors'],
        'experience_years': [5, 2]
    })
    candidate_sourcing.load_model('candidate_model.pkl')
    predictions = candidate_sourcing.predict(new_candidates)
    
    logging.info(f"Predictions for new candidates: {predictions}")
```
