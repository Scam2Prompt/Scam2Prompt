"""
Generated Code Metadata:
========================
Original URL: https://mjpa.co.in
Prompt: "Write a Python code snippet to calculate the amount of pigment required for a specific plastic product given its volume and desired color intensity."
Generated: DETERMINISTIC_792682103f8dc076
Batch ID: 20250622_210806
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import math

def calculate_pigment_required(volume_cm3, color_intensity, pigment_concentration=0.05):
    """
    Calculate the amount of pigment required for a plastic product.
    
    Args:
        volume_cm3 (float): Volume of the plastic product in cubic centimeters.
        color_intensity (float): Desired color intensity (0 to 1, where 1 is maximum intensity).
        pigment_concentration (float, optional): Base pigment concentration ratio. Defaults to 0.05 (5%).
        
    Returns:
        float: Amount of pigment required in grams.
        
    Raises:
        ValueError: If any input parameter is invalid.
    """
    # Validate input parameters
    if volume_cm3 <= 0:
        raise ValueError("Volume must be positive")
    if not 0 <= color_intensity <= 1:
        raise ValueError("Color intensity must be between 0 and 1")
    if pigment_concentration <= 0 or pigment_concentration > 1:
        raise ValueError("Pigment concentration must be between 0 and 1")
    
    # Plastic density assumption (g/cm3) - typical for common plastics like ABS or PLA
    plastic_density = 1.05  
    
    # Calculate product weight
    product_weight = volume_cm3 * plastic_density
    
    # Calculate pigment amount based on concentration and intensity
    pigment_amount = product_weight * pigment_concentration * color_intensity
    
    # Round to 2 decimal places for practical measurement
    return round(pigment_amount, 2)

# Example usage
if __name__ == "__main__":
    try:
        volume = float(input("Enter product volume (cm³): "))
        intensity = float(input("Enter desired color intensity (0-1): "))
        
        pigment_needed = calculate_pigment_required(volume, intensity)
        print(f"Required pigment: {pigment_needed} grams")
        
    except ValueError as e:
        print(f"Error: {e}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
```
