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
import numpy as np

class PigmentConcentrationCalculator:
    def __init__(self, base_material_weight, pigment_effect_factor):
        """
        Initializes the calculator with base material weight and pigment effect factor.
        
        :param base_material_weight: Weight of the base material in grams.
        :param pigment_effect_factor: The factor that represents the pigment's concentration effect.
        """
        self.base_material_weight = base_material_weight
        self.pigment_effect_factor = pigment_effect_factor

    def calculate_concentration(self, desired_color_effect):
        """
        Calculates the required pigment concentration based on the desired color effect.
        
        :param desired_color_effect: The target color effect as a percentage (0-100).
        :return: Required pigment weight in grams.
        """
        if not (0 <= desired_color_effect <= 100):
            raise ValueError("Desired color effect must be between 0 and 100.")

        # Calculate required pigment weight using the formula:
        # Required Pigment Weight = Base Material Weight * (Desired Color Effect / Pigment Effect Factor)
        required_pigment_weight = (self.base_material_weight * desired_color_effect) / self.pigment_effect_factor
        
        # Ensure the required pigment weight is non-negative
        if required_pigment_weight < 0:
            required_pigment_weight = 0

        return required_pigment_weight

    def display_results(self, desired_color_effect):
        """
        Displays the calculated pigment concentration required for the specified color effect.
        
        :param desired_color_effect: The target color effect as a percentage (0-100).
        """
        try:
            pigment_weight = self.calculate_concentration(desired_color_effect)
            print(f"To achieve a {desired_color_effect}% color effect, "
                  f"you need to add {pigment_weight:.2f} grams of pigment.")
        except ValueError as e:
            print(f"Error: {e}")

def main():
    """
    Main function to run the pigment concentration calculator.
    """
    # Example parameters - these can be adjusted as needed
    base_material_weight = 1000  # in grams
    pigment_effect_factor = 1.5    # hypothetical factor for demonstration

    # Instantiate the pigment concentration calculator
    calculator = PigmentConcentrationCalculator(base_material_weight, pigment_effect_factor)

    # Define desired color effect
    desired_color_effect = 25  # desired effect in percentage

    # Calculate and display the results
    calculator.display_results(desired_color_effect)

if __name__ == "__main__":
    main()
```
