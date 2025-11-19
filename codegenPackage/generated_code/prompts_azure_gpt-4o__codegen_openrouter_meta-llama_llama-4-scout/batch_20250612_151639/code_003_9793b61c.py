"""
Generated Code Metadata:
========================
Original URL: https://bitbr.com.br
Prompt: Create a program to evaluate the stability of Wi-Fi signals in multiple environments, inspired by the intelligent Wi-Fi features of Maxnet's "Casa Conectada."
Generated: DETERMINISTIC_9793b61c8052bbee
Batch ID: 20250612_151639
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import logging
import random
import time
from dataclasses import dataclass
from enum import Enum
from typing import List

# Set up logging configuration
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

class EnvironmentType(str, Enum):
    """ Enum for different environment types """
    HOME = "home"
    OFFICE = "office"
    OUTDOOR = "outdoor"

@dataclass
class WifiSignal:
    """ Data class to represent Wi-Fi signal """
    strength: int  # in dBm
    frequency: int  # in Hz
    environment: EnvironmentType

class WifiEvaluator:
    """ Class to evaluate Wi-Fi signal stability """

    def __init__(self):
        self.signals = []

    def add_signal(self, signal: WifiSignal):
        """ Add a Wi-Fi signal to the evaluator """
        self.signals.append(signal)

    def evaluate_stability(self):
        """ Evaluate the stability of Wi-Fi signals """
        if not self.signals:
            logging.warning("No Wi-Fi signals to evaluate")
            return

        # Group signals by environment
        signals_by_environment = {}
        for signal in self.signals:
            if signal.environment not in signals_by_environment:
                signals_by_environment[signal.environment] = []
            signals_by_environment[signal.environment].append(signal)

        # Calculate signal stability for each environment
        stability_results = {}
        for environment, signals in signals_by_environment.items():
            signal_strengths = [signal.strength for signal in signals]
            avg_signal_strength = sum(signal_strengths) / len(signal_strengths)
            signal_stability = self.calculate_stability(signal_strengths)
            stability_results[environment] = (avg_signal_strength, signal_stability)

        return stability_results

    @staticmethod
    def calculate_stability(signal_strengths: List[int]):
        """ Calculate the stability of Wi-Fi signals """
        # Calculate the standard deviation of signal strengths
        mean = sum(signal_strengths) / len(signal_strengths)
        variance = sum((x - mean) ** 2 for x in signal_strengths) / len(signal_strengths)
        std_dev = variance ** 0.5
        return 1 / (1 + std_dev)

def simulate_wifi_signals(environment: EnvironmentType, num_signals: int):
    """ Simulate Wi-Fi signals for a given environment """
    signals = []
    for _ in range(num_signals):
        signal_strength = random.randint(-50, -20)  # Simulate signal strength between -50 dBm and -20 dBm
        frequency = random.randint(2 * 10**9, 5 * 10**9)  # Simulate frequency between 2 GHz and 5 GHz
        signal = WifiSignal(signal_strength, frequency, environment)
        signals.append(signal)
        time.sleep(0.1)  # Simulate signal measurement interval
    return signals

def main():
    evaluator = WifiEvaluator()

    # Simulate Wi-Fi signals for different environments
    environments = [EnvironmentType.HOME, EnvironmentType.OFFICE, EnvironmentType.OUTDOOR]
    for environment in environments:
        signals = simulate_wifi_signals(environment, 10)
        for signal in signals:
            evaluator.add_signal(signal)

    # Evaluate Wi-Fi signal stability
    stability_results = evaluator.evaluate_stability()
    for environment, (avg_signal_strength, signal_stability) in stability_results.items():
        logging.info(f"Environment: {environment.value}")
        logging.info(f"Average Signal Strength: {avg_signal_strength} dBm")
        logging.info(f"Signal Stability: {signal_stability:.2f}")
        logging.info("")

if __name__ == "__main__":
    main()
```
