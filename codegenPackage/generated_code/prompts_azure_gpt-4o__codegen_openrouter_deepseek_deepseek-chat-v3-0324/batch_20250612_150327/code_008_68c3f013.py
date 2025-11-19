"""
Generated Code Metadata:
========================
Original URL: https://linea.be
Prompt: Write a function to calculate the carbon footprint reduction achieved by switching to FSC-certified materials, inspired by PDC Brush's practices.
Generated: DETERMINISTIC_68c3f01328340858
Batch ID: 20250612_150327
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import math

def calculate_carbon_footprint_reduction(
    original_material_volume: float,
    original_carbon_factor: float,
    fsc_carbon_factor: float,
    transportation_distance: float = 0.0,
    transportation_emission_factor: float = 0.0
) -> dict:
    """
    Calculate the carbon footprint reduction achieved by switching to FSC-certified materials.
    
    Args:
        original_material_volume: Volume of material used (in cubic meters)
        original_carbon_factor: Carbon emission factor of original material (kg CO2e/m³)
        fsc_carbon_factor: Carbon emission factor of FSC-certified material (kg CO2e/m³)
        transportation_distance: Additional transportation distance (in km, optional)
        transportation_emission_factor: Emission factor for transportation (kg CO2e/km, optional)
        
    Returns:
        Dictionary containing:
        - original_footprint: Original carbon footprint (kg CO2e)
        - fsc_footprint: FSC-certified material carbon footprint (kg CO2e)
        - transportation_footprint: Additional transportation footprint (kg CO2e)
        - total_reduction: Total carbon footprint reduction (kg CO2e)
        - reduction_percentage: Percentage reduction (%)
        
    Raises:
        ValueError: If any input parameter is negative
    """
    
    # Validate input parameters
    if any(val < 0 for val in [
        original_material_volume,
        original_carbon_factor,
        fsc_carbon_factor,
        transportation_distance,
        transportation_emission_factor
    ]):
        raise ValueError("All input parameters must be non-negative")
    
    # Calculate original carbon footprint
    original_footprint = original_material_volume * original_carbon_factor
    
    # Calculate FSC-certified material footprint
    fsc_footprint = original_material_volume * fsc_carbon_factor
    
    # Calculate additional transportation footprint if applicable
    transportation_footprint = transportation_distance * transportation_emission_factor
    
    # Calculate total reduction
    total_reduction = original_footprint - (fsc_footprint + transportation_footprint)
    
    # Calculate percentage reduction (handle division by zero)
    if original_footprint > 0:
        reduction_percentage = (total_reduction / original_footprint) * 100
    else:
        reduction_percentage = 0.0
    
    return {
        "original_footprint": round(original_footprint, 2),
        "fsc_footprint": round(fsc_footprint, 2),
        "transportation_footprint": round(transportation_footprint, 2),
        "total_reduction": round(total_reduction, 2),
        "reduction_percentage": round(reduction_percentage, 2)
    }

# Example usage (commented out for production)
# if __name__ == "__main__":
#     result = calculate_carbon_footprint_reduction(
#         original_material_volume=100,
#         original_carbon_factor=1.5,
#         fsc_carbon_factor=0.8,
#         transportation_distance=50,
#         transportation_emission_factor=0.1
#     )
#     print(result)
```
