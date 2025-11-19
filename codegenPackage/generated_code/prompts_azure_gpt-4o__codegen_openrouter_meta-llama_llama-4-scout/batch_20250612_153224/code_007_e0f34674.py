"""
Generated Code Metadata:
========================
Original URL: https://petrozartaj.com
Prompt: Create a Python program to calculate the mass or volume flow rate of a two-phase fluid in a dynamic metering system, ensuring compliance with petrochemical industry standards.
Generated: DETERMINISTIC_e0f34674019c22bc
Batch ID: 20250612_153224
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
"""
Dynamic Metering System Calculator for Two-Phase Fluid
=====================================================

This program calculates the mass or volume flow rate of a two-phase fluid
in a dynamic metering system, following petrochemical industry standards.

References:
- API 14.5: Design and Operation of Custody Transfer Metering Systems
- ISO 17078: Petroleum, Petrochemical and Natural Gas Industries - Subsurface Sucker Rod Pumps and Fittings
"""

import math

def calculate_mass_flow_rate(density_mixture, velocity_mixture, cross_sectional_area):
    """
    Calculate mass flow rate of a two-phase fluid.

    Args:
        density_mixture (float): Density of the mixture (kg/m^3)
        velocity_mixture (float): Velocity of the mixture (m/s)
        cross_sectional_area (float): Cross-sectional area of the pipe (m^2)

    Returns:
        float: Mass flow rate (kg/s)
    """
    return density_mixture * velocity_mixture * cross_sectional_area


def calculate_volume_flow_rate(velocity_mixture, cross_sectional_area):
    """
    Calculate volume flow rate of a two-phase fluid.

    Args:
        velocity_mixture (float): Velocity of the mixture (m/s)
        cross_sectional_area (float): Cross-sectional area of the pipe (m^2)

    Returns:
        float: Volume flow rate (m^3/s)
    """
    return velocity_mixture * cross_sectional_area


def calculate_mixture_density(density_gas, density_liquid, gas_fraction):
    """
    Calculate density of a two-phase fluid mixture.

    Args:
        density_gas (float): Density of the gas phase (kg/m^3)
        density_liquid (float): Density of the liquid phase (kg/m^3)
        gas_fraction (float): Gas fraction (unitless, between 0 and 1)

    Returns:
        float: Density of the mixture (kg/m^3)
    """
    if gas_fraction < 0 or gas_fraction > 1:
        raise ValueError("Gas fraction must be between 0 and 1")

    return density_gas * gas_fraction + density_liquid * (1 - gas_fraction)


def calculate_velocity_mixture(velocity_gas, velocity_liquid, gas_fraction):
    """
    Calculate velocity of a two-phase fluid mixture.

    Args:
        velocity_gas (float): Velocity of the gas phase (m/s)
        velocity_liquid (float): Velocity of the liquid phase (m/s)
        gas_fraction (float): Gas fraction (unitless, between 0 and 1)

    Returns:
        float: Velocity of the mixture (m/s)
    """
    if gas_fraction < 0 or gas_fraction > 1:
        raise ValueError("Gas fraction must be between 0 and 1")

    return velocity_gas * gas_fraction + velocity_liquid * (1 - gas_fraction)


def main():
    try:
        # Input parameters
        density_gas = float(input("Enter density of gas phase (kg/m^3): "))
        density_liquid = float(input("Enter density of liquid phase (kg/m^3): "))
        gas_fraction = float(input("Enter gas fraction (between 0 and 1): "))
        velocity_gas = float(input("Enter velocity of gas phase (m/s): "))
        velocity_liquid = float(input("Enter velocity of liquid phase (m/s): "))
        pipe_diameter = float(input("Enter pipe diameter (m): "))

        # Calculate cross-sectional area
        cross_sectional_area = math.pi * (pipe_diameter / 2) ** 2

        # Calculate mixture density and velocity
        density_mixture = calculate_mixture_density(density_gas, density_liquid, gas_fraction)
        velocity_mixture = calculate_velocity_mixture(velocity_gas, velocity_liquid, gas_fraction)

        # Calculate mass and volume flow rates
        mass_flow_rate = calculate_mass_flow_rate(density_mixture, velocity_mixture, cross_sectional_area)
        volume_flow_rate = calculate_volume_flow_rate(velocity_mixture, cross_sectional_area)

        # Print results
        print(f"Mass flow rate: {mass_flow_rate:.2f} kg/s")
        print(f"Volume flow rate: {volume_flow_rate:.2f} m^3/s")

    except ValueError as e:
        print(f"Error: {e}")
    except Exception as e:
        print(f"An error occurred: {e}")


if __name__ == "__main__":
    main()
```
