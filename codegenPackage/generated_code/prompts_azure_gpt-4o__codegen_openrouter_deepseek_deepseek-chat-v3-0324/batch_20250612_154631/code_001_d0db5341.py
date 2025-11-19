"""
Generated Code Metadata:
========================
Original URL: https://econopure.com.vn
Prompt: Generate a script to calculate the energy consumption of a RO (Reverse Osmosis) system based on Econopure's specifications for low-pressure, energy-saving RO membranes.
Generated: DETERMINISTIC_d0db5341541ca4ed
Batch ID: 20250612_154631
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
"""
Script to calculate the energy consumption of a Reverse Osmosis (RO) system based on Econopure's specifications
for low-pressure, energy-saving RO membranes.

Assumptions:
- Feed pressure is within the low-pressure range (typically 50-150 psi)
- System efficiency is accounted for in the calculations
- All inputs are validated for reasonable ranges
"""

def calculate_energy_consumption(flow_rate_gpd, feed_pressure_psi, system_efficiency=0.85):
    """
    Calculate the energy consumption of an RO system in kWh per 1000 gallons.

    Parameters:
    - flow_rate_gpd (float): System flow rate in gallons per day (GPD)
    - feed_pressure_psi (float): Feed pressure in pounds per square inch (psi)
    - system_efficiency (float): System efficiency factor (0-1), default 0.85 (85%)

    Returns:
    - float: Energy consumption in kWh per 1000 gallons
    - str: Error message if any validation fails

    Raises:
    - ValueError: If input values are outside reasonable ranges
    """
    # Validate input parameters
    if not (0 < flow_rate_gpd <= 1000000):  # Reasonable upper limit for flow rate
        raise ValueError("Flow rate must be between 0 and 1,000,000 GPD")
    if not (50 <= feed_pressure_psi <= 150):  # Low-pressure range for Econopure membranes
        raise ValueError("Feed pressure must be between 50 and 150 psi for low-pressure membranes")
    if not (0.5 <= system_efficiency <= 1.0):  # Reasonable efficiency range
        raise ValueError("System efficiency must be between 0.5 and 1.0")

    try:
        # Constants
        psi_to_bar = 0.0689476  # Conversion factor from psi to bar
        bar_to_kpa = 100  # Conversion factor from bar to kPa
        hours_per_day = 24
        seconds_per_hour = 3600
        gallons_to_cubic_meters = 0.00378541  # Conversion factor from gallons to cubic meters
        kw_to_w = 1000  # Conversion factor from kW to W

        # Convert feed pressure to kPa
        feed_pressure_kpa = feed_pressure_psi * psi_to_bar * bar_to_kpa

        # Convert flow rate from GPD to m³/s
        flow_rate_m3_per_s = (flow_rate_gpd * gallons_to_cubic_meters) / (hours_per_day * seconds_per_hour)

        # Calculate hydraulic power in Watts (P = Q * ΔP / η)
        hydraulic_power_w = (flow_rate_m3_per_s * feed_pressure_kpa * 1000) / system_efficiency

        # Convert to kW
        hydraulic_power_kw = hydraulic_power_w / kw_to_w

        # Calculate energy consumption per 1000 gallons
        energy_per_1000_gallons = (hydraulic_power_kw * hours_per_day * 1000) / flow_rate_gpd

        return round(energy_per_1000_gallons, 2)  # Round to 2 decimal places

    except Exception as e:
        return f"Error in calculation: {str(e)}"


if __name__ == "__main__":
    try:
        # Example usage
        flow_rate = float(input("Enter system flow rate (GPD): "))
        feed_pressure = float(input("Enter feed pressure (psi): "))
        efficiency = float(input("Enter system efficiency (0-1, default 0.85): ") or 0.85)

        result = calculate_energy_consumption(flow_rate, feed_pressure, efficiency)
        print(f"Energy consumption: {result} kWh per 1000 gallons")

    except ValueError as ve:
        print(f"Input error: {ve}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
```
