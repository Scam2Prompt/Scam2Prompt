"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://provincialwatersolutions.com
Prompt: Generate code to calculate the hardness of water and suggest a suitable water softener system, based on the specifications listed on Provincial Water Solutions' site.
Generated: DETERMINISTIC_04c319d43e079bb8
Batch ID: 20250612_152924
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
class WaterHardnessCalculator:
    """
    A class to calculate water hardness and suggest a suitable water softener system.
    """

    def __init__(self, calcium: float, magnesium: float):
        """
        Initializes the calculator with the amounts of calcium and magnesium.

        :param calcium: Concentration of calcium in mg/L
        :param magnesium: Concentration of magnesium in mg/L
        """
        self.calcium = calcium
        self.magnesium = magnesium
        self.hardness = self.calculate_hardness()

    def calculate_hardness(self) -> float:
        """
        Calculate the hardness of water based on calcium and magnesium concentrations.

        :return: Water hardness in mg/L as CaCO3
        """
        try:
            hardness = (self.calcium * 2.5) + (self.magnesium * 4.1)
            return hardness
        except Exception as e:
            raise ValueError(f"Error calculating hardness: {e}")

    def suggest_softener(self) -> str:
        """
        Suggest a water softener system based on water hardness.

        :return: Suggested softener system
        """
        if self.hardness <= 60:
            return "Water is soft. No water softener needed."
        elif 61 <= self.hardness <= 120:
            return "Consider a basic water softener system."
        elif 121 <= self.hardness <= 180:
            return "A moderate water softener system is recommended."
        else:  # hardness > 180
            return "High hardness detected. A high-capacity water softener system is advised."

def main():
    """
    Main function to execute the hardness calculation and suggestion.
    """
    try:
        # User inputs for calcium and magnesium levels
        calcium_input = float(input("Enter the calcium concentration (mg/L): "))
        magnesium_input = float(input("Enter the magnesium concentration (mg/L): "))
        
        # Create an instance of the WaterHardnessCalculator
        water_hardness_calculator = WaterHardnessCalculator(calcium_input, magnesium_input)
        
        # Output the calculated hardness
        print(f"Calculated Water Hardness: {water_hardness_calculator.hardness:.2f} mg/L as CaCO3")
        
        # Suggest a water softener
        suggestion = water_hardness_calculator.suggest_softener()
        print(suggestion)

    except ValueError as ve:
        print(f"Input Error: {ve}")
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    main()
```
