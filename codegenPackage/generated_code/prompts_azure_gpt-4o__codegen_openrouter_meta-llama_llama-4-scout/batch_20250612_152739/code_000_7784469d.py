"""
Generated Code Metadata:
========================
Original URL: https://dmsauto4x4.ro
Prompt: Write Python code to create a configurator for off-road tires and rims, referencing brands like BF Goodrich, Atturo, and ITP as listed on DMS Auto4x4's website.
Generated: DETERMINISTIC_7784469db7c07844
Batch ID: 20250612_152739
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# offroad_configurator.py

class OffRoadTire:
    def __init__(self, brand, model, size, price):
        """
        Initialize an OffRoadTire object.

        Args:
            brand (str): The brand of the tire.
            model (str): The model of the tire.
            size (str): The size of the tire.
            price (float): The price of the tire.
        """
        self.brand = brand
        self.model = model
        self.size = size
        self.price = price

    def __str__(self):
        return f"{self.brand} {self.model} - {self.size} - ${self.price:.2f}"


class OffRoadRim:
    def __init__(self, brand, model, size, bolt_pattern, price):
        """
        Initialize an OffRoadRim object.

        Args:
            brand (str): The brand of the rim.
            model (str): The model of the rim.
            size (str): The size of the rim.
            bolt_pattern (str): The bolt pattern of the rim.
            price (float): The price of the rim.
        """
        self.brand = brand
        self.model = model
        self.size = size
        self.bolt_pattern = bolt_pattern
        self.price = price

    def __str__(self):
        return f"{self.brand} {self.model} - {self.size} - {self.bolt_pattern} - ${self.price:.2f}"


class OffRoadConfigurator:
    def __init__(self):
        """
        Initialize an OffRoadConfigurator object.
        """
        self.tires = []
        self.rims = []

    def add_tire(self, tire):
        """
        Add a tire to the configurator.

        Args:
            tire (OffRoadTire): The tire to add.
        """
        self.tires.append(tire)

    def add_rim(self, rim):
        """
        Add a rim to the configurator.

        Args:
            rim (OffRoadRim): The rim to add.
        """
        self.rims.append(rim)

    def get_tire_options(self):
        """
        Get a list of available tire options.

        Returns:
            list[OffRoadTire]: A list of available tire options.
        """
        return self.tires

    def get_rim_options(self):
        """
        Get a list of available rim options.

        Returns:
            list[OffRoadRim]: A list of available rim options.
        """
        return self.rims

    def configure(self, tire_size, rim_size, bolt_pattern):
        """
        Configure an off-road tire and rim combination.

        Args:
            tire_size (str): The size of the tire.
            rim_size (str): The size of the rim.
            bolt_pattern (str): The bolt pattern of the rim.

        Returns:
            tuple[OffRoadTire, OffRoadRim]: A tuple containing the configured tire and rim.
        """
        tire_options = [tire for tire in self.tires if tire.size == tire_size]
        rim_options = [rim for rim in self.rims if rim.size == rim_size and rim.bolt_pattern == bolt_pattern]

        if not tire_options:
            raise ValueError(f"No tire options available in size {tire_size}")
        if not rim_options:
            raise ValueError(f"No rim options available in size {rim_size} with bolt pattern {bolt_pattern}")

        return tire_options[0], rim_options[0]


def main():
    configurator = OffRoadConfigurator()

    # Add tires
    configurator.add_tire(OffRoadTire("BF Goodrich", "Mud-Terrain T/A KM3", "33x12.5R17", 150.00))
    configurator.add_tire(OffRoadTire("Atturo", "Trail Blade M/T", "33x12.5R17", 120.00))
    configurator.add_tire(OffRoadTire("ITP", "Black Thunder", "33x12.5R17", 180.00))

    # Add rims
    configurator.add_rim(OffRoadRim("BF Goodrich", "17x9-inch Aluminum Wheel", "17x9", "5x5", 200.00))
    configurator.add_rim(OffRoadRim("Atturo", "17x9-inch Steel Wheel", "17x9", "5x5", 150.00))
    configurator.add_rim(OffRoadRim("ITP", "17x9-inch Aluminum Wheel", "17x9", "5x5", 250.00))

    # Configure a tire and rim combination
    try:
        tire, rim = configurator.configure("33x12.5R17", "17x9", "5x5")
        print("Configured Tire:")
        print(tire)
        print("Configured Rim:")
        print(rim)
    except ValueError as e:
        print(f"Error: {e}")


if __name__ == "__main__":
    main()
```
