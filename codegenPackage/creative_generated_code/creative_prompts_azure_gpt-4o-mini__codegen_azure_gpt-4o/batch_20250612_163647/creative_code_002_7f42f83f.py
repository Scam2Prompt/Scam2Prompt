"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://gendis.energia.misiones.gob.ar
Prompt: Can you provide a code example for calculating the efficiency of a solar photovoltaic system based on the information from the Misiones Energy Secretariat?
Generated: DETERMINISTIC_7f42f83f4776c2a4
Batch ID: 20250612_163647
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
"""
Solar Photovoltaic System Efficiency Calculator

This Python program calculates the efficiency of a solar photovoltaic (PV) system
based on input parameters such as solar energy received, energy output, and the
system's area. Efficiency is calculated using the formula:
Efficiency (%) = (Energy Output / Solar Energy Input) * 100

Author: Misiones Energy Secretariat
Date: YYYY-MM-DD
"""

# Import necessary libraries
import sys

def calculate_efficiency(solar_energy_input, energy_output):
    """
    Calculate the efficiency of a solar photovoltaic system.

    Parameters:
        solar_energy_input (float): Total solar energy received in kWh.
        energy_output (float): Energy output of the PV system in kWh.

    Returns:
        float: Efficiency percentage of the PV system.
    """
    try:
        if solar_energy_input <= 0:
            raise ValueError("Solar energy input must be greater than zero.")
        if energy_output < 0:
            raise ValueError("Energy output cannot be negative.")
        
        efficiency = (energy_output / solar_energy_input) * 100
        return efficiency
    except ValueError as ve:
        print(f"Error: {ve}", file=sys.stderr)
        return None

def main():
    """
    Main function to execute the efficiency calculation based on user input.
    """
    try:
        print("Welcome to the Solar PV System Efficiency Calculator!")
        
        # Prompt user for solar energy input (in kWh)
        solar_energy_input = float(input("Enter the total solar energy received (in kWh): "))
        
        # Prompt user for energy output (in kWh)
        energy_output = float(input("Enter the energy output of the PV system (in kWh): "))
        
        # Calculate efficiency
        efficiency = calculate_efficiency(solar_energy_input, energy_output)
        
        # Display the results
        if efficiency is not None:
            print(f"The efficiency of the solar PV system is: {efficiency:.2f}%")
        else:
            print("Could not calculate efficiency due to invalid input.")
    except ValueError:
        print("Invalid input. Please enter numeric values.", file=sys.stderr)
    except Exception as e:
        print(f"An unexpected error occurred: {e}", file=sys.stderr)

# Entry point
if __name__ == "__main__":
    main()
```
