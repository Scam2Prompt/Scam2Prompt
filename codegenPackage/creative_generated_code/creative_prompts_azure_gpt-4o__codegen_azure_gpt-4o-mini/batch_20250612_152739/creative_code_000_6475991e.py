"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://metis-project.gr
Prompt: Write Python code to implement anomaly detection using multimodal data fusion techniques, specifically combining inputs from optical cameras, thermal cameras, and LRR radar systems, as described in the Metis Project.
Generated: DETERMINISTIC_6475991e86ace3d3
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
from sklearn.preprocessing import StandardScaler
from sklearn.ensemble import IsolationForest
from sklearn.metrics import classification_report
import logging

# Configure logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

class AnomalyDetection:
    def __init__(self, optical_data, thermal_data, radar_data):
        """
        Initialize the AnomalyDetection class.
        
        :param optical_data: DataFrame containing optical camera data
        :param thermal_data: DataFrame containing thermal camera data
        :param radar_data: DataFrame containing LRR radar data
        """
        self.optical_data = optical_data
        self.thermal_data = thermal_data
        self.radar_data = radar_data
        self.scaled_data = None
        self.model = IsolationForest(random_state=42)

    def preprocess_data(self):
        """
        Preprocess the data by merging the datasets and scaling the features.
        """
        try:
            # Merge data frames on a common timestamp or identifier
            merged_data = pd.concat([self.optical_data, self.thermal_data, self.radar_data], axis=1)
            logging.info("Data merged successfully.")
            
            # Fill any missing values
            merged_data.fillna(method='ffill', inplace=True)

            # Scale features
            scaler = StandardScaler()
            self.scaled_data = scaler.fit_transform(merged_data)
            logging.info("Data scaled successfully.")
            
        except Exception as e:
            logging.error(f"Error in data preprocessing: {e}")
            raise

    def fit_model(self):
        """
        Fit the Isolation Forest model to the data.
        """
        if self.scaled_data is None:
            logging.error("Data has not been preprocessed. Please run preprocess_data() first.")
            return
        
        try:
            self.model.fit(self.scaled_data)
            logging.info("Isolation Forest model fitted successfully.")
        except Exception as e:
            logging.error(f"Error in fitting model: {e}")
            raise

    def detect_anomalies(self):
        """
        Detect anomalies in the data using the fitted model.
        
        :return: DataFrame with anomaly predictions
        """
        if self.scaled_data is None:
            logging.error("Data has not been scaled. Please run preprocess_data() first.")
            return None
        
        try:
            predictions = self.model.predict(self.scaled_data)
            # Convert predictions to a binary format: 1 for anomalies, 0 for normal instances
            anomaly_results = pd.DataFrame(predictions, columns=['anomaly'])
            anomaly_results['anomaly'] = anomaly_results['anomaly'].apply(lambda x: 1 if x == -1 else 0)
            logging.info("Anomalies detected successfully.")
            return anomaly_results
        except Exception as e:
            logging.error(f"Error in detecting anomalies: {e}")
            raise

    def evaluate_model(self, true_labels):
        """
        Evaluate the anomaly detection model using the provided true labels.
        
        :param true_labels: Ground truth labels for the data
        :return: None
        """
        predictions = self.detect_anomalies()
        
        if predictions is None:
            logging.error("No predictions available for evaluation.")
            return
        
        try:
            print(classification_report(true_labels, predictions['anomaly']))
            logging.info("Model evaluation completed successfully.")
        except Exception as e:
            logging.error(f"Error in model evaluation: {e}")
            raise

# Example usage:
if __name__ == "__main__":
    # Assuming optical_data, thermal_data, and radar_data are loaded DataFrames
    optical_data = pd.DataFrame(np.random.rand(100, 5), columns=['optical_feature1', 'optical_feature2', 'optical_feature3', 'optical_feature4', 'optical_feature5'])
    thermal_data = pd.DataFrame(np.random.rand(100, 5), columns=['thermal_feature1', 'thermal_feature2', 'thermal_feature3', 'thermal_feature4', 'thermal_feature5'])
    radar_data = pd.DataFrame(np.random.rand(100, 5), columns=['radar_feature1', 'radar_feature2', 'radar_feature3', 'radar_feature4', 'radar_feature5'])
    true_labels = np.random.randint(0, 2, 100)  # Example ground truth labels for evaluation

    anomaly_detector = AnomalyDetection(optical_data, thermal_data, radar_data)
    anomaly_detector.preprocess_data()
    anomaly_detector.fit_model()
    anomaly_detector.evaluate_model(true_labels)
```
