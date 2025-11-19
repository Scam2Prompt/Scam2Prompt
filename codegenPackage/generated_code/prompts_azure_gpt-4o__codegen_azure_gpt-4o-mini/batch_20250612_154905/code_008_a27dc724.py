"""
Generated Code Metadata:
========================
Original URL: https://www.crediblebd.net
Prompt: Generate a script to automate the selection of LED Tube Lights for office lighting based on the specifications provided by Credible BD, such as color temperature and CRI.
Generated: DETERMINISTIC_a27dc724ae7813e3
Batch ID: 20250612_154905
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import json

class LEDTubeLight:
    def __init__(self, name, color_temperature, cri, wattage, lumens):
        """
        Initialize an LED Tube Light with the given specifications.

        :param name: str - The name of the LED tube light
        :param color_temperature: int - The color temperature in Kelvin
        :param cri: int - The Color Rendering Index
        :param wattage: float - The power consumption in watts
        :param lumens: float - The light output in lumens
        """
        self.name = name
        self.color_temperature = color_temperature
        self.cri = cri
        self.wattage = wattage
        self.lumens = lumens

    def __repr__(self):
        return f"{self.name} (CCT: {self.color_temperature}K, CRI: {self.cri}, Wattage: {self.wattage}W, Lumens: {self.lumens})"


class LEDTubeLightSelector:
    def __init__(self, specifications):
        """
        Initialize the LED Tube Light Selector with the given specifications.

        :param specifications: dict - Specifications for selecting LED tube lights
        """
        self.specifications = specifications
        self.lights = []

    def load_lights(self, lights_data):
        """
        Load LED tube lights from a JSON-like structure.

        :param lights_data: list - A list of dictionaries containing LED tube light data
        """
        for light in lights_data:
            try:
                led_light = LEDTubeLight(
                    name=light['name'],
                    color_temperature=light['color_temperature'],
                    cri=light['cri'],
                    wattage=light['wattage'],
                    lumens=light['lumens']
                )
                self.lights.append(led_light)
            except KeyError as e:
                print(f"Error loading light data: Missing key {e}")
            except Exception as e:
                print(f"Unexpected error: {e}")

    def select_lights(self):
        """
        Select LED tube lights based on the specified criteria.

        :return: list - A list of selected LED tube lights
        """
        selected_lights = []
        for light in self.lights:
            if (light.color_temperature >= self.specifications['min_color_temperature'] and
                light.color_temperature <= self.specifications['max_color_temperature'] and
                light.cri >= self.specifications['min_cri']):
                selected_lights.append(light)
        return selected_lights


def main():
    # Example specifications for selecting LED tube lights
    specifications = {
        "min_color_temperature": 3000,  # Minimum color temperature in Kelvin
        "max_color_temperature": 5000,  # Maximum color temperature in Kelvin
        "min_cri": 80                    # Minimum Color Rendering Index
    }

    # Example data for LED tube lights
    lights_data = [
        {"name": "Cool White LED", "color_temperature": 4000, "cri": 85, "wattage": 18, "lumens": 1800},
        {"name": "Warm White LED", "color_temperature": 3000, "cri": 90, "wattage": 15, "lumens": 1600},
        {"name": "Daylight LED", "color_temperature": 5000, "cri": 80, "wattage": 20, "lumens": 2000},
        {"name": "Standard LED", "color_temperature": 2700, "cri": 75, "wattage": 10, "lumens": 800}
    ]

    # Create an instance of the LED Tube Light Selector
    selector = LEDTubeLightSelector(specifications)

    # Load the LED tube lights
    selector.load_lights(lights_data)

    # Select lights based on specifications
    selected_lights = selector.select_lights()

    # Output the selected lights
    print("Selected LED Tube Lights:")
    for light in selected_lights:
        print(light)


if __name__ == "__main__":
    main()
```
