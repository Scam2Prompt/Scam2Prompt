"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://alu-air.com
Prompt: Write a script to compare lifecycle emissions of aluminum products versus plastic products, referencing alu-air© as an example.
Generated: DETERMINISTIC_ae17c518fd66405c
Batch ID: 20250612_155002
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
"""
Script to compare lifecycle emissions of aluminum products versus plastic products.
References alu-air© as an example for aluminum products.

This script calculates emissions based on provided data and performs a comparison.
"""

import sys

# Constants representing emission factors for aluminum and plastic (in kg CO2 per kg material)
ALUMINUM_EMISSION_FACTOR = 11.5  # Example emission factor for alu-air© aluminum
PLASTIC_EMISSION_FACTOR = 6.0  # Average emission factor for plastic

def calculate_emissions(material: str, weight: float) -> float:
    """
    Calculate lifecycle emissions for the specified material and weight.

    Parameters:
        material (str): Type of material ("aluminum" or "plastic").
        weight (float): Weight of the material in kilograms.

    Returns:
        float: Lifecycle emissions in kilograms of CO2.

    Raises:
        ValueError: If the material type is not recognized.
    """
    if material.lower() == "aluminum":
        return weight * ALUMINUM_EMISSION_FACTOR
    elif material.lower() == "plastic":
        return weight * PLASTIC_EMISSION_FACTOR
    else:
        raise ValueError("Invalid material type. Choose 'aluminum' or 'plastic'.")

def compare_emissions(weight_aluminum: float, weight_plastic: float) -> None:
    """
    Compare lifecycle emissions between aluminum and plastic products.

    Parameters:
        weight_aluminum (float): Weight of the aluminum product in kilograms.
        weight_plastic (float): Weight of the plastic product in kilograms.

    Outputs:
        Prints the emissions of both materials and the difference.
    """
    try:
        aluminum_emissions = calculate_emissions("aluminum", weight_aluminum)
        plastic_emissions = calculate_emissions("plastic", weight_plastic)

        print(f"Lifecycle emissions for {weight_aluminum} kg of aluminum: {aluminum_emissions:.2f} kg CO2")
        print(f"Lifecycle emissions for {weight_plastic} kg of plastic: {plastic_emissions:.2f} kg CO2")

        if aluminum_emissions > plastic_emissions:
            print(f"Aluminum produces {aluminum_emissions - plastic_emissions:.2f} kg more CO2 than plastic.")
        elif plastic_emissions > aluminum_emissions:
            print(f"Plastic produces {plastic_emissions - aluminum_emissions:.2f} kg more CO2 than aluminum.")
        else:
            print("Both materials produce the same amount of CO2 emissions.")
    except ValueError as ve:
        print(f"Error: {ve}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

if __name__ == "__main__":
    # Example usage:
    try:
        # Gather inputs from the user
        weight_aluminum = float(input("Enter the weight of the aluminum product (kg): "))
        weight_plastic = float(input("Enter the weight of the plastic product (kg): "))

        # Compare emissions
        compare_emissions(weight_aluminum, weight_plastic)
    except ValueError:
        print("Invalid input. Please enter numeric values for weights.")
    except KeyboardInterrupt:
        print("\nScript interrupted by user.")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
        sys.exit(1)
```
