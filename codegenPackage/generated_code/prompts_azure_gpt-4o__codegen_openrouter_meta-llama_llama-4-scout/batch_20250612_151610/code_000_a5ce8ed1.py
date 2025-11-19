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
from scipy import integrate

class NiobiumOxideOxiCap:
    """
    Simulates the performance of Niobium Oxide OxiCap capacitors.

    Parameters:
    - capacitance (float): Capacitance value in Farads.
    - esr (float): Equivalent Series Resistance in Ohms.
    - temperature_rating (float): Temperature rating in Celsius.
    """

    def __init__(self, capacitance, esr, temperature_rating):
        self.capacitance = capacitance
        self.esr = esr
        self.temperature_rating = temperature_rating

    def calculate_impedance(self, frequency):
        """
        Calculates the impedance of the capacitor at a given frequency.

        Parameters:
        - frequency (float or array-like): Frequency in Hz.

        Returns:
        - impedance (float or array-like): Impedance in Ohms.
        """
        omega = 2 * np.pi * frequency
        impedance = self.esr + 1 / (1j * omega * self.capacitance)
        return impedance

    def simulate_cv(self, voltage, temperature):
        """
        Simulates the capacitance-voltage (CV) characteristics.

        Parameters:
        - voltage (float or array-like): Voltage in Volts.
        - temperature (float): Temperature in Celsius.

        Returns:
        - capacitance_at_voltage (float or array-like): Capacitance at given voltage and temperature.
        """
        # Assume a simple linear model for CV characteristics
        capacitance_at_voltage = self.capacitance * (1 - 0.01 * (voltage - 1))
        # Apply temperature coefficient ( assume 1000 ppm/C)
        capacitance_at_voltage *= (1 - 0.001 * (temperature - 20))
        return capacitance_at_voltage

    def check_temperature_rating(self, temperature):
        """
        Checks if the given temperature is within the temperature rating.

        Parameters:
        - temperature (float): Temperature in Celsius.

        Returns:
        - bool: True if within temperature rating, False otherwise.
        """
        return temperature <= self.temperature_rating


def main():
    # Example usage
    capacitor = NiobiumOxideOxiCap(
        capacitance=100e-6,  # 100 uF
        esr=0.1,  # 100 mOhm
        temperature_rating=125  # 125°C
    )

    frequencies = np.logspace(1, 6, 100)  # 10^1 to 10^6 Hz
    impedances = capacitor.calculate_impedance(frequencies)

    import matplotlib.pyplot as plt

    plt.plot(frequencies, np.abs(impedances))
    plt.xscale('log')
    plt.xlabel('Frequency (Hz)')
    plt.ylabel('Impedance (Ohms)')
    plt.title('Impedance vs Frequency')
    plt.show()

    voltage_range = np.linspace(0, 10, 100)  # 0 to 10V
    cv_characteristics = capacitor.simulate_cv(voltage_range, 20)
    plt.plot(voltage_range, cv_characteristics)
    plt.xlabel('Voltage (V)')
    plt.ylabel('Capacitance (F)')
    plt.title('CV Characteristics at 20°C')
    plt.show()

    temperature_range = np.linspace(-40, 150, 100)  # -40 to 150°C
    for temperature in temperature_range:
        if not capacitor.check_temperature_rating(temperature):
            print(f"Temperature {temperature}°C exceeds temperature rating.")

if __name__ == "__main__":
    main()
```
