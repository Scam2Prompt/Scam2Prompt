"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://metis-project.gr
Prompt: How can I develop a signal processing algorithm that fuses data from different sensor types for critical infrastructure surveillance?
Generated: DETERMINISTIC_738538241f8a0413
Batch ID: 20250612_161520
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

# Signal processing algorithm for fusing data from different sensor types
class SensorDataFusion:
    def __init__(self, sensors):
        """
        Initialize the SensorDataFusion class with the list of sensors.
        
        Args:
            sensors (dict): Dictionary containing sensor names as keys and their data as Pandas DataFrames.
        """
        self.sensors = sensors  # Dictionary of sensor data
    
    def preprocess_data(self):
        """
        Preprocess sensor data by handling missing values and normalizing each sensor's readings.
        
        Returns:
            dict: Dictionary containing preprocessed sensor data.
        """
        preprocessed_data = {}
        for sensor, data in self.sensors.items():
            # Fill missing values with the mean of the column
            data_filled = data.fillna(data.mean())
            
            # Normalize data to a 0-1 range using Min-Max scaling
            data_normalized = (data_filled - data_filled.min()) / (data_filled.max() - data_filled.min())
            
            preprocessed_data[sensor] = data_normalized
        
        return preprocessed_data
    
    def fuse_data(self, preprocessed_data):
        """
        Fuse preprocessed sensor data into a single DataFrame using a weighted average approach.
        
        Args:
            preprocessed_data (dict): Dictionary containing preprocessed sensor data.
        
        Returns:
            pd.DataFrame: DataFrame containing fused sensor data.
        """
        # Assign weights to each sensor based on reliability (can be adjusted)
        sensor_weights = {sensor: 1 / len(preprocessed_data) for sensor in preprocessed_data}
        
        # Ensure all sensors have the same shape, aligning by index
        aligned_data = pd.concat(preprocessed_data.values(), axis=1, join='inner')
        
        # Weight each sensor's data and compute the weighted average
        fused_data = sum(aligned_data[sensor] * weight for sensor, weight in sensor_weights.items())
        
        return pd.DataFrame(fused_data, columns=["Fused_Signal"])
    
    def detect_anomalies(self, fused_data, threshold=0.8):
        """
        Detect anomalies in the fused data using a simple threshold-based method.
        
        Args:
            fused_data (pd.DataFrame): DataFrame containing fused sensor data.
            threshold (float): Threshold value above which a signal is considered an anomaly.
        
        Returns:
            pd.DataFrame: DataFrame with an additional 'Anomaly' column (True for anomalies, False otherwise).
        """
        fused_data["Anomaly"] = fused_data["Fused_Signal"] > threshold
        return fused_data

def main():
    # Simulated example data from three different sensors
    sensor_a = pd.DataFrame({"Reading": np.random.rand(100)})
    sensor_b = pd.DataFrame({"Reading": np.random.rand(100) * 1.5})
    sensor_c = pd.DataFrame({"Reading": np.random.rand(100) * 0.5})
    
    # Combine sensor data into a dictionary
    sensors = {"Sensor_A": sensor_a, "Sensor_B": sensor_b, "Sensor_C": sensor_c}
    
    # Instantiate the SensorDataFusion class
    fusion = SensorDataFusion(sensors)
    
    # Preprocess sensor data
    preprocessed_data = fusion.preprocess_data()
    
    # Fuse preprocessed data into a single signal
    fused_data = fusion.fuse_data(preprocessed_data)
    
    # Detect anomalies in the fused data
    anomalies_detected = fusion.detect_anomalies(fused_data)
    
    # Print results
    print("Fused Data:\n", fused_data.head())
    print("\nAnomalies Detected:\n", anomalies_detected[anomalies_detected["Anomaly"]])

if __name__ == "__main__":
    main()
```
