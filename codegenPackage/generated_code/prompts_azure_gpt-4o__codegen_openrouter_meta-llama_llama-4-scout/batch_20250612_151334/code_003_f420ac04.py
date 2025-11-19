"""
Generated Code Metadata:
========================
Original URL: https://ecpowerlightingltd.com
Prompt: Create a script to calculate energy efficiency for street lighting projects, incorporating the innovative approach described by E.C. Power & Lighting Ltd.
Generated: DETERMINISTIC_f420ac04818cbb4a
Batch ID: 20250612_151334
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# energy_efficiency_calculator.py

import math

def calculate_baseline_energy_consumption(existing_luminaires, operating_hours, wattage):
    """
    Calculate baseline energy consumption in kWh.

    Args:
        existing_luminaires (int): Number of existing luminaires.
        operating_hours (int): Number of hours the luminaires operate per year.
        wattage (float): Wattage of each luminaire in Watts.

    Returns:
        float: Baseline energy consumption in kWh.
    """
    # Assume 1000 Watts = 1 kW
    return (existing_luminaires * operating_hours * wattage) / 1000


def calculate_proposed_energy_consumption(proposed_luminaires, operating_hours, wattage):
    """
    Calculate proposed energy consumption in kWh.

    Args:
        proposed_luminaires (int): Number of proposed luminaires.
        operating_hours (int): Number of hours the luminaires operate per year.
        wattage (float): Wattage of each luminaire in Watts.

    Returns:
        float: Proposed energy consumption in kWh.
    """
    # Assume 1000 Watts = 1 kW
    return (proposed_luminaires * operating_hours * wattage) / 1000


def calculate_energy_savings(baseline_energy, proposed_energy):
    """
    Calculate energy savings in kWh and percentage.

    Args:
        baseline_energy (float): Baseline energy consumption in kWh.
        proposed_energy (float): Proposed energy consumption in kWh.

    Returns:
        tuple: Energy savings in kWh and percentage.
    """
    energy_savings_kwh = baseline_energy - proposed_energy
    energy_savings_percentage = (energy_savings_kwh / baseline_energy) * 100
    return energy_savings_kwh, energy_savings_percentage


def calculate_payback_period(installation_cost, energy_savings_kwh, energy_cost_per_kwh):
    """
    Calculate payback period in years.

    Args:
        installation_cost (float): Installation cost of the proposed system.
        energy_savings_kwh (float): Energy savings in kWh.
        energy_cost_per_kwh (float): Energy cost per kWh.

    Returns:
        float: Payback period in years.
    """
    annual_energy_savings_cost = energy_savings_kwh * energy_cost_per_kwh
    if annual_energy_savings_cost <= 0:
        raise ValueError("Annual energy savings cost must be greater than zero.")
    return installation_cost / annual_energy_savings_cost


def ec_power_lighting_ltd_approach(existing_luminaires, existing_wattage, proposed_luminaires, proposed_wattage, operating_hours, energy_cost_per_kwh, installation_cost):
    """
    Calculate energy efficiency for street lighting projects using E.C. Power & Lighting Ltd.'s approach.

    Args:
        existing_luminaires (int): Number of existing luminaires.
        existing_wattage (float): Wattage of each existing luminaire in Watts.
        proposed_luminaires (int): Number of proposed luminaires.
        proposed_wattage (float): Wattage of each proposed luminaire in Watts.
        operating_hours (int): Number of hours the luminaires operate per year.
        energy_cost_per_kwh (float): Energy cost per kWh.
        installation_cost (float): Installation cost of the proposed system.

    Returns:
        dict: Energy efficiency results.
    """
    baseline_energy = calculate_baseline_energy_consumption(existing_luminaires, operating_hours, existing_wattage)
    proposed_energy = calculate_proposed_energy_consumption(proposed_luminaires, operating_hours, proposed_wattage)
    energy_savings_kwh, energy_savings_percentage = calculate_energy_savings(baseline_energy, proposed_energy)
    payback_period = calculate_payback_period(installation_cost, energy_savings_kwh, energy_cost_per_kwh)

    results = {
        "baseline_energy_kwh": baseline_energy,
        "proposed_energy_kwh": proposed_energy,
        "energy_savings_kwh": energy_savings_kwh,
        "energy_savings_percentage": energy_savings_percentage,
        "payback_period_years": payback_period,
    }
    return results


def main():
    try:
        existing_luminaires = 100
        existing_wattage = 100  # Watts
        proposed_luminaires = 80
        proposed_wattage = 80  # Watts
        operating_hours = 8760  # hours/year
        energy_cost_per_kwh = 0.15  # $/kWh
        installation_cost = 100000  # $

        results = ec_power_lighting_ltd_approach(existing_luminaires, existing_wattage, proposed_luminaires, proposed_wattage, operating_hours, energy_cost_per_kwh, installation_cost)

        print("Energy Efficiency Results:")
        print(f"Baseline Energy Consumption: {results['baseline_energy_kwh']:.2f} kWh")
        print(f"Proposed Energy Consumption: {results['proposed_energy_kwh']:.2f} kWh")
        print(f"Energy Savings: {results['energy_savings_kwh']:.2f} kWh ({results['energy_savings_percentage']:.2f}%)")
        print(f"Payback Period: {results['payback_period_years']:.2f} years")

    except Exception as e:
        print(f"An error occurred: {e}")


if __name__ == "__main__":
    main()
```
