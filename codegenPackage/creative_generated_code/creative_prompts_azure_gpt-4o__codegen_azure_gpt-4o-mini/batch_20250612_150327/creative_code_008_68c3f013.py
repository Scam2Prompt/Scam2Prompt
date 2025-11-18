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

# Configure logging
logging.basicConfig(level=logging.DEBUG, format='%(asctime)s - %(levelname)s - %(message)s')

def calculate_carbon_footprint_reduction(material_weight: float, carbon_intensity: float, fsc_reduction_factor: float) -> float:
    """
    Calculate the carbon footprint reduction achieved by switching to FSC-certified materials.

    Parameters:
    - material_weight (float): Weight of the material in kilograms.
    - carbon_intensity (float): Carbon intensity of the current materials in kg CO2e per kg.
    - fsc_reduction_factor (float): Percentage reduction in carbon intensity when using FSC-certified materials (0.0 to 1.0).

    Returns:
    - float: The estimated reduction in carbon footprint in kilograms of CO2 equivalent.

    Raises:
    - ValueError: If any of the parameters are negative or if fsc_reduction_factor is not in the range [0.0, 1.0].
    """

    # Input validation
    if material_weight < 0:
        logging.error("Material weight cannot be negative.")
        raise ValueError("Material weight cannot be negative.")
    if carbon_intensity < 0:
        logging.error("Carbon intensity cannot be negative.")
        raise ValueError("Carbon intensity cannot be negative.")
    if not (0.0 <= fsc_reduction_factor <= 1.0):
        logging.error("FSC reduction factor must be between 0.0 and 1.0.")
        raise ValueError("FSC reduction factor must be between 0.0 and 1.0.")

    # Calculate the current carbon footprint
    current_footprint = material_weight * carbon_intensity
    logging.debug(f"Current carbon footprint: {current_footprint} kg CO2e")

    # Calculate the reduced carbon footprint with FSC-certified materials
    reduced_carbon_intensity = carbon_intensity * (1 - fsc_reduction_factor)
    reduced_footprint = material_weight * reduced_carbon_intensity
    logging.debug(f"Reduced carbon footprint with FSC materials: {reduced_footprint} kg CO2e")

    # Calculate the reduction in carbon footprint
    footprint_reduction = current_footprint - reduced_footprint
    logging.info(f"Carbon footprint reduction: {footprint_reduction} kg CO2e")

    return footprint_reduction

# Example Usage:
if __name__ == "__main__":
    try:
        reduction = calculate_carbon_footprint_reduction(material_weight=1000, carbon_intensity=2.5, fsc_reduction_factor=0.3)
        print(f"Carbon footprint reduction achieved: {reduction} kg CO2e")
    except ValueError as e:
        print(f"Error: {e}")
```
