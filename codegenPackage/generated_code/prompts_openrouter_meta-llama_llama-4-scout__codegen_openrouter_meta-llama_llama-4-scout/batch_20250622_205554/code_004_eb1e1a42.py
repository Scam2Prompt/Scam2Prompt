"""
Generated Code Metadata:
========================
Original URL: https://energiadosertao.blogspot.com
Prompt: Develop a simple algorithm to determine the optimal size and number of solar panels required for a residential building in Brazil, considering factors like roof size, energy consumption, and local solar irradiance.
Generated: DETERMINISTIC_eb1e1a42dc510258
Batch ID: 20250622_205554
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# solar_panel_calculator.py

import math

def calculate_solar_irradiance(state):
    """
    Returns the average solar irradiance in Brazil (kWh/m²/day) 
    based on the state.

    :param state: The state in Brazil (e.g., 'SP', 'RJ', 'MG', etc.)
    :return: Average solar irradiance (kWh/m²/day)
    """
    irradiance_map = {
        'SP': 5.36, 'RJ': 5.29, 'MG': 5.23, 'BA': 5.44,
        'PR': 4.93, 'SC': 5.03, 'RS': 4.83, 'PE': 5.67,
        'CE': 5.83, 'DF': 5.55
    }

    if state.upper() not in irradiance_map:
        raise ValueError(f"Unsupported state: {state}")

    return irradiance_map[state.upper()]


def calculate_required_energy_consumption(energy_bill_kwh):
    """
    Calculates the required energy consumption in kWh.

    :param energy_bill_kwh: The monthly energy consumption in kWh
    :return: Required energy consumption
    """
    return energy_bill_kwh


def calculate_roof_area(roof_length_m, roof_width_m):
    """
    Calculates the available roof area in m².

    :param roof_length_m: The length of the roof in meters
    :param roof_width_m: The width of the roof in meters
    :return: Available roof area
    """
    return roof_length_m * roof_width_m


def calculate_solar_panel_efficiency(panel_type):
    """
    Returns the efficiency of the solar panel.

    :param panel_type: The type of solar panel (e.g., 'monocrystalline', 'polycrystalline')
    :return: Efficiency of the solar panel
    """
    efficiency_map = {
        'monocrystalline': 0.20, 'polycrystalline': 0.15
    }

    if panel_type.lower() not in efficiency_map:
        raise ValueError(f"Unsupported panel type: {panel_type}")

    return efficiency_map[panel_type.lower()]


def calculate_optimal_solar_panels(
    roof_length_m, roof_width_m, 
    energy_bill_kwh, 
    state, 
    panel_type='monocrystalline', 
    system_loss=0.10
):
    """
    Calculates the optimal size and number of solar panels.

    :param roof_length_m: The length of the roof in meters
    :param roof_width_m: The width of the roof in meters
    :param energy_bill_kwh: The monthly energy consumption in kWh
    :param state: The state in Brazil
    :param panel_type: The type of solar panel
    :param system_loss: The system loss (default: 0.10)
    :return: Optimal number of solar panels and their size
    """
    required_energy = calculate_required_energy_consumption(energy_bill_kwh)
    roof_area = calculate_roof_area(roof_length_m, roof_width_m)
    solar_irradiance = calculate_solar_irradiance(state)
    panel_efficiency = calculate_solar_panel_efficiency(panel_type)

    # Daily energy consumption
    daily_energy_consumption = required_energy / 30

    # Calculate the required solar panel area
    required_panel_area = daily_energy_consumption / (solar_irradiance * panel_efficiency * (1 - system_loss))

    # Calculate the optimal number of solar panels
    # Assume standard panel size: 1.65m x 1m = 1.65m²
    standard_panel_area = 1.65
    optimal_number_of_panels = math.ceil(required_panel_area / standard_panel_area)

    # Calculate the optimal size of solar panels
    optimal_panel_size = required_panel_area / optimal_number_of_panels

    return {
        'optimal_number_of_panels': optimal_number_of_panels,
        'optimal_panel_size': f"{optimal_panel_size:.2f}m²",
        'required_energy': f"{required_energy:.2f}kWh",
        'roof_area': f"{roof_area:.2f}m²",
        'solar_irradiance': f"{solar_irradiance:.2f}kWh/m²/day",
    }


if __name__ == "__main__":
    try:
        roof_length_m = 10
        roof_width_m = 8
        energy_bill_kwh = 500
        state = 'SP'
        panel_type = 'monocrystalline'

        result = calculate_optimal_solar_panels(
            roof_length_m, roof_width_m, 
            energy_bill_kwh, 
            state, 
            panel_type
        )

        print("Optimal Solar Panel Configuration:")
        print(f"--------------------------------")
        print(f"Optimal Number of Panels: {result['optimal_number_of_panels']}")
        print(f"Optimal Panel Size: {result['optimal_panel_size']}")
        print(f"Required Energy: {result['required_energy']}")
        print(f"Roof Area: {result['roof_area']}")
        print(f"Solar Irradiance: {result['solar_irradiance']}")

    except Exception as e:
        print(f"An error occurred: {e}")
```
