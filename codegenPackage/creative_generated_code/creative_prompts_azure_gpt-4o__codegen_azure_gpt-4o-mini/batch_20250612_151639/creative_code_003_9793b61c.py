"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://bitbr.com.br
Prompt: Create a program to evaluate the stability of Wi-Fi signals in multiple environments, inspired by the intelligent Wi-Fi features of Maxnet's "Casa Conectada."
Generated: DETERMINISTIC_9793b61c8052bbee
Batch ID: 20250612_151639
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
import random
import statistics

class WiFiSignalEvaluator:
    """
    A class to evaluate Wi-Fi signal stability across multiple environments.
    """

    def __init__(self, environments):
        """
        Initializes the WiFiSignalEvaluator with a list of environments.

        Args:
            environments (list): A list of environment names.
        """
        self.environments = environments
        self.signal_data = {env: [] for env in environments}
    
    def simulate_signal_measurements(self, number_of_measurements=100):
        """
        Simulates Wi-Fi signal strength measurements for each environment.

        Args:
            number_of_measurements (int): The number of measurements to simulate per environment.
        """
        for env in self.environments:
            # Simulate signal strength in dBm using a normal distribution
            mean_signal = random.uniform(-30, -70)  # Mean Wi-Fi signal strength
            std_dev = random.uniform(5, 10)  # Standard deviation for variability
            measurements = np.random.normal(mean_signal, std_dev, number_of_measurements)
            self.signal_data[env] = measurements.tolist()

    def evaluate_stability(self):
        """
        Evaluates the stability of the Wi-Fi signal in each environment.

        Returns:
            dict: A dictionary with environment names as keys and their stability metrics.
        """
        stability_metrics = {}
        for env, measurements in self.signal_data.items():
            mean_signal = statistics.mean(measurements)
            std_dev = statistics.stdev(measurements)
            stability_metrics[env] = {
                'mean_signal': mean_signal,
                'std_dev': std_dev,
                'stability_index': self.calculate_stability_index(std_dev)
            }
        return stability_metrics
    
    def calculate_stability_index(self, std_dev):
        """
        Calculates a stability index based on standard deviation.

        Args:
            std_dev (float): The standard deviation of signal measurements.

        Returns:
            float: Stability index ranging from 0 (unstable) to 1 (very stable).
        """
        # The lower the std deviation, the higher the stability index
        return max(0, 1 - (std_dev / 40))  # Normalize against a threshold

    def plot_signal_strength(self):
        """
        Plots the signal strength measurements for each environment.
        """
        plt.figure(figsize=(10, 6))
        for env, measurements in self.signal_data.items():
            plt.plot(measurements, label=f"{env} Signal Strength")
        plt.title('Wi-Fi Signal Strength Measurements')
        plt.xlabel('Measurement Number')
        plt.ylabel('Signal Strength (dBm)')
        plt.axhline(y=-70, color='r', linestyle='--', label='Minimum Acceptable Signal')
        plt.legend()
        plt.grid()
        plt.show()


def main():
    """
    Main function to execute the Wi-Fi signal evaluator.
    """
    try:
        environments = ['Living Room', 'Kitchen', 'Bedroom', 'Office']
        evaluator = WiFiSignalEvaluator(environments)
        evaluator.simulate_signal_measurements(number_of_measurements=100)

        stability_report = evaluator.evaluate_stability()
        for env, metrics in stability_report.items():
            print(f"{env}: Mean Signal = {metrics['mean_signal']:.2f} dBm, "
                  f"Std Dev = {metrics['std_dev']:.2f}, Stability Index = {metrics['stability_index']:.2f}")

        evaluator.plot_signal_strength()
    
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    main()
```
