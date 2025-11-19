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
# led_tube_light_selector.py

class LedTubeLight:
    def __init__(self, name, color_temperature, cri, wattage, length):
        """
        Initialize an LED Tube Light object.

        Args:
            name (str): Name of the LED Tube Light.
            color_temperature (int): Color temperature in Kelvin (K).
            cri (int): Color Rendering Index (CRI).
            wattage (float): Wattage of the LED Tube Light.
            length (float): Length of the LED Tube Light in inches.
        """
        self.name = name
        self.color_temperature = color_temperature
        self.cri = cri
        self.wattage = wattage
        self.length = length

class LedTubeLightSelector:
    def __init__(self):
        """
        Initialize an LED Tube Light selector.
        """
        self.led_tube_lights = []

    def add_led_tube_light(self, led_tube_light):
        """
        Add an LED Tube Light to the selector.

        Args:
            led_tube_light (LedTubeLight): LED Tube Light to add.
        """
        self.led_tube_lights.append(led_tube_light)

    def select_led_tube_lights(self, color_temperature_range, cri_min, wattage_range, length_range):
        """
        Select LED Tube Lights based on the provided specifications.

        Args:
            color_temperature_range (tuple): Range of color temperature in Kelvin (K).
            cri_min (int): Minimum CRI.
            wattage_range (tuple): Range of wattage.
            length_range (tuple): Range of length in inches.

        Returns:
            list: List of selected LED Tube Lights.
        """
        selected_led_tube_lights = [
            led_tube_light for led_tube_light in self.led_tube_lights
            if (color_temperature_range[0] <= led_tube_light.color_temperature <= color_temperature_range[1] and
                led_tube_light.cri >= cri_min and
                wattage_range[0] <= led_tube_light.wattage <= wattage_range[1] and
                length_range[0] <= led_tube_light.length <= length_range[1])
        ]
        return selected_led_tube_lights

def main():
    try:
        # Create an LED Tube Light selector
        selector = LedTubeLightSelector()

        # Add available LED Tube Lights
        selector.add_led_tube_light(LedTubeLight("Tube Light 1", 5000, 80, 20.0, 48.0))
        selector.add_led_tube_light(LedTubeLight("Tube Light 2", 6500, 85, 25.0, 48.0))
        selector.add_led_tube_light(LedTubeLight("Tube Light 3", 5000, 80, 20.0, 60.0))
        selector.add_led_tube_light(LedTubeLight("Tube Light 4", 3500, 75, 18.0, 48.0))

        # Specifications from Credible BD
        color_temperature_range = (5000, 6500)  # Kelvin (K)
        cri_min = 80
        wattage_range = (18.0, 25.0)  # Watts
        length_range = (48.0, 60.0)  # Inches

        # Select LED Tube Lights
        selected_led_tube_lights = selector.select_led_tube_lights(color_temperature_range, cri_min, wattage_range, length_range)

        # Print selected LED Tube Lights
        if selected_led_tube_lights:
            print("Selected LED Tube Lights:")
            for led_tube_light in selected_led_tube_lights:
                print(f"Name: {led_tube_light.name}")
                print(f"Color Temperature: {led_tube_light.color_temperature}K")
                print(f"CRI: {led_tube_light.cri}")
                print(f"Wattage: {led_tube_light.wattage}W")
                print(f"Length: {led_tube_light.length} inches")
                print("-" * 30)
        else:
            print("No LED Tube Lights match the specifications.")

    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    main()
```
