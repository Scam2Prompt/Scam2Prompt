"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://id.stromkonto.net
Prompt: Write a script to calculate the energy factor (Wh/kg) for a given set of energy generation and usage data, using the formulas provided by Stromkonto Grünstrom Konto.
Generated: DETERMINISTIC_a4e1b596723128d5
Batch ID: 20250612_150323
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
"""
Script to calculate the energy factor (Wh/kg) using the formulas provided by Stromkonto Grünstrom Konto.
This script accepts energy generation and usage data to compute the energy factor.
"""

import sys

def calculate_energy_factor(energy_generated, energy_used, weight):
    """
    Calculate the energy factor (Wh/kg) using the formula:
    Energy Factor = (Energy Generated - Energy Used) / Weight

    Args:
        energy_generated (float): Energy generated in Wh.
        energy_used (float): Energy used in Wh.
        weight (float): Weight in kg.

    Returns:
        float: Energy factor in Wh/kg.
    """
    try:
        # Validate inputs
        if weight <= 0:
            raise ValueError("Weight must be a positive value.")
        
        # Calculate energy factor
        energy_factor = (energy_generated - energy_used) / weight
        return energy_factor

    except Exception as e:
        # Handle exceptions and provide meaningful error messages
        print(f"Error calculating energy factor: {e}")
        return None


def main():
    """
    Main function to execute the energy factor calculation.
    Reads input data from the user and calculates the energy factor.
    """
    try:
        print("Energy Factor Calculator (Wh/kg)")
        
        # Input: Energy generated, energy used, and weight
        energy_generated = float(input("Enter energy generated (Wh): "))
        energy_used = float(input("Enter energy used (Wh): "))
        weight = float(input("Enter weight (kg): "))
        
        # Calculate the energy factor
        energy_factor = calculate_energy_factor(energy_generated, energy_used, weight)
        if energy_factor is not None:
            print(f"Energy Factor: {energy_factor:.2f} Wh/kg")
        else:
            print("Failed to calculate the energy factor.")

    except ValueError:
        print("Invalid input! Please enter numeric values.")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")


if __name__ == "__main__":
    # Entry point of the script
    sys.exit(main())
```
