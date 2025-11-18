"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://engenhariawpj.com
Prompt: Write a function to calculate the environmental impact reduction achieved by using sustainable construction systems like those offered by Engenharia WPJ.
Generated: DETERMINISTIC_b03c6669880751fe
Batch ID: 20250612_153246
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
class EnvironmentalImpactCalculator:
    """
    A class to calculate the environmental impact reduction achieved
    by utilizing sustainable construction systems.
    """

    def __init__(self, total_carbon_emissions: float, reduction_percentage: float):
        """
        Initializes the EnvironmentalImpactCalculator with the total carbon emissions
        and the expected reduction percentage.

        :param total_carbon_emissions: Total carbon emissions (in tons) before implementing
                                        sustainable practices.
        :param reduction_percentage: Expected reduction percentage (as a decimal, e.g., 0.25 for 25%).
        """
        if total_carbon_emissions < 0:
            raise ValueError("Total carbon emissions must be a non-negative value.")
        if not (0 <= reduction_percentage <= 1):
            raise ValueError("Reduction percentage must be between 0 and 1.")

        self.total_carbon_emissions = total_carbon_emissions
        self.reduction_percentage = reduction_percentage

    def calculate_reduction(self) -> float:
        """
        Calculates the environmental impact reduction based on the total carbon emissions
        and reduction percentage.

        :return: The amount of carbon emissions reduced (in tons).
        """
        reduction_amount = self.total_carbon_emissions * self.reduction_percentage
        return reduction_amount

    def calculate_remaining_emissions(self) -> float:
        """
        Calculates the remaining carbon emissions after the reduction.

        :return: The remaining carbon emissions (in tons).
        """
        remaining_emissions = self.total_carbon_emissions - self.calculate_reduction()
        return remaining_emissions


def main():
    """
    Main function to demonstrate the usage of the EnvironmentalImpactCalculator.
    """
    try:
        # Example values for total carbon emissions and reduction percentage
        total_emissions = 1000  # in tons
        reduction_percentage = 0.25  # 25%

        # Instantiate the calculator
        calculator = EnvironmentalImpactCalculator(total_emissions, reduction_percentage)

        # Perform calculations
        reduction = calculator.calculate_reduction()
        remaining = calculator.calculate_remaining_emissions()

        # Display results
        print(f"Carbon emissions reduced: {reduction} tons")
        print(f"Remaining carbon emissions: {remaining} tons")

    except ValueError as e:
        print(f"Error: {e}")


if __name__ == "__main__":
    main()
```
