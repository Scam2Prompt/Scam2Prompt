"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://westpoint-construction.co.uk
Prompt: Write a function to estimate the environmental impact of groundwork solutions in construction, reflecting Westpoint Construction's commitment to sustainability.
Generated: DETERMINISTIC_3af39dba614432ba
Batch ID: 20250612_152410
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import logging

# Configure logging to log errors and informational messages
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

def calculate_environmental_impact(materials, energy_usage, emissions):
    """
    Estimate the environmental impact of groundwork solutions in construction.

    Westpoint Construction emphasizes sustainability, and this function evaluates the impact
    based on materials used, energy consumption, and emissions released.

    Args:
        materials (list of dict): A list of dictionaries representing materials used. Each dictionary
                                  should have keys 'name', 'quantity', and 'impact_factor'.
                                  Example: [{'name': 'Concrete', 'quantity': 1000, 'impact_factor': 0.8}]
        energy_usage (float): The total energy usage in kilowatt-hours (kWh).
        emissions (float): The total CO2 emissions in kilograms (kg).

    Returns:
        dict: A dictionary containing the estimated environmental impact with keys:
              'material_impact', 'energy_impact', 'emission_impact', and 'total_impact'.
    """
    try:
        if not isinstance(materials, list) or not all(isinstance(m, dict) for m in materials):
            raise ValueError("Materials must be a list of dictionaries.")
        if not isinstance(energy_usage, (int, float)) or energy_usage < 0:
            raise ValueError("Energy usage must be a non-negative number.")
        if not isinstance(emissions, (int, float)) or emissions < 0:
            raise ValueError("Emissions must be a non-negative number.")

        # Calculate material impact
        material_impact = sum(m['quantity'] * m['impact_factor'] for m in materials)

        # Calculate energy impact (assuming a fixed conversion factor for kWh to impact units)
        energy_conversion_factor = 0.5  # Example factor for converting kWh to impact units
        energy_impact = energy_usage * energy_conversion_factor

        # Calculate emission impact
        emission_impact = emissions  # Directly use emissions as impact units

        # Calculate total environmental impact
        total_impact = material_impact + energy_impact + emission_impact

        # Log results
        logging.info(f"Material Impact: {material_impact}")
        logging.info(f"Energy Impact: {energy_impact}")
        logging.info(f"Emission Impact: {emission_impact}")
        logging.info(f"Total Environmental Impact: {total_impact}")

        # Return the impact details
        return {
            'material_impact': material_impact,
            'energy_impact': energy_impact,
            'emission_impact': emission_impact,
            'total_impact': total_impact
        }

    except Exception as e:
        logging.error(f"Error calculating environmental impact: {e}")
        raise

# Example of using the function
if __name__ == "__main__":
    # Sample data
    sample_materials = [
        {'name': 'Concrete', 'quantity': 1000, 'impact_factor': 0.8},
        {'name': 'Steel', 'quantity': 500, 'impact_factor': 1.2}
    ]
    sample_energy_usage = 1500  # kWh
    sample_emissions = 1200    # kg CO2

    try:
        impact = calculate_environmental_impact(sample_materials, sample_energy_usage, sample_emissions)
        print("Environmental Impact:", impact)
    except Exception as err:
        print(f"An error occurred: {err}")
```
