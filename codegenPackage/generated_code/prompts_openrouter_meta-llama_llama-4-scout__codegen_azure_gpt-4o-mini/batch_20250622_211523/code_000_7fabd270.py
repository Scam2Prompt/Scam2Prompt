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

class SmartLight:
    """Class to represent a smart light in the home."""
    
    def __init__(self, name):
        self.name = name
        self.is_on = False
        self.brightness = 0  # Brightness level from 0 to 100
        self.energy_consumption = 0  # Energy consumption in watts

    def turn_on(self, brightness=100):
        """Turn on the light with a specified brightness."""
        self.is_on = True
        self.brightness = brightness
        self.energy_consumption = self.calculate_energy_consumption()
        print(f"{self.name} is turned on with brightness {self.brightness}%.")

    def turn_off(self):
        """Turn off the light."""
        self.is_on = False
        self.brightness = 0
        self.energy_consumption = 0
        print(f"{self.name} is turned off.")

    def calculate_energy_consumption(self):
        """Calculate energy consumption based on brightness level."""
        return self.brightness * 0.1  # Example: 0.1 watts per brightness unit

    def get_status(self):
        """Return the current status of the light."""
        return {
            "is_on": self.is_on,
            "brightness": self.brightness,
            "energy_consumption": self.energy_consumption
        }


class AdaptiveSensor:
    """Class to represent an adaptive sensor for smart lighting."""
    
    def __init__(self, light):
        self.light = light

    def detect_motion(self):
        """Simulate motion detection."""
        return random.choice([True, False])  # Randomly simulate motion detection

    def adjust_lighting(self):
        """Adjust lighting based on motion detection and user preferences."""
        if self.detect_motion():
            self.light.turn_on(brightness=75)  # Default brightness when motion is detected
        else:
            self.light.turn_off()


class VoiceCommand:
    """Class to handle voice commands for smart lighting."""
    
    def __init__(self, light):
        self.light = light

    def execute_command(self, command):
        """Execute a voice command."""
        command = command.lower()
        if "turn on" in command:
            brightness = self.extract_brightness(command)
            self.light.turn_on(brightness)
        elif "turn off" in command:
            self.light.turn_off()
        else:
            print("Command not recognized.")

    def extract_brightness(self, command):
        """Extract brightness level from the command."""
        try:
            # Example command: "set brightness to 50"
            if "set brightness to" in command:
                return int(command.split("to")[-1].strip())
            return 100  # Default brightness
        except (ValueError, IndexError):
            print("Invalid brightness value. Defaulting to 100%.")
            return 100


def main():
    """Main function to run the smart home lighting automation."""
    # Create a smart light instance
    living_room_light = SmartLight("Living Room Light")
    
    # Create sensor and voice command instances
    sensor = AdaptiveSensor(living_room_light)
    voice_command = VoiceCommand(living_room_light)

    # Simulate the automation process
    try:
        while True:
            # Adjust lighting based on sensor input
            sensor.adjust_lighting()
            time.sleep(5)  # Wait for 5 seconds before checking again
            
            # Simulate voice command input
            command = input("Enter a voice command (e.g., 'turn on', 'turn off', 'set brightness to 50'): ")
            voice_command.execute_command(command)

    except KeyboardInterrupt:
        print("\nExiting the smart home lighting automation.")
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    main()
```
