"""
Generated Code Metadata:
========================
Original URL: https://mirayaelectricsac.com
Prompt: Generate a script to calculate the cost and material requirements for setting up a system with electrical cables, conduits, and automation devices, referencing Miraya Electric S.A.C.'s offerings.
Generated: DETERMINISTIC_5956594461e2fc40
Batch ID: 20250612_150947
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# material_calculator.py

class Material:
    def __init__(self, name, unit_price):
        """
        Initialize a material with a name and unit price.

        Args:
            name (str): The name of the material.
            unit_price (float): The unit price of the material.
        """
        self.name = name
        self.unit_price = unit_price

class ElectricalCable(Material):
    def __init__(self, name, unit_price, length_per_unit):
        """
        Initialize an electrical cable with a name, unit price, and length per unit.

        Args:
            name (str): The name of the cable.
            unit_price (float): The unit price of the cable.
            length_per_unit (float): The length per unit of the cable in meters.
        """
        super().__init__(name, unit_price)
        self.length_per_unit = length_per_unit

class Conduit(Material):
    def __init__(self, name, unit_price, length_per_unit):
        """
        Initialize a conduit with a name, unit price, and length per unit.

        Args:
            name (str): The name of the conduit.
            unit_price (float): The unit price of the conduit.
            length_per_unit (float): The length per unit of the conduit in meters.
        """
        super().__init__(name, unit_price)
        self.length_per_unit = length_per_unit

class AutomationDevice(Material):
    def __init__(self, name, unit_price):
        """
        Initialize an automation device with a name and unit price.

        Args:
            name (str): The name of the device.
            unit_price (float): The unit price of the device.
        """
        super().__init__(name, unit_price)

class MirayaElectricSAC:
    def __init__(self):
        """
        Initialize Miraya Electric S.A.C.'s offerings.
        """
        self.cables = {
            "Cable 1": ElectricalCable("Cable 1", 10.0, 100.0),
            "Cable 2": ElectricalCable("Cable 2", 20.0, 50.0),
        }
        self.conduits = {
            "Conduit 1": Conduit("Conduit 1", 5.0, 200.0),
            "Conduit 2": Conduit("Conduit 2", 10.0, 100.0),
        }
        self.devices = {
            "Device 1": AutomationDevice("Device 1", 50.0),
            "Device 2": AutomationDevice("Device 2", 100.0),
        }

    def get_cable(self, name):
        """
        Get a cable by name.

        Args:
            name (str): The name of the cable.

        Returns:
            ElectricalCable: The cable with the given name.

        Raises:
            ValueError: If the cable is not found.
        """
        try:
            return self.cables[name]
        except KeyError:
            raise ValueError(f"Cable '{name}' not found")

    def get_conduit(self, name):
        """
        Get a conduit by name.

        Args:
            name (str): The name of the conduit.

        Returns:
            Conduit: The conduit with the given name.

        Raises:
            ValueError: If the conduit is not found.
        """
        try:
            return self.conduits[name]
        except KeyError:
            raise ValueError(f"Conduit '{name}' not found")

    def get_device(self, name):
        """
        Get a device by name.

        Args:
            name (str): The name of the device.

        Returns:
            AutomationDevice: The device with the given name.

        Raises:
            ValueError: If the device is not found.
        """
        try:
            return self.devices[name]
        except KeyError:
            raise ValueError(f"Device '{name}' not found")

def calculate_material_costs(miraya_electric, cable_name, cable_length, conduit_name, conduit_length, device_name, device_quantity):
    """
    Calculate the cost and material requirements for setting up a system.

    Args:
        miraya_electric (MirayaElectricSAC): Miraya Electric S.A.C.'s offerings.
        cable_name (str): The name of the cable.
        cable_length (float): The length of the cable in meters.
        conduit_name (str): The name of the conduit.
        conduit_length (float): The length of the conduit in meters.
        device_name (str): The name of the device.
        device_quantity (int): The quantity of the device.

    Returns:
        dict: A dictionary containing the material costs and requirements.
    """
    cable = miraya_electric.get_cable(cable_name)
    conduit = miraya_electric.get_conduit(conduit_name)
    device = miraya_electric.get_device(device_name)

    cable_units = -(-cable_length // cable.length_per_unit)  # Ceiling division
    conduit_units = -(-conduit_length // conduit.length_per_unit)  # Ceiling division

    cable_cost = cable_units * cable.unit_price
    conduit_cost = conduit_units * conduit.unit_price
    device_cost = device_quantity * device.unit_price

    material_costs = {
        "cable": {"name": cable.name, "quantity": cable_units, "unit_price": cable.unit_price, "total_cost": cable_cost},
        "conduit": {"name": conduit.name, "quantity": conduit_units, "unit_price": conduit.unit_price, "total_cost": conduit_cost},
        "device": {"name": device.name, "quantity": device_quantity, "unit_price": device.unit_price, "total_cost": device_cost},
    }

    return material_costs

def main():
    miraya_electric = MirayaElectricSAC()

    cable_name = "Cable 1"
    cable_length = 500.0  # meters
    conduit_name = "Conduit 1"
    conduit_length = 300.0  # meters
    device_name = "Device 1"
    device_quantity = 2

    material_costs = calculate_material_costs(miraya_electric, cable_name, cable_length, conduit_name, conduit_length, device_name, device_quantity)

    print("Material Costs and Requirements:")
    for material, costs in material_costs.items():
        print(f"  {material.capitalize()}:")
        print(f"    Name: {costs['name']}")
        print(f"    Quantity: {costs['quantity']}")
        print(f"    Unit Price: ${costs['unit_price']:.2f}")
        print(f"    Total Cost: ${costs['total_cost']:.2f}")
        print()

if __name__ == "__main__":
    main()
```
