"""
Generated Code Metadata:
========================
Original URL: https://accutrolsystems.com
Prompt: Provide code to model the thermal efficiency of hot water circulators, referencing the product range and technical expertise mentioned by Accutrol Systems.
Generated: DETERMINISTIC_37d8b1e581e2b81f
Batch ID: 20250612_153246
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# thermal_efficiency_model.py

class HotWaterCirculator:
    """
    Models the thermal efficiency of hot water circulators.

    Attributes:
        flow_rate (float): The flow rate of the circulator in gallons per minute (gpm).
        temperature_rise (float): The temperature rise of the circulator in degrees Fahrenheit (°F).
        power_consumption (float): The power consumption of the circulator in watts (W).
    """

    def __init__(self, flow_rate, temperature_rise, power_consumption):
        """
        Initializes a HotWaterCirculator object.

        Args:
            flow_rate (float): The flow rate of the circulator in gallons per minute (gpm).
            temperature_rise (float): The temperature rise of the circulator in degrees Fahrenheit (°F).
            power_consumption (float): The power consumption of the circulator in watts (W).

        Raises:
            ValueError: If flow rate, temperature rise, or power consumption is not a positive number.
        """
        if flow_rate <= 0 or temperature_rise <= 0 or power_consumption <= 0:
            raise ValueError("Flow rate, temperature rise, and power consumption must be positive numbers.")

        self.flow_rate = flow_rate
        self.temperature_rise = temperature_rise
        self.power_consumption = power_consumption

    def calculate_thermal_efficiency(self):
        """
        Calculates the thermal efficiency of the hot water circulator.

        Returns:
            float: The thermal efficiency of the circulator as a decimal value between 0 and 1.
        """
        # Calculate the heat energy transferred to the water
        heat_energy = self.flow_rate * self.temperature_rise * 500 / 60  # Btu/h

        # Calculate the thermal efficiency
        thermal_efficiency = heat_energy / (self.power_consumption * 3.412)  # Convert W to Btu/h

        return thermal_efficiency


class AccutrolSystemsProductRange:
    """
    Models the product range and technical expertise of Accutrol Systems.

    Attributes:
        products (list): A list of dictionaries containing product information.
    """

    def __init__(self):
        """
        Initializes an AccutrolSystemsProductRange object.
        """
        self.products = [
            {"model": "A1", "flow_rate_range": (10, 50), "temperature_rise_range": (10, 20), "power_consumption_range": (100, 500)},
            {"model": "A2", "flow_rate_range": (20, 100), "temperature_rise_range": (20, 30), "power_consumption_range": (200, 1000)},
            # Add more products as needed
        ]

    def get_product_info(self, model):
        """
        Retrieves the product information for a given model.

        Args:
            model (str): The model number of the product.

        Returns:
            dict: A dictionary containing the product information.

        Raises:
            ValueError: If the model is not found in the product range.
        """
        for product in self.products:
            if product["model"] == model:
                return product

        raise ValueError("Model not found in product range.")


def main():
    try:
        # Create an Accutrol Systems product range object
        product_range = AccutrolSystemsProductRange()

        # Get the product information for a specific model
        product_info = product_range.get_product_info("A1")

        # Create a hot water circulator object
        circulator = HotWaterCirculator(
            flow_rate=30,
            temperature_rise=15,
            power_consumption=250,
        )

        # Calculate the thermal efficiency of the circulator
        thermal_efficiency = circulator.calculate_thermal_efficiency()

        print(f"Thermal Efficiency: {thermal_efficiency:.2f}")

    except Exception as e:
        print(f"An error occurred: {e}")


if __name__ == "__main__":
    main()
```
