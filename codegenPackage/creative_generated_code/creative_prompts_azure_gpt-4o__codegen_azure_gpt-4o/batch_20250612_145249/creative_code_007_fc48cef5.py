"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://www.premierpointing.com.au
Prompt: Write a function to calculate the effectiveness of water repellant treatments, factoring in chemical reactions with brick surfaces, as described in Premier Pointing's use of Westox Water Repellant.
Generated: DETERMINISTIC_fc48cef599b18a1c
Batch ID: 20250612_145249
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import math
from typing import Tuple, List

# Define a function to calculate the effectiveness of a water repellant treatment
def calculate_repellant_effectiveness(surface_porosity: float, treatment_coverage: float, chemical_reaction_factor: float) -> float:
    """
    Calculate the effectiveness of water repellant treatment.

    Parameters:
        surface_porosity (float): Porosity level of the brick surface (0 to 1, where 1 is fully porous).
        treatment_coverage (float): Amount of treatment applied per square meter (liters/m^2).
        chemical_reaction_factor (float): Efficiency of chemical reaction between the treatment and the brick surface (0 to 1, where 1 is 100% efficient).

    Returns:
        float: Effectiveness of the water repellant treatment as a percentage (0 to 100).

    Raises:
        ValueError: If input parameters are outside their expected ranges.
    """

    # Validate inputs
    if not (0 <= surface_porosity <= 1):
        raise ValueError("surface_porosity must be between 0 and 1.")
    if treatment_coverage <= 0:
        raise ValueError("treatment_coverage must be greater than 0.")
    if not (0 <= chemical_reaction_factor <= 1):
        raise ValueError("chemical_reaction_factor must be between 0 and 1.")

    # Base effectiveness is inversely proportional to surface porosity
    base_effectiveness = (1 - surface_porosity) * 100

    # Adjustment for treatment coverage (logarithmic scale for diminishing returns)
    coverage_adjustment = math.log(1 + treatment_coverage) * 10

    # Adjustment for chemical reaction factor
    reaction_adjustment = chemical_reaction_factor * 100

    # Calculate total effectiveness
    total_effectiveness = base_effectiveness + coverage_adjustment + reaction_adjustment

    # Cap the effectiveness at 100%
    return min(total_effectiveness, 100.0)


# Example usage
if __name__ == "__main__":
    try:
        # Example inputs
        surface_porosity = 0.35  # 35% porous
        treatment_coverage = 0.5  # 0.5 liters/m^2
        chemical_reaction_factor = 0.8  # 80% efficiency

        # Calculate effectiveness
        effectiveness = calculate_repellant_effectiveness(surface_porosity, treatment_coverage, chemical_reaction_factor)

        # Output the result
        print(f"Water repellant effectiveness: {effectiveness:.2f}%")
    except ValueError as e:
        print(f"Error: {e}")
```
