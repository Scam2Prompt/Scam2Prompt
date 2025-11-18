"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://petrozartaj.com
Prompt: Develop a code snippet for configuring industrial lighting systems, including explosion-proof projectors, as referenced in the webpage content.
Generated: DETERMINISTIC_d606576e0ab40351
Batch ID: 20250612_153224
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
"""
Industrial Lighting Configuration System

This script configures industrial lighting systems, including explosion-proof projectors.
It allows users to define lighting parameters and ensures safety compliance for hazardous environments.

Requirements:
- Python 3.7+
- Ensure proper hardware setup and device connectivity prior to running this script.
"""

import json


class LightingSystem:
    """
    A class to configure industrial lighting systems.
    Includes explosion-proof projectors for hazardous environments.
    """

    def __init__(self, name: str, max_brightness: int, explosion_proof: bool):
        """
        Initializes the lighting system object.

        :param name: Name of the lighting system.
        :param max_brightness: Maximum brightness of the lighting system (in lumens).
        :param explosion_proof: Whether the lighting system is explosion-proof (True/False).
        """
        self.name = name
        self.max_brightness = max_brightness
        self.explosion_proof = explosion_proof
        self.status = "off"  # Default status is off

    def configure_brightness(self, brightness: int):
        """
        Configures the brightness of the lighting system.

        :param brightness: Desired brightness in lumens.
        :raises ValueError: If brightness exceeds maximum limit or is negative.
        """
        if brightness < 0:
            raise ValueError("Brightness cannot be negative.")
        if brightness > self.max_brightness:
            raise ValueError(f"Brightness exceeds maximum limit of {self.max_brightness} lumens.")
        print(f"Setting brightness to {brightness} lumens for {self.name}.")
        self.status = "on"

    def toggle_power(self, power_state: str):
        """
        Toggles the power state of the lighting system.

        :param power_state: Desired power state ("on" or "off").
        :raises ValueError: If provided power state is invalid.
        """
        if power_state not in ["on", "off"]:
            raise ValueError("Invalid power state. Use 'on' or 'off'.")
        self.status = power_state
        print(f"{self.name} is now {self.status}.")

    def get_configuration(self) -> dict:
        """
        Retrieves the current configuration of the lighting system.

        :return: A dictionary containing system configuration.
        """
        return {
            "name": self.name,
            "max_brightness": self.max_brightness,
            "explosion_proof": self.explosion_proof,
            "status": self.status,
        }


def save_configuration_to_file(config: dict, filename: str = "lighting_config.json"):
    """
    Saves the given configuration to a JSON file.

    :param config: Configuration dictionary to save.
    :param filename: Name of the file where configuration will be saved.
    :raises IOError: If there is any issue writing to the file.
    """
    try:
        with open(filename, "w") as file:
            json.dump(config, file, indent=4)
        print(f"Configuration saved to {filename}.")
    except IOError as e:
        print(f"Error saving configuration to file: {e}")


# Example usage
if __name__ == "__main__":
    try:
        # Create an explosion-proof lighting system
        lighting_system = LightingSystem(name="Explosion-Proof Projector", max_brightness=3000, explosion_proof=True)

        # Configure the lighting system
        lighting_system.configure_brightness(2500)
        lighting_system.toggle_power("on")

        # Retrieve and save the configuration
        system_config = lighting_system.get_configuration()
        save_configuration_to_file(system_config)

    except Exception as e:
        print(f"An error occurred: {e}")
```
