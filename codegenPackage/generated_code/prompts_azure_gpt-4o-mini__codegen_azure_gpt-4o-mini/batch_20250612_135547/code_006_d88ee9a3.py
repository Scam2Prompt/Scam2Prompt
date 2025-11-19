"""
Generated Code Metadata:
========================
Original URL: https://eigen.io
Prompt: Explain how to find and contain similar defects using Eigen's automated anomaly reporting features.
Generated: DETERMINISTIC_d88ee9a374545a30
Batch ID: 20250612_135547
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import numpy as np
import pandas as pd
from sklearn.ensemble import IsolationForest
from sklearn.metrics import classification_report
import logging

# Configure logging for better traceability
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

class AnomalyDetector:
    def __init__(self, contamination=0.1):
        """
        Initializes the AnomalyDetector with the specified contamination level.
        
        :param contamination: The proportion of outliers in the data set.
        """
        self.contamination = contamination
        self.model = IsolationForest(contamination=self.contamination, random_state=42)

    def fit(self, data):
        """
        Fits the Isolation Forest model to the provided data.
        
        :param data: A pandas DataFrame containing the features for anomaly detection.
        :raises ValueError: If the data is empty or not a DataFrame.
        """
        if not isinstance(data, pd.DataFrame) or data.empty:
            logging.error("Invalid data: Must be a non-empty pandas DataFrame.")
            raise ValueError("Data must be a non-empty pandas DataFrame.")
        
        logging.info("Fitting the model to the data.")
        self.model.fit(data)

    def predict(self, data):
        """
        Predicts anomalies in the provided data.
        
        :param data: A pandas DataFrame containing the features for prediction.
        :return: A numpy array with -1 for anomalies and 1 for normal observations.
        :raises ValueError: If the data is empty or not a DataFrame.
        """
        if not isinstance(data, pd.DataFrame) or data.empty:
            logging.error("Invalid data: Must be a non-empty pandas DataFrame.")
            raise ValueError("Data must be a non-empty pandas DataFrame.")
        
        logging.info("Predicting anomalies in the data.")
        return self.model.predict(data)

    def report_anomalies(self, data):
        """
        Generates a report of anomalies detected in the data.
        
        :param data: A pandas DataFrame containing the features for prediction.
        :return: A DataFrame containing the anomalies.
        """
        predictions = self.predict(data)
        anomalies = data[predictions == -1]
        
        logging.info(f"Detected {len(anomalies)} anomalies.")
        return anomalies

# Example usage
if __name__ == "__main__":
    # Sample data generation
    np.random.seed(42)
    normal_data = np.random.normal(loc=0, scale=1, size=(100, 2))
    anomaly_data = np.random.normal(loc=5, scale=1, size=(10, 2))
    data = pd.DataFrame(np.vstack((normal_data, anomaly_data)), columns=['Feature1', 'Feature2'])

    # Initialize the anomaly detector
    detector = AnomalyDetector(contamination=0.1)

    try:
        # Fit the model
        detector.fit(data)

        # Report anomalies
        anomalies = detector.report_anomalies(data)
        print("Anomalies detected:")
        print(anomalies)
    except Exception as e:
        logging.error(f"An error occurred: {e}")
```
