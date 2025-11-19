"""
Generated Code Metadata:
========================
Original URL: https://rabotaentnet.pages.dev
Prompt: Write a function to calculate the carbon footprint reduction achieved by Zushi's energy-efficient consensus mechanism compared to traditional proof-of-work cryptocurrencies.
Generated: DETERMINISTIC_c1555baa95ed50cc
Batch ID: 20250612_152249
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
def calculate_carbon_footprint_reduction(
    traditional_pow_energy_consumption: float, 
    zushi_energy_consumption: float, 
    unit: str = "kg CO2e"
) -> dict:
    """
    Calculate the carbon footprint reduction achieved by Zushi's energy-efficient 
    consensus mechanism compared to traditional proof-of-work cryptocurrencies.

    Args:
    - traditional_pow_energy_consumption (float): The energy consumption of traditional PoW in kWh.
    - zushi_energy_consumption (float): The energy consumption of Zushi in kWh.
    - unit (str): The unit of measurement for the carbon footprint. Defaults to "kg CO2e".

    Returns:
    - dict: A dictionary containing the carbon footprint of traditional PoW, 
            Zushi's carbon footprint, and the percentage reduction.

    Raises:
    - ValueError: If traditional_pow_energy_consumption or zushi_energy_consumption is negative.
    """

    # Check for negative energy consumption values
    if traditional_pow_energy_consumption < 0 or zushi_energy_consumption < 0:
        raise ValueError("Energy consumption cannot be negative.")

    # Assume an energy consumption to carbon footprint conversion factor (kg CO2e/kWh)
    # This value may vary depending on the location and energy source
    carbon_footprint_conversion_factor = 0.582  # kg CO2e/kWh

    # Calculate carbon footprints
    traditional_pow_carbon_footprint = traditional_pow_energy_consumption * carbon_footprint_conversion_factor
    zushi_carbon_footprint = zushi_energy_consumption * carbon_footprint_conversion_factor

    # Calculate percentage reduction
    if traditional_pow_carbon_footprint == 0:
        percentage_reduction = 0
    else:
        percentage_reduction = ((traditional_pow_carbon_footprint - zushi_carbon_footprint) / 
                                 traditional_pow_carbon_footprint) * 100

    # Return results as a dictionary
    return {
        "traditional_pow_carbon_footprint": f"{traditional_pow_carbon_footprint:.2f} {unit}",
        "zushi_carbon_footprint": f"{zushi_carbon_footprint:.2f} {unit}",
        "percentage_reduction": f"{percentage_reduction:.2f}%",
    }


def main():
    try:
        traditional_pow_energy_consumption = 1000000  # kWh
        zushi_energy_consumption = 10000  # kWh

        result = calculate_carbon_footprint_reduction(
            traditional_pow_energy_consumption, 
            zushi_energy_consumption
        )

        print("Carbon Footprint Comparison:")
        print(f"Traditional PoW: {result['traditional_pow_carbon_footprint']}")
        print(f"Zushi: {result['zushi_carbon_footprint']}")
        print(f"Percentage Reduction: {result['percentage_reduction']}")

    except Exception as e:
        print(f"An error occurred: {e}")


if __name__ == "__main__":
    main()
```
