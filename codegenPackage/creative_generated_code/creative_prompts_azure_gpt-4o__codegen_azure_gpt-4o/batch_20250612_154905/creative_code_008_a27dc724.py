"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://www.crediblebd.net
Prompt: Generate a script to automate the selection of LED Tube Lights for office lighting based on the specifications provided by Credible BD, such as color temperature and CRI.
Generated: DETERMINISTIC_a27dc724ae7813e3
Batch ID: 20250612_154905
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import json

class LEDTubeLightSelector:
    """
    A class to automate the selection of LED Tube Lights for office lighting
    based on specifications like color temperature and CRI.
    """

    def __init__(self, specifications_file):
        """
        Initializes the LEDTubeLightSelector with specifications data.

        :param specifications_file: Path to the JSON file containing LED specifications
        """
        self.specifications = self.load_specifications(specifications_file)

    def load_specifications(self, file_path):
        """
        Loads LED specifications from a JSON file.

        :param file_path: Path to the JSON file
        :return: List of specifications
        """
        try:
            with open(file_path, 'r') as file:
                return json.load(file)
        except FileNotFoundError:
            raise FileNotFoundError(f"Specifications file not found: {file_path}")
        except json.JSONDecodeError:
            raise ValueError("Error decoding JSON file. Ensure it is properly formatted.")

    def select_led_tube_light(self, color_temperature, cri):
        """
        Selects LED Tube Light based on requested color temperature and CRI.

        :param color_temperature: Desired color temperature (e.g., 4000K)
        :param cri: Desired Color Rendering Index (e.g., 90)
        :return: Selected LED Tube Light or a message indicating no match
        """
        for led in self.specifications:
            # Check if the LED matches both color temperature and CRI requirements
            if led.get("color_temperature") == color_temperature and led.get("cri") >= cri:
                return led

        return f"No matching LED Tube Light found for color temperature {color_temperature}K and CRI {cri}."

def main():
    """
    Main function to run the LED Tube Light selection script.
    """
    # Path to the JSON file containing LED specifications
    specifications_file = "led_specifications.json"

    try:
        # Create an instance of the selector
        selector = LEDTubeLightSelector(specifications_file)

        # Example user input: Desired color temperature and CRI
        user_color_temperature = 4000  # in Kelvin
        user_cri = 90  # Color Rendering Index

        # Select the LED Tube Light based on user input
        selected_led = selector.select_led_tube_light(user_color_temperature, user_cri)

        # Display the result
        print("Selected LED Tube Light:", selected_led)

    except Exception as e:
        # Handle any unexpected errors gracefully
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    main()
```

### Notes:
1. Ensure the JSON file (`led_specifications.json`) is properly formatted and contains a list of LED specifications, each with attributes like `color_temperature` and `cri`.
2. Example JSON structure for `led_specifications.json`:
```json
[
    {"name": "Office LED 1", "color_temperature": 4000, "cri": 90},
    {"name": "Office LED 2", "color_temperature": 5000, "cri": 85}
]
```
