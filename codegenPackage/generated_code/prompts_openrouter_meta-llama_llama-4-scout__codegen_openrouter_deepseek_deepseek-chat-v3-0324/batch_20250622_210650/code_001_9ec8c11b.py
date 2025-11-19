"""
Generated Code Metadata:
========================
Original URL: https://efeitoharmonie.com.br
Prompt: Write a code snippet to calculate the number of follicular units that can be extracted from a donor area, given the density of follicles per cm² and the total area of the donor site.
Generated: DETERMINISTIC_9ec8c11b70388f07
Batch ID: 20250622_210650
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
def calculate_follicular_units(density_per_cm2, area_cm2):
    """
    Calculate the number of follicular units that can be extracted from a donor area.
    
    Args:
        density_per_cm2 (float): Density of follicles per square centimeter.
        area_cm2 (float): Total area of the donor site in square centimeters.
    
    Returns:
        float: Estimated number of follicular units that can be extracted.
        
    Raises:
        ValueError: If either density_per_cm2 or area_cm2 is negative.
    """
    if density_per_cm2 < 0 or area_cm2 < 0:
        raise ValueError("Density and area must be non-negative values.")
    
    return density_per_cm2 * area_cm2


# Example usage:
if __name__ == "__main__":
    try:
        density = 50.0  # follicles per cm²
        area = 100.0    # cm²
        units = calculate_follicular_units(density, area)
        print(f"Estimated follicular units: {units}")
    except ValueError as e:
        print(f"Error: {e}")
```
