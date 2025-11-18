"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://jauconsulting.com
Prompt: Generate a script to simulate electrical studies for engineering projects, incorporating the expertise areas mentioned by Jau Consulting.
Generated: DETERMINISTIC_da36b6b6c8b63cdf
Batch ID: 20250612_153246
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

class ElectricalStudySimulator:
    """
    A class to simulate electrical studies for engineering projects.
    
    Attributes:
        voltage (float): The voltage in volts.
        resistance (float): The resistance in ohms.
    """

    def __init__(self, voltage, resistance):
        """
        Initializes the simulator with voltage and resistance values.
        
        Parameters:
            voltage (float): The voltage in volts.
            resistance (float): The resistance in ohms.
        
        Raises:
            ValueError: If voltage or resistance is not a positive number.
        """
        if voltage <= 0 or resistance <= 0:
            raise ValueError("Voltage and resistance must be positive numbers.")
        
        self.voltage = voltage
        self.resistance = resistance

    def calculate_current(self):
        """
        Calculate the current using Ohm's Law (I = V / R).
        
        Returns:
            float: The current in amperes.
        """
        return self.voltage / self.resistance

    def plot_current_vs_voltage(self, voltage_range):
        """
        Plots the current against a range of voltage values.
        
        Parameters:
            voltage_range (list): A list of voltage values to plot against.
        """
        try:
            current_values = [voltage / self.resistance for voltage in voltage_range]
            
            plt.figure(figsize=(10, 6))
            plt.plot(voltage_range, current_values, label='Current vs Voltage', color='blue')
            plt.title('Current vs Voltage')
            plt.xlabel('Voltage (V)')
            plt.ylabel('Current (A)')
            plt.grid(True)
            plt.axhline(0, color='black',linewidth=0.5, ls='--')
            plt.axvline(0, color='black',linewidth=0.5, ls='--')
            plt.legend()
            plt.show()
        except Exception as e:
            print(f"An error occurred while plotting: {e}")

    def generate_report(self):
        """
        Generate a report of the study including voltage, resistance, and calculated current.
        
        Returns:
            pd.DataFrame: A DataFrame containing the study report.
        """
        current = self.calculate_current()
        report = {
            'Voltage (V)': [self.voltage],
            'Resistance (Ω)': [self.resistance],
            'Current (A)': [current]
        }
        return pd.DataFrame(report)

# Example of using the ElectricalStudySimulator class
if __name__ == "__main__":
    try:
        # Initialize simulator with voltage of 12V and resistance of 4Ω
        simulator = ElectricalStudySimulator(voltage=12, resistance=4)
        
        # Calculate current
        current = simulator.calculate_current()
        print(f"Calculated Current: {current} A")
        
        # Plot current vs voltage
        voltage_range = np.linspace(0, 24, 100)  # Voltage range from 0 to 24V
        simulator.plot_current_vs_voltage(voltage_range)
        
        # Generate and print report
        report_df = simulator.generate_report()
        print(report_df)
    
    except ValueError as ve:
        print(f"ValueError: {ve}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
```
