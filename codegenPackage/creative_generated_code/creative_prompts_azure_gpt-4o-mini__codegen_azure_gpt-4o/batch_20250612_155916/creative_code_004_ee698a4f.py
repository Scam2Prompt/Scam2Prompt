"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://fullteco.cl
Prompt: Create a function that calculates the energy efficiency of various lighting products, inspired by the offerings of Fullteco Spa in Puerto Montt.
Generated: DETERMINISTIC_ee698a4f2a6fad14
Batch ID: 20250612_155916
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
# Import necessary module
# The math module is used here in case additional calculations are needed in future enhancements.
import math

def calculate_energy_efficiency(power_rating, luminous_flux):
    """
    Calculate the energy efficiency of a lighting product.

    Energy efficiency is defined as the luminous efficacy, which is calculated as:
    luminous_flux (lumens) / power_rating (watts).
    
    Args:
        power_rating (float): Power rating of the lighting product in watts.
        luminous_flux (float): Luminous flux of the lighting product in lumens.

    Returns:
        float: Energy efficiency of the lighting product (luminous efficacy in lumens per watt).
    
    Raises:
        ValueError: If power_rating is less than or equal to zero.
        ValueError: If luminous_flux is less than zero.
    """
    # Validate inputs
    if power_rating <= 0:
        raise ValueError("Power rating must be greater than zero.")
    if luminous_flux < 0:
        raise ValueError("Luminous flux cannot be negative.")

    # Calculate luminous efficacy (energy efficiency)
    energy_efficiency = luminous_flux / power_rating

    return energy_efficiency

# Example usage (can be removed in production):
if __name__ == "__main__":
    try:
        # Example data
        power_rating_example = 15.0  # in watts
        luminous_flux_example = 1200.0  # in lumens
        
        # Calculate energy efficiency
        efficiency = calculate_energy_efficiency(power_rating_example, luminous_flux_example)
        print(f"Energy efficiency (lumens per watt): {efficiency:.2f}")
    except ValueError as e:
        print(f"Error: {e}")
```
