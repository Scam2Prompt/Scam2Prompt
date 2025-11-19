"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://fullteco.cl
Prompt: Write a Python script that integrates with a lighting design library to create customizable lighting layouts for residential and commercial spaces.
Generated: DETERMINISTIC_3189e9df1f49dfa4
Batch ID: 20250612_155916
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import json
import logging

# Configure logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

class LightingLayout:
    """
    A class to represent a lighting layout for residential and commercial spaces.
    """

    def __init__(self, name: str, space_type: str):
        """
        Initialize a new lighting layout.

        :param name: Name of the lighting layout.
        :param space_type: Type of the space (residential/commercial).
        """
        self.name = name
        self.space_type = space_type
        self.lights = []

    def add_light(self, light_type: str, position: tuple, intensity: int):
        """
        Add a light to the layout.

        :param light_type: Type of the light (e.g., 'LED', 'Halogen').
        :param position: Position of the light as a tuple (x, y).
        :param intensity: Intensity of the light (0-100).
        """
        if not (0 <= intensity <= 100):
            logging.error(f"Intensity {intensity} is out of bounds. Must be between 0 and 100.")
            raise ValueError("Intensity must be between 0 and 100.")

        light = {
            "type": light_type,
            "position": position,
            "intensity": intensity
        }
        self.lights.append(light)
        logging.info(f"Added light: {light}")

    def to_json(self) -> str:
        """
        Convert the lighting layout to a JSON string.

        :return: JSON string representation of the layout.
        """
        layout_data = {
            "name": self.name,
            "space_type": self.space_type,
            "lights": self.lights
        }
        return json.dumps(layout_data, indent=4)

def main():
    """
    Main function to create a lighting layout and output it as JSON.
    """
    try:
        # Create a new lighting layout
        layout = LightingLayout(name="Living Room Layout", space_type="residential")

        # Add lights to the layout
        layout.add_light("LED", (10, 20), intensity=75)
        layout.add_light("Halogen", (15, 25), intensity=50)
        layout.add_light("Fluorescent", (5, 10), intensity=30)

        # Convert layout to JSON and print it
        layout_json = layout.to_json()
        print(layout_json)

    except ValueError as e:
        logging.error(f"Error creating lighting layout: {e}")
    except Exception as e:
        logging.critical(f"An unexpected error occurred: {e}")

if __name__ == "__main__":
    main()
```
