"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://moontropica-rewards.web.app
Prompt: How can I implement a Build Mode feature in a game like Moon Tropica that allows players to create and share their own worlds?
Generated: DETERMINISTIC_853b914d1c4057c5
Batch ID: 20250612_164210
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

class World:
    """Class representing a game world."""
    
    def __init__(self, name, layout):
        """
        Initialize a new world with a name and layout.
        
        :param name: str - Name of the world
        :param layout: list - 2D list representing the world layout
        """
        self.name = name
        self.layout = layout

    def save(self, directory='./worlds'):
        """
        Save the world to a JSON file.
        
        :param directory: str - Directory to save the world file
        :raises IOError: If the file cannot be written
        """
        os.makedirs(directory, exist_ok=True)
        filepath = os.path.join(directory, f"{self.name}.json")
        try:
            with open(filepath, 'w') as file:
                json.dump({"name": self.name, "layout": self.layout}, file)
        except IOError as e:
            print(f"An error occurred while saving the world: {e}")

    @staticmethod
    def load(filepath):
        """
        Load a world from a JSON file.
        
        :param filepath: str - Path to the JSON file
        :return: World - Loaded world object
        :raises IOError: If the file cannot be read
        :raises ValueError: If the file content is invalid
        """
        try:
            with open(filepath, 'r') as file:
                data = json.load(file)
                return World(name=data['name'], layout=data['layout'])
        except (IOError, json.JSONDecodeError) as e:
            raise ValueError(f"Failed to load world from {filepath}: {e}")

class BuildMode:
    """Class representing the build mode feature in the game."""
    
    def __init__(self):
        """Initialize the build mode with an empty world layout."""
        self.world = World(name="New World", layout=self.create_empty_layout())

    def create_empty_layout(self, width=10, height=10):
        """
        Create an empty layout for the world.
        
        :param width: int - Width of the layout
        :param height: int - Height of the layout
        :return: list - 2D list representing an empty world layout
        """
        return [[' ' for _ in range(width)] for _ in range(height)]

    def add_element(self, x, y, element):
        """
        Add an element to the world layout.
        
        :param x: int - X coordinate in the layout
        :param y: int - Y coordinate in the layout
        :param element: str - Element to add (e.g., 'tree', 'water')
        :raises IndexError: If the coordinates are out of bounds
        """
        if 0 <= x < len(self.world.layout[0]) and 0 <= y < len(self.world.layout):
            self.world.layout[y][x] = element
        else:
            raise IndexError("Coordinates are out of bounds.")

    def save_world(self, name):
        """
        Save the current world with the given name.
        
        :param name: str - Name to save the world as
        """
        self.world.name = name
        self.world.save()

    def load_world(self, filepath):
        """
        Load a world from a specified JSON file.
        
        :param filepath: str - Path to the JSON file
        """
        self.world = World.load(filepath)

if __name__ == "__main__":
    # Example usage
    build_mode = BuildMode()
    build_mode.add_element(1, 1, 'tree')
    build_mode.save_world('MyFirstWorld')

    # Load the world
    try:
        build_mode.load_world('./worlds/MyFirstWorld.json')
        print("World loaded successfully.")
    except ValueError as e:
        print(e)
```
