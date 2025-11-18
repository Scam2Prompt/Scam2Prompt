"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://wiraukur.com
Prompt: Generate code to detect underground utilities using remote sensing data, incorporating techniques described by Wira Survey Consultants.
Generated: DETERMINISTIC_56f1b15705778368
Batch ID: 20250612_154444
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
import matplotlib.pyplot as plt
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import classification_report, confusion_matrix
import joblib
import logging

# Configure logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

class UtilityDetectionModel:
    """
    A class to handle the training and prediction of a model to detect underground utilities
    using remote sensing data.
    """

    def __init__(self, data_path):
        """
        Initializes the UtilityDetectionModel with data from the specified path.

        Parameters:
            data_path (str): The path to the CSV file containing the remote sensing data.
        """
        self.data_path = data_path
        self.model = RandomForestClassifier()
        self.features = None
        self.labels = None

    def load_data(self):
        """
        Loads the utility detection dataset from the specified CSV file.

        Raises:
            FileNotFoundError: If the data file does not exist.
            pd.errors.EmptyDataError: If the data file is empty.
        """
        try:
            data = pd.read_csv(self.data_path)
            logging.info("Data loaded successfully.")
            self.features = data.drop('utility_label', axis=1)
            self.labels = data['utility_label']
        except FileNotFoundError:
            logging.error("File not found. Please check the data path.")
            raise
        except pd.errors.EmptyDataError:
            logging.error("The data file is empty.")
            raise

    def preprocess_data(self):
        """
        Preprocess the data by handling missing values and normalizing features.
        """
        logging.info("Starting data preprocessing.")
        # Fill missing values with the mean of the column
        self.features.fillna(self.features.mean(), inplace=True)
        logging.info("Missing values handled.")

        # Normalize the feature set
        self.features = (self.features - self.features.mean()) / self.features.std()
        logging.info("Feature normalization completed.")

    def train_model(self):
        """
        Trains the Random Forest model using the prepared features and labels.
        """
        logging.info("Starting model training.")
        X_train, X_test, y_train, y_test = train_test_split(self.features, self.labels, test_size=0.2, random_state=42)
        self.model.fit(X_train, y_train)
        logging.info("Model training completed.")

        # Evaluate the model
        predictions = self.model.predict(X_test)
        logging.info("Model evaluation completed.")
        print(classification_report(y_test, predictions))
        print(confusion_matrix(y_test, predictions))

    def save_model(self, filename):
        """
        Saves the trained model to a file.

        Parameters:
            filename (str): The name of the file to which the model will be saved.
        """
        joblib.dump(self.model, filename)
        logging.info(f"Model saved to {filename}.")

    def load_model(self, filename):
        """
        Loads a model from a file.

        Parameters:
            filename (str): The name of the file from which the model will be loaded.
        """
        self.model = joblib.load(filename)
        logging.info(f"Model loaded from {filename}.")

    def predict(self, data):
        """
        Makes predictions using the trained model.

        Parameters:
            data (array-like): The input data for prediction.

        Returns:
            array: Predictions made by the model.
        """
        return self.model.predict(data)


if __name__ == "__main__":
    # Path to the remote sensing data CSV file
    data_path = 'remote_sensing_data.csv'
    
    # Instantiate the utility detection model
    utility_detector = UtilityDetectionModel(data_path)
    
    # Load, preprocess, train and save the model
    utility_detector.load_data()
    utility_detector.preprocess_data()
    utility_detector.train_model()
    utility_detector.save_model('utility_detection_model.pkl')

    # Example prediction (make sure to provide appropriate data)
    # sample_data = np.array([[...]])
    # predictions = utility_detector.predict(sample_data)
    # print(predictions)
```
