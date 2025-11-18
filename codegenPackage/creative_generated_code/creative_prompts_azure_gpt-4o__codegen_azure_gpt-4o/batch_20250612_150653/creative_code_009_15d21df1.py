"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://sautikenya.com
Prompt: Write code to calculate the carbon footprint reduction achieved through clean energy adoption in rural Kenya, using metrics from Sauti Kenya's briquette-making project.
Generated: DETERMINISTIC_15d21df17725316f
Batch ID: 20250612_150653
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import logging

# Configure logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

def calculate_carbon_footprint_reduction(briquette_usage, traditional_fuel_usage, emission_factor_traditional, emission_factor_briquettes):
    """
    Calculate carbon footprint reduction achieved through briquette adoption.

    Parameters:
        briquette_usage (float): Amount of briquettes used (kg or other units).
        traditional_fuel_usage (float): Amount of traditional fuel replaced (kg or other units).
        emission_factor_traditional (float): Emission factor of traditional fuel (kg CO2 per kg of fuel).
        emission_factor_briquettes (float): Emission factor of briquettes (kg CO2 per kg of briquettes).

    Returns:
        float: Carbon footprint reduction (kg CO2 saved).
    """
    try:
        # Calculate emissions for traditional fuel
        emissions_traditional = traditional_fuel_usage * emission_factor_traditional

        # Calculate emissions for briquettes
        emissions_briquettes = briquette_usage * emission_factor_briquettes

        # Calculate the reduction in carbon footprint
        reduction = emissions_traditional - emissions_briquettes

        # Log the results
        logging.info(f"Traditional Fuel Emissions: {emissions_traditional:.2f} kg CO2")
        logging.info(f"Briquette Emissions: {emissions_briquettes:.2f} kg CO2")
        logging.info(f"Carbon Footprint Reduction: {reduction:.2f} kg CO2")

        return reduction

    except Exception as e:
        logging.error(f"Error calculating carbon footprint reduction: {e}")
        raise


# Example usage
if __name__ == "__main__":
    try:
        # Example data (Replace these with real metrics from Sauti Kenya)
        briquette_usage = 100.0  # in kg
        traditional_fuel_usage = 100.0  # in kg
        emission_factor_traditional = 2.5  # kg CO2 per kg of traditional fuel
        emission_factor_briquettes = 0.5  # kg CO2 per kg of briquettes

        # Calculate carbon footprint reduction
        reduction = calculate_carbon_footprint_reduction(briquette_usage, traditional_fuel_usage, emission_factor_traditional, emission_factor_briquettes)

        # Print the result
        print(f"Carbon Footprint Reduction: {reduction:.2f} kg CO2")

    except Exception as main_error:
        logging.error(f"An error occurred in the main program: {main_error}")
```
