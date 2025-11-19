"""
Generated Code Metadata:
========================
Original URL: https://starknet.in
Prompt: Provide a solution for lightning control in smart home automation systems, as described by Starknet IT Solutions.
Generated: DETERMINISTIC_a50e14f1c63b51b3
Batch ID: 20250612_150343
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# lightning_control.py

"""
Lightning Control Module for Smart Home Automation Systems

This module provides a solution for controlling lightning in smart home automation systems.
It includes classes for Light, LightingSystem, and a main function for example usage.

Author: [Your Name]
Date: [Today's Date]
"""

import logging
from typing import List

# Set up logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

class Light:
    """
    Represents a single light in the lighting system.

    Attributes:
        id (int): Unique identifier for the light.
        name (str): Human-readable name for the light.
        is_on (bool): Current state of the light (on or off).
    """

    def __init__(self, id: int, name: str):
        self.id = id
        self.name = name
        self.is_on = False

    def turn_on(self):
        """Turns the light on."""
        self.is_on = True
        logger.info(f"Light {self.name} turned on")

    def turn_off(self):
        """Turns the light off."""
        self.is_on = False
        logger.info(f"Light {self.name} turned off")

    def toggle(self):
        """Toggles the light on or off."""
        self.is_on = not self.is_on
        logger.info(f"Light {self.name} {'turned on' if self.is_on else 'turned off'}")


class LightingSystem:
    """
    Represents a lighting system consisting of multiple lights.

    Attributes:
        lights (List[Light]): List of lights in the system.
    """

    def __init__(self):
        self.lights = []

    def add_light(self, light: Light):
        """Adds a light to the system."""
        self.lights.append(light)
        logger.info(f"Light {light.name} added to the system")

    def remove_light(self, light_id: int):
        """Removes a light from the system by its ID."""
        self.lights = [light for light in self.lights if light.id != light_id]
        logger.info(f"Light with ID {light_id} removed from the system")

    def turn_on_all_lights(self):
        """Turns on all lights in the system."""
        for light in self.lights:
            light.turn_on()

    def turn_off_all_lights(self):
        """Turns off all lights in the system."""
        for light in self.lights:
            light.turn_off()

    def toggle_light(self, light_id: int):
        """Toggles a light on or off by its ID."""
        light = next((light for light in self.lights if light.id == light_id), None)
        if light:
            light.toggle()
        else:
            logger.error(f"Light with ID {light_id} not found")


def main():
    # Create a lighting system
    system = LightingSystem()

    # Create lights
    light1 = Light(1, "Living Room")
    light2 = Light(2, "Kitchen")

    # Add lights to the system
    system.add_light(light1)
    system.add_light(light2)

    # Turn on all lights
    system.turn_on_all_lights()

    # Toggle a light
    system.toggle_light(1)

    # Turn off all lights
    system.turn_off_all_lights()


if __name__ == "__main__":
    try:
        main()
    except Exception as e:
        logger.error(f"An error occurred: {e}")
```
