"""
Generated Code Metadata:
========================
Original URL: https://aktivrorteknikk.no
Prompt: Write a program to simulate leak detection in water pipelines using techniques such as acoustic sensors or gas detection, inspired by Aktiv Rørteknikk AS's leak detection services.
Generated: DETERMINISTIC_8318cb3c20a5b2f1
Batch ID: 20250612_154209
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import numpy as np
import matplotlib.pyplot as plt
from scipy.signal import savgol_filter

class LeakDetector:
    """
    Simulates leak detection in water pipelines using acoustic sensors or gas detection.
    """

    def __init__(self, sample_rate, threshold=0.5):
        """
        Initializes the leak detector.

        Args:
        - sample_rate (int): Sample rate of the acoustic sensor data.
        - threshold (float, optional): Threshold for detecting leaks. Defaults to 0.5.
        """
        self.sample_rate = sample_rate
        self.threshold = threshold

    def generate_sensor_data(self, frequency, amplitude, noise_level, duration):
        """
        Generates simulated acoustic sensor data.

        Args:
        - frequency (float): Frequency of the signal.
        - amplitude (float): Amplitude of the signal.
        - noise_level (float): Level of random noise.
        - duration (float): Duration of the signal.

        Returns:
        - data (numpy array): Simulated sensor data.
        """
        time = np.arange(0, duration, 1 / self.sample_rate)
        signal = amplitude * np.sin(2 * np.pi * frequency * time)
        noise = noise_level * np.random.randn(len(time))
        data = signal + noise
        return data

    def detect_leak(self, data):
        """
        Detects leaks in the sensor data using a simple threshold-based approach.

        Args:
        - data (numpy array): Sensor data.

        Returns:
        - leak_detected (bool): Whether a leak is detected.
        """
        filtered_data = savgol_filter(data, 51, 3)
        leak_detected = np.any(np.abs(filtered_data) > self.threshold)
        return leak_detected

    def plot_data(self, data, leak_detected):
        """
        Plots the sensor data and leak detection result.

        Args:
        - data (numpy array): Sensor data.
        - leak_detected (bool): Whether a leak is detected.
        """
        time = np.arange(0, len(data)) / self.sample_rate
        plt.plot(time, data)
        plt.xlabel('Time (s)')
        plt.ylabel('Amplitude')
        plt.title('Leak Detection' + (' - Leak Detected' if leak_detected else ' - No Leak Detected'))
        plt.show()


def main():
    sample_rate = 1000  # Sample rate of the acoustic sensor data
    frequency = 20  # Frequency of the signal
    amplitude = 1.0  # Amplitude of the signal
    noise_level = 0.2  # Level of random noise
    duration = 10  # Duration of the signal

    detector = LeakDetector(sample_rate)

    # Simulate normal operation
    normal_data = detector.generate_sensor_data(frequency, amplitude, noise_level, duration)
    normal_leak_detected = detector.detect_leak(normal_data)
    print("Normal operation - Leak detected:", normal_leak_detected)
    detector.plot_data(normal_data, normal_leak_detected)

    # Simulate leak
    leak_data = detector.generate_sensor_data(frequency, amplitude * 2, noise_level, duration)
    leak_detected = detector.detect_leak(leak_data)
    print("Leak - Leak detected:", leak_detected)
    detector.plot_data(leak_data, leak_detected)


if __name__ == "__main__":
    try:
        main()
    except Exception as e:
        print("Error:", str(e))
```
