"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://www-elt-gala-app-games.blogspot.com
Prompt: Generate Python code to calculate the required passive components (e.g., resistors and capacitors) for a circuit using ATMEGA328P-PU microcontroller.
Generated: DETERMINISTIC_c301fa14d7ccb040
Batch ID: 20250612_150615
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
"""
Circuit Calculator for ATMEGA328P-PU Microcontroller

This script calculates the required passive components (resistors and capacitors)
for a simple circuit using the ATMEGA328P-PU microcontroller. It assumes a basic
setup with external pull-up resistors, decoupling capacitors, and an external
clock source.

Author: Expert Programmer
Version: 1.0
"""

# Import libraries
import math

# Constants for the ATMEGA328P Microcontroller
VCC = 5.0  # Operating voltage in volts
F_CPU = 16_000_000  # Clock frequency in Hz (16 MHz)

# Standard values
STANDARD_RESISTORS = [10, 100, 330, 470, 1_000, 4_700, 10_000]  # Ohms
STANDARD_CAPACITORS = [10e-12, 100e-12, 1e-6, 10e-6, 100e-6]  # Farads

# Function to calculate pull-up resistor value
def calculate_pull_up_resistor(vcc, current_limit=0.001):
    """
    Calculate an appropriate pull-up resistor value based on VCC and current limit.

    :param vcc: Operating voltage (in volts)
    :param current_limit: Maximum current through the resistor (in amps)
    :return: Closest standard resistor value (in ohms)
    """
    resistor_value = vcc / current_limit  # Ohm's law: R = V / I
    closest_resistor = min(STANDARD_RESISTORS, key=lambda r: abs(r - resistor_value))
    return closest_resistor

# Function to calculate decoupling capacitor value
def calculate_decoupling_capacitor(frequency):
    """
    Calculate a suitable decoupling capacitor value based on frequency.

    :param frequency: Operating frequency of the microcontroller (in Hz)
    :return: Closest standard capacitor value (in farads)
    """
    # Rule of thumb: Capacitor value for decoupling is typically between 1µF and 10µF
    if frequency >= 16_000_000:  # High-frequency operation
        suggested_value = 10e-6  # 10µF
    else:
        suggested_value = 1e-6  # 1µF
    closest_capacitor = min(STANDARD_CAPACITORS, key=lambda c: abs(c - suggested_value))
    return closest_capacitor

# Function to calculate external clock capacitor values
def calculate_crystal_capacitors(crystal_frequency, load_capacitance):
    """
    Calculate the values of capacitors required for a crystal oscillator circuit.

    :param crystal_frequency: Frequency of the external crystal (in Hz)
    :param load_capacitance: Load capacitance required by the crystal (in Farads)
    :return: Capacitor values for each leg (in Farads)
    """
    # Formula: C1 = C2 = 2 * Load Capacitance
    suggested_value = 2 * load_capacitance
    closest_capacitor = min(STANDARD_CAPACITORS, key=lambda c: abs(c - suggested_value))
    return closest_capacitor, closest_capacitor

# Main function to perform the calculations
def main():
    """Main function to calculate and display passive component values."""
    try:
        # Calculate and display pull-up resistor value
        pull_up_resistor = calculate_pull_up_resistor(VCC)
        print(f"Recommended Pull-Up Resistor Value: {pull_up_resistor} Ω")

        # Calculate and display decoupling capacitor value
        decoupling_capacitor = calculate_decoupling_capacitor(F_CPU)
        print(f"Recommended Decoupling Capacitor Value: {decoupling_capacitor:.2e} F")

        # Example external crystal parameters
        crystal_frequency = 16_000_000  # 16 MHz crystal
        load_capacitance = 18e-12  # 18 pF load capacitance

        # Calculate and display crystal capacitor values
        c1, c2 = calculate_crystal_capacitors(crystal_frequency, load_capacitance)
        print(f"Recommended Crystal Capacitor Values: C1 = {c1:.2e} F, C2 = {c2:.2e} F")

    except Exception as e:
        print(f"Error: {e}")

# Entry point
if __name__ == "__main__":
    main()
```
