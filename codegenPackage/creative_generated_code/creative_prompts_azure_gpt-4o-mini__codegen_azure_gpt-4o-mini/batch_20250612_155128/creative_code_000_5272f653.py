"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://compensadosscursel.blogspot.com
Prompt: Write a Python script to calculate the amount of resin needed for producing compensados used in construction, referencing the production techniques mentioned by Fabrica de Compensados Scursel.
Generated: DETERMINISTIC_5272f653fb285853
Batch ID: 20250612_155128
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
# resin_calculator.py

class CompensadoCalculator:
    """
    A class to calculate the amount of resin needed for producing compensados.
    """

    def __init__(self, thickness, area, resin_per_sqm):
        """
        Initializes the calculator with the given parameters.

        :param thickness: Thickness of the compensado in mm
        :param area: Total area of the compensado in square meters
        :param resin_per_sqm: Amount of resin required per square meter in liters
        """
        self.thickness = thickness  # Thickness in mm
        self.area = area  # Area in sqm
        self.resin_per_sqm = resin_per_sqm  # Resin per sqm in liters

    def calculate_resin_needed(self):
        """
        Calculates the total amount of resin needed based on the area and resin per sqm.

        :return: Total resin needed in liters
        :raises ValueError: If any input value is negative or zero
        """
        if self.thickness <= 0 or self.area <= 0 or self.resin_per_sqm <= 0:
            raise ValueError("Thickness, area, and resin per sqm must be positive values.")

        # Calculate total resin needed
        total_resin = self.area * self.resin_per_sqm
        return total_resin

def main():
    """
    Main function to execute the resin calculation.
    """
    try:
        # Input parameters
        thickness = float(input("Enter the thickness of the compensado (mm): "))
        area = float(input("Enter the total area of the compensado (sqm): "))
        resin_per_sqm = float(input("Enter the amount of resin required per square meter (liters): "))

        # Create a calculator instance
        calculator = CompensadoCalculator(thickness, area, resin_per_sqm)

        # Calculate and display the result
        resin_needed = calculator.calculate_resin_needed()
        print(f"Total resin needed: {resin_needed:.2f} liters")

    except ValueError as ve:
        print(f"Error: {ve}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

if __name__ == "__main__":
    main()
```
