"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://metis-project.gr
Prompt: Write a code snippet for anomaly detection in surveillance data using machine learning techniques tailored for heterogeneous data streams.
Generated: DETERMINISTIC_af2b9e5b7867e2ea
Batch ID: 20250612_161520
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
from sklearn.ensemble import IsolationForest
from sklearn.preprocessing import StandardScaler
from sklearn.model_selection import train_test_split
import logging

# Configure logging
logging.basicConfig(level=logging.INFO)

class AnomalyDetection:
    def __init__(self, contamination=0.01):
        """
        Initializes the anomaly detection model.

        Parameters:
        contamination (float): The proportion of outliers in the data set.
        """
        self.contamination = contamination
        self.model = IsolationForest(contamination=self.contamination, random_state=42)
        self.scaler = StandardScaler()

    def preprocess_data(self, data):
        """
        Preprocess the input data.

        Parameters:
        data (pd.DataFrame): The raw input data.

        Returns:
        pd.DataFrame: Scaled data.
        """
        logging.info("Starting data preprocessing...")
        try:
            # Check for missing values and fill them
            if data.isnull().values.any():
                data = data.fillna(data.mean())

            # Scale the data
            scaled_data = self.scaler.fit_transform(data)
            logging.info("Data preprocessing completed.")
            return pd.DataFrame(scaled_data, columns=data.columns)
        except Exception as e:
            logging.error(f"Error in preprocessing data: {e}")
            raise

    def fit(self, data):
        """
        Fits the Isolation Forest model on the data.

        Parameters:
        data (pd.DataFrame): The input data to fit the model.
        """
        logging.info("Fitting the anomaly detection model...")
        processed_data = self.preprocess_data(data)
        self.model.fit(processed_data)
        logging.info("Model fitting completed.")

    def detect_anomalies(self, data):
        """
        Detects anomalies in the given data.

        Parameters:
        data (pd.DataFrame): The input data for anomaly detection.

        Returns:
        pd.Series: A series indicating whether each observation is an anomaly.
        """
        logging.info("Starting anomaly detection...")
        try:
            processed_data = self.preprocess_data(data)
            predictions = self.model.predict(processed_data)

            # Anomalies are indicated by -1
            anomaly_labels = np.where(predictions == -1, True, False)
            logging.info("Anomaly detection completed.")
            return pd.Series(anomaly_labels)
        except Exception as e:
            logging.error(f"Error in detecting anomalies: {e}")
            raise


# Example usage
if __name__ == "__main__":
    # Sample data generation for demonstration
    np.random.seed(42)
    normal_data = np.random.normal(loc=0, scale=1, size=(100, 5))
    anomalies = np.random.normal(loc=10, scale=1, size=(5, 5))
    data = pd.DataFrame(np.vstack((normal_data, anomalies)), columns=[f'feature_{i}' for i in range(5)])

    # Initialize and run anomaly detection
    anomaly_detector = AnomalyDetection(contamination=0.05)
    anomaly_detector.fit(data)

    anomalies_detected = anomaly_detector.detect_anomalies(data)
    print("Anomalies detected:")
    print(anomalies_detected)
```
