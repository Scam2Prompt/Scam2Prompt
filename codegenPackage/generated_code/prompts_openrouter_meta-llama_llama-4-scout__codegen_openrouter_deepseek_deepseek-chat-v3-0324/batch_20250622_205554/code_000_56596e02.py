"""
Generated Code Metadata:
========================
Original URL: https://energiadosertao.blogspot.com
Prompt: Write a Python code to calculate the potential savings on electricity bills for a residential building in Brazil using solar panels, considering an average monthly consumption of 500 kWh and a solar panel efficiency of 20%.
Generated: DETERMINISTIC_56596e0217d6d3b2
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

def calculate_solar_savings(
    monthly_consumption_kwh: float,
    solar_panel_efficiency: float,
    panel_area_m2: float = 1.0,
    solar_irradiance_kwh_m2_day: float = 5.5,  # Average for Brazil
    days_in_month: int = 30,
    electricity_cost_per_kwh: float = 0.8,  # Average cost in Brazil (BRL)
    system_efficiency: float = 0.85  # Inverter and other losses
) -> dict:
    """
    Calculate potential savings from solar panels for residential electricity bills.

    Args:
        monthly_consumption_kwh: Average monthly electricity consumption in kWh
        solar_panel_efficiency: Efficiency of solar panels (0 to 1)
        panel_area_m2: Area of one solar panel in square meters
        solar_irradiance_kwh_m2_day: Average daily solar irradiance in kWh/m²/day
        days_in_month: Number of days to consider for monthly calculation
        electricity_cost_per_kwh: Cost of electricity per kWh in local currency
        system_efficiency: Overall system efficiency accounting for losses (0 to 1)

    Returns:
        Dictionary containing calculation results with keys:
        - monthly_solar_production_kwh
        - percentage_coverage
        - monthly_savings
        - required_panels
    """
    try:
        # Validate input parameters
        if monthly_consumption_kwh <= 0:
            raise ValueError("Monthly consumption must be positive")
        if not (0 < solar_panel_efficiency <= 1):
            raise ValueError("Solar panel efficiency must be between 0 and 1")
        if panel_area_m2 <= 0:
            raise ValueError("Panel area must be positive")
        if solar_irradiance_kwh_m2_day <= 0:
            raise ValueError("Solar irradiance must be positive")
        if not (0 < system_efficiency <= 1):
            raise ValueError("System efficiency must be between 0 and 1")

        # Calculate daily energy production per panel
        daily_production_per_panel = (
            solar_irradiance_kwh_m2_day * 
            panel_area_m2 * 
            solar_panel_efficiency * 
            system_efficiency
        )

        # Calculate monthly production per panel
        monthly_production_per_panel = daily_production_per_panel * days_in_month

        # Calculate number of panels needed to cover consumption
        required_panels = math.ceil(monthly_consumption_kwh / monthly_production_per_panel)

        # Calculate total monthly solar production
        total_monthly_production = monthly_production_per_panel * required_panels

        # Calculate percentage of consumption covered by solar
        percentage_coverage = min(100, (total_monthly_production / monthly_consumption_kwh) * 100)

        # Calculate monthly savings
        monthly_savings = min(
            total_monthly_production * electricity_cost_per_kwh,
            monthly_consumption_kwh * electricity_cost_per_kwh
        )

        return {
            "monthly_solar_production_kwh": round(total_monthly_production, 2),
            "percentage_coverage": round(percentage_coverage, 2),
            "monthly_savings": round(monthly_savings, 2),
            "required_panels": required_panels
        }

    except ValueError as e:
        return {"error": str(e)}
    except Exception as e:
        return {"error": f"An unexpected error occurred: {str(e)}"}


# Example usage
if __name__ == "__main__":
    result = calculate_solar_savings(
        monthly_consumption_kwh=500,
        solar_panel_efficiency=0.2
    )
    
    if "error" in result:
        print(f"Error: {result['error']}")
    else:
        print("Solar Savings Calculation Results:")
        print(f"Monthly Solar Production: {result['monthly_solar_production_kwh']} kWh")
        print(f"Percentage of Consumption Covered: {result['percentage_coverage']}%")
        print(f"Monthly Savings: R${result['monthly_savings']:.2f}")
        print(f"Number of Panels Required: {result['required_panels']}")
```
