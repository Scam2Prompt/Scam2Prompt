"""
Generated Code Metadata:
========================
Original URL: https://gendis.energia.misiones.gob.ar
Prompt: "Write a Python script to calculate the potential energy savings of installing a solar photovoltaic system in a rural area of Misiones."
Generated: DETERMINISTIC_f997b2390eca7601
Batch ID: 20250622_211548
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Solar PV Potential Energy Savings Calculator for Misiones, Argentina

This script calculates the potential energy savings from installing a solar PV system
in a rural area of Misiones based on solar irradiance data, system efficiency, and local electricity costs.
"""

import math
from typing import Tuple, Optional

# Constants
AVERAGE_SOLAR_IRRADIANCE_MISIONES = 4.5  # kWh/m²/day (average for Misiones)
SYSTEM_EFFICIENCY = 0.15  # Typical efficiency of commercial PV systems (15%)
ANNUAL_DEGRADATION_RATE = 0.005  # 0.5% annual efficiency degradation
ELECTRICITY_COST_MISIONES = 5.0  # Average cost per kWh in ARS (Argentine Peso)
SYSTEM_LIFESPAN_YEARS = 25  # Typical lifespan of a solar PV system


def calculate_annual_energy_production(
    system_size_kw: float,
    solar_irradiance: float = AVERAGE_SOLAR_IRRADIANCE_MISIONES,
    system_efficiency: float = SYSTEM_EFFICIENCY,
) -> float:
    """
    Calculate annual energy production of a solar PV system.

    Args:
        system_size_kw: Installed capacity of the PV system in kW.
        solar_irradiance: Average daily solar irradiance in kWh/m²/day.
        system_efficiency: Efficiency of the PV system (0-1).

    Returns:
        Annual energy production in kWh.
    """
    if system_size_kw <= 0:
        raise ValueError("System size must be positive")
    if not (0 < system_efficiency <= 1):
        raise ValueError("System efficiency must be between 0 and 1")
    if solar_irradiance <= 0:
        raise ValueError("Solar irradiance must be positive")

    daily_production = system_size_kw * solar_irradiance * system_efficiency
    return daily_production * 365  # Convert daily to annual


def calculate_lifetime_savings(
    system_size_kw: float,
    electricity_cost: float = ELECTRICITY_COST_MISIONES,
    lifespan_years: int = SYSTEM_LIFESPAN_YEARS,
    **kwargs,
) -> Tuple[float, float]:
    """
    Calculate lifetime energy production and monetary savings.

    Args:
        system_size_kw: Installed capacity of the PV system in kW.
        electricity_cost: Cost per kWh in local currency.
        lifespan_years: Expected lifespan of the system in years.
        **kwargs: Additional arguments for calculate_annual_energy_production.

    Returns:
        Tuple of (total_lifetime_energy_kWh, total_lifetime_savings)
    """
    if lifespan_years <= 0:
        raise ValueError("Lifespan must be positive")
    if electricity_cost <= 0:
        raise ValueError("Electricity cost must be positive")

    total_energy = 0.0
    total_savings = 0.0
    current_efficiency = kwargs.get("system_efficiency", SYSTEM_EFFICIENCY)

    for year in range(1, lifespan_years + 1):
        annual_energy = calculate_annual_energy_production(
            system_size_kw,
            system_efficiency=current_efficiency,
            **{k: v for k, v in kwargs.items() if k != "system_efficiency"},
        )
        total_energy += annual_energy
        total_savings += annual_energy * electricity_cost
        current_efficiency *= (1 - ANNUAL_DEGRADATION_RATE)  # Apply annual degradation

    return (total_energy, total_savings)


def main():
    """Main function to execute the solar savings calculation."""
    try:
        print("Solar PV Potential Energy Savings Calculator for Misiones")
        print("-------------------------------------------------------")

        # Get user inputs
        system_size = float(input("Enter PV system size (kW): "))
        custom_irradiance = input("Enter custom solar irradiance (kWh/m²/day) [leave blank for default 4.5]: ")
        custom_efficiency = input("Enter custom system efficiency (0-1) [leave blank for default 0.15]: ")
        custom_cost = input("Enter custom electricity cost (ARS/kWh) [leave blank for default 5.0]: ")

        # Process inputs
        irradiance = float(custom_irradiance) if custom_irradiance else AVERAGE_SOLAR_IRRADIANCE_MISIONES
        efficiency = float(custom_efficiency) if custom_efficiency else SYSTEM_EFFICIENCY
        cost = float(custom_cost) if custom_cost else ELECTRICITY_COST_MISIONES

        # Calculate and display results
        annual_energy = calculate_annual_energy_production(
            system_size,
            solar_irradiance=irradiance,
            system_efficiency=efficiency,
        )
        lifetime_energy, lifetime_savings = calculate_lifetime_savings(
            system_size,
            electricity_cost=cost,
            solar_irradiance=irradiance,
            system_efficiency=efficiency,
        )

        print("\nResults:")
        print(f"Annual Energy Production: {annual_energy:,.2f} kWh")
        print(f"Lifetime Energy Production ({SYSTEM_LIFESPAN_YEARS} years): {lifetime_energy:,.2f} kWh")
        print(f"Lifetime Savings: ARS {lifetime_savings:,.2f}")

    except ValueError as e:
        print(f"Error: {e}. Please enter valid numerical values.")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")


if __name__ == "__main__":
    main()
```
