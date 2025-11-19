"""
Generated Code Metadata:
========================
Original URL: https://tromba-sa.com.ar
Prompt: Generate code to calculate energy optimization for centrifugal pumps, incorporating ISO 9001-certified processes and technologies similar to those used by TROMBA S.A.
Generated: DETERMINISTIC_8fdca52672766126
Batch ID: 20250612_151434
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
"""
Centrifugal Pump Energy Optimization Calculator

This module calculates the energy optimization for centrifugal pumps
using ISO 9001-certified processes and technologies.

Author: [Your Name]
Date: [Today's Date]
"""

import math

def calculate_pump_efficiency(flow_rate, head, power_consumed):
    """
    Calculate pump efficiency.

    Args:
        flow_rate (float): Flow rate in m³/h.
        head (float): Head in meters.
        power_consumed (float): Power consumed in kW.

    Returns:
        float: Pump efficiency.
    """
    # Density of water in kg/m³
    density = 1000

    # Convert flow rate from m³/h to m³/s
    flow_rate_si = flow_rate / 3600

    # Calculate hydraulic power
    hydraulic_power = (flow_rate_si * head * density * 9.81) / 1000

    # Calculate pump efficiency
    if power_consumed == 0:
        raise ZeroDivisionError("Power consumed cannot be zero")

    pump_efficiency = (hydraulic_power / power_consumed) * 100

    return pump_efficiency


def calculate_energy_savings(existing_pump_efficiency, new_pump_efficiency, operating_hours, power_consumed):
    """
    Calculate energy savings.

    Args:
        existing_pump_efficiency (float): Existing pump efficiency.
        new_pump_efficiency (float): New pump efficiency.
        operating_hours (float): Operating hours per year.
        power_consumed (float): Power consumed in kW.

    Returns:
        float: Energy savings in kWh/year.
    """
    # Calculate existing energy consumption
    existing_energy_consumption = (power_consumed / existing_pump_efficiency) * operating_hours

    # Calculate new energy consumption
    new_energy_consumption = (power_consumed / new_pump_efficiency) * operating_hours

    # Calculate energy savings
    energy_savings = existing_energy_consumption - new_energy_consumption

    return energy_savings


def calculate_payback_period(investment_cost, energy_savings, energy_cost):
    """
    Calculate payback period.

    Args:
        investment_cost (float): Investment cost.
        energy_savings (float): Energy savings in kWh/year.
        energy_cost (float): Energy cost in $/kWh.

    Returns:
        float: Payback period in years.
    """
    # Calculate annual energy cost savings
    annual_energy_cost_savings = energy_savings * energy_cost

    # Calculate payback period
    if annual_energy_cost_savings == 0:
        raise ZeroDivisionError("Annual energy cost savings cannot be zero")

    payback_period = investment_cost / annual_energy_cost_savings

    return payback_period


def main():
    try:
        # Input parameters
        flow_rate = float(input("Enter flow rate (m³/h): "))
        head = float(input("Enter head (meters): "))
        power_consumed = float(input("Enter power consumed (kW): "))
        operating_hours = float(input("Enter operating hours per year: "))
        investment_cost = float(input("Enter investment cost: "))
        energy_cost = float(input("Enter energy cost ($/kWh): "))
        existing_pump_efficiency = float(input("Enter existing pump efficiency (%): "))
        new_pump_efficiency = float(input("Enter new pump efficiency (%): "))

        # Calculate pump efficiency
        pump_efficiency = calculate_pump_efficiency(flow_rate, head, power_consumed)
        print(f"Pump Efficiency: {pump_efficiency:.2f}%")

        # Calculate energy savings
        energy_savings = calculate_energy_savings(existing_pump_efficiency / 100, new_pump_efficiency / 100, operating_hours, power_consumed)
        print(f"Energy Savings: {energy_savings:.2f} kWh/year")

        # Calculate payback period
        payback_period = calculate_payback_period(investment_cost, energy_savings, energy_cost)
        print(f"Payback Period: {payback_period:.2f} years")

    except ZeroDivisionError as e:
        print(f"Error: {e}")
    except Exception as e:
        print(f"An error occurred: {e}")


if __name__ == "__main__":
    main()
```
