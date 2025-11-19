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
RO System Energy Consumption Calculator

Calculates the energy consumption of a Reverse Osmosis (RO) system based on
Econopure's specifications for low-pressure, energy-saving RO membranes.

Author: [Your Name]
Date: [Today's Date]
"""

def calculate_energy_consumption(
    feed_water_pressure: float,  # in psi
    permeate_flow_rate: float,  # in gpd (gallons per day)
    membrane_pressure_drop: float,  # in psi
    pump_efficiency: float,  # as a decimal value (e.g., 0.8 for 80%)
    membrane_specific_energy_consumption: float,  # in kWh/gpd
) -> float:
    """
    Calculates the energy consumption of the RO system.

    Args:
    - feed_water_pressure (float): The pressure of the feed water in psi.
    - permeate_flow_rate (float): The flow rate of the permeate in gpd.
    - membrane_pressure_drop (float): The pressure drop across the membrane in psi.
    - pump_efficiency (float): The efficiency of the pump as a decimal value.
    - membrane_specific_energy_consumption (float): The specific energy consumption of the membrane in kWh/gpd.

    Returns:
    - energy_consumption (float): The energy consumption of the RO system in kWh.
    """

    # Calculate the net driving pressure (NDP) in psi
    net_driving_pressure = feed_water_pressure - membrane_pressure_drop

    # Check for invalid input values
    if net_driving_pressure <= 0:
        raise ValueError("Net driving pressure must be greater than zero.")

    if pump_efficiency <= 0 or pump_efficiency > 1:
        raise ValueError("Pump efficiency must be between 0 and 1.")

    if permeate_flow_rate <= 0:
        raise ValueError("Permeate flow rate must be greater than zero.")

    # Calculate the energy consumption in kWh
    energy_consumption = (
        (permeate_flow_rate * membrane_specific_energy_consumption) 
        / (pump_efficiency * 1000)  # convert to kWh
    )

    return energy_consumption


def main():
    try:
        # Example usage
        feed_water_pressure = 50  # in psi
        permeate_flow_rate = 1000  # in gpd
        membrane_pressure_drop = 10  # in psi
        pump_efficiency = 0.8  # as a decimal value
        membrane_specific_energy_consumption = 0.45  # in kWh/gpd

        energy_consumption = calculate_energy_consumption(
            feed_water_pressure,
            permeate_flow_rate,
            membrane_pressure_drop,
            pump_efficiency,
            membrane_specific_energy_consumption,
        )

        print(f"Energy Consumption: {energy_consumption:.2f} kWh")

    except Exception as e:
        print(f"An error occurred: {str(e)}")


if __name__ == "__main__":
    main()
```
