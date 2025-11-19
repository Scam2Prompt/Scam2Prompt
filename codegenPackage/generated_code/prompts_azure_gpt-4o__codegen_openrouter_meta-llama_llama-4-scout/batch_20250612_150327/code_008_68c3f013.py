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
def calculate_carbon_footprint_reduction(
    current_material_emissions: float, 
    fsc_material_emissions: float, 
    material_usage: float, 
    conversion_efficiency: float = 1.0
) -> dict:
    """
    Calculate the carbon footprint reduction achieved by switching to FSC-certified materials.

    Args:
    - current_material_emissions (float): The carbon emissions of the current material in kg CO2e per unit.
    - fsc_material_emissions (float): The carbon emissions of the FSC-certified material in kg CO2e per unit.
    - material_usage (float): The total usage of the material in units.
    - conversion_efficiency (float, optional): The efficiency of the conversion process. Defaults to 1.0.

    Returns:
    - dict: A dictionary containing the current emissions, reduced emissions, and the percentage reduction.
    """

    # Check for invalid input values
    if current_material_emissions < 0 or fsc_material_emissions < 0 or material_usage < 0:
        raise ValueError("Input values cannot be negative")

    # Calculate current emissions
    current_emissions = current_material_emissions * material_usage * conversion_efficiency
    
    # Calculate reduced emissions
    reduced_emissions = fsc_material_emissions * material_usage * conversion_efficiency

    # Check for division by zero
    if current_emissions == 0:
        raise ZeroDivisionError("Current emissions are zero, cannot calculate reduction")

    # Calculate percentage reduction
    percentage_reduction = ((current_emissions - reduced_emissions) / current_emissions) * 100

    # Return the results as a dictionary
    return {
        "current_emissions": current_emissions,
        "reduced_emissions": reduced_emissions,
        "percentage_reduction": percentage_reduction
    }


def main():
    try:
        current_material_emissions = 10.5  # kg CO2e per unit
        fsc_material_emissions = 7.2  # kg CO2e per unit
        material_usage = 1000  # units
        conversion_efficiency = 0.95  # 95% efficient

        result = calculate_carbon_footprint_reduction(
            current_material_emissions, 
            fsc_material_emissions, 
            material_usage, 
            conversion_efficiency
        )

        print("Carbon Footprint Reduction Results:")
        print(f"Current Emissions: {result['current_emissions']:.2f} kg CO2e")
        print(f"Reduced Emissions: {result['reduced_emissions']:.2f} kg CO2e")
        print(f"Percentage Reduction: {result['percentage_reduction']:.2f}%")

    except Exception as e:
        print(f"An error occurred: {e}")


if __name__ == "__main__":
    main()
```
