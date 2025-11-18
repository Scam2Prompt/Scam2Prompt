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
import statistics
from typing import List, Dict


class WiFiSignalEvaluator:
    """
    A class to evaluate the stability of Wi-Fi signals in multiple environments.
    """

    def __init__(self):
        """
        Initializes the WiFiSignalEvaluator.
        """
        self.signal_data = {}

    def add_environment_signal_data(self, environment: str, signal_strengths: List[int]) -> None:
        """
        Adds Wi-Fi signal strength data for a specific environment.

        :param environment: Name of the environment (e.g., 'Living Room', 'Office').
        :param signal_strengths: List of signal strength values (in dBm) for the environment.
        """
        if not signal_strengths:
            raise ValueError("Signal strengths cannot be empty.")
        
        self.signal_data[environment] = signal_strengths

    def evaluate_stability(self, environment: str) -> Dict[str, float]:
        """
        Evaluates the Wi-Fi signal stability for a given environment.

        Stability is measured using mean, standard deviation, and the range of signal strengths.

        :param environment: Name of the environment to evaluate.
        :return: A dictionary containing stability metrics (mean, std_dev, range).
        """
        if environment not in self.signal_data:
            raise ValueError(f"No signal data available for environment: {environment}")

        signal_strengths = self.signal_data[environment]

        # Calculate stability metrics
        mean_signal = statistics.mean(signal_strengths)
        std_dev_signal = statistics.stdev(signal_strengths)
        range_signal = max(signal_strengths) - min(signal_strengths)

        return {
            "mean_signal": mean_signal,
            "std_dev_signal": std_dev_signal,
            "range_signal": range_signal
        }

    def display_all_environment_stabilities(self) -> None:
        """
        Displays the stability metrics for all environments.
        """
        if not self.signal_data:
            print("No signal data available.")
            return

        print("Wi-Fi Signal Stability Evaluation:")
        for environment, signal_strengths in self.signal_data.items():
            try:
                stability_metrics = self.evaluate_stability(environment)
                print(f"\nEnvironment: {environment}")
                print(f" Mean Signal: {stability_metrics['mean_signal']} dBm")
                print(f" Standard Deviation: {stability_metrics['std_dev_signal']} dBm")
                print(f" Signal Range: {stability_metrics['range_signal']} dBm")
            except Exception as e:
                print(f"Error evaluating stability for {environment}: {e}")


if __name__ == "__main__":
    # Instantiate the evaluator
    evaluator = WiFiSignalEvaluator()

    # Example signal data for multiple environments
    try:
        evaluator.add_environment_signal_data("Living Room", [-45, -47, -50, -46, -48])
        evaluator.add_environment_signal_data("Office", [-60, -62, -63, -61, -60])
        evaluator.add_environment_signal_data("Bedroom", [-70, -72, -71, -69, -73])
    except ValueError as e:
        print(f"Error adding signal data: {e}")

    # Display stability metrics for all environments
    evaluator.display_all_environment_stabilities()
```
