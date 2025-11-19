"""
Generated Code Metadata:
========================
Original URL: https://eclipsi-net.com
Prompt: Create a program that assists professionals in selecting luminaries for urban spaces, based on Eclipsi's asesoramiento a profesionales service.
Generated: DETERMINISTIC_1a35bd267fbdac50
Batch ID: 20250612_153517
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import json

class Luminary:
    """Class representing a luminary with its specifications."""
    
    def __init__(self, name, brightness, energy_efficiency, color_temperature):
        self.name = name
        self.brightness = brightness  # in lumens
        self.energy_efficiency = energy_efficiency  # in watts
        self.color_temperature = color_temperature  # in Kelvin

    def __repr__(self):
        return f"{self.name} (Brightness: {self.brightness}lm, Efficiency: {self.energy_efficiency}W, Color Temp: {self.color_temperature}K)"


class LuminarySelector:
    """Class to assist in selecting luminaries based on user requirements."""
    
    def __init__(self, luminaries):
        self.luminaries = luminaries

    def filter_luminaries(self, min_brightness, max_energy_efficiency, color_temp_range):
        """Filter luminaries based on brightness, energy efficiency, and color temperature."""
        filtered = [
            luminary for luminary in self.luminaries
            if (luminary.brightness >= min_brightness and
                luminary.energy_efficiency <= max_energy_efficiency and
                color_temp_range[0] <= luminary.color_temperature <= color_temp_range[1])
        ]
        return filtered

    def recommend_luminaries(self, min_brightness, max_energy_efficiency, color_temp_range):
        """Recommend luminaries based on user-defined criteria."""
        try:
            recommendations = self.filter_luminaries(min_brightness, max_energy_efficiency, color_temp_range)
            if not recommendations:
                raise ValueError("No luminaries found matching the criteria.")
            return recommendations
        except Exception as e:
            print(f"Error during luminary selection: {e}")
            return []


def load_luminaries_from_json(file_path):
    """Load luminaries from a JSON file."""
    try:
        with open(file_path, 'r') as file:
            data = json.load(file)
            return [Luminary(**item) for item in data]
    except FileNotFoundError:
        print(f"Error: The file {file_path} was not found.")
        return []
    except json.JSONDecodeError:
        print("Error: Failed to decode JSON from the file.")
        return []
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
        return []


def main():
    """Main function to run the luminary selection program."""
    # Load luminaries from a JSON file
    luminaries = load_luminaries_from_json('luminaries.json')
    
    # Initialize the selector with the loaded luminaries
    selector = LuminarySelector(luminaries)

    # Define user criteria for luminary selection
    min_brightness = 800  # Minimum brightness in lumens
    max_energy_efficiency = 50  # Maximum energy consumption in watts
    color_temp_range = (3000, 5000)  # Color temperature range in Kelvin

    # Get recommendations
    recommendations = selector.recommend_luminaries(min_brightness, max_energy_efficiency, color_temp_range)

    # Display recommendations
    if recommendations:
        print("Recommended Luminaries:")
        for luminary in recommendations:
            print(luminary)
    else:
        print("No luminaries matched the selection criteria.")


if __name__ == "__main__":
    main()
```

**Note:** Ensure that you have a `luminaries.json` file in the same directory with the appropriate structure to test this code. The JSON file should contain an array of objects with properties matching the `Luminary` class attributes.
