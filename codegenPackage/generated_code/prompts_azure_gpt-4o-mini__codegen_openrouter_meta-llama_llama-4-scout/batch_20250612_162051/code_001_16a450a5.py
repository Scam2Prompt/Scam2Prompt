"""
Generated Code Metadata:
========================
Original URL: https://dolphiniran.com
Prompt: Generate a Python script that simulates the functionality of a smart home system, allowing remote control of bathroom accessories like the "آینه ضد بخار" from Dolphin Iran.
Generated: DETERMINISTIC_16a450a51d1a679d
Batch ID: 20250612_162051
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# smart_home_system.py

class BathroomAccessory:
    """Base class for bathroom accessories."""

    def __init__(self, name):
        """
        Initialize a bathroom accessory.

        Args:
            name (str): The name of the accessory.
        """
        self.name = name
        self.is_on = False

    def turn_on(self):
        """Turn on the accessory."""
        self.is_on = True
        print(f"{self.name} is on.")

    def turn_off(self):
        """Turn off the accessory."""
        self.is_on = False
        print(f"{self.name} is off.")


class AntiFogMirror(BathroomAccessory):
    """Simulate the 'آینه ضد بخار' from Dolphin Iran."""

    def __init__(self, name):
        """
        Initialize the anti-fog mirror.

        Args:
            name (str): The name of the mirror.
        """
        super().__init__(name)

    def defog(self):
        """Defog the mirror."""
        if self.is_on:
            print(f"{self.name} is defogging.")
        else:
            print(f"{self.name} is off. Please turn it on to defog.")


class SmartHomeSystem:
    """Simulate a smart home system."""

    def __init__(self):
        """Initialize the smart home system."""
        self.accessories = {}

    def add_accessory(self, accessory):
        """
        Add a bathroom accessory to the system.

        Args:
            accessory (BathroomAccessory): The accessory to add.
        """
        self.accessories[accessory.name] = accessory

    def remove_accessory(self, name):
        """
        Remove a bathroom accessory from the system.

        Args:
            name (str): The name of the accessory to remove.

        Raises:
            KeyError: If the accessory is not found.
        """
        if name in self.accessories:
            del self.accessories[name]
        else:
            raise KeyError(f"Accessory '{name}' not found.")

    def control_accessory(self, name, action):
        """
        Control a bathroom accessory.

        Args:
            name (str): The name of the accessory to control.
            action (str): The action to perform (e.g., 'turn_on', 'turn_off', 'defog').

        Raises:
            KeyError: If the accessory is not found.
            ValueError: If the action is invalid.
        """
        if name in self.accessories:
            accessory = self.accessories[name]
            if action == "turn_on":
                accessory.turn_on()
            elif action == "turn_off":
                accessory.turn_off()
            elif action == "defog" and isinstance(accessory, AntiFogMirror):
                accessory.defog()
            else:
                raise ValueError(f"Invalid action '{action}' for accessory '{name}'.")
        else:
            raise KeyError(f"Accessory '{name}' not found.")


def main():
    # Create a smart home system
    system = SmartHomeSystem()

    # Create bathroom accessories
    mirror = AntiFogMirror("آینه ضد بخار")

    # Add accessories to the system
    system.add_accessory(mirror)

    try:
        # Control accessories
        system.control_accessory("آینه ضد بخار", "turn_on")
        system.control_accessory("آینه ضد بخار", "defog")
        system.control_accessory("آینه ضد بخار", "turn_off")
    except (KeyError, ValueError) as e:
        print(f"Error: {e}")


if __name__ == "__main__":
    main()
```
