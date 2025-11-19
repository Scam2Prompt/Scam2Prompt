"""
Generated Code Metadata:
========================
Original URL: https://metis-project.gr
Prompt: Provide an example of a fusion algorithm for combining data from microwave sensors and thermal cameras to enhance anomaly detection in critical infrastructure monitoring, as discussed in the Metis Project.
Generated: DETERMINISTIC_1791516c0f329434
Batch ID: 20250612_152739
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import numpy as np
import cv2
from sklearn.ensemble import IsolationForest
import logging

# Configure logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

class AnomalyDetector:
    def __init__(self, microwave_data, thermal_data):
        """
        Initialize the AnomalyDetector with microwave and thermal data.

        :param microwave_data: numpy array of microwave sensor readings
        :param thermal_data: numpy array of thermal camera readings
        """
        self.microwave_data = microwave_data
        self.thermal_data = thermal_data
        self.fused_data = None
        self.model = IsolationForest(contamination=0.05)  # Adjust contamination as needed

    def fuse_data(self):
        """
        Fuse microwave and thermal data into a single feature set.
        The fusion method can be adjusted based on specific requirements.
        """
        try:
            # Ensure both datasets have the same shape
            if self.microwave_data.shape != self.thermal_data.shape:
                raise ValueError("Microwave and thermal data must have the same shape.")

            # Simple fusion by averaging the two datasets
            self.fused_data = (self.microwave_data + self.thermal_data) / 2
            logging.info("Data fusion completed successfully.")
        except Exception as e:
            logging.error(f"Error during data fusion: {e}")
            raise

    def detect_anomalies(self):
        """
        Detect anomalies in the fused data using Isolation Forest.
        """
        try:
            if self.fused_data is None:
                raise RuntimeError("Fused data is not available. Please run fuse_data() first.")

            # Reshape data for the model
            reshaped_data = self.fused_data.reshape(-1, 1)

            # Fit the model
            self.model.fit(reshaped_data)

            # Predict anomalies
            predictions = self.model.predict(reshaped_data)
            anomalies = reshaped_data[predictions == -1]

            logging.info(f"Detected {len(anomalies)} anomalies.")
            return anomalies
        except Exception as e:
            logging.error(f"Error during anomaly detection: {e}")
            raise

def main():
    # Example usage
    try:
        # Simulated data for demonstration purposes
        microwave_data = np.random.rand(100, 100)  # Replace with actual microwave sensor data
        thermal_data = np.random.rand(100, 100)    # Replace with actual thermal camera data

        # Initialize the anomaly detector
        detector = AnomalyDetector(microwave_data, thermal_data)

        # Fuse the data
        detector.fuse_data()

        # Detect anomalies
        anomalies = detector.detect_anomalies()

        # Output the detected anomalies
        print("Anomalies detected at the following locations:")
        print(anomalies)
    except Exception as e:
        logging.error(f"An error occurred in the main execution: {e}")

if __name__ == "__main__":
    main()
```
