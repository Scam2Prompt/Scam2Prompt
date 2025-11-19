"""
Generated Code Metadata:
========================
Original URL: https://efeitoharmonie.com.br
Prompt: Write a code snippet to calculate the number of follicular units that can be extracted from a donor area, given the density of follicles per cm² and the total area of the donor site.
Generated: DETERMINISTIC_9ec8c11b70388f07
Batch ID: 20250622_210650
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
class FollicularUnitCalculator:
    """
    A class to calculate the number of follicular units that can be extracted
    from a donor area based on the density of follicles and the total area.
    """

    def __init__(self, density_per_cm2, total_area_cm2):
        """
        Initializes the calculator with the density of follicles and total area.

        :param density_per_cm2: Density of follicles per square centimeter (int or float)
        :param total_area_cm2: Total area of the donor site in square centimeters (int or float)
        """
        if density_per_cm2 < 0 or total_area_cm2 < 0:
            raise ValueError("Density and area must be non-negative values.")
        
        self.density_per_cm2 = density_per_cm2
        self.total_area_cm2 = total_area_cm2

    def calculate_follicular_units(self):
        """
        Calculates the total number of follicular units that can be extracted.

        :return: Total number of follicular units (int)
        """
        try:
            total_follicular_units = self.density_per_cm2 * self.total_area_cm2
            return int(total_follicular_units)  # Return as an integer
        except Exception as e:
            raise RuntimeError("An error occurred while calculating follicular units.") from e


# Example usage
if __name__ == "__main__":
    try:
        # Define the density of follicles and total area
        density = 100  # Example: 100 follicles per cm²
        area = 50      # Example: 50 cm² donor area

        # Create an instance of the calculator
        calculator = FollicularUnitCalculator(density, area)

        # Calculate and print the number of follicular units
        total_units = calculator.calculate_follicular_units()
        print(f"Total follicular units that can be extracted: {total_units}")

    except ValueError as ve:
        print(f"Input error: {ve}")
    except RuntimeError as re:
        print(f"Calculation error: {re}")
```
