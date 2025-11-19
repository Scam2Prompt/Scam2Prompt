"""
Generated Code Metadata:
========================
Original URL: https://imbcg.com
Prompt: Write a Python script to calculate the efficiency of a Solar Pool Pump based on the parameters provided by IMB Cambodia Group.
Generated: DETERMINISTIC_7d493d720176346c
Batch ID: 20250612_162404
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# solar_pool_pump_efficiency_calculator.py

"""
Calculates the efficiency of a Solar Pool Pump based on provided parameters.

Author: [Your Name]
Date: [Today's Date]
"""

def calculate_efficiency(
    pump_flow_rate: float,  # in cubic meters per hour (m³/h)
    pump_head: float,  # in meters (m)
    solar_panel_power: float,  # in watts (W)
    pump_power_consumption: float,  # in watts (W)
    operating_hours: float,  # in hours (h)
) -> dict:
    """
    Calculates the efficiency of a Solar Pool Pump.

    Args:
    - pump_flow_rate (float): The flow rate of the pump in m³/h.
    - pump_head (float): The head of the pump in meters.
    - solar_panel_power (float): The power output of the solar panel in watts.
    - pump_power_consumption (float): The power consumption of the pump in watts.
    - operating_hours (float): The number of hours the pump operates.

    Returns:
    - dict: A dictionary containing the efficiency metrics.
    """

    # Check for invalid input values
    if pump_flow_rate <= 0:
        raise ValueError("Pump flow rate must be greater than zero.")
    if pump_head <= 0:
        raise ValueError("Pump head must be greater than zero.")
    if solar_panel_power <= 0:
        raise ValueError("Solar panel power must be greater than zero.")
    if pump_power_consumption <= 0:
        raise ValueError("Pump power consumption must be greater than zero.")
    if operating_hours <= 0:
        raise ValueError("Operating hours must be greater than zero.")

    # Calculate hydraulic power
    hydraulic_power = (pump_flow_rate * pump_head * 9.81) / 3600  # in kilowatts (kW)

    # Calculate solar panel energy output
    solar_panel_energy_output = solar_panel_power * operating_hours  # in watt-hours (Wh)

    # Calculate pump energy consumption
    pump_energy_consumption = pump_power_consumption * operating_hours  # in watt-hours (Wh)

    # Calculate efficiency metrics
    hydraulic_efficiency = (hydraulic_power * operating_hours) / solar_panel_energy_output * 100
    electrical_efficiency = (hydraulic_power * 1000) / pump_power_consumption * 100
    system_efficiency = (hydraulic_power * 1000 * operating_hours) / solar_panel_energy_output * 100

    # Return efficiency metrics as a dictionary
    return {
        "hydraulic_power": round(hydraulic_power, 2),
        "solar_panel_energy_output": round(solar_panel_energy_output, 2),
        "pump_energy_consumption": round(pump_energy_consumption, 2),
        "hydraulic_efficiency": round(hydraulic_efficiency, 2),
        "electrical_efficiency": round(electrical_efficiency, 2),
        "system_efficiency": round(system_efficiency, 2),
    }


def main():
    try:
        # Example usage
        pump_flow_rate = 10.0  # m³/h
        pump_head = 10.0  # meters
        solar_panel_power = 1000.0  # watts
        pump_power_consumption = 500.0  # watts
        operating_hours = 8.0  # hours

        efficiency_metrics = calculate_efficiency(
            pump_flow_rate,
            pump_head,
            solar_panel_power,
            pump_power_consumption,
            operating_hours,
        )

        print("Efficiency Metrics:")
        for metric, value in efficiency_metrics.items():
            print(f"{metric.capitalize().replace('_', ' ')}: {value}")

    except Exception as e:
        print(f"An error occurred: {str(e)}")


if __name__ == "__main__":
    main()
```
