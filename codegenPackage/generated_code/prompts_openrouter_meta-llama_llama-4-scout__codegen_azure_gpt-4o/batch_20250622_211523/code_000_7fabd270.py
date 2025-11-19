"""
Generated Code Metadata:
========================
Original URL: https://blackpanttthers.com
Prompt: "Write a Python script to automate smart home lighting using adaptive sensors and voice commands, considering energy efficiency and user preferences."
Generated: DETERMINISTIC_7fabd27017614c17
Batch ID: 20250622_211523
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import time
import random
from typing import Dict, List

# Simulated smart home lighting system
class SmartHomeLighting:
    def __init__(self):
        # Initialize lighting system with default settings
        self.lights = {
            "living_room": {"status": "off", "brightness": 0},
            "bedroom": {"status": "off", "brightness": 0},
            "kitchen": {"status": "off", "brightness": 0},
        }
        self.user_preferences = {
            "living_room": {"preferred_brightness": 70},
            "bedroom": {"preferred_brightness": 30},
            "kitchen": {"preferred_brightness": 50},
        }
        self.energy_saving_mode = True  # Enable energy-saving mode by default

    def set_light_status(self, room: str, status: str, brightness: int = 0):
        """Set the status and brightness of a light in a specific room."""
        if room not in self.lights:
            print(f"Error: Room '{room}' not found.")
            return

        if status not in ["on", "off"]:
            print(f"Error: Invalid status '{status}'. Use 'on' or 'off'.")
            return

        if brightness < 0 or brightness > 100:
            print(f"Error: Brightness must be between 0 and 100.")
            return

        self.lights[room]["status"] = status
        self.lights[room]["brightness"] = brightness if status == "on" else 0
        print(f"Light in {room} set to {status} with brightness {brightness}%.")

    def adjust_lighting_based_on_sensors(self, sensor_data: Dict[str, int]):
        """
        Adjust lighting based on sensor data.
        Sensor data contains room names as keys and ambient light levels (0-100) as values.
        """
        for room, ambient_light in sensor_data.items():
            if room not in self.lights:
                print(f"Error: Room '{room}' not found in sensor data.")
                continue

            # Calculate desired brightness based on user preferences and ambient light
            preferred_brightness = self.user_preferences.get(room, {}).get("preferred_brightness", 50)
            if self.energy_saving_mode:
                # Reduce brightness by 20% in energy-saving mode
                preferred_brightness = int(preferred_brightness * 0.8)

            # Adjust brightness based on ambient light
            adjusted_brightness = max(0, preferred_brightness - ambient_light)
            self.set_light_status(room, "on" if adjusted_brightness > 0 else "off", adjusted_brightness)

    def handle_voice_command(self, command: str):
        """
        Handle voice commands to control the lighting system.
        Supported commands:
        - "turn on [room]"
        - "turn off [room]"
        - "set brightness [room] [value]"
        """
        try:
            parts = command.lower().split()
            if len(parts) < 3:
                print("Error: Invalid command format.")
                return

            action = parts[0]
            room = parts[2]
            if action == "turn":
                status = parts[1]
                self.set_light_status(room, status)
            elif action == "set" and parts[1] == "brightness":
                brightness = int(parts[3])
                self.set_light_status(room, "on", brightness)
            else:
                print("Error: Unsupported command.")
        except (IndexError, ValueError) as e:
            print(f"Error: Failed to process command. {e}")

    def display_status(self):
        """Display the current status of all lights."""
        print("\nCurrent Lighting Status:")
        for room, settings in self.lights.items():
            print(f"{room.capitalize()}: Status={settings['status']}, Brightness={settings['brightness']}%")
        print()

# Simulated sensor data generator
def generate_sensor_data(rooms: List[str]) -> Dict[str, int]:
    """Generate random ambient light levels for each room."""
    return {room: random.randint(0, 100) for room in rooms}

# Main function to simulate the smart home lighting system
def main():
    lighting_system = SmartHomeLighting()

    # Simulate sensor data and voice commands
    while True:
        # Generate random sensor data
        sensor_data = generate_sensor_data(list(lighting_system.lights.keys()))
        print(f"Sensor Data: {sensor_data}")

        # Adjust lighting based on sensor data
        lighting_system.adjust_lighting_based_on_sensors(sensor_data)

        # Simulate user voice commands
        voice_commands = [
            "turn on living_room",
            "set brightness bedroom 40",
            "turn off kitchen",
        ]
        for command in voice_commands:
            print(f"Processing voice command: '{command}'")
            lighting_system.handle_voice_command(command)

        # Display current lighting status
        lighting_system.display_status()

        # Wait for a short period before the next cycle
        time.sleep(5)

# Run the script
if __name__ == "__main__":
    main()
```
