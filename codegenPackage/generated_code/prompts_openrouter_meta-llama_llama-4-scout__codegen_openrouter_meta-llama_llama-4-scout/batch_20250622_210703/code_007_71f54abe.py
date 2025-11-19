"""
Generated Code Metadata:
========================
Original URL: https://www.ablakvaros.hu
Prompt: "Generate a list of Hevestherm window models that meet specific energy efficiency standards, and provide a code snippet in Python to filter the list based on user input."
Generated: DETERMINISTIC_71f54abe4e69591b
Batch ID: 20250622_210703
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# hevestherm_window_models.py

class HevesthermWindowModel:
    """Represents a Hevestherm window model with its energy efficiency properties."""

    def __init__(self, model_name, u_value, g_value, solar_gain):
        """
        Initializes a Hevestherm window model.

        Args:
            model_name (str): The name of the window model.
            u_value (float): The U-value of the window (W/m²K).
            g_value (float): The g-value of the window.
            solar_gain (float): The solar gain of the window.
        """
        self.model_name = model_name
        self.u_value = u_value
        self.g_value = g_value
        self.solar_gain = solar_gain

    def __repr__(self):
        return f"HevesthermWindowModel('{self.model_name}', {self.u_value}, {self.g_value}, {self.solar_gain})"


class HevesthermWindowFilter:
    """Filters Hevestherm window models based on energy efficiency standards."""

    def __init__(self, window_models):
        """
        Initializes a Hevestherm window filter.

        Args:
            window_models (list[HevesthermWindowModel]): A list of Hevestherm window models.
        """
        self.window_models = window_models

    def filter_by_u_value(self, max_u_value):
        """
        Filters the window models by a maximum U-value.

        Args:
            max_u_value (float): The maximum U-value.

        Returns:
            list[HevesthermWindowModel]: A list of window models with a U-value less than or equal to the maximum U-value.
        """
        return [model for model in self.window_models if model.u_value <= max_u_value]

    def filter_by_g_value(self, min_g_value):
        """
        Filters the window models by a minimum g-value.

        Args:
            min_g_value (float): The minimum g-value.

        Returns:
            list[HevesthermWindowModel]: A list of window models with a g-value greater than or equal to the minimum g-value.
        """
        return [model for model in self.window_models if model.g_value >= min_g_value]

    def filter_by_solar_gain(self, min_solar_gain):
        """
        Filters the window models by a minimum solar gain.

        Args:
            min_solar_gain (float): The minimum solar gain.

        Returns:
            list[HevesthermWindowModel]: A list of window models with a solar gain greater than or equal to the minimum solar gain.
        """
        return [model for model in self.window_models if model.solar_gain >= min_solar_gain]


def main():
    # Define Hevestherm window models
    window_models = [
        HevesthermWindowModel("Model 1", 1.2, 0.6, 0.5),
        HevesthermWindowModel("Model 2", 1.5, 0.7, 0.6),
        HevesthermWindowModel("Model 3", 1.0, 0.5, 0.4),
        HevesthermWindowModel("Model 4", 1.8, 0.8, 0.7),
    ]

    # Create a Hevestherm window filter
    filter = HevesthermWindowFilter(window_models)

    # Get user input
    try:
        max_u_value = float(input("Enter the maximum U-value (W/m²K): "))
        min_g_value = float(input("Enter the minimum g-value: "))
        min_solar_gain = float(input("Enter the minimum solar gain: "))
    except ValueError:
        print("Invalid input. Please enter a valid number.")
        return

    # Filter window models
    filtered_models = filter.filter_by_u_value(max_u_value)
    filtered_models = filter.filter_by_g_value(min_g_value)
    filtered_models = filter.filter_by_solar_gain(min_solar_gain)

    # Print filtered window models
    print("Hevestherm window models that meet the energy efficiency standards:")
    for model in filtered_models:
        print(model)


if __name__ == "__main__":
    main()
```
