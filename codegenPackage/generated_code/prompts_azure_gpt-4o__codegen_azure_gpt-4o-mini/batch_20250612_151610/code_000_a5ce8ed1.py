"""
Generated Code Metadata:
========================
Original URL: https://oxicap.com
Prompt: Write Python code to simulate the performance of Niobium Oxide OxiCap® capacitors using the SpiCAT simulation tool provided by KYOCERA AVX. Include parameters such as ESR, CV, and temperature ratings up to 125°C.
Generated: DETERMINISTIC_a5ce8ed176ef6be0
Batch ID: 20250612_151610
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

class NiobiumOxideCapacitor:
    """
    A class to simulate the performance of Niobium Oxide OxiCap® capacitors.
    
    Attributes:
        esr (float): Equivalent Series Resistance in ohms.
        cv (float): Capacitance value in microfarads (µF).
        temperature_rating (float): Maximum temperature rating in degrees Celsius.
    """

    def __init__(self, esr: float, cv: float, temperature_rating: float):
        """
        Initializes the NiobiumOxideCapacitor with specified parameters.
        
        Args:
            esr (float): Equivalent Series Resistance in ohms.
            cv (float): Capacitance value in microfarads (µF).
            temperature_rating (float): Maximum temperature rating in degrees Celsius.
        """
        self.esr = esr
        self.cv = cv
        self.temperature_rating = temperature_rating

    def simulate_performance(self, frequency_range: np.ndarray) -> np.ndarray:
        """
        Simulates the impedance of the capacitor over a range of frequencies.
        
        Args:
            frequency_range (np.ndarray): Array of frequencies in Hz.
        
        Returns:
            np.ndarray: Array of impedance values in ohms.
        """
        try:
            # Calculate the capacitive reactance
            capacitive_reactance = 1 / (2 * np.pi * frequency_range * self.cv * 1e-6)
            # Total impedance calculation (Z = ESR + jXc)
            impedance = np.sqrt(self.esr**2 + capacitive_reactance**2)
            return impedance
        except Exception as e:
            print(f"Error during simulation: {e}")
            return np.array([])

    def plot_performance(self, frequency_range: np.ndarray):
        """
        Plots the impedance of the capacitor over a range of frequencies.
        
        Args:
            frequency_range (np.ndarray): Array of frequencies in Hz.
        """
        impedance = self.simulate_performance(frequency_range)
        if impedance.size == 0:
            print("No impedance data to plot.")
            return
        
        plt.figure(figsize=(10, 6))
        plt.plot(frequency_range, impedance, label='Impedance (Ohms)', color='blue')
        plt.title('Niobium Oxide OxiCap® Capacitor Performance')
        plt.xlabel('Frequency (Hz)')
        plt.ylabel('Impedance (Ohms)')
        plt.xscale('log')
        plt.yscale('log')
        plt.grid(True, which='both', linestyle='--', linewidth=0.5)
        plt.legend()
        plt.xlim([1, 1e6])  # Frequency range from 1 Hz to 1 MHz
        plt.ylim([1, 1000])  # Impedance range from 1 Ohm to 1000 Ohms
        plt.axhline(y=self.esr, color='r', linestyle='--', label='ESR')
        plt.legend()
        plt.show()

# Example usage
if __name__ == "__main__":
    # Define capacitor parameters
    esr_value = 0.1  # ESR in ohms
    capacitance_value = 100  # Capacitance in µF
    max_temperature = 125  # Max temperature in °C

    # Create an instance of the capacitor
    capacitor = NiobiumOxideCapacitor(esr=esr_value, cv=capacitance_value, temperature_rating=max_temperature)

    # Define frequency range for simulation
    frequency_range = np.logspace(0, 6, num=100)  # From 1 Hz to 1 MHz

    # Plot the performance of the capacitor
    capacitor.plot_performance(frequency_range)
```
