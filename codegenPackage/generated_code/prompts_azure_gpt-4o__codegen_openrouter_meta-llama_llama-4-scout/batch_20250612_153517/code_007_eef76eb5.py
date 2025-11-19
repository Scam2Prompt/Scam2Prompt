"""
Generated Code Metadata:
========================
Original URL: https://payeshnirooco.com
Prompt: Generate code for calculating the efficiency of a CCHP (Combined Cooling, Heat, and Power) system, incorporating the technical specifications provided by پایش نیرو.
Generated: DETERMINISTIC_eef76eb55f66ea97
Batch ID: 20250612_153517
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# -*- coding: utf-8 -*-

"""
CCHP Efficiency Calculator

This module calculates the efficiency of a Combined Cooling, Heat, and Power (CCHP) system.

References:
    - پایش نیرو technical specifications
"""

import math

class CCHPSystem:
    def __init__(self, 
                 electrical_power_output: float, 
                 heat_output: float, 
                 cooling_output: float, 
                 fuel_input: float, 
                 electrical_efficiency: float, 
                 heat_recovery_efficiency: float, 
                 cooling_efficiency: float):
        """
        Initialize the CCHP system with technical specifications.

        Args:
        - electrical_power_output (float): Electrical power output in kW.
        - heat_output (float): Heat output in kW.
        - cooling_output (float): Cooling output in kW.
        - fuel_input (float): Fuel input in kW.
        - electrical_efficiency (float): Electrical efficiency of the system.
        - heat_recovery_efficiency (float): Heat recovery efficiency of the system.
        - cooling_efficiency (float): Cooling efficiency of the system.
        """
        self.electrical_power_output = electrical_power_output
        self.heat_output = heat_output
        self.cooling_output = cooling_output
        self.fuel_input = fuel_input
        self.electrical_efficiency = electrical_efficiency
        self.heat_recovery_efficiency = heat_recovery_efficiency
        self.cooling_efficiency = cooling_efficiency

    def calculate_electrical_efficiency(self) -> float:
        """
        Calculate the electrical efficiency of the CCHP system.

        Returns:
        - electrical_efficiency (float): Electrical efficiency of the system.
        """
        if self.fuel_input == 0:
            raise ZeroDivisionError("Fuel input cannot be zero.")
        return self.electrical_power_output / self.fuel_input

    def calculate_heat_recovery_efficiency(self) -> float:
        """
        Calculate the heat recovery efficiency of the CCHP system.

        Returns:
        - heat_recovery_efficiency (float): Heat recovery efficiency of the system.
        """
        if self.fuel_input == 0:
            raise ZeroDivisionError("Fuel input cannot be zero.")
        return self.heat_output / self.fuel_input

    def calculate_cooling_efficiency(self) -> float:
        """
        Calculate the cooling efficiency of the CCHP system.

        Returns:
        - cooling_efficiency (float): Cooling efficiency of the system.
        """
        if self.fuel_input == 0:
            raise ZeroDivisionError("Fuel input cannot be zero.")
        return self.cooling_output / self.fuel_input

    def calculate_total_efficiency(self) -> float:
        """
        Calculate the total efficiency of the CCHP system.

        Returns:
        - total_efficiency (float): Total efficiency of the system.
        """
        if self.fuel_input == 0:
            raise ZeroDivisionError("Fuel input cannot be zero.")
        total_output = self.electrical_power_output + self.heat_output + self.cooling_output
        return total_output / self.fuel_input

def main():
    try:
        # Example usage:
        electrical_power_output = 100  # kW
        heat_output = 150  # kW
        cooling_output = 50  # kW
        fuel_input = 300  # kW
        electrical_efficiency = 0.35  # 35%
        heat_recovery_efficiency = 0.45  # 45%
        cooling_efficiency = 0.25  # 25%

        cchp_system = CCHPSystem(electrical_power_output, 
                                 heat_output, 
                                 cooling_output, 
                                 fuel_input, 
                                 electrical_efficiency, 
                                 heat_recovery_efficiency, 
                                 cooling_efficiency)

        print("Electrical Efficiency: {:.2f}%".format(cchp_system.calculate_electrical_efficiency() * 100))
        print("Heat Recovery Efficiency: {:.2f}%".format(cchp_system.calculate_heat_recovery_efficiency() * 100))
        print("Cooling Efficiency: {:.2f}%".format(cchp_system.calculate_cooling_efficiency() * 100))
        print("Total Efficiency: {:.2f}%".format(cchp_system.calculate_total_efficiency() * 100))

    except Exception as e:
        print("An error occurred: ", str(e))

if __name__ == "__main__":
    main()
```
