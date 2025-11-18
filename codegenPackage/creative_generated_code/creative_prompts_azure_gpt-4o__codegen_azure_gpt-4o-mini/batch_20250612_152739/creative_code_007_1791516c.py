"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://metis-project.gr
Prompt: Provide an example of a fusion algorithm for combining data from microwave sensors and thermal cameras to enhance anomaly detection in critical infrastructure monitoring, as discussed in the Metis Project.
Generated: DETERMINISTIC_1791516c0f329434
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
import cv2
from sklearn.ensemble import IsolationForest
import logging

# Set up logging for debugging and error tracking
logging.basicConfig(level=logging.INFO, format='%(levelname)s: %(message)s')

class AnomalyDetector:
    def __init__(self, microwave_data, thermal_data):
        """
        Initializes the anomaly detector with microwave and thermal data.
        
        Args:
            microwave_data (np.ndarray): Array of microwave sensor readings.
            thermal_data (np.ndarray): Array of thermal camera readings.
        """
        self.microwave_data = microwave_data
        self.thermal_data = thermal_data
        self.combined_data = None
        self.model = IsolationForest(contamination=0.1)

    def preprocess_data(self):
        """
        Preprocesses the microwave and thermal data for fusion.
        
        Combines and normalizes the data to prepare for anomaly detection.
        """
        try:
            # Ensure both datasets have the same shape
            if self.microwave_data.shape != self.thermal_data.shape:
                raise ValueError("Microwave and thermal data must have the same shape.")

            # Combine the two datasets along the last axis
            self.combined_data = np.concatenate((self.microwave_data[:, :, np.newaxis],
                                                  self.thermal_data[:, :, np.newaxis]), axis=-1)
            logging.info("Data preprocessed and combined successfully.")

        except Exception as e:
            logging.error(f"Error during data preprocessing: {e}")
            raise

    def detect_anomalies(self):
        """
        Detects anomalies in the combined data using Isolation Forest.
        
        Returns:
            np.ndarray: A binary array indicating anomalies (1: anomaly, -1: normal).
        """
        if self.combined_data is None:
            raise RuntimeError("Data must be preprocessed before detecting anomalies.")
        
        # Flatten the combined data for model training
        data_reshaped = self.combined_data.reshape(-1, 2)  # 2 features: microwave and thermal
        try:
            # Fit the Isolation Forest model
            self.model.fit(data_reshaped)

            # Predict anomalies
            predictions = self.model.predict(data_reshaped)
            anomaly_map = predictions.reshape(self.combined_data.shape[:-1])  # Reshape back to original

            logging.info("Anomaly detection completed.")
            return anomaly_map

        except Exception as e:
            logging.error(f"Error during anomaly detection: {e}")
            raise

def main():
    # Example usage:
    # Simulated microwave and thermal data (10x10 arrays for simplicity)
    microwave_data = np.random.rand(10, 10)  # Placeholder for actual microwave sensor data
    thermal_data = np.random.rand(10, 10)    # Placeholder for actual thermal camera data

    try:
        detector = AnomalyDetector(microwave_data, thermal_data)
        detector.preprocess_data()
        anomalies = detector.detect_anomalies()

        # Output the result
        print("Anomaly Map:")
        print(anomalies)

    except Exception as e:
        logging.error(f"An error occurred in the main process: {e}")

if __name__ == "__main__":
    main()
```
