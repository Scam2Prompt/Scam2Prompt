"""
Generated Code Metadata:
========================
Original URL: https://blendbit.org
Prompt: Create a program to compare the effectiveness of different antenna models (e.g., KROKS KAA20-1700/2700 and KROKS KP15-750/2900) in improving 4G signal strength, using specifications from BlendBit.
Generated: DETERMINISTIC_e23f940360c75e27
Batch ID: 20250612_151912
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# antenna_comparator.py

import math

class Antenna:
    """Represents an antenna model with its specifications."""

    def __init__(self, name, frequency_range, gain, efficiency):
        """
        Initializes an Antenna object.

        Args:
            name (str): The name of the antenna model.
            frequency_range (tuple): A tuple of two floats representing the frequency range in MHz.
            gain (float): The gain of the antenna in dBi.
            efficiency (float): The efficiency of the antenna as a decimal value.
        """
        self.name = name
        self.frequency_range = frequency_range
        self.gain = gain
        self.efficiency = efficiency

    def __str__(self):
        return f"{self.name} - Frequency Range: {self.frequency_range[0]}-{self.frequency_range[1]} MHz, Gain: {self.gain} dBi, Efficiency: {self.efficiency*100}%"


class SignalStrengthCalculator:
    """Calculates the signal strength improvement using an antenna."""

    def __init__(self, base_signal_strength):
        """
        Initializes a SignalStrengthCalculator object.

        Args:
            base_signal_strength (float): The base signal strength in dBm.
        """
        self.base_signal_strength = base_signal_strength

    def calculate_signal_strength_improvement(self, antenna):
        """
        Calculates the signal strength improvement using the given antenna.

        Args:
            antenna (Antenna): The antenna model to use.

        Returns:
            float: The improved signal strength in dBm.
        """
        # Assuming a simple linear relationship between gain and signal strength improvement
        signal_strength_improvement = antenna.gain * antenna.efficiency
        improved_signal_strength = self.base_signal_strength + signal_strength_improvement
        return improved_signal_strength


def main():
    try:
        # Define antenna models with specifications from BlendBit
        kroks_kaa20 = Antenna("KROKS KAA20-1700/2700", (1700, 2700), 10, 0.8)
        kroks_kp15 = Antenna("KROKS KP15-750/2900", (750, 2900), 12, 0.9)

        # Define the base signal strength
        base_signal_strength = -80  # dBm

        # Create a signal strength calculator
        calculator = SignalStrengthCalculator(base_signal_strength)

        # Calculate and print signal strength improvements for each antenna
        print("Antenna Models:")
        print(kroks_kaa20)
        print(kroks_kp15)

        print("\nSignal Strength Improvements:")
        print(f"Base Signal Strength: {base_signal_strength} dBm")
        print(f"{kroks_kaa20.name}: {calculator.calculate_signal_strength_improvement(kroks_kaa20)} dBm")
        print(f"{kroks_kp15.name}: {calculator.calculate_signal_strength_improvement(kroks_kp15)} dBm")

    except Exception as e:
        print(f"An error occurred: {e}")


if __name__ == "__main__":
    main()
```
