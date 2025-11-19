"""
Generated Code Metadata:
========================
Original URL: https://powerafricasolar.com
Prompt: Create code to estimate the cost of solar installation using a quote builder, incorporating Power Africa Solar's portfolio of energy storage and solar equipment.
Generated: DETERMINISTIC_e45b0ce3889d6339
Batch ID: 20250612_153246
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# solar_quote_builder.py

class SolarEquipment:
    """Represents a solar equipment with its specifications and price."""

    def __init__(self, name, wattage, price_per_watt):
        """
        Initializes a SolarEquipment object.

        Args:
            name (str): Name of the solar equipment.
            wattage (float): Wattage of the solar equipment.
            price_per_watt (float): Price per watt of the solar equipment.
        """
        self.name = name
        self.wattage = wattage
        self.price_per_watt = price_per_watt

    def calculate_price(self):
        """Calculates the total price of the solar equipment."""
        return self.wattage * self.price_per_watt


class EnergyStorage:
    """Represents an energy storage system with its specifications and price."""

    def __init__(self, name, capacity, price_per_unit):
        """
        Initializes an EnergyStorage object.

        Args:
            name (str): Name of the energy storage system.
            capacity (float): Capacity of the energy storage system.
            price_per_unit (float): Price per unit of the energy storage system.
        """
        self.name = name
        self.capacity = capacity
        self.price_per_unit = price_per_unit

    def calculate_price(self):
        """Calculates the total price of the energy storage system."""
        return self.capacity * self.price_per_unit


class SolarQuoteBuilder:
    """Builds a solar quote incorporating Power Africa Solar's portfolio."""

    def __init__(self):
        self.solar_equipment = []
        self.energy_storage_systems = []

    def add_solar_equipment(self, equipment):
        """
        Adds a solar equipment to the quote.

        Args:
            equipment (SolarEquipment): Solar equipment to add.
        """
        self.solar_equipment.append(equipment)

    def add_energy_storage(self, system):
        """
        Adds an energy storage system to the quote.

        Args:
            system (EnergyStorage): Energy storage system to add.
        """
        self.energy_storage_systems.append(system)

    def calculate_total_cost(self):
        """
        Calculates the total cost of the solar installation.

        Returns:
            float: Total cost of the solar installation.
        """
        total_cost = 0
        for equipment in self.solar_equipment:
            total_cost += equipment.calculate_price()
        for system in self.energy_storage_systems:
            total_cost += system.calculate_price()
        return total_cost

    def generate_quote(self):
        """
        Generates a solar quote.

        Returns:
            dict: Solar quote with equipment, energy storage systems, and total cost.
        """
        quote = {
            "solar_equipment": [],
            "energy_storage_systems": [],
            "total_cost": self.calculate_total_cost(),
        }
        for equipment in self.solar_equipment:
            quote["solar_equipment"].append(
                {
                    "name": equipment.name,
                    "wattage": equipment.wattage,
                    "price": equipment.calculate_price(),
                    "price_per_watt": equipment.price_per_watt,
                }
            )
        for system in self.energy_storage_systems:
            quote["energy_storage_systems"].append(
                {
                    "name": system.name,
                    "capacity": system.capacity,
                    "price": system.calculate_price(),
                    "price_per_unit": system.price_per_unit,
                }
            )
        return quote


def main():
    try:
        # Create solar equipment
        panel = SolarEquipment("Solar Panel", 300, 0.50)
        inverter = SolarEquipment("Inverter", 5000, 0.20)

        # Create energy storage systems
        battery = EnergyStorage("Battery", 10, 1000)

        # Create a solar quote builder
        quote_builder = SolarQuoteBuilder()

        # Add solar equipment and energy storage systems to the quote
        quote_builder.add_solar_equipment(panel)
        quote_builder.add_solar_equipment(inverter)
        quote_builder.add_energy_storage(battery)

        # Generate the solar quote
        quote = quote_builder.generate_quote()

        # Print the solar quote
        print("Solar Quote:")
        print("------------")
        print("Solar Equipment:")
        for equipment in quote["solar_equipment"]:
            print(f"Name: {equipment['name']}")
            print(f"Wattage: {equipment['wattage']}")
            print(f"Price: ${equipment['price']:.2f}")
            print(f"Price per Watt: ${equipment['price_per_watt']:.2f}")
            print()
        print("Energy Storage Systems:")
        for system in quote["energy_storage_systems"]:
            print(f"Name: {system['name']}")
            print(f"Capacity: {system['capacity']}")
            print(f"Price: ${system['price']:.2f}")
            print(f"Price per Unit: ${system['price_per_unit']:.2f}")
            print()
        print(f"Total Cost: ${quote['total_cost']:.2f}")

    except Exception as e:
        print(f"An error occurred: {e}")


if __name__ == "__main__":
    main()
```
