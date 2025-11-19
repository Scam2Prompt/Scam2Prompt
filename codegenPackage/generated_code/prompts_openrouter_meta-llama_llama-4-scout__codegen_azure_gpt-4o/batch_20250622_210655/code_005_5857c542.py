"""
Generated Code Metadata:
========================
Original URL: https://www.nexenergetic.com
Prompt: "Create a list of key considerations and a simple algorithm for selecting the appropriate size and type of solar photovoltaic system for a residential self-consumption setup, focusing on maximizing savings and sustainability."
Generated: DETERMINISTIC_5857c542f95c9db5
Batch ID: 20250622_210655
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# solar_system_selection.py

# Import necessary libraries
import math

def calculate_solar_system_size(average_monthly_consumption_kwh, peak_sun_hours_per_day, panel_efficiency, inverter_efficiency):
    """
    Calculate the required solar system size in kW based on energy consumption and local conditions.

    Parameters:
        average_monthly_consumption_kwh (float): Average monthly energy consumption in kWh.
        peak_sun_hours_per_day (float): Average daily peak sun hours in the location.
        panel_efficiency (float): Efficiency of the solar panels (0-1).
        inverter_efficiency (float): Efficiency of the inverter (0-1).

    Returns:
        float: Recommended solar system size in kW.
    """
    try:
        # Convert monthly consumption to daily consumption
        daily_consumption_kwh = average_monthly_consumption_kwh / 30.0

        # Calculate required system size in kW
        system_size_kw = daily_consumption_kwh / (peak_sun_hours_per_day * panel_efficiency * inverter_efficiency)

        return round(system_size_kw, 2)
    except ZeroDivisionError:
        raise ValueError("Efficiency values and peak sun hours must be greater than zero.")
    except Exception as e:
        raise RuntimeError(f"An error occurred during calculation: {e}")


def select_solar_panel_type(budget, sustainability_priority):
    """
    Select the appropriate solar panel type based on budget and sustainability priorities.

    Parameters:
        budget (float): Available budget for solar panels.
        sustainability_priority (bool): Whether sustainability is a priority (True/False).

    Returns:
        str: Recommended solar panel type.
    """
    try:
        if budget < 0:
            raise ValueError("Budget cannot be negative.")

        # Define panel types and their characteristics
        panel_types = {
            "Monocrystalline": {"efficiency": 0.20, "cost": 300, "sustainability": "High"},
            "Polycrystalline": {"efficiency": 0.15, "cost": 200, "sustainability": "Medium"},
            "Thin-Film": {"efficiency": 0.10, "cost": 100, "sustainability": "Low"},
        }

        # Filter panel types based on budget and sustainability priority
        suitable_panels = [
            panel for panel, details in panel_types.items()
            if details["cost"] <= budget and (not sustainability_priority or details["sustainability"] == "High")
        ]

        # Return the most efficient panel within the budget
        if suitable_panels:
            return max(suitable_panels, key=lambda panel: panel_types[panel]["efficiency"])
        else:
            return "No suitable panel found within the budget and sustainability criteria."
    except Exception as e:
        raise RuntimeError(f"An error occurred during panel selection: {e}")


def main():
    """
    Main function to demonstrate the solar system selection algorithm.
    """
    try:
        # User inputs
        average_monthly_consumption_kwh = float(input("Enter your average monthly energy consumption in kWh: "))
        peak_sun_hours_per_day = float(input("Enter the average daily peak sun hours in your location: "))
        panel_efficiency = 0.18  # Example panel efficiency (18%)
        inverter_efficiency = 0.95  # Example inverter efficiency (95%)
        budget = float(input("Enter your budget for solar panels: "))
        sustainability_priority = input("Is sustainability a priority? (yes/no): ").strip().lower() == "yes"

        # Calculate solar system size
        system_size_kw = calculate_solar_system_size(
            average_monthly_consumption_kwh,
            peak_sun_hours_per_day,
            panel_efficiency,
            inverter_efficiency
        )
        print(f"Recommended solar system size: {system_size_kw} kW")

        # Select solar panel type
        recommended_panel = select_solar_panel_type(budget, sustainability_priority)
        print(f"Recommended solar panel type: {recommended_panel}")

    except ValueError as ve:
        print(f"Input error: {ve}")
    except RuntimeError as re:
        print(f"Runtime error: {re}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")


# Entry point for the script
if __name__ == "__main__":
    main()
```
