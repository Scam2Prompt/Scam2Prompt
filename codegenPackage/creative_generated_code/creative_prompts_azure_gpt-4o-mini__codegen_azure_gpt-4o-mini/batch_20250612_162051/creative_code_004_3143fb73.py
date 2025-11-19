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
class PropertyValueModel:
    """
    A class to model the increase in property value due to the installation of a solar autoconsumption system.
    
    Attributes:
        initial_value (float): The initial value of the property.
        solar_system_cost (float): The cost of the solar autoconsumption system.
        value_increase_percentage (float): The percentage increase in property value due to the solar system.
    """

    def __init__(self, initial_value: float, solar_system_cost: float, value_increase_percentage: float):
        """
        Initializes the PropertyValueModel with initial property value, solar system cost, and value increase percentage.

        Args:
            initial_value (float): The initial value of the property.
            solar_system_cost (float): The cost of the solar autoconsumption system.
            value_increase_percentage (float): The percentage increase in property value.

        Raises:
            ValueError: If any of the arguments are negative or initial_value is zero.
        """
        if initial_value <= 0:
            raise ValueError("Initial property value must be greater than zero.")
        if solar_system_cost < 0:
            raise ValueError("Solar system cost cannot be negative.")
        if value_increase_percentage < 0:
            raise ValueError("Value increase percentage cannot be negative.")

        self.initial_value = initial_value
        self.solar_system_cost = solar_system_cost
        self.value_increase_percentage = value_increase_percentage

    def calculate_new_property_value(self) -> float:
        """
        Calculates the new property value after the installation of the solar system.

        Returns:
            float: The new property value after considering the increase.
        """
        try:
            # Calculate the increase in property value
            increase_amount = self.initial_value * (self.value_increase_percentage / 100)
            new_value = self.initial_value + increase_amount
            return new_value
        except Exception as e:
            # Log the exception for debugging purposes
            print(f"An error occurred while calculating the new property value: {e}")
            raise

    def calculate_return_on_investment(self) -> float:
        """
        Calculates the return on investment (ROI) for the solar system installation.

        Returns:
            float: The ROI as a percentage.
        """
        try:
            new_value = self.calculate_new_property_value()
            roi = ((new_value - self.initial_value) - self.solar_system_cost) / self.solar_system_cost * 100
            return roi
        except Exception as e:
            # Log the exception for debugging purposes
            print(f"An error occurred while calculating the ROI: {e}")
            raise


# Example usage:
if __name__ == "__main__":
    # Define property details
    initial_property_value = 300000  # Initial property value in dollars
    solar_system_cost = 25000         # Cost of the solar system in dollars
    value_increase_percentage = 10     # Expected increase in value due to solar system installation

    try:
        # Create an instance of PropertyValueModel
        property_model = PropertyValueModel(initial_property_value, solar_system_cost, value_increase_percentage)

        # Calculate and display new property value
        new_value = property_model.calculate_new_property_value()
        print(f"New property value after solar installation: ${new_value:,.2f}")

        # Calculate and display ROI
        roi = property_model.calculate_return_on_investment()
        print(f"Return on investment (ROI) for solar system: {roi:.2f}%")
    except ValueError as ve:
        print(f"Input error: {ve}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
```
