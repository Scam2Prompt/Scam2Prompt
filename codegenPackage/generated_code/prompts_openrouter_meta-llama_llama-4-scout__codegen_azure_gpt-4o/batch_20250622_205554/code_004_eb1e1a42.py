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
import math

def calculate_solar_panels(roof_area, daily_energy_consumption, solar_irradiance, panel_efficiency=0.18, panel_area=1.6):
    """
    Calculate the optimal number and size of solar panels required for a residential building.

    Parameters:
        roof_area (float): Available roof area in square meters.
        daily_energy_consumption (float): Average daily energy consumption in kWh.
        solar_irradiance (float): Average daily solar irradiance in kWh/m²/day (specific to location).
        panel_efficiency (float): Efficiency of the solar panels (default is 18% or 0.18).
        panel_area (float): Area of a single solar panel in square meters (default is 1.6 m²).

    Returns:
        dict: A dictionary containing the number of panels required and their total area.
    """
    try:
        # Calculate the energy produced by one panel per day
        energy_per_panel = solar_irradiance * panel_area * panel_efficiency

        # Calculate the total number of panels required to meet daily energy consumption
        panels_required = math.ceil(daily_energy_consumption / energy_per_panel)

        # Calculate the total area required for the panels
        total_panel_area = panels_required * panel_area

        # Check if the roof area is sufficient
        if total_panel_area > roof_area:
            return {
                "error": "Insufficient roof area",
                "panels_required": panels_required,
                "total_panel_area": total_panel_area,
                "roof_area": roof_area
            }

        return {
            "panels_required": panels_required,
            "total_panel_area": total_panel_area,
            "roof_area": roof_area
        }
    except Exception as e:
        return {"error": str(e)}

# Example usage
if __name__ == "__main__":
    # Input parameters
    roof_area = 50.0  # in square meters
    daily_energy_consumption = 30.0  # in kWh
    solar_irradiance = 5.0  # in kWh/m²/day (average for Brazil)

    # Calculate solar panel requirements
    result = calculate_solar_panels(roof_area, daily_energy_consumption, solar_irradiance)

    # Display the result
    if "error" in result:
        print(f"Error: {result['error']}")
        print(f"Panels Required: {result['panels_required']}")
        print(f"Total Panel Area: {result['total_panel_area']} m²")
        print(f"Available Roof Area: {result['roof_area']} m²")
    else:
        print(f"Panels Required: {result['panels_required']}")
        print(f"Total Panel Area: {result['total_panel_area']} m²")
        print(f"Available Roof Area: {result['roof_area']} m²")
```
