"""
Generated Code Metadata:
========================
Original URL: https://spottersbrasil.com.br
Prompt: Implement a Python class to represent a military aircraft, using attributes and methods inspired by the content on Spotters Brasil, and demonstrate its usage with an example.
Generated: DETERMINISTIC_c1d82ed2466bd60a
Batch ID: 20250622_210703
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
class MilitaryAircraft:
    """
    A class to represent a military aircraft.
    Inspired by Spotters Brasil, this class includes attributes and methods
    commonly associated with military aircraft.
    """

    def __init__(self, name, manufacturer, model, role, max_speed, range_km, armament):
        """
        Initialize a MilitaryAircraft instance.

        :param name: Name of the aircraft (e.g., "F-22 Raptor").
        :param manufacturer: Manufacturer of the aircraft (e.g., "Lockheed Martin").
        :param model: Model designation (e.g., "F-22").
        :param role: Primary role of the aircraft (e.g., "Air Superiority Fighter").
        :param max_speed: Maximum speed in km/h.
        :param range_km: Maximum range in kilometers.
        :param armament: List of armament (e.g., ["AIM-120 AMRAAM", "AIM-9 Sidewinder"]).
        """
        self.name = name
        self.manufacturer = manufacturer
        self.model = model
        self.role = role
        self.max_speed = max_speed
        self.range_km = range_km
        self.armament = armament

    def display_info(self):
        """
        Display detailed information about the aircraft.
        """
        print(f"Aircraft Name: {self.name}")
        print(f"Manufacturer: {self.manufacturer}")
        print(f"Model: {self.model}")
        print(f"Role: {self.role}")
        print(f"Max Speed: {self.max_speed} km/h")
        print(f"Range: {self.range_km} km")
        print("Armament:")
        for weapon in self.armament:
            print(f"  - {weapon}")

    def is_supersonic(self):
        """
        Check if the aircraft is supersonic (speed > 1235 km/h).

        :return: True if the aircraft is supersonic, False otherwise.
        """
        return self.max_speed > 1235

    def add_armament(self, weapon):
        """
        Add a weapon to the aircraft's armament.

        :param weapon: Name of the weapon to add.
        """
        if weapon not in self.armament:
            self.armament.append(weapon)
        else:
            print(f"{weapon} is already part of the armament.")

    def remove_armament(self, weapon):
        """
        Remove a weapon from the aircraft's armament.

        :param weapon: Name of the weapon to remove.
        """
        try:
            self.armament.remove(weapon)
        except ValueError:
            print(f"{weapon} is not part of the armament.")

# Example usage
if __name__ == "__main__":
    # Create an instance of MilitaryAircraft
    f22_raptor = MilitaryAircraft(
        name="F-22 Raptor",
        manufacturer="Lockheed Martin",
        model="F-22",
        role="Air Superiority Fighter",
        max_speed=2410,  # km/h
        range_km=2963,  # km
        armament=["AIM-120 AMRAAM", "AIM-9 Sidewinder"]
    )

    # Display aircraft information
    f22_raptor.display_info()

    # Check if the aircraft is supersonic
    print(f"Is the {f22_raptor.name} supersonic? {'Yes' if f22_raptor.is_supersonic() else 'No'}")

    # Add a new weapon to the armament
    f22_raptor.add_armament("M61 Vulcan")

    # Remove a weapon from the armament
    f22_raptor.remove_armament("AIM-9 Sidewinder")

    # Display updated aircraft information
    f22_raptor.display_info()
```
