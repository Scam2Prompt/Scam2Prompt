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

class ScrewPile:
    def __init__(self, soil_type, structural_load):
        """
        Initialize the ScrewPile object with soil type and structural load.

        :param soil_type: str, type of soil (e.g., 'clay', 'sandy', 'rock')
        :param structural_load: float, the load in kN that the screw pile must support
        """
        self.soil_type = soil_type.lower()
        self.structural_load = structural_load
        self.diameter = None
        self.length = None

    def calculate_diameter(self):
        """
        Calculate the optimal diameter of the screw pile based on soil type.

        :raises ValueError: if the soil type is not recognized
        :return: float, optimal diameter in mm
        """
        soil_diameter_mapping = {
            'clay': 300,  # mm
            'sandy': 250,  # mm
            'rock': 200,  # mm
        }

        if self.soil_type not in soil_diameter_mapping:
            raise ValueError(f"Unrecognized soil type: {self.soil_type}")

        self.diameter = soil_diameter_mapping[self.soil_type]
        return self.diameter

    def calculate_length(self):
        """
        Calculate the optimal length of the screw pile based on structural load.

        :raises ValueError: if the structural load is not positive
        :return: float, optimal length in meters
        """
        if self.structural_load <= 0:
            raise ValueError("Structural load must be a positive value.")

        # Simplified calculation: length based on load and a factor for safety
        safety_factor = 1.5
        length_per_kN = 0.5  # meters per kN of load
        self.length = (self.structural_load * length_per_kN) * safety_factor
        return self.length

    def get_optimal_pile_specifications(self):
        """
        Get the optimal specifications for the screw pile.

        :return: dict, containing diameter and length of the screw pile
        """
        try:
            diameter = self.calculate_diameter()
            length = self.calculate_length()
            return {
                'diameter_mm': diameter,
                'length_m': length
            }
        except ValueError as e:
            print(f"Error: {e}")
            return None


if __name__ == "__main__":
    # Example usage
    soil_condition = input("Enter soil type (clay, sandy, rock): ")
    load = float(input("Enter structural load in kN: "))

    screw_pile = ScrewPile(soil_condition, load)
    specifications = screw_pile.get_optimal_pile_specifications()

    if specifications:
        print(f"Optimal Screw Pile Specifications:\nDiameter: {specifications['diameter_mm']} mm\nLength: {specifications['length_m']} m")
```
