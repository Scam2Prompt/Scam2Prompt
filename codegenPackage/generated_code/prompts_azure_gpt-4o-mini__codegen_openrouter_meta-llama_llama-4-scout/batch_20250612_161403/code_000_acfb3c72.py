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
"""
Water Leak Detection Function
==============================

This function utilizes the pandas library for data manipulation and 
scikit-learn for machine learning tasks to detect water leaks in residential 
plumbing systems.

Requires:
- pandas
- scikit-learn
- numpy
"""

import pandas as pd
from sklearn.ensemble import IsolationForest
from sklearn.preprocessing import StandardScaler
import numpy as np

def detect_water_leak(flow_rates, pressure_readings, threshold=0.1):
    """
    Detect water leaks in residential plumbing systems.

    Parameters:
    - flow_rates (list): List of water flow rates.
    - pressure_readings (list): List of water pressure readings.
    - threshold (float): Threshold for anomaly detection (default=0.1).

    Returns:
    - leak_detected (bool): True if water leak detected, False otherwise.
    """

    # Combine flow rates and pressure readings into a single DataFrame
    data = pd.DataFrame({
        'flow_rate': flow_rates,
        'pressure_reading': pressure_readings
    })

    # Check for empty data
    if data.empty:
        raise ValueError("No data provided")

    # Scale data using StandardScaler
    scaler = StandardScaler()
    scaled_data = scaler.fit_transform(data)

    # Isolation Forest for anomaly detection
    isolation_forest = IsolationForest(contamination=threshold)
    isolation_forest.fit(scaled_data)

    # Predict anomalies (water leaks)
    predictions = isolation_forest.predict(scaled_data)

    # Check for anomalies
    leak_detected = np.any(predictions == -1)

    return leak_detected


def main():
    # Example usage
    flow_rates = [10.0, 12.0, 11.5, 100.0, 12.5]  # Normal flow rates with an anomaly
    pressure_readings = [50.0, 55.0, 52.0, 30.0, 58.0]  # Normal pressure readings with an anomaly

    try:
        leak_detected = detect_water_leak(flow_rates, pressure_readings)
        print(f"Water leak detected: {leak_detected}")
    except Exception as e:
        print(f"An error occurred: {str(e)}")


if __name__ == "__main__":
    main()
```
