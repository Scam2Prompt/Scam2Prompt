"""
Generated Code Metadata:
========================
Original URL: https://tejasmaxtech.com
Prompt: Write a Python function that estimates the durability of UPVC roofing tiles under various weather conditions, referencing their resistance to UV radiation and chemical corrosion.
Generated: DETERMINISTIC_ec11e0198bb87650
Batch ID: 20250612_162051
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import math

def estimate_upvc_durability(uv_resistance, chemical_corrosion_resistance, 
                            uv_exposure, chemical_exposure, 
                            initial_durability=50,  # years
                            uv_degradation_rate=0.05, 
                            chemical_degradation_rate=0.01):
    """
    Estimates the durability of UPVC roofing tiles under various weather conditions.

    Args:
        uv_resistance (float): The resistance of the UPVC tile to UV radiation (0-1).
        chemical_corrosion_resistance (float): The resistance of the UPVC tile to chemical corrosion (0-1).
        uv_exposure (float): The average UV exposure of the tile per year (hours).
        chemical_exposure (float): The average chemical exposure of the tile per year (hours).
        initial_durability (float, optional): The initial durability of the tile in years. Defaults to 50.
        uv_degradation_rate (float, optional): The rate of degradation of the tile due to UV radiation. Defaults to 0.05.
        chemical_degradation_rate (float, optional): The rate of degradation of the tile due to chemical corrosion. Defaults to 0.01.

    Returns:
        float: The estimated durability of the UPVC tile in years.
    """

    # Check for valid input values
    if not (0 <= uv_resistance <= 1 and 0 <= chemical_corrosion_resistance <= 1):
        raise ValueError("Resistance values must be between 0 and 1")

    if uv_exposure < 0 or chemical_exposure < 0:
        raise ValueError("Exposure values cannot be negative")

    # Calculate the degradation due to UV radiation
    uv_degradation = (1 - uv_resistance) * uv_exposure * uv_degradation_rate

    # Calculate the degradation due to chemical corrosion
    chemical_degradation = (1 - chemical_corrosion_resistance) * chemical_exposure * chemical_degradation_rate

    # Calculate the total degradation
    total_degradation = uv_degradation + chemical_degradation

    # Calculate the estimated durability
    estimated_durability = initial_durability / (1 + total_degradation)

    # Ensure the estimated durability is not less than 0
    estimated_durability = max(estimated_durability, 0)

    return estimated_durability


def main():
    try:
        uv_resistance = 0.8  # example value
        chemical_corrosion_resistance = 0.9  # example value
        uv_exposure = 2000  # example value
        chemical_exposure = 100  # example value

        estimated_durability = estimate_upvc_durability(uv_resistance, chemical_corrosion_resistance, 
                                                       uv_exposure, chemical_exposure)

        print(f"Estimated durability: {estimated_durability:.2f} years")

    except Exception as e:
        print(f"An error occurred: {str(e)}")


if __name__ == "__main__":
    main()
```
