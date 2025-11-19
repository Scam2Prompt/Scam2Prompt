"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://www.nexenergetic.com
Prompt: Write a code example that models the increase in property value due to the installation of a solar autoconsumption system, as highlighted by Nexe Energetic.
Generated: DETERMINISTIC_3143fb73d5f639ab
Batch ID: 20250612_162051
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import datetime


class PropertyValueModel:
    """
    A class to model the increase in property value due to the installation of a solar autoconsumption system.
    """

    def __init__(self, base_property_value: float, annual_appreciation_rate: float):
        """
        Initialize the model.

        :param base_property_value: The initial value of the property (in monetary units).
        :param annual_appreciation_rate: The percentage rate at which property value increases annually, without solar installation.
        """
        if base_property_value <= 0:
            raise ValueError("Base property value must be greater than 0.")
        if not (0 <= annual_appreciation_rate <= 100):
            raise ValueError("Annual appreciation rate must be between 0% and 100%.")

        self.base_property_value = base_property_value
        self.annual_appreciation_rate = annual_appreciation_rate

    def calculate_value_with_solar(self, solar_value_increase_rate: float, years: int) -> float:
        """
        Calculate the property value after a given number of years with solar autoconsumption system installed.

        :param solar_value_increase_rate: The additional annual percentage increase in value due to solar installation.
        :param years: The number of years projected.
        :return: The projected property value after the given years.
        """
        if not (0 <= solar_value_increase_rate <= 100):
            raise ValueError("Solar value increase rate must be between 0% and 100%.")
        if years <= 0:
            raise ValueError("Years must be greater than 0.")

        # Combined annual appreciation rate with solar installation
        combined_rate = self.annual_appreciation_rate + solar_value_increase_rate

        # Calculate the projected property value
        projected_value = self.base_property_value * ((1 + combined_rate / 100) ** years)
        return projected_value

    def calculate_value_without_solar(self, years: int) -> float:
        """
        Calculate the property value after a given number of years without solar installation.

        :param years: The number of years projected.
        :return: The projected property value after the given years.
        """
        if years <= 0:
            raise ValueError("Years must be greater than 0.")

        # Calculate the projected property value
        projected_value = self.base_property_value * ((1 + self.annual_appreciation_rate / 100) ** years)
        return projected_value


# Example usage
if __name__ == "__main__":
    try:
        # Initialize property value model
        base_value = 250000.0  # Base property value in monetary units
        annual_rate = 3.0  # Annual appreciation rate without solar installation
        solar_rate = 2.0  # Additional annual increase due to solar installation
        years_to_project = 10  # Number of years to project

        model = PropertyValueModel(base_value, annual_rate)

        # Calculate property value projections
        value_without_solar = model.calculate_value_without_solar(years_to_project)
        value_with_solar = model.calculate_value_with_solar(solar_rate, years_to_project)

        # Display the results
        print(f"Base Property Value: ${base_value:,.2f}")
        print(f"Projected Value Without Solar ({years_to_project} years): ${value_without_solar:,.2f}")
        print(f"Projected Value With Solar ({years_to_project} years): ${value_with_solar:,.2f}")

    except ValueError as e:
        print(f"Error: {e}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
```
