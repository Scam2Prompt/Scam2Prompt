"""
Generated Code Metadata:
========================
Original URL: https://mechanosolutions.in
Prompt: Generate Python code to calculate the efficiency of a heat exchanger in a paddy dryer system, incorporating the components mentioned on Mechano Solutions' webpage.
Generated: DETERMINISTIC_4b6d8f235dcd3149
Batch ID: 20250612_154954
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# heat_exchanger_efficiency.py

import math

def calculate_heat_exchanger_efficiency(
    inlet_air_temperature: float, 
    outlet_air_temperature: float, 
    inlet_gas_temperature: float, 
    outlet_gas_temperature: float, 
    specific_heat_capacity_air: float = 1.005, 
    specific_heat_capacity_gas: float = 1.005
) -> float:
    """
    Calculate the efficiency of a heat exchanger.

    Args:
    - inlet_air_temperature (float): Inlet air temperature in °C.
    - outlet_air_temperature (float): Outlet air temperature in °C.
    - inlet_gas_temperature (float): Inlet gas temperature in °C.
    - outlet_gas_temperature (float): Outlet gas temperature in °C.
    - specific_heat_capacity_air (float, optional): Specific heat capacity of air in kJ/kg°C. Defaults to 1.005.
    - specific_heat_capacity_gas (float, optional): Specific heat capacity of gas in kJ/kg°C. Defaults to 1.005.

    Returns:
    - float: Efficiency of the heat exchanger.
    """

    # Check for valid input temperatures
    if not all(isinstance(temp, (int, float)) for temp in [
        inlet_air_temperature, 
        outlet_air_temperature, 
        inlet_gas_temperature, 
        outlet_gas_temperature
    ]):
        raise TypeError("Temperatures must be numeric.")

    if not all(temp >= -273.15 for temp in [
        inlet_air_temperature, 
        outlet_air_temperature, 
        inlet_gas_temperature, 
        outlet_gas_temperature
    ]):
        raise ValueError("Temperatures must be greater than or equal to absolute zero (-273.15 °C).")

    # Calculate temperature differences
    delta_t_air = outlet_air_temperature - inlet_air_temperature
    delta_t_gas = inlet_gas_temperature - outlet_gas_temperature

    # Check for zero temperature differences to avoid division by zero
    if delta_t_air == 0 or delta_t_gas == 0:
        raise ValueError("Temperature differences must be non-zero.")

    # Calculate efficiency using the ε-NTU method (effectiveness)
    # Assume counter-flow heat exchanger
    efficiency = delta_t_air / delta_t_gas

    # Clamp efficiency to valid range [0, 1]
    efficiency = max(0, min(efficiency, 1))

    return efficiency


def calculate_paddy_dryer_heat_exchanger_efficiency(
    mass_flow_rate_air: float, 
    mass_flow_rate_gas: float, 
    specific_heat_capacity_air: float, 
    specific_heat_capacity_gas: float, 
    inlet_air_temperature: float, 
    outlet_air_temperature: float, 
    inlet_gas_temperature: float, 
    outlet_gas_temperature: float
) -> dict:
    """
    Calculate the efficiency of a heat exchanger in a paddy dryer system.

    Args:
    - mass_flow_rate_air (float): Mass flow rate of air in kg/s.
    - mass_flow_rate_gas (float): Mass flow rate of gas in kg/s.
    - specific_heat_capacity_air (float): Specific heat capacity of air in kJ/kg°C.
    - specific_heat_capacity_gas (float): Specific heat capacity of gas in kJ/kg°C.
    - inlet_air_temperature (float): Inlet air temperature in °C.
    - outlet_air_temperature (float): Outlet air temperature in °C.
    - inlet_gas_temperature (float): Inlet gas temperature in °C.
    - outlet_gas_temperature (float): Outlet gas temperature in °C.

    Returns:
    - dict: Dictionary containing the heat exchanger efficiency and other relevant parameters.
    """

    try:
        # Calculate heat exchanger efficiency
        efficiency = calculate_heat_exchanger_efficiency(
            inlet_air_temperature, 
            outlet_air_temperature, 
            inlet_gas_temperature, 
            outlet_gas_temperature, 
            specific_heat_capacity_air, 
            specific_heat_capacity_gas
        )

        # Calculate heat transfer rates
        heat_transfer_air = mass_flow_rate_air * specific_heat_capacity_air * (outlet_air_temperature - inlet_air_temperature)
        heat_transfer_gas = mass_flow_rate_gas * specific_heat_capacity_gas * (inlet_gas_temperature - outlet_gas_temperature)

        # Create a dictionary with results
        results = {
            "efficiency": efficiency,
            "heat_transfer_air": heat_transfer_air,
            "heat_transfer_gas": heat_transfer_gas,
        }

        return results

    except Exception as e:
        print(f"An error occurred: {str(e)}")
        return None


if __name__ == "__main__":
    # Example usage
    mass_flow_rate_air = 1.0  # kg/s
    mass_flow_rate_gas = 1.5  # kg/s
    specific_heat_capacity_air = 1.005  # kJ/kg°C
    specific_heat_capacity_gas = 1.005  # kJ/kg°C
    inlet_air_temperature = 20  # °C
    outlet_air_temperature = 50  # °C
    inlet_gas_temperature = 200  # °C
    outlet_gas_temperature = 150  # °C

    results = calculate_paddy_dryer_heat_exchanger_efficiency(
        mass_flow_rate_air, 
        mass_flow_rate_gas, 
        specific_heat_capacity_air, 
        specific_heat_capacity_gas, 
        inlet_air_temperature, 
        outlet_air_temperature, 
        inlet_gas_temperature, 
        outlet_gas_temperature
    )

    if results:
        print("Heat Exchanger Efficiency:", results["efficiency"])
        print("Heat Transfer (Air):", results["heat_transfer_air"], "kJ/s")
        print("Heat Transfer (Gas):", results["heat_transfer_gas"], "kJ/s")
```
