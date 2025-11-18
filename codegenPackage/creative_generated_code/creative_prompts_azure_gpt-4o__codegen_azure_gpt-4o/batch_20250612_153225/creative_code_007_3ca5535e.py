"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://soltec-solutions.de
Prompt: Create a function to estimate the long-term environmental impact of switching to solar energy, using metrics like CO₂ reduction and energy savings discussed by Soltec Solutions.
Generated: DETERMINISTIC_3ca5535eacf9d137
Batch ID: 20250612_153225
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import math

def estimate_solar_impact(avg_daily_energy_usage_kwh, solar_panel_efficiency, avg_co2_emission_per_kwh, years=25):
    """
    Estimate the long-term environmental impact of switching to solar energy.

    Parameters:
        avg_daily_energy_usage_kwh (float): Average daily energy usage in kilowatt-hours (kWh).
        solar_panel_efficiency (float): Efficiency of the installed solar panels (0.0 to 1.0).
        avg_co2_emission_per_kwh (float): Average CO₂ emissions per kWh (kg).
        years (int): Number of years over which the impact is calculated (default is 25 years).

    Returns:
        dict: A dictionary containing the estimated total CO₂ reduction (kg) and total energy savings (kWh).
    """
    try:
        # Validate inputs
        if not (0 <= solar_panel_efficiency <= 1):
            raise ValueError("Solar panel efficiency must be between 0.0 and 1.0")
        if avg_daily_energy_usage_kwh < 0 or avg_co2_emission_per_kwh < 0 or years < 0:
            raise ValueError("Input values for energy usage, CO₂ emissions, and years must be non-negative")

        # Calculate daily energy savings from solar panels
        daily_energy_savings_kwh = avg_daily_energy_usage_kwh * solar_panel_efficiency

        # Calculate total energy savings over the specified years
        total_energy_savings_kwh = daily_energy_savings_kwh * 365 * years

        # Calculate total CO₂ reduction over the specified years
        total_co2_reduction_kg = total_energy_savings_kwh * avg_co2_emission_per_kwh

        # Return results in a dictionary
        return {
            "total_energy_savings_kwh": round(total_energy_savings_kwh, 2),
            "total_co2_reduction_kg": round(total_co2_reduction_kg, 2)
        }

    except ValueError as e:
        # Handle invalid input values
        return {"error": str(e)}

    except Exception as e:
        # Handle any unforeseen errors
        return {"error": f"An unexpected error occurred: {str(e)}"}


# Example usage:
if __name__ == "__main__":
    # User-provided values
    avg_daily_energy_usage_kwh = 30  # Average energy usage in kWh
    solar_panel_efficiency = 0.8     # Solar panel efficiency (80%)
    avg_co2_emission_per_kwh = 0.7   # Average CO₂ emissions per kWh (kg)

    result = estimate_solar_impact(avg_daily_energy_usage_kwh, solar_panel_efficiency, avg_co2_emission_per_kwh)
    print("Solar Impact Estimate:", result)
```
