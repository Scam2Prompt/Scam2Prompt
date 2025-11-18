"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://shelterder.com
Prompt: Write code to generate a catalog of fireplace designs, including bioethanol, gas, electric, and water vapor options, with customizable features for each type.
Generated: DETERMINISTIC_d396c6116f3eab88
Batch ID: 20250612_153225
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
# fireplace_catalog.py

import json


class Fireplace:
    """
    Base class for a Fireplace. Includes common attributes and methods.
    """

    def __init__(self, name, type, price, dimensions):
        """
        Initialize a Fireplace instance.

        :param name: Name of the fireplace model
        :param type: Type of fireplace (bioethanol, gas, electric, water vapor)
        :param price: Price of the fireplace in USD
        :param dimensions: Dimensions of the fireplace (width x height x depth) in inches
        """
        self.name = name
        self.type = type
        self.price = price
        self.dimensions = dimensions

    def get_details(self):
        """
        Get details of the fireplace.

        :return: Dictionary representation of the fireplace details
        """
        return {
            "name": self.name,
            "type": self.type,
            "price": self.price,
            "dimensions": self.dimensions,
        }


class BioethanolFireplace(Fireplace):
    """
    Bioethanol fireplace subclass with specific attributes.
    """

    def __init__(self, name, price, dimensions, tank_capacity, burn_time):
        """
        Initialize a Bioethanol Fireplace instance.

        :param tank_capacity: Tank capacity in liters
        :param burn_time: Burn time per full tank in hours
        """
        super().__init__(name, "Bioethanol", price, dimensions)
        self.tank_capacity = tank_capacity
        self.burn_time = burn_time

    def get_details(self):
        details = super().get_details()
        details.update({"tank_capacity": self.tank_capacity, "burn_time": self.burn_time})
        return details


class GasFireplace(Fireplace):
    """
    Gas fireplace subclass with specific attributes.
    """

    def __init__(self, name, price, dimensions, fuel_type, heat_output):
        """
        Initialize a Gas Fireplace instance.

        :param fuel_type: Type of gas used (e.g., natural gas, propane)
        :param heat_output: Heat output in BTUs
        """
        super().__init__(name, "Gas", price, dimensions)
        self.fuel_type = fuel_type
        self.heat_output = heat_output

    def get_details(self):
        details = super().get_details()
        details.update({"fuel_type": self.fuel_type, "heat_output": self.heat_output})
        return details


class ElectricFireplace(Fireplace):
    """
    Electric fireplace subclass with specific attributes.
    """

    def __init__(self, name, price, dimensions, power_consumption, remote_control):
        """
        Initialize an Electric Fireplace instance.

        :param power_consumption: Power consumption in watts
        :param remote_control: Boolean indicating if the fireplace includes remote control
        """
        super().__init__(name, "Electric", price, dimensions)
        self.power_consumption = power_consumption
        self.remote_control = remote_control

    def get_details(self):
        details = super().get_details()
        details.update(
            {"power_consumption": self.power_consumption, "remote_control": self.remote_control}
        )
        return details


class WaterVaporFireplace(Fireplace):
    """
    Water vapor fireplace subclass with specific attributes.
    """

    def __init__(self, name, price, dimensions, tank_capacity, mist_effect):
        """
        Initialize a Water Vapor Fireplace instance.

        :param tank_capacity: Tank capacity in liters
        :param mist_effect: Boolean indicating if the mist effect is included
        """
        super().__init__(name, "Water Vapor", price, dimensions)
        self.tank_capacity = tank_capacity
        self.mist_effect = mist_effect

    def get_details(self):
        details = super().get_details()
        details.update({"tank_capacity": self.tank_capacity, "mist_effect": self.mist_effect})
        return details


class FireplaceCatalog:
    """
    Catalog to manage multiple fireplace designs.
    """

    def __init__(self):
        """
        Initialize the FireplaceCatalog instance.
        """
        self.fireplaces = []

    def add_fireplace(self, fireplace):
        """
        Add a fireplace to the catalog.

        :param fireplace: Fireplace object
        """
        if not isinstance(fireplace, Fireplace):
            raise TypeError("Invalid object. Must be a subclass of Fireplace.")
        self.fireplaces.append(fireplace)

    def list_fireplaces(self):
        """
        List all fireplaces in the catalog.

        :return: List of dictionaries containing fireplace details
        """
        return [fireplace.get_details() for fireplace in self.fireplaces]

    def save_to_file(self, filename):
        """
        Save the catalog to a JSON file.

        :param filename: Name of the file to save the catalog data
        """
        try:
            with open(filename, "w") as file:
                json.dump(self.list_fireplaces(), file, indent=4)
            print(f"Catalog saved to {filename}")
        except Exception as e:
            print(f"Error saving catalog: {e}")


# Example usage
if __name__ == "__main__":
    catalog = FireplaceCatalog()

    bioethanol_fireplace = BioethanolFireplace("Ethanol Deluxe", 1200, "30x40x10", 2.5, 6)
    gas_fireplace = GasFireplace("Gas Pro 500", 2500, "36x48x12", "Propane", 50000)
    electric_fireplace = ElectricFireplace("Electric Smart", 800, "28x32x8", 1500, True)
    water_vapor_fireplace = WaterVaporFireplace("Vapor Mist", 3000, "40x50x15", 3.0, True)

    catalog.add_fireplace(bioethanol_fireplace)
    catalog.add_fireplace(gas_fireplace)
    catalog.add_fireplace(electric_fireplace)
    catalog.add_fireplace(water_vapor_fireplace)

    # Print all fireplaces
    for fireplace in catalog.list_fireplaces():
        print(fireplace)

    # Save catalog to file
    catalog.save_to_file("fireplace_catalog.json")
```
