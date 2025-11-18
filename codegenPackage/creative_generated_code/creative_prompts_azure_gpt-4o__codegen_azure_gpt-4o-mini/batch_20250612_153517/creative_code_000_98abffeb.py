"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://eclipsi-net.com
Prompt: Write Python code to calculate luminary requirements for an architectural lighting project, referencing Eclipsi's approach to cálculos lumínicos.
Generated: DETERMINISTIC_98abffeb54cd1457
Batch ID: 20250612_153517
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
class LightingCalculator:
    """
    A class to calculate luminary requirements based on the area to be illuminated,
    the desired illuminance levels, and the luminous output of the luminaries.
    """

    def __init__(self, area: float, illuminance: float, luminous_output: float):
        """
        Initializes the LightingCalculator with the following parameters:
        
        :param area: Area to be illuminated in square meters (m²)
        :param illuminance: Desired illuminance level in lux (lx)
        :param luminous_output: Luminous output of the luminaries in lumens (lm)
        """
        self.area = area
        self.illuminance = illuminance
        self.luminous_output = luminous_output

    def calculate_luminaries_needed(self) -> int:
        """
        Calculates the number of luminaries required for the project.
        
        :return: The number of luminaries needed (rounded up to the nearest whole number)
        :raises ValueError: If any of the input parameters are non-positive
        """
        if self.area <= 0:
            raise ValueError("Area must be a positive value.")
        if self.illuminance <= 0:
            raise ValueError("Illuminance must be a positive value.")
        if self.luminous_output <= 0:
            raise ValueError("Luminous output must be a positive value.")

        # Calculate the total luminous flux required
        total_luminous_flux = self.area * self.illuminance
        
        # Calculate the number of luminaries needed
        luminaries_needed = total_luminous_flux / self.luminous_output
        
        return int(-(-luminaries_needed // 1))  # Ceiling division

def main():
    """
    Main function to execute the lighting calculation.
    """
    try:
        # Example parameters
        area = 50.0  # in m²
        illuminance = 300.0  # in lx
        luminous_output = 1200.0  # in lm

        # Create a LightingCalculator instance
        lighting_calculator = LightingCalculator(area, illuminance, luminous_output)

        # Calculate and display the number of luminaries needed
        luminaries = lighting_calculator.calculate_luminaries_needed()
        print(f"Number of luminaries required: {luminaries}")

    except ValueError as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    main()
```
