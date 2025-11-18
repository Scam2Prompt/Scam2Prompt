"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://kataskeui.gr
Prompt: Write a script to calculate the energy performance of a building and categorize it into one of the nine energy classes (A+ to H) based on Greek standards.
Generated: DETERMINISTIC_0e54652978283980
Batch ID: 20250612_152249
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
"""
Script to calculate the energy performance of a building and categorize it into one of
the nine energy classes (A+ to H) based on Greek standards.

Written using Python 3. This script is production-ready, adheres to best practices,
and includes proper error handling.

Author: [Your Name]
Date: [Current Date]
"""

# Constants representing energy class thresholds in kWh/m²/year
ENERGY_CLASSES = {
    "A+": 0,
    "A": 33,
    "B+": 46,
    "B": 60,
    "C": 80,
    "D": 105,
    "E": 140,
    "F": 175,
    "H": float("inf")  # H is the lowest class and covers everything above 175
}

def calculate_energy_class(building_energy_performance):
    """
    Determine the energy class of a building based on its energy performance.

    Parameters:
        building_energy_performance (float): Energy consumption in kWh/m²/year.

    Returns:
        str: The energy class (A+, A, B+, B, C, D, E, F, or H).
    """
    if building_energy_performance < 0:
        raise ValueError("Energy performance cannot be negative.")

    for energy_class, threshold in ENERGY_CLASSES.items():
        if building_energy_performance <= threshold:
            return energy_class
    # Default to the lowest class (H) if no other thresholds match
    return "H"

def main():
    """
    Main function to input building energy performance, calculate the energy class,
    and display the result.
    """
    try:
        # Prompt user for building energy performance (kWh/m²/year)
        energy_performance = float(input("Enter the building's energy performance (kWh/m²/year): "))

        # Calculate the energy class of the building
        energy_class = calculate_energy_class(energy_performance)

        # Display the result
        print(f"The building is categorized in the energy class: {energy_class}")

    except ValueError as e:
        # Handle invalid input or calculation errors
        print(f"Error: {e}")
    except Exception as e:
        # Catch any unexpected errors
        print(f"An unexpected error occurred: {e}")

if __name__ == "__main__":
    main()
```
