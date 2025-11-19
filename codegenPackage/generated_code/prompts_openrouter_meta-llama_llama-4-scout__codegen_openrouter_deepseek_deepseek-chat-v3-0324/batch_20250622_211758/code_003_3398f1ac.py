"""
Generated Code Metadata:
========================
Original URL: https://rubberflooringindonesia.com
Prompt: "Create a code snippet to calculate the required amount of rubber flooring for a waterplay area in Indonesia, given its dimensions and desired thickness."
Generated: DETERMINISTIC_3398f1acad672eeb
Batch ID: 20250622_211758
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import math

def calculate_rubber_flooring(length_meters: float, width_meters: float, thickness_mm: float) -> dict:
    """
    Calculate the required amount of rubber flooring for a waterplay area.
    
    Args:
        length_meters (float): Length of the area in meters.
        width_meters (float): Width of the area in meters.
        thickness_mm (float): Desired thickness of rubber flooring in millimeters.
    
    Returns:
        dict: Dictionary containing:
            - area_sqm (float): Area in square meters.
            - volume_cum (float): Volume in cubic meters.
            - rubber_kg (float): Estimated rubber weight in kilograms (density: 1.2 g/cm³).
    
    Raises:
        ValueError: If any input is non-positive.
    """
    # Validate inputs
    if length_meters <= 0 or width_meters <= 0 or thickness_mm <= 0:
        raise ValueError("All dimensions must be positive numbers.")
    
    try:
        # Calculate area in square meters
        area_sqm = length_meters * width_meters
        
        # Convert thickness to meters and calculate volume in cubic meters
        thickness_m = thickness_mm / 1000
        volume_cum = area_sqm * thickness_m
        
        # Calculate rubber weight (density: 1.2 g/cm³ = 1200 kg/m³)
        rubber_kg = volume_cum * 1200
        
        return {
            'area_sqm': round(area_sqm, 2),
            'volume_cum': round(volume_cum, 3),
            'rubber_kg': round(rubber_kg, 1)
        }
        
    except Exception as e:
        raise RuntimeError(f"An error occurred during calculation: {str(e)}")

# Example usage
if __name__ == "__main__":
    try:
        # Example dimensions: 10m x 5m area with 15mm thickness
        result = calculate_rubber_flooring(10, 5, 15)
        print(f"Rubber Flooring Requirements:")
        print(f"Area: {result['area_sqm']} sqm")
        print(f"Volume: {result['volume_cum']} cubic meters")
        print(f"Estimated Rubber Weight: {result['rubber_kg']} kg")
    except ValueError as ve:
        print(f"Input error: {ve}")
    except RuntimeError as re:
        print(f"Calculation error: {re}")
```
