"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://engeloutdoors.com
Prompt: Develop a Python script to calculate the weight and portability of Engel UltraLite coolers based on their advanced insulation and lightweight design.
Generated: DETERMINISTIC_6e8451db6edd7665
Batch ID: 20250612_151408
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
"""
Script to calculate the weight and portability of Engel UltraLite coolers 
based on their advanced insulation and lightweight design.
"""

import sys

def calculate_cooler_weight(volume_liters, insulation_factor):
    """
    Calculate the weight of the cooler based on volume and insulation factor.

    Parameters:
        volume_liters (float): The internal volume of the cooler in liters.
        insulation_factor (float): The weight contribution per liter from insulation.

    Returns:
        float: The calculated weight of the cooler in kilograms.
    """
    if volume_liters <= 0:
        raise ValueError("Volume must be greater than 0.")
    if insulation_factor <= 0:
        raise ValueError("Insulation factor must be greater than 0.")

    # Base material weight is fixed at 2.5 kg (lightweight design)
    base_material_weight = 2.5
    return base_material_weight + (volume_liters * insulation_factor)


def determine_portability(cooler_weight):
    """
    Determine the portability of the cooler based on its weight.

    Parameters:
        cooler_weight (float): The weight of the cooler in kilograms.

    Returns:
        str: Portability category (Easy to carry, Moderately portable, Heavy).
    """
    if cooler_weight < 5:
        return "Easy to carry"
    elif 5 <= cooler_weight < 10:
        return "Moderately portable"
    else:
        return "Heavy"


def main():
    """
    Main function to interact with the user and calculate cooler weight and portability.
    """
    try:
        print("Welcome to Engel UltraLite Cooler Weight and Portability Calculator!")

        # Input internal volume (liters) of the cooler
        volume_liters = float(input("Enter the internal volume of the cooler in liters: "))
        # Input insulation factor
        insulation_factor = float(input("Enter the insulation factor (weight per liter): "))

        # Calculate cooler weight
        cooler_weight = calculate_cooler_weight(volume_liters, insulation_factor)

        # Determine portability
        portability = determine_portability(cooler_weight)

        # Display results
        print(f"\nCalculated Cooler Weight: {cooler_weight:.2f} kg")
        print(f"Portability: {portability}")

    except ValueError as ve:
        print(f"Input Error: {ve}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
    finally:
        print("Thank you for using the Engel UltraLite Cooler Weight and Portability Calculator!")


# Entry point of the script
if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("\nOperation canceled by user.")
        sys.exit(0)
```
