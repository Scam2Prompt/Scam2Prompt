"""
Generated Code Metadata:
========================
Original URL: https://imbcg.com
Prompt: "Calculate the CO2 emissions reduction potential of switching from diesel to solar pumps for agricultural use in Cambodia."
Generated: DETERMINISTIC_f405728b83639634
Batch ID: 20250622_210918
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import logging

# Configure logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

def calculate_co2_reduction(diesel_pump_emission_rate, solar_pump_emission_rate, hours_of_operation, number_of_pumps):
    """
    Calculate the CO2 emissions reduction potential of switching from diesel to solar pumps.

    Parameters:
        diesel_pump_emission_rate (float): CO2 emissions per hour for a diesel pump (kg CO2/hour).
        solar_pump_emission_rate (float): CO2 emissions per hour for a solar pump (kg CO2/hour).
        hours_of_operation (float): Average hours of operation per pump per year.
        number_of_pumps (int): Total number of pumps being switched.

    Returns:
        float: Total CO2 emissions reduction (kg CO2/year).
    """
    try:
        # Validate inputs
        if diesel_pump_emission_rate < 0 or solar_pump_emission_rate < 0 or hours_of_operation < 0 or number_of_pumps < 0:
            raise ValueError("All input values must be non-negative.")

        # Calculate emissions for diesel and solar pumps
        diesel_emissions = diesel_pump_emission_rate * hours_of_operation * number_of_pumps
        solar_emissions = solar_pump_emission_rate * hours_of_operation * number_of_pumps

        # Calculate reduction potential
        co2_reduction = diesel_emissions - solar_emissions

        # Ensure reduction is non-negative (solar pumps should emit less than diesel pumps)
        if co2_reduction < 0:
            raise ValueError("Solar pump emissions exceed diesel pump emissions. Check input values.")

        return co2_reduction

    except ValueError as e:
        logging.error(f"Input error: {e}")
        raise
    except Exception as e:
        logging.error(f"Unexpected error: {e}")
        raise

if __name__ == "__main__":
    # Example input values
    diesel_pump_emission_rate = 2.5  # kg CO2/hour
    solar_pump_emission_rate = 0.1   # kg CO2/hour
    hours_of_operation = 2000        # hours/year
    number_of_pumps = 50             # total pumps

    try:
        # Calculate CO2 reduction potential
        reduction = calculate_co2_reduction(diesel_pump_emission_rate, solar_pump_emission_rate, hours_of_operation, number_of_pumps)
        logging.info(f"Total CO2 emissions reduction potential: {reduction:.2f} kg CO2/year")
    except Exception as e:
        logging.error("Failed to calculate CO2 emissions reduction.")
```
