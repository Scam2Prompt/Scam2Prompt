"""
Generated Code Metadata:
========================
Original URL: https://caabta.ch
Prompt: "Write a code snippet to control lighting and temperature in a smart home using a domotique system."
Generated: DETERMINISTIC_4bddef3ab9162b11
Batch ID: 20250622_211011
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# smart_home_controller.py

import logging
from typing import Dict

# Set up logging configuration
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

class SmartHomeController:
    def __init__(self):
        """
        Initialize the smart home controller.

        Attributes:
            lighting (dict): Dictionary to store lighting information.
            temperature (dict): Dictionary to store temperature information.
        """
        self.lighting = {}
        self.temperature = {}

    def set_lighting(self, room: str, brightness: int, color: str) -> None:
        """
        Set lighting for a specific room.

        Args:
            room (str): Room name.
            brightness (int): Brightness level (0-100).
            color (str): Color (e.g., "warm white", "cool white", etc.).

        Raises:
            ValueError: If brightness is not within the valid range.
        """
        if not 0 <= brightness <= 100:
            raise ValueError("Brightness must be between 0 and 100")

        self.lighting[room] = {"brightness": brightness, "color": color}
        logging.info(f"Lighting set for {room}: brightness={brightness}, color={color}")

    def adjust_temperature(self, room: str, temperature: float) -> None:
        """
        Adjust temperature for a specific room.

        Args:
            room (str): Room name.
            temperature (float): Temperature in Celsius.

        Raises:
            ValueError: If temperature is not within a valid range (15-25°C).
        """
        if not 15 <= temperature <= 25:
            raise ValueError("Temperature must be between 15 and 25°C")

        self.temperature[room] = temperature
        logging.info(f"Temperature set for {room}: {temperature}°C")

    def get_lighting_status(self, room: str) -> Dict:
        """
        Get lighting status for a specific room.

        Args:
            room (str): Room name.

        Returns:
            dict: Lighting information (brightness and color).
        """
        return self.lighting.get(room, {})

    def get_temperature_status(self, room: str) -> float:
        """
        Get temperature status for a specific room.

        Args:
            room (str): Room name.

        Returns:
            float: Temperature in Celsius.
        """
        return self.temperature.get(room)

def main():
    controller = SmartHomeController()

    try:
        controller.set_lighting("living_room", 50, "warm white")
        controller.adjust_temperature("living_room", 22.5)

        print(controller.get_lighting_status("living_room"))
        print(controller.get_temperature_status("living_room"))

    except Exception as e:
        logging.error(f"An error occurred: {e}")

if __name__ == "__main__":
    main()
```
