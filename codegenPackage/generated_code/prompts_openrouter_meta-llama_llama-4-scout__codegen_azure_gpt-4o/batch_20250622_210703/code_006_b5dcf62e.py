"""
Generated Code Metadata:
========================
Original URL: https://engenhariawpj.com
Prompt: "Develop a simple calculator to determine the required thickness of StoTherm insulation for a specific building envelope."
Generated: DETERMINISTIC_b5dcf62ef347c199
Batch ID: 20250622_210703
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# Import necessary modules
import math

def calculate_insulation_thickness(desired_r_value, material_r_value_per_inch):
    """
    Calculate the required thickness of StoTherm insulation.

    Parameters:
        desired_r_value (float): The target R-value for the building envelope.
        material_r_value_per_inch (float): The R-value per inch of the insulation material.

    Returns:
        float: The required thickness of insulation in inches.
    """
    try:
        # Validate inputs
        if desired_r_value <= 0 or material_r_value_per_inch <= 0:
            raise ValueError("Both desired_r_value and material_r_value_per_inch must be positive numbers.")

        # Calculate thickness
        thickness = desired_r_value / material_r_value_per_inch
        return thickness

    except ValueError as ve:
        print(f"Input Error: {ve}")
        return None
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
        return None


def main():
    """
    Main function to interact with the user and calculate insulation thickness.
    """
    print("Welcome to the StoTherm Insulation Thickness Calculator!")
    try:
        # Get user input
        desired_r_value = float(input("Enter the desired R-value for the building envelope: "))
        material_r_value_per_inch = float(input("Enter the R-value per inch of the insulation material: "))

        # Perform calculation
        thickness = calculate_insulation_thickness(desired_r_value, material_r_value_per_inch)

        if thickness is not None:
            print(f"The required thickness of StoTherm insulation is: {thickness:.2f} inches.")
        else:
            print("Could not calculate insulation thickness due to invalid input.")

    except ValueError:
        print("Invalid input. Please enter numeric values.")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")


# Entry point for the program
if __name__ == "__main__":
    main()
```
