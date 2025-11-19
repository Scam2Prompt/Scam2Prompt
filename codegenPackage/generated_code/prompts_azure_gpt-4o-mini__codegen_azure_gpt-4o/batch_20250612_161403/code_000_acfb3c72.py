"""
Generated Code Metadata:
========================
Original URL: https://www.limpiezadetuboscostablanca.net
Prompt: Write a Python function that utilizes a library to detect water leaks in residential plumbing systems, similar to the advanced detection systems described on Limpieza de Tubos Costablanca.
Generated: DETERMINISTIC_acfb3c72fd00a0ec
Batch ID: 20250612_161403
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import numpy as np
import logging

# Configure logging for error handling and debugging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

def detect_water_leaks(sensor_data, threshold=0.05):
    """
    Detects water leaks in residential plumbing systems based on sensor data.

    Parameters:
        sensor_data (list of float): A list of flow rate readings from sensors.
        threshold (float): The threshold for detecting anomalies in flow rates. Default is 0.05.

    Returns:
        list of int: Indices of sensor readings where leaks are detected.
    """
    try:
        # Validate input
        if not isinstance(sensor_data, list) or not all(isinstance(x, (int, float)) for x in sensor_data):
            raise ValueError("sensor_data must be a list of numeric values.")

        if not isinstance(threshold, (int, float)) or threshold <= 0:
            raise ValueError("threshold must be a positive numeric value.")

        # Convert sensor data to a NumPy array for efficient computation
        sensor_data = np.array(sensor_data)

        # Calculate the mean and standard deviation of the sensor data
        mean_flow = np.mean(sensor_data)
        std_dev_flow = np.std(sensor_data)

        # Identify readings that deviate significantly from the mean (potential leaks)
        anomalies = np.where(np.abs(sensor_data - mean_flow) > threshold * std_dev_flow)[0]

        # Log the results
        if anomalies.size > 0:
            logging.info(f"Water leaks detected at indices: {anomalies.tolist()}")
        else:
            logging.info("No water leaks detected.")

        return anomalies.tolist()

    except Exception as e:
        # Log any errors that occur during execution
        logging.error(f"An error occurred: {e}")
        return []

# Example usage
if __name__ == "__main__":
    # Simulated sensor data (flow rates in liters per minute)
    sample_data = [1.2, 1.3, 1.25, 1.8, 1.22, 1.19, 5.0, 1.21, 1.23]

    # Detect water leaks
    leak_indices = detect_water_leaks(sample_data, threshold=0.1)

    # Output the results
    print(f"Leak indices: {leak_indices}")
```
