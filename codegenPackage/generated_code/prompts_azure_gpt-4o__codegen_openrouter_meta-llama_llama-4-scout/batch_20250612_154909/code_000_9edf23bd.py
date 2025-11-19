"""
Generated Code Metadata:
========================
Original URL: https://www.limpiezadetuboscostablanca.net
Prompt: Write Python code to simulate a system for detecting water leaks using non-invasive methods, referencing advanced techniques described by Limpieza de Tubos Costablanca.
Generated: DETERMINISTIC_9edf23bd78e92232
Batch ID: 20250612_154909
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# water_leak_detection.py

import numpy as np
from scipy.signal import savgol_filter
import logging

# Set up logging configuration
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

class WaterLeakDetector:
    """
    Simulates a system for detecting water leaks using non-invasive methods.

    Attributes:
        pressure_data (list): List of pressure readings from the tube.
        flow_rate_data (list): List of flow rate readings from the tube.
        threshold (float): Threshold value for detecting leaks.
    """

    def __init__(self, pressure_data, flow_rate_data, threshold=0.5):
        """
        Initializes the WaterLeakDetector with pressure and flow rate data.

        Args:
            pressure_data (list): List of pressure readings from the tube.
            flow_rate_data (list): List of flow rate readings from the tube.
            threshold (float, optional): Threshold value for detecting leaks. Defaults to 0.5.
        """
        self.pressure_data = np.array(pressure_data)
        self.flow_rate_data = np.array(flow_rate_data)
        self.threshold = threshold

    def _filter_data(self, data):
        """
        Applies a Savitzky-Golay filter to the given data.

        Args:
            data (numpy.ndarray): Data to be filtered.

        Returns:
            numpy.ndarray: Filtered data.
        """
        return savgol_filter(data, 51, 3)

    def detect_leak(self):
        """
        Detects water leaks based on pressure and flow rate data.

        Returns:
            bool: True if a leak is detected, False otherwise.
        """
        try:
            # Filter pressure and flow rate data
            filtered_pressure = self._filter_data(self.pressure_data)
            filtered_flow_rate = self._filter_data(self.flow_rate_data)

            # Calculate the standard deviation of the filtered data
            pressure_std = np.std(filtered_pressure)
            flow_rate_std = np.std(filtered_flow_rate)

            # Check if the standard deviations exceed the threshold
            if pressure_std > self.threshold or flow_rate_std > self.threshold:
                logging.warning("Water leak detected!")
                return True
            else:
                logging.info("No water leak detected.")
                return False

        except Exception as e:
            logging.error(f"Error detecting leak: {str(e)}")
            return False


# Example usage
if __name__ == "__main__":
    pressure_data = [10.0, 12.0, 11.0, 13.0, 15.0, 14.0, 16.0, 18.0, 17.0, 19.0]
    flow_rate_data = [5.0, 6.0, 5.5, 7.0, 8.0, 7.5, 9.0, 10.0, 9.5, 11.0]

    detector = WaterLeakDetector(pressure_data, flow_rate_data)
    detector.detect_leak()
```
