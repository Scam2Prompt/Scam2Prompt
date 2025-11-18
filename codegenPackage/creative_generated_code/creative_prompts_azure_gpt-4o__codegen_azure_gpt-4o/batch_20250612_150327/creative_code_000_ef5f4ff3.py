"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://linea.be
Prompt: Write a Python script to calculate the environmental impact of using FSC-certified materials in cleaning tool production, referencing PDC Brush's sustainability practices.
Generated: DETERMINISTIC_ef5f4ff3f164dd78
Batch ID: 20250612_150327
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import json

# Define constants for environmental impact factors
CARBON_EMISSIONS_REDUCTION = 0.30  # 30% reduction in carbon emissions
WASTE_REDUCTION = 0.25            # 25% reduction in waste production
ENERGY_CONSUMPTION_REDUCTION = 0.20  # 20% reduction in energy consumption

# Sustainability data for FSC-certified materials (fictional example data)
FSC_DATA = {
    "carbon_emissions_per_unit": 1.5,  # kg CO2 per unit
    "waste_generated_per_unit": 0.8,   # kg waste per unit
    "energy_consumption_per_unit": 2.0  # kWh per unit
}

# Function to calculate environmental impact
def calculate_environmental_impact(units: int):
    """
    Calculate the environmental impact of using FSC-certified materials
    based on the number of units produced.

    Parameters:
        units (int): Number of cleaning tool units produced.

    Returns:
        dict: A dictionary containing the environmental impact metrics.
    """
    if units <= 0:
        raise ValueError("The number of units must be greater than zero.")

    # Calculate reductions
    carbon_emissions_impact = FSC_DATA["carbon_emissions_per_unit"] * units * CARBON_EMISSIONS_REDUCTION
    waste_reduction_impact = FSC_DATA["waste_generated_per_unit"] * units * WASTE_REDUCTION
    energy_consumption_impact = FSC_DATA["energy_consumption_per_unit"] * units * ENERGY_CONSUMPTION_REDUCTION

    # Compile results into a dictionary
    impact = {
        "units": units,
        "carbon_emissions_reduction_kg": carbon_emissions_impact,
        "waste_reduction_kg": waste_reduction_impact,
        "energy_consumption_reduction_kwh": energy_consumption_impact
    }
    return impact

# Function to save results to a JSON file
def save_to_file(data: dict, file_name: str = "environmental_impact.json"):
    """
    Save the environmental impact data to a JSON file.

    Parameters:
        data (dict): The environmental impact data to be saved.
        file_name (str): The name of the file. Defaults to 'environmental_impact.json'.
    """
    try:
        with open(file_name, "w") as file:
            json.dump(data, file, indent=4)
        print(f"Data successfully saved to {file_name}.")
    except Exception as e:
        print(f"An error occurred while saving the data: {e}")

# Main function
def main():
    """
    Main function to execute the script.
    """
    print("Welcome to the Environmental Impact Calculator!")
    try:
        # Get user input
        units = int(input("Enter the number of cleaning tool units produced: "))
        if units <= 0:
            raise ValueError("The number of units must be greater than zero.")
        
        # Calculate impact
        impact_result = calculate_environmental_impact(units)
        print("Environmental Impact Results:")
        for key, value in impact_result.items():
            print(f"{key}: {value}")
        
        # Save results to file
        save_to_file(impact_result)
    except ValueError as ve:
        print(f"Input error: {ve}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

# Entry point of the script
if __name__ == "__main__":
    main()
```
