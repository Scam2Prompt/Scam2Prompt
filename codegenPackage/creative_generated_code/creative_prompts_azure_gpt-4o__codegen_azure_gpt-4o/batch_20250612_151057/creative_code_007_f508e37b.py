"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://sctoll.io
Prompt: Provide code to calculate the weight reduction and stress resistance improvements of Brixton Forged™ wheels compared to OEM wheels.
Generated: DETERMINISTIC_f508e37b7b1328aa
Batch ID: 20250612_151057
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
# Import necessary modules
import math

# Define constants
# Constants for OEM wheels (example values, adjust as needed)
OEM_WHEEL_WEIGHT_KG = 12.0  # Weight of an OEM wheel in kilograms
OEM_STRESS_RESISTANCE_INDEX = 100  # Stress resistance index of OEM wheel (arbitrary unit)

# Constants for Brixton Forged wheels (example values, adjust as needed)
BRIXTON_WHEEL_WEIGHT_KG = 8.0  # Weight of Brixton Forged wheel in kilograms
BRIXTON_STRESS_RESISTANCE_INDEX = 150  # Stress resistance index of Brixton Forged wheel (arbitrary unit)

def calculate_weight_reduction(oem_weight, custom_weight):
    """
    Calculate weight reduction percentage.
    
    :param oem_weight: Weight of the OEM wheel in kilograms.
    :param custom_weight: Weight of the custom wheel in kilograms.
    :return: Weight reduction percentage.
    """
    try:
        weight_reduction = ((oem_weight - custom_weight) / oem_weight) * 100
        return round(weight_reduction, 2)
    except ZeroDivisionError:
        raise ValueError("OEM wheel weight must be greater than zero.")

def calculate_stress_resistance_improvement(oem_resistance, custom_resistance):
    """
    Calculate stress resistance improvement percentage.
    
    :param oem_resistance: Stress resistance index of the OEM wheel.
    :param custom_resistance: Stress resistance index of the custom wheel.
    :return: Stress resistance improvement percentage.
    """
    try:
        improvement = ((custom_resistance - oem_resistance) / oem_resistance) * 100
        return round(improvement, 2)
    except ZeroDivisionError:
        raise ValueError("OEM stress resistance index must be greater than zero.")

def main():
    """
    Main function to calculate and display improvements of Brixton Forged wheels.
    """
    try:
        weight_reduction_percentage = calculate_weight_reduction(OEM_WHEEL_WEIGHT_KG, BRIXTON_WHEEL_WEIGHT_KG)
        stress_resistance_improvement_percentage = calculate_stress_resistance_improvement(OEM_STRESS_RESISTANCE_INDEX, BRIXTON_STRESS_RESISTANCE_INDEX)
        
        # Display results
        print("Brixton Forged™ Wheel Improvements:")
        print(f"- Weight Reduction: {weight_reduction_percentage}%")
        print(f"- Stress Resistance Improvement: {stress_resistance_improvement_percentage}%")
    except ValueError as e:
        print(f"Error: {e}")
    except Exception as e:
        # Catch any unexpected exceptions
        print(f"An unexpected error occurred: {e}")

# Run the main function
if __name__ == "__main__":
    main()
```
