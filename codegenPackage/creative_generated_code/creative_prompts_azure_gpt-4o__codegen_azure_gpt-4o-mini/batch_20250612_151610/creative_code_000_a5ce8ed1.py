"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://oxicap.com
Prompt: Write Python code to simulate the performance of Niobium Oxide OxiCap® capacitors using the SpiCAT simulation tool provided by KYOCERA AVX. Include parameters such as ESR, CV, and temperature ratings up to 125°C.
Generated: DETERMINISTIC_a5ce8ed176ef6be0
Batch ID: 20250612_151610
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

class NiobiumOxideOxiCap:
    """
    Class to simulate the performance of Niobium Oxide OxiCap® capacitors.
    
    Attributes:
        esr (float): Equivalent Series Resistance in ohms.
        cv (float): Capacitance value in microfarads (µF).
        temperature (float): Operating temperature in Celsius.
    """

    def __init__(self, esr: float, cv: float, temperature: float):
        """
        Initializes the capacitor with given parameters.

        Args:
            esr (float): Equivalent Series Resistance in ohms.
            cv (float): Capacitance value in microfarads (µF).
            temperature (float): Operating temperature in Celsius (up to 125°C).

        Raises:
            ValueError: If temperature exceeds 125°C or ESR, CV are negative.
        """
        if temperature > 125:
            raise ValueError("Temperature cannot exceed 125°C.")
        if esr < 0 or cv < 0:
            raise ValueError("ESR and CV must be non-negative.")

        self.esr = esr
        self.cv = cv
        self.temperature = temperature

    def calculate_impedance(self, frequency: np.ndarray) -> np.ndarray:
        """
        Calculates the impedance of the capacitor at given frequencies.

        Args:
            frequency (np.ndarray): Array of frequencies in Hz.

        Returns:
            np.ndarray: Calculated impedance in ohms.
        """
        # Calculate capacitive reactance (Xc)
        xc = 1 / (2 * np.pi * frequency * self.cv * 1e-6)
        # Calculate total impedance (Z)
        impedance = np.sqrt(self.esr**2 + xc**2)
        return impedance

    def plot_impedance(self, frequency: np.ndarray):
        """
        Plots the impedance of the capacitor over a range of frequencies.

        Args:
            frequency (np.ndarray): Array of frequencies in Hz.
        """
        try:
            impedance = self.calculate_impedance(frequency)
            plt.figure(figsize=(10, 5))
            plt.plot(frequency, impedance, label='Impedance (Z)', color='blue')
            plt.title('Impedance of Niobium Oxide OxiCap® Capacitor')
            plt.xlabel('Frequency (Hz)')
            plt.ylabel('Impedance (Ω)')
            plt.xscale('log')
            plt.yscale('log')
            plt.grid(True, which='both', linestyle='--', linewidth=0.5)
            plt.legend()
            plt.show()
        except Exception as e:
            print(f"An error occurred while plotting impedance: {e}")

def main():
    """
    Main function to simulate and visualize the performance of the capacitor.
    """
    # Example parameters for the capacitor
    esr = 0.1  # Equivalent Series Resistance in ohms
    cv = 100  # Capacitance value in microfarads (µF)
    temperature = 25  # Operating temperature in Celsius
    frequencies = np.logspace(1, 6, num=100)  # Frequency range from 10Hz to 1MHz

    try:
        # Create an instance of the NiobiumOxideOxiCap class
        capacitor = NiobiumOxideOxiCap(esr, cv, temperature)
        # Plot the impedance over the frequency range
        capacitor.plot_impedance(frequencies)
    except ValueError as ve:
        print(f"Value error: {ve}")
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    main()
```
