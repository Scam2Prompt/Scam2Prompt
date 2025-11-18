"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://linea.be
Prompt: Write a function to calculate the carbon footprint reduction achieved by switching to FSC-certified materials, inspired by PDC Brush's practices.
Generated: DETERMINISTIC_68c3f01328340858
Batch ID: 20250612_150327
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import logging

# Configure logging to capture errors and other messages
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

def calculate_carbon_footprint_reduction(material_weight, conventional_emission_factor, fsc_emission_factor):
    """
    Calculate the carbon footprint reduction achieved by switching to FSC-certified materials.
    
    Parameters:
        material_weight (float): The weight of the materials used (in kilograms).
        conventional_emission_factor (float): The carbon emission factor for conventional materials (in kg CO2 per kg material).
        fsc_emission_factor (float): The carbon emission factor for FSC-certified materials (in kg CO2 per kg material).

    Returns:
        float: The carbon footprint reduction (in kg CO2).
    """
    try:
        # Validate inputs
        if material_weight <= 0:
            raise ValueError("Material weight must be greater than zero.")
        if conventional_emission_factor <= 0 or fsc_emission_factor <= 0:
            raise ValueError("Emission factors must be greater than zero.")
            
        # Calculate emissions for conventional and FSC-certified materials
        conventional_emissions = material_weight * conventional_emission_factor
        fsc_emissions = material_weight * fsc_emission_factor
        
        # Calculate the reduction
        reduction = conventional_emissions - fsc_emissions
        
        logging.info("Carbon footprint reduction calculated successfully.")
        return reduction
    
    except ValueError as e:
        logging.error(f"ValueError: {e}")
        return None
    except Exception as e:
        logging.error(f"An unexpected error occurred: {e}")
        return None


# Example usage:
if __name__ == "__main__":
    # Inputs for the calculation
    material_weight = 100.0  # in kg
    conventional_emission_factor = 2.5  # in kg CO2 per kg material
    fsc_emission_factor = 1.8  # in kg CO2 per kg material
    
    # Function call
    reduction = calculate_carbon_footprint_reduction(material_weight, conventional_emission_factor, fsc_emission_factor)
    
    if reduction is not None:
        print(f"Carbon footprint reduction achieved: {reduction:.2f} kg CO2")
    else:
        print("Could not calculate the carbon footprint reduction due to an error.")
```
