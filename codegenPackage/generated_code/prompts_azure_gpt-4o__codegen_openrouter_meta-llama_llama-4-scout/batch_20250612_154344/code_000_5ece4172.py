"""
Generated Code Metadata:
========================
Original URL: https://www.pavainc.com
Prompt: Write Python code to calculate the optimal quantity of UltraPRO™ Premium with InstaHeat™ deicer needed for a snow removal program based on area size and temperature thresholds.
Generated: DETERMINISTIC_5ece4172d4b460ad
Batch ID: 20250612_154344
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
"""
UltraPRO Premium with InstaHeat Deicer Calculator

Calculates the optimal quantity of UltraPRO Premium with InstaHeat deicer needed
for a snow removal program based on area size and temperature thresholds.
"""

import math

class DeicerCalculator:
    def __init__(self, area_size_sqft, temperature_threshold_f):
        """
        Initializes the DeicerCalculator with area size and temperature threshold.

        Args:
            area_size_sqft (float): Area size in square feet.
            temperature_threshold_f (float): Temperature threshold in Fahrenheit.
        """
        self.area_size_sqft = area_size_sqft
        self.temperature_threshold_f = temperature_threshold_f

    def calculate_deicer_quantity(self):
        """
        Calculates the optimal quantity of UltraPRO Premium with InstaHeat deicer.

        Returns:
            float: The optimal quantity of deicer in pounds.
        """
        # Define the deicer application rate in pounds per square foot per inch of snowfall
        # For UltraPRO Premium with InstaHeat, the recommended application rate is 0.1-0.2 lb/sqft
        application_rate_lbs_sqft = 0.15  # Use 0.15 as the default application rate

        # Adjust application rate based on temperature threshold
        if self.temperature_threshold_f < 15:
            application_rate_lbs_sqft *= 1.25  # Increase application rate by 25% for temperatures below 15°F
        elif self.temperature_threshold_f < 25:
            application_rate_lbs_sqft *= 1.1  # Increase application rate by 10% for temperatures between 15°F and 25°F

        # Calculate the optimal quantity of deicer
        deicer_quantity_lbs = self.area_size_sqft * application_rate_lbs_sqft

        return deicer_quantity_lbs


def main():
    try:
        area_size_sqft = float(input("Enter the area size in square feet: "))
        temperature_threshold_f = float(input("Enter the temperature threshold in Fahrenheit: "))

        calculator = DeicerCalculator(area_size_sqft, temperature_threshold_f)
        deicer_quantity_lbs = calculator.calculate_deicer_quantity()

        print(f"The optimal quantity of UltraPRO Premium with InstaHeat deicer needed is: {deicer_quantity_lbs:.2f} pounds")

    except ValueError:
        print("Invalid input. Please enter a valid number.")
    except Exception as e:
        print(f"An error occurred: {str(e)}")


if __name__ == "__main__":
    main()
```
