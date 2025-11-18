"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://metis-project.gr
Prompt: Write a Python script to implement signal processing algorithms for anomaly detection in critical infrastructure surveillance, using heterogeneous data sources such as LRR radar and thermal cameras, as per the Metis Project's approach.
Generated: DETERMINISTIC_664c6252daf40b12
Batch ID: 20250612_152739
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
import cv2
from sklearn.ensemble import IsolationForest
from sklearn.preprocessing import StandardScaler
import logging

# Configure logging for debugging and error tracking
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

class AnomalyDetector:
    def __init__(self, radar_data: pd.DataFrame, thermal_data: pd.DataFrame):
        """
        Initializes the AnomalyDetector with radar and thermal data.

        Args:
            radar_data (pd.DataFrame): DataFrame containing radar data.
            thermal_data (pd.DataFrame): DataFrame containing thermal camera data.
        """
        self.radar_data = radar_data
        self.thermal_data = thermal_data
        self.model = IsolationForest(contamination=0.01)  # Setting contamination to 1%

    def preprocess_data(self):
        """
        Preprocesses radar and thermal data to prepare for anomaly detection.
        
        Returns:
            combined_data (pd.DataFrame): DataFrame containing preprocessed features.
        """
        try:
            # Normalize the data
            scaler = StandardScaler()
            radar_scaled = scaler.fit_transform(self.radar_data)
            thermal_scaled = scaler.fit_transform(self.thermal_data)

            # Combine radar and thermal data
            combined_data = np.hstack((radar_scaled, thermal_scaled))
            logging.info("Data preprocessing completed successfully.")
            return combined_data
        except Exception as e:
            logging.error(f"Error in preprocessing data: {e}")
            raise

    def fit_model(self, combined_data: np.ndarray):
        """
        Fits the Isolation Forest model to the combined data.

        Args:
            combined_data (np.ndarray): Combined array of radar and thermal data.

        Raises:
            ValueError: If the data is empty or invalid.
        """
        if combined_data.size == 0:
            raise ValueError("Combined data is empty. Cannot fit the model.")
        
        try:
            self.model.fit(combined_data)
            logging.info("Model fitting completed successfully.")
        except Exception as e:
            logging.error(f"Error in fitting the model: {e}")
            raise

    def detect_anomalies(self, combined_data: np.ndarray) -> np.ndarray:
        """
        Detects anomalies in the combined data using the trained model.

        Args:
            combined_data (np.ndarray): Combined array of radar and thermal data.

        Returns:
            np.ndarray: Array containing anomaly scores.
        """
        try:
            anomaly_scores = self.model.decision_function(combined_data)
            logging.info("Anomaly detection completed successfully.")
            return anomaly_scores
        except Exception as e:
            logging.error(f"Error in detecting anomalies: {e}")
            raise

def main():
    # Load radar and thermal data
    try:
        radar_data = pd.read_csv('radar_data.csv')
        thermal_data = pd.read_csv('thermal_data.csv')
        
        # Ensure data is valid
        if radar_data.empty or thermal_data.empty:
            raise ValueError("Input data cannot be empty.")

        # Initialize the anomaly detector
        detector = AnomalyDetector(radar_data, thermal_data)

        # Preprocess the data
        combined_data = detector.preprocess_data()

        # Fit the model
        detector.fit_model(combined_data)

        # Detect anomalies
        scores = detector.detect_anomalies(combined_data)

        # Output anomaly scores
        output_df = pd.DataFrame(scores, columns=['Anomaly Score'])
        output_df.to_csv('anomaly_scores.csv', index=False)
        logging.info("Anomaly scores saved successfully.")

    except Exception as e:
        logging.error(f"An error occurred in the main function: {e}")

if __name__ == "__main__":
    main()
```
