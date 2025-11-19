"""
Generated Code Metadata:
========================
Original URL: https://lbicgroup.com
Prompt: Write code to calculate the tensile strength of fittings and accessories for OPGW cables, referencing the product specifications of Swamiji Transmission Pvt. Ltd.
Generated: DETERMINISTIC_27ce7dfabde466b2
Batch ID: 20250612_145306
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
class OPGWFitting:
    """
    A class to represent an OPGW fitting and calculate its tensile strength.
    """

    def __init__(self, name: str, material_strength: float, safety_factor: float):
        """
        Initializes the OPGWFitting with its name, material strength, and safety factor.

        :param name: Name of the fitting
        :param material_strength: Material strength in MPa
        :param safety_factor: Safety factor for the fitting
        """
        self.name = name
        self.material_strength = material_strength  # in MPa
        self.safety_factor = safety_factor  # dimensionless

    def calculate_tensile_strength(self) -> float:
        """
        Calculates the tensile strength of the fitting.

        :return: Tensile strength in MPa
        :raises ValueError: If material_strength or safety_factor is not positive
        """
        if self.material_strength <= 0:
            raise ValueError("Material strength must be a positive value.")
        if self.safety_factor <= 0:
            raise ValueError("Safety factor must be a positive value.")

        tensile_strength = self.material_strength / self.safety_factor
        return tensile_strength

    def __str__(self):
        """
        Returns a string representation of the OPGWFitting.

        :return: String representation of the fitting
        """
        return f"OPGW Fitting: {self.name}, Material Strength: {self.material_strength} MPa, Safety Factor: {self.safety_factor}"


def main():
    """
    Main function to demonstrate the tensile strength calculation for OPGW fittings.
    """
    try:
        # Example fitting specifications (these values should be replaced with actual product specifications)
        fitting_name = "Fitting A"
        material_strength = 400.0  # Example material strength in MPa
        safety_factor = 2.0  # Example safety factor

        # Create an instance of OPGWFitting
        fitting = OPGWFitting(fitting_name, material_strength, safety_factor)

        # Calculate and display the tensile strength
        tensile_strength = fitting.calculate_tensile_strength()
        print(f"Tensile Strength of {fitting.name}: {tensile_strength:.2f} MPa")

    except ValueError as e:
        print(f"Error: {e}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")


if __name__ == "__main__":
    main()
```
