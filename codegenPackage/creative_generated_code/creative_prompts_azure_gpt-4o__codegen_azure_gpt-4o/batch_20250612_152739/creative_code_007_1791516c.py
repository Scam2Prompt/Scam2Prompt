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
from scipy.stats import zscore

class DataFusion:
    """
    A class to perform data fusion for anomaly detection using microwave sensor 
    and thermal camera data.
    """

    def __init__(self):
        """
        Initializes the DataFusion class.
        """
        pass

    def preprocess_data(self, microwave_data, thermal_data):
        """
        Preprocesses the input data by normalizing it using Z-score normalization.

        :param microwave_data: A numpy array of microwave sensor readings.
        :param thermal_data: A numpy array of thermal camera readings.
        :return: Tuple of normalized microwave and thermal data.
        """
        try:
            # Normalize the data using Z-score normalization
            microwave_normalized = zscore(microwave_data, axis=0)
            thermal_normalized = zscore(thermal_data, axis=0)
            return microwave_normalized, thermal_normalized
        except Exception as e:
            raise ValueError(f"Error in preprocessing data: {str(e)}")

    def fuse_data(self, microwave_data, thermal_data):
        """
        Fuses the microwave sensor and thermal camera data to enhance anomaly detection.

        :param microwave_data: A numpy array of normalized microwave sensor readings.
        :param thermal_data: A numpy array of normalized thermal camera readings.
        :return: A numpy array of fused data.
        """
        try:
            # Ensure both data arrays have the same dimensions
            if microwave_data.shape != thermal_data.shape:
                raise ValueError("Microwave and thermal data must have the same shape.")
            
            # Perform weighted fusion (equal weights for demonstration)
            fused_data = (0.5 * microwave_data + 0.5 * thermal_data)
            return fused_data
        except Exception as e:
            raise ValueError(f"Error in fusing data: {str(e)}")

    def detect_anomalies(self, fused_data, threshold=2.0):
        """
        Detects anomalies in the fused data based on a threshold.

        :param fused_data: A numpy array of fused data.
        :param threshold: A float value representing the anomaly detection threshold.
        :return: A list of indices where anomalies were detected.
        """
        try:
            # Identify anomalies based on the threshold
            anomalies = np.where(np.abs(fused_data) > threshold)[0]
            return anomalies.tolist()
        except Exception as e:
            raise ValueError(f"Error in detecting anomalies: {str(e)}")


def main():
    """
    Main function to demonstrate the usage of the DataFusion class.
    """
    # Example microwave sensor and thermal camera data
    microwave_data = np.array([3.1, 2.9, 3.0, 7.5, 3.2, 3.0])
    thermal_data = np.array([3.0, 2.8, 3.1, 7.8, 3.2, 3.1])

    try:
        # Instantiate the DataFusion class
        fusion = DataFusion()

        # Preprocess the data
        microwave_normalized, thermal_normalized = fusion.preprocess_data(microwave_data, thermal_data)

        # Fuse the data
        fused_data = fusion.fuse_data(microwave_normalized, thermal_normalized)

        # Detect anomalies
        anomalies = fusion.detect_anomalies(fused_data, threshold=2.0)

        # Display results
        print("Anomalies detected at indices:", anomalies)

    except Exception as error:
        print(f"Error in main: {str(error)}")


if __name__ == "__main__":
    main()
```
