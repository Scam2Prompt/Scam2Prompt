"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://www.limpiezadetuboscostablanca.net
Prompt: Write a Python function that utilizes a library to detect water leaks in residential plumbing systems, similar to the advanced detection systems described on Limpieza de Tubos Costablanca.
Generated: DETERMINISTIC_acfb3c72fd00a0ec
Batch ID: 20250612_161403
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import numpy as np
import matplotlib.pyplot as plt
from scipy.signal import find_peaks


def detect_water_leaks(flow_data, threshold=0.1, plot=False):
    """
    Detects potential water leaks in residential plumbing systems based on flow rate data.

    Parameters:
        flow_data (list or np.ndarray): A list or numpy array of water flow rate measurements over time.
        threshold (float): The flow rate threshold to identify abnormal spikes (default: 0.1).
        plot (bool): If True, plot the flow data with detected leaks highlighted (default: False).
    
    Returns:
        list: A list of indices where potential water leaks are detected.
    """
    try:
        # Ensure flow_data is a numpy array
        if not isinstance(flow_data, np.ndarray):
            flow_data = np.array(flow_data)

        # Check if the flow_data is non-empty
        if flow_data.size == 0:
            raise ValueError("Flow data is empty. Cannot detect water leaks.")

        # Identify peaks in the flow rate data that exceed the threshold
        peaks, _ = find_peaks(flow_data, height=threshold)

        if plot:
            # Plot the data and mark detected peaks
            plt.figure(figsize=(10, 6))
            plt.plot(flow_data, label="Flow Rate")
            plt.plot(peaks, flow_data[peaks], "ro", label="Potential Leak")
            plt.axhline(y=threshold, color="gray", linestyle="--", label="Threshold")
            plt.title("Water Flow Rate and Leak Detection")
            plt.xlabel("Time")
            plt.ylabel("Flow Rate")
            plt.legend()
            plt.grid(True)
            plt.show()

        return peaks.tolist()

    except Exception as e:
        # Handle any unexpected error gracefully
        print(f"Error in detect_water_leaks: {str(e)}")
        return []


# Example usage
if __name__ == "__main__":
    # Simulated flow data (replace with real sensor data)
    simulated_flow_data = [0.05, 0.08, 0.15, 0.07, 0.09, 0.12, 0.2, 0.06, 0.05, 0.25]
    
    # Detect leaks and plot the results
    detected_leaks = detect_water_leaks(simulated_flow_data, threshold=0.1, plot=True)
    print(f"Detected leaks at indices: {detected_leaks}")
```
