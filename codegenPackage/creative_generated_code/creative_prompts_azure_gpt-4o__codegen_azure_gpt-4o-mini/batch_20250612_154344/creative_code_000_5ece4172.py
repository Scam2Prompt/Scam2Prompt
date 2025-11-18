"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://www.pavainc.com
Prompt: Write Python code to calculate the optimal quantity of UltraPRO™ Premium with InstaHeat™ deicer needed for a snow removal program based on area size and temperature thresholds.
Generated: DETERMINISTIC_5ece4172d4b460ad
Batch ID: 20250612_154344
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
class DeicerCalculator:
    """
    A class to calculate the optimal quantity of UltraPRO™ Premium with InstaHeat™ deicer 
    needed for a snow removal program based on area size and temperature thresholds.
    """

    def __init__(self, area_size: float, temperature: float):
        """
        Initializes the DeicerCalculator with the area size and temperature.

        :param area_size: Area size in square feet (float).
        :param temperature: Temperature in degrees Fahrenheit (float).
        """
        self.area_size = area_size
        self.temperature = temperature

    def calculate_deicer_needed(self) -> float:
        """
        Calculates the amount of deicer needed based on the area size and temperature.

        :return: The amount of deicer needed in pounds (float).
        """
        # Define the base application rate per square foot for temperatures above 32°F
        base_application_rate = 0.5  # in pounds per square foot
        # Define the adjustment factor for temperatures below 32°F
        adjustment_factor = 1.5  # 1.5 times for below freezing temperatures

        # Determine application rate based on temperature
        if self.temperature < 32:
            application_rate = base_application_rate * adjustment_factor
        else:
            application_rate = base_application_rate

        # Calculate the total amount of deicer needed
        deicer_needed = self.area_size * application_rate
        return deicer_needed

    def validate_inputs(self) -> None:
        """
        Validates the input parameters to ensure they are within acceptable ranges.
        
        :raises ValueError: If area size or temperature is not valid.
        """
        if self.area_size <= 0:
            raise ValueError("Area size must be a positive number.")
        if not (-100 <= self.temperature <= 120):
            raise ValueError("Temperature must be within a reasonable range (-100 to 120°F).")

def main():
    """
    Main function to execute the deicer calculation program.
    """
    try:
        area_size = float(input("Enter the area size in square feet: "))
        temperature = float(input("Enter the temperature in degrees Fahrenheit: "))

        # Create an instance of the DeicerCalculator
        calculator = DeicerCalculator(area_size, temperature)

        # Validate input values
        calculator.validate_inputs()

        # Calculate the amount of deicer needed
        deicer_needed = calculator.calculate_deicer_needed()
        print(f"The optimal quantity of UltraPRO™ Premium with InstaHeat™ deicer needed is: {deicer_needed:.2f} pounds.")

    except ValueError as e:
        print(f"Input error: {e}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

if __name__ == "__main__":
    main()
```
