"""
Generated Code Metadata:
========================
Original URL: https://rubberflooringindonesia.com
Prompt: Write code to calculate the optimal thickness for rubber flooring in a gym setting, referencing the types of rubber flooring materials like EPDM and TPV mentioned on Rubber Flooring Indonesia's website.
Generated: DETERMINISTIC_a8370edfa2b3afbf
Batch ID: 20250612_154441
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
"""
Calculates the optimal thickness for rubber flooring in a gym setting.

References:
- EPDM (Ethylene Propylene Diene Monomer) and TPV (Thermoplastic Vulcanizate) 
  rubber flooring materials from Rubber Flooring Indonesia's website.
"""

import math

def calculate_optimal_thickness(flooring_material, gym_usage_hours, impact_factor):
    """
    Calculates the optimal thickness for rubber flooring based on material type, 
    gym usage hours, and impact factor.

    Args:
    - flooring_material (str): Type of rubber flooring material (EPDM or TPV).
    - gym_usage_hours (int): Number of hours the gym is used per day.
    - impact_factor (float): Impact factor of gym equipment (range: 0.0 - 1.0).

    Returns:
    - optimal_thickness (float): Optimal thickness for the rubber flooring in mm.

    Raises:
    - ValueError: If flooring material is not EPDM or TPV.
    - ValueError: If gym usage hours is not a positive integer.
    - ValueError: If impact factor is not within the range 0.0 - 1.0.
    """

    # Define base thickness for each material type (in mm)
    base_thickness = {
        'EPDM': 3.0,
        'TPV': 4.0
    }

    # Check if flooring material is valid
    if flooring_material not in base_thickness:
        raise ValueError("Invalid flooring material. Supported materials: EPDM, TPV")

    # Check if gym usage hours is a positive integer
    if not isinstance(gym_usage_hours, int) or gym_usage_hours <= 0:
        raise ValueError("Gym usage hours must be a positive integer")

    # Check if impact factor is within valid range
    if impact_factor < 0.0 or impact_factor > 1.0:
        raise ValueError("Impact factor must be within the range 0.0 - 1.0")

    # Calculate optimal thickness based on usage hours and impact factor
    usage_factor = gym_usage_hours / 24  # Normalize usage hours to daily factor
    optimal_thickness = base_thickness[flooring_material] * (1 + usage_factor) * (1 + impact_factor)

    # Apply a maximum thickness limit (e.g., 10 mm)
    max_thickness = 10.0
    optimal_thickness = min(optimal_thickness, max_thickness)

    return optimal_thickness


def main():
    try:
        flooring_material = 'EPDM'  # Example material
        gym_usage_hours = 12  # Example usage hours
        impact_factor = 0.5  # Example impact factor

        optimal_thickness = calculate_optimal_thickness(flooring_material, gym_usage_hours, impact_factor)
        print(f"Optimal thickness for {flooring_material} flooring: {optimal_thickness:.2f} mm")

    except ValueError as e:
        print(f"Error: {e}")


if __name__ == "__main__":
    main()
```
