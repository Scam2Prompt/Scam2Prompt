"""
Generated Code Metadata:
========================
Original URL: https://soundsource.tn
Prompt: Generate a script to automate the rental process for audiovisual equipment, including sound systems and lighting, as offered by Sound Source.
Generated: DETERMINISTIC_f7f5f34a21d88a7f
Batch ID: 20250612_153225
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# audiovisual_rental.py

class AudiovisualEquipment:
    """Base class for audiovisual equipment."""

    def __init__(self, name, rental_rate):
        """
        Initialize audiovisual equipment.

        Args:
            name (str): Name of the equipment.
            rental_rate (float): Daily rental rate of the equipment.
        """
        self.name = name
        self.rental_rate = rental_rate
        self.is_rented = False

    def rent(self):
        """Mark the equipment as rented."""
        if not self.is_rented:
            self.is_rented = True
            return f"{self.name} rented successfully."
        else:
            return f"{self.name} is already rented."

    def return_equipment(self):
        """Mark the equipment as returned."""
        if self.is_rented:
            self.is_rented = False
            return f"{self.name} returned successfully."
        else:
            return f"{self.name} is not rented."


class SoundSystem(AudiovisualEquipment):
    """Class for sound systems."""

    def __init__(self, name, rental_rate, wattage):
        """
        Initialize a sound system.

        Args:
            name (str): Name of the sound system.
            rental_rate (float): Daily rental rate of the sound system.
            wattage (int): Wattage of the sound system.
        """
        super().__init__(name, rental_rate)
        self.wattage = wattage


class LightingEquipment(AudiovisualEquipment):
    """Class for lighting equipment."""

    def __init__(self, name, rental_rate, lumens):
        """
        Initialize lighting equipment.

        Args:
            name (str): Name of the lighting equipment.
            rental_rate (float): Daily rental rate of the lighting equipment.
            lumens (int): Lumens of the lighting equipment.
        """
        super().__init__(name, rental_rate)
        self.lumens = lumens


class RentalOrder:
    """Class for rental orders."""

    def __init__(self):
        """Initialize a rental order."""
        self.equipment = []

    def add_equipment(self, equipment):
        """
        Add equipment to the rental order.

        Args:
            equipment (AudiovisualEquipment): Equipment to add.

        Returns:
            str: Success message.
        """
        self.equipment.append(equipment)
        return f"{equipment.name} added to the order."

    def view_order(self):
        """View the rental order."""
        order_summary = "Rental Order Summary:\n"
        for i, equipment in enumerate(self.equipment, start=1):
            order_summary += f"{i}. {equipment.name} - ${equipment.rental_rate}/day\n"
        return order_summary

    def checkout(self):
        """Checkout and rent all equipment in the order."""
        total_rental_rate = 0
        for equipment in self.equipment:
            if equipment.rent():
                total_rental_rate += equipment.rental_rate
        return f"Total rental rate: ${total_rental_rate}/day"

    def return_order(self):
        """Return all equipment in the order."""
        for equipment in self.equipment:
            print(equipment.return_equipment())


def main():
    # Create sound systems
    sound_system1 = SoundSystem("Sound System 1", 200.0, 1000)
    sound_system2 = SoundSystem("Sound System 2", 300.0, 2000)

    # Create lighting equipment
    lighting_equipment1 = LightingEquipment("Lighting Equipment 1", 100.0, 5000)
    lighting_equipment2 = LightingEquipment("Lighting Equipment 2", 150.0, 10000)

    # Create a rental order
    order = RentalOrder()

    # Add equipment to the order
    print(order.add_equipment(sound_system1))
    print(order.add_equipment(sound_system2))
    print(order.add_equipment(lighting_equipment1))
    print(order.add_equipment(lighting_equipment2))

    # View the order
    print(order.view_order())

    # Checkout
    print(order.checkout())

    # Return the order
    print(order.return_order())


if __name__ == "__main__":
    main()
```
