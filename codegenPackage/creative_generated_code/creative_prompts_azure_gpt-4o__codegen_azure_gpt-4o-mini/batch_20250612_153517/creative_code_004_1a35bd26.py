"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://eclipsi-net.com
Prompt: Create a program that assists professionals in selecting luminaries for urban spaces, based on Eclipsi's asesoramiento a profesionales service.
Generated: DETERMINISTIC_1a35bd267fbdac50
Batch ID: 20250612_153517
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import json

class Luminary:
    def __init__(self, name, luminosity, energy_efficiency, lifespan, color_temperature):
        self.name = name
        self.luminosity = luminosity  # in lumens
        self.energy_efficiency = energy_efficiency  # in lumens per watt
        self.lifespan = lifespan  # in hours
        self.color_temperature = color_temperature  # in Kelvin

    def __repr__(self):
        return f"Luminary(name={self.name}, luminosity={self.luminosity}, " \
               f"energy_efficiency={self.energy_efficiency}, lifespan={self.lifespan}, " \
               f"color_temperature={self.color_temperature})"

class LuminarySelector:
    def __init__(self, luminaries):
        """
        Initializes the LuminarySelector with a list of available luminaries.
        :param luminaries: List of Luminary objects
        """
        self.luminaries = luminaries

    def filter_luminaries(self, min_luminosity, max_energy_efficiency):
        """
        Filters luminaries based on specified luminosity and energy efficiency.
        :param min_luminosity: Minimum required luminosity (in lumens)
        :param max_energy_efficiency: Maximum allowed energy efficiency (in lumens per watt)
        :return: List of filtered luminaries
        """
        filtered = [
            luminary for luminary in self.luminaries 
            if luminary.luminosity >= min_luminosity and luminary.energy_efficiency <= max_energy_efficiency
        ]
        return filtered

def load_luminaries_from_json(file_path):
    """
    Loads luminary data from a JSON file.
    :param file_path: Path to the JSON file
    :return: List of Luminary objects
    """
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

if __name__ == "__main__":
    # Load luminaries from a JSON file
    luminaries = load_luminaries_from_json('luminaries.json')

    # Initialize the selector with loaded luminaries
    selector = LuminarySelector(luminaries)

    # Example filter criteria
    min_luminosity = 800  # Minimum lumens
    max_energy_efficiency = 100  # Max lumens per watt

    # Get filtered luminaries based on criteria
    filtered_luminaries = selector.filter_luminaries(min_luminosity, max_energy_efficiency)

    # Output the filtered results
    if filtered_luminaries:
        print("Filtered Luminaries:")
        for luminary in filtered_luminaries:
            print(luminary)
    else:
        print("No luminaries found matching the criteria.")
```
