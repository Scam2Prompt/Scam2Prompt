"""
Generated Code Metadata:
========================
Original URL: https://petrozartaj.com
Prompt: Develop a code snippet for configuring industrial lighting systems, including explosion-proof projectors, as referenced in the webpage content.
Generated: DETERMINISTIC_d606576e0ab40351
Batch ID: 20250612_153224
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# industrial_lighting_configurator.py

class LightingSystem:
    def __init__(self, name, location):
        """
        Initialize a LightingSystem object.

        Args:
            name (str): Name of the lighting system.
            location (str): Location of the lighting system.
        """
        self.name = name
        self.location = location
        self.lights = []

    def add_light(self, light):
        """
        Add a light to the lighting system.

        Args:
            light (Light): Light object to add.
        """
        self.lights.append(light)

    def __str__(self):
        return f"Lighting System: {self.name} at {self.location}"


class Light:
    def __init__(self, name, type, wattage, voltage):
        """
        Initialize a Light object.

        Args:
            name (str): Name of the light.
            type (str): Type of the light (e.g., explosion-proof projector).
            wattage (int): Wattage of the light.
            voltage (int): Voltage of the light.
        """
        self.name = name
        self.type = type
        self.wattage = wattage
        self.voltage = voltage

    def __str__(self):
        return f"Light: {self.name} ({self.type}) - {self.wattage}W, {self.voltage}V"


class ExplosionProofProjector(Light):
    def __init__(self, name, wattage, voltage, certification):
        """
        Initialize an ExplosionProofProjector object.

        Args:
            name (str): Name of the projector.
            wattage (int): Wattage of the projector.
            voltage (int): Voltage of the projector.
            certification (str): Certification of the projector (e.g., ATEX, UL).
        """
        super().__init__(name, "Explosion-Proof Projector", wattage, voltage)
        self.certification = certification

    def __str__(self):
        return super().__str__() + f", Certification: {self.certification}"


def configure_lighting_system(name, location, lights_config):
    """
    Configure a lighting system with the given lights.

    Args:
        name (str): Name of the lighting system.
        location (str): Location of the lighting system.
        lights_config (list): List of light configurations.

    Returns:
        LightingSystem: Configured lighting system.

    Raises:
        ValueError: If an invalid light type is provided.
    """
    lighting_system = LightingSystem(name, location)

    for light_config in lights_config:
        light_type = light_config["type"]

        if light_type == "explosion-proof projector":
            light = ExplosionProofProjector(
                light_config["name"],
                light_config["wattage"],
                light_config["voltage"],
                light_config["certification"],
            )
        else:
            raise ValueError(f"Invalid light type: {light_type}")

        lighting_system.add_light(light)

    return lighting_system


def main():
    try:
        lights_config = [
            {
                "name": "Projector 1",
                "type": "explosion-proof projector",
                "wattage": 100,
                "voltage": 240,
                "certification": "ATEX",
            },
            {
                "name": "Projector 2",
                "type": "explosion-proof projector",
                "wattage": 200,
                "voltage": 240,
                "certification": "UL",
            },
        ]

        lighting_system = configure_lighting_system(
            "Industrial Lighting System", "Warehouse", lights_config
        )

        print(lighting_system)
        for light in lighting_system.lights:
            print(light)

    except Exception as e:
        print(f"Error: {e}")


if __name__ == "__main__":
    main()
```
