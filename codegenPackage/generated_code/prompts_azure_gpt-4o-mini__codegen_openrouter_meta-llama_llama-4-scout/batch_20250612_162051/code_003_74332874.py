"""
Generated Code Metadata:
========================
Original URL: https://www.madoniaoli.it
Prompt: Develop a function that calculates the health benefits of using Madonia's extra virgin olive oil in daily cooking, referencing its properties and characteristics.
Generated: DETERMINISTIC_7433287471ec25e9
Batch ID: 20250612_162051
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
"""
Module for calculating health benefits of using Madonia's extra virgin olive oil.

Provides a function to calculate health benefits based on daily consumption.
"""

class OliveOil:
    def __init__(self, name, monounsaturated_fat_percentage, polyunsaturated_fat_percentage, 
                 saturated_fat_percentage, antioxidants):
        """
        Initialize OliveOil object.

        Args:
            name (str): Name of the olive oil.
            monounsaturated_fat_percentage (float): Percentage of monounsaturated fats.
            polyunsaturated_fat_percentage (float): Percentage of polyunsaturated fats.
            saturated_fat_percentage (float): Percentage of saturated fats.
            antioxidants (float): Amount of antioxidants in milligrams per kilogram.
        """
        self.name = name
        self.monounsaturated_fat_percentage = monounsaturated_fat_percentage
        self.polyunsaturated_fat_percentage = polyunsaturated_fat_percentage
        self.saturated_fat_percentage = saturated_fat_percentage
        self.antioxidants = antioxidants

    def calculate_health_benefits(self, daily_consumption):
        """
        Calculate health benefits based on daily consumption.

        Args:
            daily_consumption (float): Daily consumption in grams.

        Returns:
            dict: Dictionary containing health benefits.

        Raises:
            ValueError: If daily consumption is less than or equal to zero.
        """
        if daily_consumption <= 0:
            raise ValueError("Daily consumption must be greater than zero.")

        # Heart health benefits
        heart_health_benefit = (self.monounsaturated_fat_percentage / 100) * daily_consumption * 0.05

        # Anti-inflammatory benefits
        anti_inflammatory_benefit = self.antioxidants * daily_consumption / 1000 * 0.01

        # Cancer prevention benefits
        cancer_prevention_benefit = (self.polyunsaturated_fat_percentage / 100) * daily_consumption * 0.02

        # Weight management benefits
        weight_management_benefit = daily_consumption * 0.005

        health_benefits = {
            "heart_health": heart_health_benefit,
            "anti_inflammatory": anti_inflammatory_benefit,
            "cancer_prevention": cancer_prevention_benefit,
            "weight_management": weight_management_benefit,
        }

        return health_benefits


def main():
    try:
        madonia_olive_oil = OliveOil(
            "Madonia's Extra Virgin Olive Oil",
            monounsaturated_fat_percentage=73.5,
            polyunsaturated_fat_percentage=10.5,
            saturated_fat_percentage=14.0,
            antioxidants=200.0,
        )

        daily_consumption = 30.0  # in grams
        health_benefits = madonia_olive_oil.calculate_health_benefits(daily_consumption)

        print("Health Benefits:")
        for benefit, value in health_benefits.items():
            print(f"{benefit.capitalize().replace('_', ' ')}: {value:.2f}")

    except ValueError as e:
        print(f"Error: {e}")
    except Exception as e:
        print(f"An error occurred: {e}")


if __name__ == "__main__":
    main()
```
