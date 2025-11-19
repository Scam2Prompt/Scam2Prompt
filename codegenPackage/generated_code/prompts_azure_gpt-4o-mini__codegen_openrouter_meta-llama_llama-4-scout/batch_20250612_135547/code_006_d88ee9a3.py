"""
Generated Code Metadata:
========================
Original URL: https://eigen.io
Prompt: Explain how to find and contain similar defects using Eigen's automated anomaly reporting features.
Generated: DETERMINISTIC_d88ee9a374545a30
Batch ID: 20250612_135547
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import numpy as np
from scipy import stats

def detect_anomalies(data, threshold=3):
    """
    Detect anomalies in a dataset using the Z-score method.

    Parameters:
    - data (list or numpy array): Input data
    - threshold (int, optional): Z-score threshold for anomaly detection. Defaults to 3.

    Returns:
    - anomalies (list): Indices of anomalous data points
    """
    # Calculate Z-scores
    z_scores = np.abs(stats.zscore(data))
    
    # Identify anomalies
    anomalies = np.where(z_scores > threshold)[0]
    
    return anomalies

def contain_defects(data, anomalies):
    """
    Contain defects by removing anomalies from the dataset.

    Parameters:
    - data (list or numpy array): Input data
    - anomalies (list): Indices of anomalous data points

    Returns:
    - cleaned_data (numpy array): Data with anomalies removed
    """
    # Convert data to numpy array
    data = np.array(data)
    
    # Remove anomalies
    cleaned_data = np.delete(data, anomalies)
    
    return cleaned_data

def eigen_anomaly_reporting(data, threshold=3):
    """
    Automated anomaly reporting using Eigen's method ( wrapper around Z-score method).

    Parameters:
    - data (list or numpy array): Input data
    - threshold (int, optional): Z-score threshold for anomaly detection. Defaults to 3.

    Returns:
    - report (dict): Anomaly report containing indices of anomalies and cleaned data
    """
    try:
        # Detect anomalies
        anomalies = detect_anomalies(data, threshold)
        
        # Contain defects
        cleaned_data = contain_defects(data, anomalies)
        
        # Generate report
        report = {
            "anomalies": anomalies.tolist(),
            "cleaned_data": cleaned_data.tolist()
        }
        
        return report
    
    except Exception as e:
        # Handle exceptions
        print(f"Error: {str(e)}")
        return None

# Example usage
if __name__ == "__main__":
    # Generate sample data
    np.random.seed(0)
    data = np.random.normal(0, 1, 100)
    data[50] = 10  # Introduce an anomaly

    # Run anomaly reporting
    report = eigen_anomaly_reporting(data)

    # Print report
    if report:
        print("Anomalies:", report["anomalies"])
        print("Cleaned Data:", report["cleaned_data"])
```
