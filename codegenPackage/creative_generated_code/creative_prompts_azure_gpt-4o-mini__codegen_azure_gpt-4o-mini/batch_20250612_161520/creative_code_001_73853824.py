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
from scipy.signal import butter, lfilter
import logging

# Set up logging for debugging and error tracking
logging.basicConfig(level=logging.DEBUG, format='%(asctime)s - %(levelname)s - %(message)s')

class SensorDataFusion:
    def __init__(self):
        self.accelerometer_data = None
        self.gyroscope_data = None
        self.temperature_data = None

    def load_data(self, accelerometer_path, gyroscope_path, temperature_path):
        """
        Load sensor data from CSV files.
        """
        try:
            self.accelerometer_data = pd.read_csv(accelerometer_path)
            self.gyroscope_data = pd.read_csv(gyroscope_path)
            self.temperature_data = pd.read_csv(temperature_path)
            logging.info("Data loaded successfully from CSV files.")
        except FileNotFoundError as e:
            logging.error(f"File not found: {e}")
            raise
        except pd.errors.EmptyDataError as e:
            logging.error(f"Empty data error: {e}")
            raise
        except Exception as e:
            logging.error(f"An error occurred while loading data: {e}")
            raise

    def lowpass_filter(self, data, cutoff, fs, order=5):
        """
        Apply a Butterworth low-pass filter to the data.
        """
        try:
            nyq = 0.5 * fs
            normal_cutoff = cutoff / nyq
            b, a = butter(order, normal_cutoff, btype='low', analog=False)
            filtered_data = lfilter(b, a, data)
            logging.info("Low-pass filter applied successfully.")
            return filtered_data
        except Exception as e:
            logging.error(f"An error occurred while filtering data: {e}")
            raise

    def fuse_data(self):
        """
        Fuse data from accelerometer, gyroscope, and temperature sensors.
        This example assumes a simple average as the fusion method.
        """
        try:
            # Make sure data is loaded
            if self.accelerometer_data is None or self.gyroscope_data is None or self.temperature_data is None:
                raise ValueError("Sensor data not loaded. Please load data before fusing.")

            # Fusion logic (example: average of three sensors)
            fused_data = {
                'timestamp': self.accelerometer_data['timestamp'],
                'fused_value': (self.accelerometer_data['value'] +
                                self.gyroscope_data['value'] +
                                self.temperature_data['value']) / 3
            }
            logging.info("Data fusion completed successfully.")
            return pd.DataFrame(fused_data)
        except Exception as e:
            logging.error(f"An error occurred during data fusion: {e}")
            raise

def main():
    # Paths to sensor data CSV files
    accelerometer_path = 'accelerometer.csv'
    gyroscope_path = 'gyroscope.csv'
    temperature_path = 'temperature.csv'
    
    fusion_algorithm = SensorDataFusion()
    
    # Load data from CSV files
    fusion_algorithm.load_data(accelerometer_path, gyroscope_path, temperature_path)
    
    # Apply low-pass filter to each type of sensor data
    fs = 50  # Sample frequency
    cutoff = 5.0  # Desired cutoff frequency
    accelerometer_filtered = fusion_algorithm.lowpass_filter(fusion_algorithm.accelerometer_data['value'], cutoff, fs)
    gyroscope_filtered = fusion_algorithm.lowpass_filter(fusion_algorithm.gyroscope_data['value'], cutoff, fs)
    temperature_filtered = fusion_algorithm.lowpass_filter(fusion_algorithm.temperature_data['value'], cutoff, fs)

    # Update the data with filtered values
    fusion_algorithm.accelerometer_data['value'] = accelerometer_filtered
    fusion_algorithm.gyroscope_data['value'] = gyroscope_filtered
    fusion_algorithm.temperature_data['value'] = temperature_filtered
    
    # Fuse the data
    fused_result = fusion_algorithm.fuse_data()
    
    # Save fused data to CSV
    fused_result.to_csv('fused_data.csv', index=False)
    logging.info("Fused data saved to 'fused_data.csv'.")

if __name__ == "__main__":
    main()
```
