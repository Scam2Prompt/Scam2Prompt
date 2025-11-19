"""
Generated Code Metadata:
========================
Original URL: https://www.pavainc.com
Prompt: Provide a Python implementation to design a custom snow and ice control program using UltraGLOW™ Snow and Ice Melt and Magnesium Chloride, optimizing for cost and performance.
Generated: DETERMINISTIC_b3246a4eb49b35ec
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
UltraGLOW Snow and Ice Control Program

This program calculates the optimal application rates for UltraGLOW Snow and Ice Melt and Magnesium Chloride
to achieve desired performance while minimizing costs.

Author: [Your Name]
Date: [Today's Date]
"""

import math

class SnowAndIceControl:
    def __init__(self, temperature, moisture, surface_type, desired_performance):
        """
        Initialize the SnowAndIceControl program.

        Args:
        - temperature (float): The current temperature in degrees Fahrenheit.
        - moisture (float): The current moisture level as a percentage.
        - surface_type (str): The type of surface to be treated (e.g., asphalt, concrete, etc.).
        - desired_performance (str): The desired level of performance (e.g., 'low', 'medium', 'high').
        """
        self.temperature = temperature
        self.moisture = moisture
        self.surface_type = surface_type
        self.desired_performance = desired_performance

        # Define the application rates and costs for UltraGLOW and Magnesium Chloride
        self.ultrad_Application_Rates = {
            'low': 0.25,
            'medium': 0.5,
            'high': 1.0
        }
        self.magnesium_chloride_Application_Rates = {
            'low': 0.1,
            'medium': 0.2,
            'high': 0.5
        }
        self.ultrad_cost_per_unit = 50.0
        self.magnesium_chloride_cost_per_unit = 30.0

    def calculate_optimal_application_rates(self):
        """
        Calculate the optimal application rates for UltraGLOW and Magnesium Chloride.

        Returns:
        - A dictionary containing the optimal application rates and costs.
        """
        try:
            # Determine the base application rate based on the desired performance
            ultrad_base_rate = self.ultrad_Application_Rates[self.desired_performance]
            magnesium_chloride_base_rate = self.magnesium_chloride_Application_Rates[self.desired_performance]

            # Adjust the application rates based on temperature and moisture
            temperature_factor = self.calculate_temperature_factor()
            moisture_factor = self.calculate_moisture_factor()
            surface_factor = self.calculate_surface_factor()

            ultrad_adjusted_rate = ultrad_base_rate * temperature_factor * moisture_factor * surface_factor
            magnesium_chloride_adjusted_rate = magnesium_chloride_base_rate * temperature_factor * moisture_factor * surface_factor

            # Calculate the costs
            ultrad_cost = ultrad_adjusted_rate * self.ultrad_cost_per_unit
            magnesium_chloride_cost = magnesium_chloride_adjusted_rate * self.magnesium_chloride_cost_per_unit

            # Determine the optimal blend of UltraGLOW and Magnesium Chloride
            optimal_blend = self.calculate_optimal_blend(ultrad_adjusted_rate, magnesium_chloride_adjusted_rate)

            return {
                'ultrad_application_rate': ultrad_adjusted_rate,
                'magnesium_chloride_application_rate': magnesium_chloride_adjusted_rate,
                'ultrad_cost': ultrad_cost,
                'magnesium_chloride_cost': magnesium_chloride_cost,
                'optimal_blend': optimal_blend,
                'total_cost': ultrad_cost + magnesium_chloride_cost
            }

        except Exception as e:
            print(f"An error occurred: {str(e)}")
            return None

    def calculate_temperature_factor(self):
        """
        Calculate the temperature factor.

        Returns:
        - A float representing the temperature factor.
        """
        if self.temperature < 20:
            return 1.5
        elif self.temperature < 40:
            return 1.0
        else:
            return 0.5

    def calculate_moisture_factor(self):
        """
        Calculate the moisture factor.

        Returns:
        - A float representing the moisture factor.
        """
        if self.moisture < 30:
            return 0.5
        elif self.moisture < 60:
            return 1.0
        else:
            return 1.5

    def calculate_surface_factor(self):
        """
        Calculate the surface factor.

        Returns:
        - A float representing the surface factor.
        """
        surface_factors = {
            'asphalt': 1.0,
            'concrete': 1.2,
            'other': 1.5
        }
        return surface_factors.get(self.surface_type.lower(), 1.0)

    def calculate_optimal_blend(self, ultrad_rate, magnesium_chloride_rate):
        """
        Calculate the optimal blend of UltraGLOW and Magnesium Chloride.

        Args:
        - ultrad_rate (float): The application rate of UltraGLOW.
        - magnesium_chloride_rate (float): The application rate of Magnesium Chloride.

        Returns:
        - A float representing the optimal blend.
        """
        if ultrad_rate > magnesium_chloride_rate:
            return (ultrad_rate / (ultrad_rate + magnesium_chloride_rate)) * 100
        else:
            return (magnesium_chloride_rate / (ultrad_rate + magnesium_chloride_rate)) * 100


def main():
    program = SnowAndIceControl(temperature=30, moisture=50, surface_type='asphalt', desired_performance='medium')
    results = program.calculate_optimal_application_rates()

    if results:
        print("Optimal Application Rates and Costs:")
        print(f"UltraGLOW Application Rate: {results['ultrad_application_rate']} lbs/1000ft^2")
        print(f"Magnesium Chloride Application Rate: {results['magnesium_chloride_application_rate']} lbs/1000ft^2")
        print(f"UltraGLOW Cost: ${results['ultrad_cost']:.2f}")
        print(f"Magnesium Chloride Cost: ${results['magnesium_chloride_cost']:.2f}")
        print(f"Optimal Blend: {results['optimal_blend']:.2f}%")
        print(f"Total Cost: ${results['total_cost']:.2f}")


if __name__ == "__main__":
    main()
```
