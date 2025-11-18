"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://gta5mod.net
Prompt: Using "Map Editor" or "Map Builder," write a script to add custom map elements like the "Statue of Liberty – LCPP V1.0" or "World Trade Center – LCPP V Final" into GTA 5.
Generated: DETERMINISTIC_0894f3d77ed544f7
Batch ID: 20250612_152358
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import json
import os

class MapElement:
    """
    A class to represent a map element in the GTA 5 map editor.
    """
    def __init__(self, name, coordinates, model):
        """
        Initialize a new map element.

        Args:
            name (str): The name of the map element.
            coordinates (tuple): The (x, y, z) coordinates for the element.
            model (str): The model file name for the element.
        """
        self.name = name
        self.coordinates = coordinates
        self.model = model

    def to_dict(self):
        """
        Convert the map element to a dictionary for JSON serialization.

        Returns:
            dict: A dictionary representation of the map element.
        """
        return {
            'name': self.name,
            'coordinates': self.coordinates,
            'model': self.model
        }


class MapEditor:
    """
    A class to manage custom map elements in the GTA 5 map editor.
    """
    def __init__(self, map_file='custom_map.json'):
        """
        Initialize the MapEditor.

        Args:
            map_file (str): The path to the JSON file storing the map elements.
        """
        self.map_file = map_file
        self.elements = self.load_map_elements()

    def load_map_elements(self):
        """
        Load existing map elements from a JSON file.

        Returns:
            list: A list of MapElement objects.
        """
        if not os.path.exists(self.map_file):
            return []

        try:
            with open(self.map_file, 'r') as file:
                elements_data = json.load(file)
            return [MapElement(**elem) for elem in elements_data]
        except (FileNotFoundError, json.JSONDecodeError) as e:
            print(f"Error loading map elements: {e}")
            return []

    def add_element(self, name, coordinates, model):
        """
        Add a new map element and save it to the JSON file.

        Args:
            name (str): The name of the map element.
            coordinates (tuple): The (x, y, z) coordinates for the element.
            model (str): The model file name for the element.
        """
        new_element = MapElement(name, coordinates, model)
        self.elements.append(new_element)
        self.save_map_elements()

    def save_map_elements(self):
        """
        Save all map elements to the JSON file.
        """
        try:
            with open(self.map_file, 'w') as file:
                json.dump([element.to_dict() for element in self.elements], file, indent=4)
        except IOError as e:
            print(f"Error saving map elements: {e}")

    def list_elements(self):
        """
        List all map elements currently in the editor.
        """
        for element in self.elements:
            print(f"Name: {element.name}, Coordinates: {element.coordinates}, Model: {element.model}")


if __name__ == "__main__":
    # Example usage of the MapEditor class
    editor = MapEditor()

    # Adding custom map elements
    editor.add_element("Statue of Liberty – LCPP V1.0", (123.45, 678.90, 21.0), "statue_of_liberty_model")
    editor.add_element("World Trade Center – LCPP V Final", (321.45, 987.65, 30.0), "world_trade_center_model")

    # Listing all map elements
    editor.list_elements()
```
