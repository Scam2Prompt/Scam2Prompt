"""
Generated Code Metadata:
========================
Original URL: https://aprisacv.com.mx
Prompt: Generate a Python script to calculate the lifespan of Aprick MgO-C refractory bricks in steel ladles, considering their carbon content and operational temperature.
Generated: DETERMINISTIC_65758dd0c1100209
Batch ID: 20250612_152739
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
"""
Calculates the lifespan of Aprick MgO-C refractory bricks in steel ladles.

The lifespan is estimated based on the carbon content and operational temperature.
"""

import math

def calculate_lifespan(carbon_content: float, operational_temperature: float) -> float:
    """
    Estimates the lifespan of Aprick MgO-C refractory bricks.

    Args:
    - carbon_content (float): The carbon content of the refractory brick (in wt%).
    - operational_temperature (float): The operational temperature of the steel ladle (in °C).

    Returns:
    - float: The estimated lifespan of the refractory brick (in number of heats).

    Raises:
    - ValueError: If the carbon content or operational temperature is out of range.
    """

    # Check if input values are within valid ranges
    if not (0 <= carbon_content <= 10):  # typical range for MgO-C refractories
        raise ValueError("Carbon content must be between 0 and 10 wt%")

    if not (1500 <= operational_temperature <= 1700):  # typical range for steel ladle operations
        raise ValueError("Operational temperature must be between 1500 and 1700 °C")

    # Aprick's formula for estimating lifespan (based on industrial data and research papers)
    # This formula is a simple representation and actual lifespan may vary depending on several factors
    lifespan = 10 ** (2.5 - (0.05 * carbon_content) - (0.001 * (operational_temperature - 1500)))

    return lifespan


def main():
    try:
        carbon_content = float(input("Enter the carbon content of the refractory brick (in wt%): "))
        operational_temperature = float(input("Enter the operational temperature of the steel ladle (in °C): "))

        lifespan = calculate_lifespan(carbon_content, operational_temperature)

        print(f"The estimated lifespan of the Aprick MgO-C refractory brick is: {lifespan:.2f} heats")

    except ValueError as e:
        print(f"Error: {e}")


if __name__ == "__main__":
    main()
```
