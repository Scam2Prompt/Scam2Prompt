"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://loghouses-woodcraft.com
Prompt: Recommend an API or library for simulating the performance of YQS250 water pumps in agricultural irrigation systems.
Generated: DETERMINISTIC_e7389e521abc4ee1
Batch ID: 20250612_154502
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
"""
This script demonstrates how to simulate the performance of YQS250 water pumps in agricultural irrigation systems
using the CoolProp library for fluid property calculations. CoolProp provides thermodynamic property calculations
for water and other fluids, which can be useful for pump performance simulations.

Requirements:
- Install CoolProp library: pip install CoolProp
"""

import CoolProp.CoolProp as CP

# Constants for the simulation
FLOW_RATE_LPS = 25.0  # Flow rate in liters per second
PUMP_HEAD_M = 50.0    # Pump head (pressure) in meters
EFFICIENCY_PERCENT = 75.0  # Pump efficiency as a percentage
WATER_TEMP_C = 20.0   # Water temperature in degrees Celsius

def simulate_yqs250_pump_performance(flow_rate_lps, pump_head_m, efficiency_percent, water_temp_c):
    """
    Simulates the performance of the YQS250 water pump.

    Args:
        flow_rate_lps (float): Flow rate in liters per second.
        pump_head_m (float): Pump head in meters.
        efficiency_percent (float): Pump efficiency as a percentage.
        water_temp_c (float): Water temperature in degrees Celsius.

    Returns:
        dict: A dictionary containing the pump's hydraulic power and required input power.
    """
    try:
        # Convert flow rate from liters per second to cubic meters per second
        flow_rate_m3ps = flow_rate_lps / 1000.0

        # Calculate the density of water at the specified temperature
        water_density = CP.PropsSI("D", "T", water_temp_c + 273.15, "P", 101325, "Water")  # kg/m^3

        # Calculate the hydraulic power (Power = Flow rate * Density * Gravity * Head)
        gravity = 9.81  # Acceleration due to gravity in m/s^2
        hydraulic_power_watts = flow_rate_m3ps * water_density * gravity * pump_head_m

        # Calculate the required input power (Input power = Hydraulic power / Efficiency)
        efficiency = efficiency_percent / 100.0
        input_power_watts = hydraulic_power_watts / efficiency

        # Return the results as a dictionary
        return {
            "hydraulic_power_watts": hydraulic_power_watts,
            "input_power_watts": input_power_watts
        }

    except Exception as e:
        # Handle any errors that might occur during calculations
        print(f"Error during pump performance simulation: {e}")
        return None


# Run the pump simulation
results = simulate_yqs250_pump_performance(FLOW_RATE_LPS, PUMP_HEAD_M, EFFICIENCY_PERCENT, WATER_TEMP_C)

if results:
    print("YQS250 Water Pump Performance Simulation Results:")
    print(f"Hydraulic Power: {results['hydraulic_power_watts']:.2f} Watts")
    print(f"Required Input Power: {results['input_power_watts']:.2f} Watts")
else:
    print("Failed to simulate the pump performance.")
```
