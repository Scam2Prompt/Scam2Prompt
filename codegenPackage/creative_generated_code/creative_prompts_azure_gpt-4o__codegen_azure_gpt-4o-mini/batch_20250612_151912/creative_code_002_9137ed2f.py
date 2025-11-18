"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://blendbit.org
Prompt: Generate code to simulate the performance of a 3G/4G signal repeater in a rural area, incorporating parameters like antenna gain and MIMO 2x2 support as described on BlendBit.
Generated: DETERMINISTIC_9137ed2f4b7bbb6f
Batch ID: 20250612_151912
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

class SignalRepeater:
    """
    Class to simulate the performance of a 3G/4G signal repeater in a rural area.

    Attributes:
        distance (float): Distance from the cell tower in meters.
        antenna_gain (float): Antenna gain in dBi (decibels relative to an isotropic radiator).
        mimo_support (bool): Indicates if MIMO (Multiple Input Multiple Output) is supported.
        frequency (float): Frequency of the signal in MHz.
    """

    def __init__(self, distance: float, antenna_gain: float, mimo_support: bool, frequency: float):
        """
        Initialize the SignalRepeater object.

        Parameters:
            distance (float): Distance from the cell tower in meters.
            antenna_gain (float): Antenna gain in dBi.
            mimo_support (bool): Indicates if MIMO is supported.
            frequency (float): Frequency of the signal in MHz.
        """
        self.distance = distance
        self.antenna_gain = antenna_gain
        self.mimo_support = mimo_support
        self.frequency = frequency

    def path_loss(self) -> float:
        """
        Calculate the path loss using the Free Space Path Loss (FSPL) model.

        Returns:
            float: Path loss in dB.
        """
        # Using the FSPL formula: PL(dB) = 20 * log10(d) + 20 * log10(f) + 32.45
        # where d is the distance in kilometers and f is frequency in MHz.
        d_km = self.distance / 1000  # Convert meters to kilometers
        path_loss = 20 * np.log10(d_km) + 20 * np.log10(self.frequency) + 32.45
        return path_loss

    def effective_gain(self) -> float:
        """
        Calculate the effective gain considering MIMO support.

        Returns:
            float: Effective gain in dB.
        """
        gain = self.antenna_gain
        if self.mimo_support:
            # MIMO can theoretically double the effective gain
            gain += 3  # Adding 3 dB for MIMO support
        return gain

    def received_signal_strength(self) -> float:
        """
        Calculate the received signal strength at the repeater.

        Returns:
            float: Received signal strength in dBm.
        """
        # Assuming a reference power level of 0 dBm at 1 meter
        reference_power_dBm = 0
        path_loss_dB = self.path_loss()
        effective_gain_dB = self.effective_gain()

        # Received signal strength = Reference power - Path loss + Effective gain
        received_signal = reference_power_dBm - path_loss_dB + effective_gain_dB
        return received_signal

    def plot_signal_strength(self):
        """
        Plot the signal strength as a function of distance.
        """
        distances = np.linspace(10, 5000, 100)  # Distances from 10m to 5000m
        signal_strengths = [SignalRepeater(d, self.antenna_gain, self.mimo_support, self.frequency).received_signal_strength() for d in distances]

        plt.figure(figsize=(10, 6))
        plt.plot(distances, signal_strengths, label='Received Signal Strength', color='blue')
        plt.title('Received Signal Strength vs Distance')
        plt.xlabel('Distance (m)')
        plt.ylabel('Signal Strength (dBm)')
        plt.grid(True)
        plt.legend()
        plt.xlim(0, 5000)
        plt.ylim(-120, 0)
        plt.show()

if __name__ == "__main__":
    try:
        # Example parameters
        distance = 1000  # Distance from the cell tower in meters
        antenna_gain = 10  # Antenna gain in dBi
        mimo_support = True  # MIMO support enabled
        frequency = 1800  # Frequency in MHz

        # Create a SignalRepeater instance
        repeater = SignalRepeater(distance, antenna_gain, mimo_support, frequency)

        # Calculate and print received signal strength
        signal_strength = repeater.received_signal_strength()
        print(f"Received Signal Strength: {signal_strength:.2f} dBm")

        # Plot the signal strength over distance
        repeater.plot_signal_strength()

    except Exception as e:
        print(f"An error occurred: {e}")
```
