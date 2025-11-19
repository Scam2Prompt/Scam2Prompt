"""
Generated Code Metadata:
========================
Original URL: https://histeknik.com
Prompt: "Generate a Python script to determine the optimal screw pile diameter and length for a given soil condition and structural load."
Generated: DETERMINISTIC_f12b50315f3bf63d
Batch ID: 20250622_210650
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import math

class ScrewPileCalculator:
    """
    A class to calculate the optimal screw pile diameter and length
    based on soil conditions and structural load.
    """

    def __init__(self, soil_bearing_capacity, structural_load, safety_factor=2.0):
        """
        Initialize the calculator with soil conditions and structural load.

        :param soil_bearing_capacity: Bearing capacity of the soil (kPa)
        :param structural_load: Total structural load to be supported (kN)
        :param safety_factor: Safety factor to ensure stability (default: 2.0)
        """
        self.soil_bearing_capacity = soil_bearing_capacity  # kPa
        self.structural_load = structural_load  # kN
        self.safety_factor = safety_factor  # Safety factor

    def calculate_diameter(self):
        """
        Calculate the optimal screw pile diameter.

        :return: Optimal diameter in meters
        """
        # Convert structural load to kPa (1 kN = 1000 N, 1 kPa = 1000 N/m^2)
        required_pressure = (self.structural_load * 1000) / self.safety_factor

        # Ensure soil can handle the pressure
        if required_pressure > self.soil_bearing_capacity:
            raise ValueError("Soil bearing capacity is insufficient for the given load.")

        # Calculate diameter using the formula: Area = Load / Pressure
        # Area = π * (diameter / 2)^2
        optimal_area = self.structural_load / self.soil_bearing_capacity
        diameter = math.sqrt((4 * optimal_area) / math.pi)

        return round(diameter, 2)

    def calculate_length(self):
        """
        Calculate the optimal screw pile length.

        :return: Optimal length in meters
        """
        # Assume a simple empirical formula for length based on load and soil capacity
        # Length = (Load / Soil Bearing Capacity) * Safety Factor
        length = (self.structural_load / self.soil_bearing_capacity) * self.safety_factor

        # Ensure a minimum length for stability
        minimum_length = 2.0  # meters
        return max(round(length, 2), minimum_length)

    def calculate_optimal_pile(self):
        """
        Calculate both the optimal diameter and length of the screw pile.

        :return: A dictionary containing diameter and length
        """
        try:
            diameter = self.calculate_diameter()
            length = self.calculate_length()
            return {"diameter": diameter, "length": length}
        except ValueError as e:
            return {"error": str(e)}


def main():
    """
    Main function to interact with the user and calculate screw pile dimensions.
    """
    print("Screw Pile Calculator")
    print("======================")

    try:
        # Get user inputs
        soil_bearing_capacity = float(input("Enter soil bearing capacity (kPa): "))
        structural_load = float(input("Enter structural load (kN): "))
        safety_factor = float(input("Enter safety factor (default is 2.0): ") or 2.0)

        # Create calculator instance
        calculator = ScrewPileCalculator(soil_bearing_capacity, structural_load, safety_factor)

        # Calculate optimal pile dimensions
        result = calculator.calculate_optimal_pile()

        # Display results
        if "error" in result:
            print(f"Error: {result['error']}")
        else:
            print(f"Optimal Screw Pile Diameter: {result['diameter']} meters")
            print(f"Optimal Screw Pile Length: {result['length']} meters")

    except ValueError:
        print("Invalid input. Please enter numeric values for all inputs.")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")


if __name__ == "__main__":
    main()
```
