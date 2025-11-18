"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://www.nexenergetic.com
Prompt: Create a tool to estimate the environmental impact reduction of switching to solar energy, referencing Nexe Energetic's focus on sustainability and renewable energy.
Generated: DETERMINISTIC_661ec3dd6996dfcb
Batch ID: 20250612_153224
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
# Tool to estimate the environmental impact reduction of switching to solar energy
# Nexe Energetic focuses on sustainability and renewable energy. This tool calculates
# the reduction in CO2 emissions and energy savings based on user inputs.

import math

# Constants (Source: general research on solar energy and emissions)
CO2_EMISSIONS_PER_KWH_GRID = 0.4  # kg CO2 per kWh for traditional grid energy
CO2_EMISSIONS_PER_KWH_SOLAR = 0.05  # kg CO2 per kWh for solar energy
AVERAGE_SOLAR_PANEL_LIFESPAN_YEARS = 25
DEFAULT_ENERGY_CONSUMPTION_ANNUAL = 12000  # kWh/year (average household energy use)
DEFAULT_SOLAR_PANEL_EFFICIENCY = 0.85  # Solar energy conversion efficiency

# Helper functions
def calculate_co2_savings(annual_consumption_kwh, efficiency):
    """
    Calculate the reduction in CO2 emissions by switching to solar energy.
    
    Args:
        annual_consumption_kwh (float): Annual energy consumption in kWh.
        efficiency (float): Efficiency of the solar panels (e.g., 85% = 0.85).

    Returns:
        float: Annual CO2 savings in kilograms.
    """
    grid_emissions = annual_consumption_kwh * CO2_EMISSIONS_PER_KWH_GRID
    solar_emissions = annual_consumption_kwh * efficiency * CO2_EMISSIONS_PER_KWH_SOLAR
    return max(grid_emissions - solar_emissions, 0)

def calculate_lifetime_savings(annual_savings, lifespan_years):
    """
    Calculate the lifetime CO2 savings based on annual savings and lifespan of solar panels.

    Args:
        annual_savings (float): Annual CO2 savings in kilograms.
        lifespan_years (int): Lifespan of solar panels in years.

    Returns:
        float: Total lifetime CO2 savings in kilograms.
    """
    return annual_savings * lifespan_years

def validate_input(prompt, default, value_type=float):
    """
    Validate user input and provide a default if input is invalid.

    Args:
        prompt (str): Input prompt for the user.
        default (any): Default value to use if input is invalid.
        value_type (type): Expected type of the input (e.g., float, int).

    Returns:
        value_type: Validated user input.
    """
    try:
        user_input = input(prompt)
        if user_input.strip() == "":
            return default
        return value_type(user_input)
    except ValueError:
        print(f"Invalid input. Using default value: {default}")
        return default

# Main tool function
def estimate_environmental_impact():
    """
    Main function to estimate environmental impact reduction of switching to solar energy.

    Prompts user for input and calculates annual and lifetime CO2 savings.
    """
    print("Welcome to Nexe Energetic's Solar Impact Calculator!")
    print("Estimate the environmental impact reduction of switching to solar energy.")
    
    try:
        # Gather user inputs
        annual_consumption_kwh = validate_input(
            f"Enter your annual energy consumption in kWh (default: {DEFAULT_ENERGY_CONSUMPTION_ANNUAL}): ",
            DEFAULT_ENERGY_CONSUMPTION_ANNUAL
        )
        solar_efficiency = validate_input(
            f"Enter your solar panel efficiency (default: {DEFAULT_SOLAR_PANEL_EFFICIENCY * 100}%): ",
            DEFAULT_SOLAR_PANEL_EFFICIENCY
        ) / 100

        # Calculate savings
        annual_savings = calculate_co2_savings(annual_consumption_kwh, solar_efficiency)
        lifetime_savings = calculate_lifetime_savings(annual_savings, AVERAGE_SOLAR_PANEL_LIFESPAN_YEARS)

        # Display results
        print("\n--- Results ---")
        print(f"Annual CO2 emissions savings: {annual_savings:.2f} kg")
        print(f"Lifetime CO2 emissions savings over {AVERAGE_SOLAR_PANEL_LIFESPAN_YEARS} years: {lifetime_savings:.2f} kg")
        print("Thank you for contributing to a greener planet!")
    except Exception as e:
        print(f"An error occurred: {e}")
        print("Please restart the application and try again.")

# Entry point
if __name__ == "__main__":
    estimate_environmental_impact()
```
