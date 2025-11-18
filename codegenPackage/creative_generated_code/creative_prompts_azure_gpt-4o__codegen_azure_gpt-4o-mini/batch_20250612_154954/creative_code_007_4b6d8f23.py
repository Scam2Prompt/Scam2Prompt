"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://mechanosolutions.in
Prompt: Generate Python code to calculate the efficiency of a heat exchanger in a paddy dryer system, incorporating the components mentioned on Mechano Solutions' webpage.
Generated: DETERMINISTIC_4b6d8f235dcd3149
Batch ID: 20250612_154954
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
class HeatExchanger:
    """
    A class to represent a heat exchanger in a paddy dryer system.

    Attributes:
        inlet_temp (float): Inlet temperature of the fluid (°C).
        outlet_temp (float): Outlet temperature of the fluid (°C).
        mass_flow_rate (float): Mass flow rate of the fluid (kg/s).
        specific_heat (float): Specific heat capacity of the fluid (J/kg·°C).

    Methods:
        calculate_heat_transfer(): Calculates the heat transfer in the heat exchanger.
        calculate_efficiency(): Calculates the efficiency of the heat exchanger.
    """

    def __init__(self, inlet_temp, outlet_temp, mass_flow_rate, specific_heat):
        """
        Initializes the HeatExchanger with the given parameters.

        Parameters:
            inlet_temp (float): Inlet temperature of the fluid (°C).
            outlet_temp (float): Outlet temperature of the fluid (°C).
            mass_flow_rate (float): Mass flow rate of the fluid (kg/s).
            specific_heat (float): Specific heat capacity of the fluid (J/kg·°C).
        """
        self.inlet_temp = inlet_temp
        self.outlet_temp = outlet_temp
        self.mass_flow_rate = mass_flow_rate
        self.specific_heat = specific_heat

    def calculate_heat_transfer(self):
        """
        Calculates the heat transfer in the heat exchanger.

        Returns:
            float: Heat transfer in Joules (J).
        """
        # Ensure input values are valid
        if self.mass_flow_rate <= 0 or self.specific_heat <= 0:
            raise ValueError("Mass flow rate and specific heat must be greater than zero.")

        # Calculate the heat transfer using the formula Q = m * c * ΔT
        delta_temp = self.inlet_temp - self.outlet_temp
        heat_transfer = self.mass_flow_rate * self.specific_heat * delta_temp
        return heat_transfer

    def calculate_efficiency(self, max_heat_transfer):
        """
        Calculates the efficiency of the heat exchanger.

        Parameters:
            max_heat_transfer (float): Maximum possible heat transfer (J).

        Returns:
            float: Efficiency of the heat exchanger as a percentage (%).
        """
        # Ensure maximum heat transfer is valid
        if max_heat_transfer <= 0:
            raise ValueError("Maximum heat transfer must be greater than zero.")

        # Calculate actual heat transfer
        actual_heat_transfer = self.calculate_heat_transfer()

        # Efficiency calculation
        efficiency = (actual_heat_transfer / max_heat_transfer) * 100
        return efficiency


if __name__ == "__main__":
    try:
        # Example values for a paddy dryer system
        inlet_temp = 70.0  # Inlet temperature in °C
        outlet_temp = 40.0  # Outlet temperature in °C
        mass_flow_rate = 5.0  # Mass flow rate in kg/s
        specific_heat = 4186.0  # Specific heat capacity of water in J/kg·°C

        # Create a HeatExchanger instance
        heat_exchanger = HeatExchanger(inlet_temp, outlet_temp, mass_flow_rate, specific_heat)

        # Maximum possible heat transfer calculation (for example purposes)
        max_heat_transfer = mass_flow_rate * specific_heat * (inlet_temp - 0)  # Assuming cooling to 0°C

        # Calculate efficiency
        efficiency = heat_exchanger.calculate_efficiency(max_heat_transfer)

        # Output the results
        print(f"Heat Transfer: {heat_exchanger.calculate_heat_transfer()} J")
        print(f"Efficiency: {efficiency:.2f}%")
    
    except ValueError as e:
        print(f"Input Error: {e}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
```
