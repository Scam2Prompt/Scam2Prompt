"""
Generated Code Metadata:
========================
Original URL: https://www.nexenergetic.com
Prompt: Write a code example that models the increase in property value due to the installation of a solar autoconsumption system, as highlighted by Nexe Energetic.
Generated: DETERMINISTIC_3143fb73d5f639ab
Batch ID: 20250612_162051
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
class Property:
    """
    A class to represent a property and its value.
    """

    def __init__(self, initial_value: float):
        """
        Initializes the Property with an initial value.

        :param initial_value: The initial market value of the property.
        """
        if initial_value < 0:
            raise ValueError("Initial property value must be non-negative.")
        self.initial_value = initial_value

    def increase_value(self, solar_system_cost: float, increase_percentage: float):
        """
        Increases the property value based on the installation of a solar autoconsumption system.

        :param solar_system_cost: The cost of the solar system installation.
        :param increase_percentage: The percentage increase in property value due to the installation.
        :return: The new property value after the increase.
        """
        if solar_system_cost < 0:
            raise ValueError("Solar system cost must be non-negative.")
        if not (0 <= increase_percentage <= 100):
            raise ValueError("Increase percentage must be between 0 and 100.")

        # Calculate the increase in property value
        increase_amount = (self.initial_value + solar_system_cost) * (increase_percentage / 100)
        new_value = self.initial_value + increase_amount

        return new_value


def main():
    """
    Main function to demonstrate the property value increase due to solar system installation.
    """
    try:
        # Create a property with an initial value
        property_value = Property(initial_value=300000)  # Example initial value in currency

        # Define solar system cost and expected increase percentage
        solar_system_cost = 15000  # Example cost of solar system
        increase_percentage = 10  # Example percentage increase in property value

        # Calculate the new property value
        new_property_value = property_value.increase_value(solar_system_cost, increase_percentage)

        # Output the results
        print(f"Initial Property Value: ${property_value.initial_value:,.2f}")
        print(f"New Property Value after Solar Installation: ${new_property_value:,.2f}")

    except ValueError as e:
        print(f"Error: {e}")


if __name__ == "__main__":
    main()
```
