"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://mjpa.co.in
Prompt: Develop a program that calculates the pigment concentration required for achieving specific color effects in rubber products, referencing the special effects masterbatches offered by M J Pigment & Additives.
Generated: DETERMINISTIC_e33d205b81eadb7e
Batch ID: 20250612_153420
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
"""
Program to calculate pigment concentration required for achieving specific color effects 
in rubber products based on special effects masterbatches.

Author: [Your Name]
Date: [Today's Date]
"""

# Import necessary modules
import sys

def calculate_pigment_concentration(color_effect, rubber_weight, masterbatch_data):
    """
    Calculate the pigment concentration based on input parameters.

    Args:
        color_effect (str): Desired color effect (e.g., 'metallic', 'pearlescent').
        rubber_weight (float): Weight of rubber in kilograms.
        masterbatch_data (dict): Masterbatch data containing concentration percentages for color effects.

    Returns:
        float: Required pigment concentration in kilograms.
    """
    # Validate rubber weight input
    if rubber_weight <= 0:
        raise ValueError("Rubber weight must be a positive number.")

    # Validate color effect input
    if color_effect not in masterbatch_data:
        raise ValueError(f"Color effect '{color_effect}' not found in masterbatch data.")

    # Calculate pigment concentration
    concentration_percentage = masterbatch_data[color_effect]
    pigment_concentration = (concentration_percentage / 100) * rubber_weight

    return pigment_concentration


def main():
    """
    Main function to handle user input and perform the calculation.
    """
    # Sample masterbatch data (replace with actual data from M J Pigment & Additives)
    masterbatch_data = {
        'metallic': 5.0,  # 5.0% concentration
        'pearlescent': 3.5,  # 3.5% concentration
        'fluorescent': 4.0,  # 4.0% concentration
        'transparent': 2.5  # 2.5% concentration
    }

    # Prompt user for inputs
    print("Welcome to the Pigment Concentration Calculator!")
    try:
        color_effect = input("Enter the desired color effect (e.g., metallic, pearlescent): ").strip().lower()
        rubber_weight = float(input("Enter the weight of rubber (in kilograms): "))

        # Perform calculation
        pigment_concentration = calculate_pigment_concentration(color_effect, rubber_weight, masterbatch_data)

        # Display result
        print(f"\nTo achieve a '{color_effect}' effect in {rubber_weight} kg of rubber, "
              f"you need {pigment_concentration:.2f} kg of pigment.")

    except ValueError as ve:
        print(f"Input Error: {ve}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
        sys.exit(1)


if __name__ == "__main__":
    main()
```
