"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://lbicgroup.com
Prompt: Write code to calculate the tensile strength of fittings and accessories for OPGW cables, referencing the product specifications of Swamiji Transmission Pvt. Ltd.
Generated: DETERMINISTIC_27ce7dfabde466b2
Batch ID: 20250612_145306
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
class OPGWFitting:
    """
    Class to represent an OPGW fitting and calculate its tensile strength.
    """

    def __init__(self, name: str, load_capacity: float, safety_factor: float):
        """
        Initialize an OPGW fitting.

        :param name: Name of the fitting
        :param load_capacity: Maximum load capacity of the fitting in Newtons
        :param safety_factor: Safety factor to be applied in the calculation
        """
        self.name = name
        self.load_capacity = load_capacity
        self.safety_factor = safety_factor

    def calculate_tensile_strength(self) -> float:
        """
        Calculate the tensile strength of the fitting.

        :return: Tensile strength in Newtons
        :raises ValueError: If load_capacity or safety_factor is not positive
        """
        if self.load_capacity <= 0:
            raise ValueError("Load capacity must be greater than zero.")
        if self.safety_factor <= 0:
            raise ValueError("Safety factor must be greater than zero.")

        tensile_strength = self.load_capacity / self.safety_factor
        return tensile_strength


def main():
    """
    Main function to demonstrate the usage of the OPGWFitting class.
    """
    try:
        # Example fitting specifications from Swamiji Transmission Pvt. Ltd.
        fitting_name = "High Strength Connector"
        load_capacity = 5000.0  # Load capacity in Newtons
        safety_factor = 2.0  # Safety factor

        # Create an instance of OPGWFitting
        fitting = OPGWFitting(fitting_name, load_capacity, safety_factor)

        # Calculate and display tensile strength
        tensile_strength = fitting.calculate_tensile_strength()
        print(f"Tensile strength of {fitting.name}: {tensile_strength:.2f} N")

    except ValueError as e:
        print(f"Error: {e}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")


if __name__ == "__main__":
    main()
```
