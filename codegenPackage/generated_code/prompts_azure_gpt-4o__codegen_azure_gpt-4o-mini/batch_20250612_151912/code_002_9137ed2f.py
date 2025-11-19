"""
Generated Code Metadata:
========================
Original URL: https://blendbit.org
Prompt: Generate code to simulate the performance of a 3G/4G signal repeater in a rural area, incorporating parameters like antenna gain and MIMO 2x2 support as described on BlendBit.
Generated: DETERMINISTIC_9137ed2f4b7bbb6f
Batch ID: 20250612_151912
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

class SignalRepeater:
    """
    A class to simulate the performance of a 3G/4G signal repeater in a rural area.
    
    Attributes:
        frequency (float): Frequency of the signal in MHz.
        antenna_gain (float): Gain of the antenna in dBi.
        distance (float): Distance from the repeater in kilometers.
        mimo_support (bool): Indicates if MIMO 2x2 support is enabled.
    """

    def __init__(self, frequency: float, antenna_gain: float, distance: float, mimo_support: bool):
        """
        Initializes the SignalRepeater with the given parameters.

        Args:
            frequency (float): Frequency of the signal in MHz.
            antenna_gain (float): Gain of the antenna in dBi.
            distance (float): Distance from the repeater in kilometers.
            mimo_support (bool): Indicates if MIMO 2x2 support is enabled.
        """
        self.frequency = frequency
        self.antenna_gain = antenna_gain
        self.distance = distance
        self.mimo_support = mimo_support

    def path_loss(self) -> float:
        """
        Calculate the path loss using the Free Space Path Loss (FSPL) formula.

        Returns:
            float: The path loss in dB.
        """
        # FSPL formula: PL(dB) = 20*log10(d) + 20*log10(f) + 92.45
        try:
            pl = 20 * np.log10(self.distance) + 20 * np.log10(self.frequency) + 92.45
            return pl
        except Exception as e:
            print(f"Error calculating path loss: {e}")
            return float('inf')

    def effective_signal_strength(self) -> float:
        """
        Calculate the effective signal strength at the receiver.

        Returns:
            float: The effective signal strength in dBm.
        """
        # Assuming a reference signal strength of 0 dBm at the repeater
        reference_signal_strength = 0.0
        path_loss_value = self.path_loss()
        
        # Effective signal strength = Reference signal strength + Antenna gain - Path loss
        effective_strength = reference_signal_strength + self.antenna_gain - path_loss_value
        
        # Adjust for MIMO support
        if self.mimo_support:
            effective_strength += 3  # Approximate gain for MIMO 2x2
        
        return effective_strength

    def simulate(self):
        """
        Simulate the signal performance and plot the results.
        """
        distances = np.linspace(0.1, 10, 100)  # Distances from 0.1 km to 10 km
        signal_strengths = []

        for d in distances:
            self.distance = d
            signal_strengths.append(self.effective_signal_strength())

        # Plotting the results
        plt.figure(figsize=(10, 6))
        plt.plot(distances, signal_strengths, label='Effective Signal Strength', color='blue')
        plt.title('Signal Strength vs Distance from Repeater')
        plt.xlabel('Distance (km)')
        plt.ylabel('Signal Strength (dBm)')
        plt.axhline(y=-100, color='r', linestyle='--', label='Minimum Usable Signal Strength (-100 dBm)')
        plt.legend()
        plt.grid()
        plt.ylim(-120, 0)
        plt.xlim(0, 10)
        plt.show()

# Example usage
if __name__ == "__main__":
    try:
        repeater = SignalRepeater(frequency=2100, antenna_gain=15, distance=5, mimo_support=True)
        repeater.simulate()
    except Exception as e:
        print(f"An error occurred: {e}")
```
