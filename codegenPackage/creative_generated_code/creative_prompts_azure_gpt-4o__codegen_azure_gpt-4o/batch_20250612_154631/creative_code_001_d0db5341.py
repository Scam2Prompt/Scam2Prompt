"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://econopure.com.vn
Prompt: Generate a script to calculate the energy consumption of a RO (Reverse Osmosis) system based on Econopure's specifications for low-pressure, energy-saving RO membranes.
Generated: DETERMINISTIC_d0db5341541ca4ed
Batch ID: 20250612_154631
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
"""
Script to calculate the energy consumption of a Reverse Osmosis (RO) system 
based on Econopure's specifications for low-pressure, energy-saving RO membranes.

This script assumes the following inputs:
- Feed water flow rate (in gallons per minute, GPM)
- Operational pressure (in PSI)
- Pump efficiency (as a percentage)
- Motor efficiency (as a percentage)

The output is the energy consumption of the RO system in kilowatt-hours (kWh).

Author: Expert Programmer
Date: YYYY-MM-DD
"""

import sys

def calculate_energy_consumption(flow_rate_gpm, pressure_psi, pump_efficiency, motor_efficiency):
    """
    Calculates the energy consumption of a Reverse Osmosis (RO) system.

    Parameters:
        flow_rate_gpm (float): Feed water flow rate in gallons per minute (GPM).
        pressure_psi (float): Operational pressure in Pounds per Square Inch (PSI).
        pump_efficiency (float): Efficiency of the pump (percentage between 0 and 100).
        motor_efficiency (float): Efficiency of the motor (percentage between 0 and 100).

    Returns:
        float: Energy consumption in kilowatt-hours (kWh).
    """
    try:
        # Validate input values
        if flow_rate_gpm <= 0 or pressure_psi <= 0:
            raise ValueError("Flow rate and pressure must be greater than zero.")
        if not (0 < pump_efficiency <= 100) or not (0 < motor_efficiency <= 100):
            raise ValueError("Efficiency values must be between 0 and 100.")

        # Constants
        WATER_DENSITY = 8.34  # Density of water in lb/gal
        PSI_TO_FEET = 2.31    # Conversion factor from PSI to feet of water column
        HORSEPOWER_TO_KWH = 0.746  # Conversion factor from horsepower to kilowatts

        # Convert PSI to feet of water column
        pressure_feet = pressure_psi * PSI_TO_FEET

        # Calculate hydraulic horsepower (HP) based on flow rate and pressure
        hydraulic_hp = (flow_rate_gpm * pressure_feet * WATER_DENSITY) / 3960

        # Adjust for pump and motor efficiency
        adjusted_hp = hydraulic_hp / (pump_efficiency / 100) / (motor_efficiency / 100)

        # Convert horsepower to kWh
        energy_consumption_kwh = adjusted_hp * HORSEPOWER_TO_KWH

        return energy_consumption_kwh

    except Exception as e:
        print(f"Error: {e}")
        sys.exit(1)

def main():
    """
    Main function to handle user input and calculate energy consumption.
    """
    print("Reverse Osmosis (RO) Energy Consumption Calculator")
    try:
        # Collect user inputs
        flow_rate_gpm = float(input("Enter feed water flow rate (GPM): "))
        pressure_psi = float(input("Enter operational pressure (PSI): "))
        pump_efficiency = float(input("Enter pump efficiency (%): "))
        motor_efficiency = float(input("Enter motor efficiency (%): "))

        # Calculate energy consumption
        energy_consumption_kwh = calculate_energy_consumption(
            flow_rate_gpm, pressure_psi, pump_efficiency, motor_efficiency
        )

        # Display the result
        print(f"Energy Consumption: {energy_consumption_kwh:.2f} kWh")

    except ValueError:
        print("Invalid input. Please enter numeric values.")
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    main()
```
