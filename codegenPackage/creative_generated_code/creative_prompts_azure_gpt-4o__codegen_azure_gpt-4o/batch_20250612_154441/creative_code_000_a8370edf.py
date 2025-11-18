"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://rubberflooringindonesia.com
Prompt: Write code to calculate the optimal thickness for rubber flooring in a gym setting, referencing the types of rubber flooring materials like EPDM and TPV mentioned on Rubber Flooring Indonesia's website.
Generated: DETERMINISTIC_a8370edfa2b3afbf
Batch ID: 20250612_154441
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import math

class RubberFlooringCalculator:
    """
    A class to calculate the optimal thickness for rubber flooring in a gym setting
    based on materials such as EPDM and TPV.
    """
    
    def __init__(self):
        """
        Initializes the calculator with default material properties.
        """
        self.material_properties = {
            "EPDM": {
                "density": 1.4,  # g/cm³
                "shock_absorption_factor": 0.8,  # Arbitrary factor for shock absorption
            },
            "TPV": {
                "density": 1.2,  # g/cm³
                "shock_absorption_factor": 0.7,  # Arbitrary factor for shock absorption
            },
        }

    def calculate_thickness(self, material, intended_use):
        """
        Calculates the optimal thickness of the rubber flooring.

        Args:
            material (str): The type of rubber material (e.g., 'EPDM' or 'TPV').
            intended_use (str): The intended use of the gym flooring (e.g., 'light', 'moderate', 'intense').

        Returns:
            float: The optimal thickness in millimeters.

        Raises:
            ValueError: If the material or intended use is invalid.
        """
        # Validate material type
        if material not in self.material_properties:
            raise ValueError(f"Invalid material: {material}. Supported materials are: {', '.join(self.material_properties.keys())}")

        # Validate intended use
        use_factor = {
            "light": 0.5,      # For yoga or light activities
            "moderate": 1.0,   # For weightlifting or moderate activities
            "intense": 1.5,    # For heavy lifting or intense activities
        }
        if intended_use not in use_factor:
            raise ValueError(f"Invalid intended use: {intended_use}. Supported uses are: {', '.join(use_factor.keys())}")

        # Get material properties
        material_density = self.material_properties[material]["density"]
        shock_absorption_factor = self.material_properties[material]["shock_absorption_factor"]

        # Calculate thickness using a formula that combines density, shock absorption, and intended use factor
        thickness = material_density * shock_absorption_factor * use_factor[intended_use] * 10  # Scale to millimeters

        return round(thickness, 2)  # Return thickness rounded to 2 decimal places

def main():
    """
    Main function to interact with the RubberFlooringCalculator.
    """
    calculator = RubberFlooringCalculator()

    print("Welcome to the Rubber Flooring Thickness Calculator!")

    try:
        # User input
        material = input("Enter the material type (EPDM/TPV): ").strip().upper()
        intended_use = input("Enter the intended use (light/moderate/intense): ").strip().lower()

        # Calculate thickness
        optimal_thickness = calculator.calculate_thickness(material, intended_use)

        print(f"The optimal thickness for {material} flooring in a {intended_use} gym setting is: {optimal_thickness} mm")

    except ValueError as e:
        print(f"Error: {e}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

if __name__ == "__main__":
    main()
```
