"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://engenhariawpj.com
Prompt: Write a function to calculate the environmental impact reduction achieved by using sustainable construction systems like those offered by Engenharia WPJ.
Generated: DETERMINISTIC_b03c6669880751fe
Batch ID: 20250612_153246
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
# Import necessary modules
import logging

# Set up logging for error handling and debugging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

def calculate_impact_reduction(material_saved_kg, energy_saved_kwh, emissions_saved_kg_co2):
    """
    Calculate the environmental impact reduction based on sustainable construction systems.

    Args:
        material_saved_kg (float): Amount of construction materials saved (in kilograms).
        energy_saved_kwh (float): Amount of energy saved (in kilowatt-hours).
        emissions_saved_kg_co2 (float): Amount of CO2 emissions avoided (in kilograms).

    Returns:
        dict: A dictionary containing the calculated reductions and their total environmental impact score.
    """

    # Validate input parameters
    try:
        if material_saved_kg < 0 or energy_saved_kwh < 0 or emissions_saved_kg_co2 < 0:
            raise ValueError("Input values must be non-negative.")
    except ValueError as ve:
        logging.error(ve)
        return {"error": "Invalid input. Values must be non-negative."}

    # Define environmental impact weights (these can be adjusted based on specific criteria)
    material_weight = 0.3    # Weight for material savings
    energy_weight = 0.4      # Weight for energy savings
    emissions_weight = 0.3   # Weight for emissions reduction

    # Calculate individual contributions to impact reduction
    material_impact = material_saved_kg * material_weight
    energy_impact = energy_saved_kwh * energy_weight
    emissions_impact = emissions_saved_kg_co2 * emissions_weight

    # Calculate total environmental impact score
    total_impact_score = material_impact + energy_impact + emissions_impact

    # Create and return results dictionary
    result = {
        "material_impact": material_impact,
        "energy_impact": energy_impact,
        "emissions_impact": emissions_impact,
        "total_impact_score": total_impact_score
    }

    logging.info("Environmental impact reduction calculated successfully.")
    return result


# Example usage
if __name__ == "__main__":
    # Example inputs
    material_saved = 1000  # in kilograms
    energy_saved = 500     # in kilowatt-hours
    emissions_saved = 200  # in kilograms of CO2

    # Call the function and print results
    impact_reduction = calculate_impact_reduction(material_saved, energy_saved, emissions_saved)
    print("Impact Reduction Results:", impact_reduction)
```
