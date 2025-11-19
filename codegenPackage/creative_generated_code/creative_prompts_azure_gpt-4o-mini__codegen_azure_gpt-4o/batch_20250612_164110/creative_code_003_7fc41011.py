"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://trattar.blogspot.com
Prompt: Develop a function that calculates the environmental impact of using treated eucalyptus versus native hardwoods in construction, based on the practices described on the Trattar website.
Generated: DETERMINISTIC_7fc41011aa048f80
Batch ID: 20250612_164110
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import math

def calculate_environmental_impact(material_type, volume, distance, energy_cost_per_unit):
    """
    Calculate the environmental impact of using treated eucalyptus versus native hardwoods in construction.

    Args:
    - material_type (str): Type of material, either "treated_eucalyptus" or "native_hardwood".
    - volume (float): Volume of material used in cubic meters.
    - distance (float): Distance transported in kilometers.
    - energy_cost_per_unit (float): Energy cost per cubic meter transported (kWh/km).

    Returns:
    - dict: Environmental impact metrics including energy usage and carbon emissions.
             {'energy_usage': float, 'carbon_emissions': float}
    """
    # Constants for environmental factors
    CARBON_EMISSIONS_FACTOR_EUCALYPTUS = 0.45  # kg CO2 per kWh for treated eucalyptus
    CARBON_EMISSIONS_FACTOR_HARDWOOD = 0.65    # kg CO2 per kWh for native hardwoods
    PRODUCTION_ENERGY_EUCALYPTUS = 20.0        # kWh per cubic meter for treated eucalyptus
    PRODUCTION_ENERGY_HARDWOOD = 30.0          # kWh per cubic meter for native hardwoods

    # Validate inputs
    if material_type not in ["treated_eucalyptus", "native_hardwood"]:
        raise ValueError("Invalid material_type. Must be 'treated_eucalyptus' or 'native_hardwood'.")
    if volume <= 0 or distance <= 0 or energy_cost_per_unit <= 0:
        raise ValueError("Volume, distance, and energy_cost_per_unit must be positive values.")

    # Determine material-specific constants
    if material_type == "treated_eucalyptus":
        production_energy = PRODUCTION_ENERGY_EUCALYPTUS
        carbon_factor = CARBON_EMISSIONS_FACTOR_EUCALYPTUS
    else:  # material_type == "native_hardwood"
        production_energy = PRODUCTION_ENERGY_HARDWOOD
        carbon_factor = CARBON_EMISSIONS_FACTOR_HARDWOOD

    # Calculate transportation energy usage
    transportation_energy = volume * distance * energy_cost_per_unit

    # Total energy usage includes production and transportation energy
    total_energy_usage = production_energy * volume + transportation_energy

    # Carbon emissions based on energy usage and carbon emissions factor
    total_carbon_emissions = total_energy_usage * carbon_factor

    # Return results as a dictionary
    return {
        "energy_usage": round(total_energy_usage, 2),  # Total energy usage (kWh)
        "carbon_emissions": round(total_carbon_emissions, 2)  # Total carbon emissions (kg CO2)
    }


# Example usage
if __name__ == "__main__":
    try:
        result = calculate_environmental_impact(
            material_type="treated_eucalyptus",
            volume=10.0,
            distance=200.0,
            energy_cost_per_unit=0.5
        )
        print("Environmental Impact:", result)
    except ValueError as e:
        print("Error:", e)
```
