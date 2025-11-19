"""
Generated Code Metadata:
========================
Original URL: https://engenhariawpj.com
Prompt: Write a function to calculate the environmental impact reduction achieved by using sustainable construction systems like those offered by Engenharia WPJ.
Generated: DETERMINISTIC_b03c6669880751fe
Batch ID: 20250612_153246
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# environmental_impact_calculator.py

class EnvironmentalImpactCalculator:
    """
    Calculates the environmental impact reduction achieved by using sustainable construction systems.
    """

    def __init__(self, baseline_emissions, sustainable_emissions):
        """
        Initializes the calculator with baseline and sustainable emissions.

        Args:
            baseline_emissions (float): The baseline emissions in kg CO2e.
            sustainable_emissions (float): The emissions from sustainable construction systems in kg CO2e.
        """
        self.baseline_emissions = baseline_emissions
        self.sustainable_emissions = sustainable_emissions

    def calculate_reduction(self):
        """
        Calculates the environmental impact reduction.

        Returns:
            float: The reduction in emissions in kg CO2e.
        """
        if self.baseline_emissions < 0 or self.sustainable_emissions < 0:
            raise ValueError("Emissions cannot be negative")

        reduction = self.baseline_emissions - self.sustainable_emissions
        return reduction

    def calculate_reduction_percentage(self):
        """
        Calculates the percentage reduction in environmental impact.

        Returns:
            float: The percentage reduction in emissions.
        """
        reduction = self.calculate_reduction()
        if self.baseline_emissions == 0:
            raise ZeroDivisionError("Cannot calculate percentage reduction with zero baseline emissions")

        reduction_percentage = (reduction / self.baseline_emissions) * 100
        return reduction_percentage


def main():
    try:
        baseline_emissions = 1000  # kg CO2e
        sustainable_emissions = 700  # kg CO2e

        calculator = EnvironmentalImpactCalculator(baseline_emissions, sustainable_emissions)
        reduction = calculator.calculate_reduction()
        reduction_percentage = calculator.calculate_reduction_percentage()

        print(f"Environmental impact reduction: {reduction:.2f} kg CO2e")
        print(f"Percentage reduction: {reduction_percentage:.2f}%")

    except Exception as e:
        print(f"An error occurred: {str(e)}")


if __name__ == "__main__":
    main()
```
