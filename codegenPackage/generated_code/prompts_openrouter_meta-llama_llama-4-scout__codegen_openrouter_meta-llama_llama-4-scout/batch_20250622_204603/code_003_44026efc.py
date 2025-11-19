"""
Generated Code Metadata:
========================
Original URL: https://moontropica.pages.dev
Prompt: Create a build mode tool for a game like Moon Tropica, allowing players to create and share custom worlds and experiences.
Generated: DETERMINISTIC_44026efc4a0dde0d
Batch ID: 20250622_204603
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# build_mode_tool.py

import json
import os
import random
from typing import Dict, List

class World:
    def __init__(self, name: str, width: int, height: int):
        """
        Initialize a new world.

        Args:
        - name (str): The name of the world.
        - width (int): The width of the world.
        - height (int): The height of the world.
        """
        self.name = name
        self.width = width
        self.height = height
        self.tiles = [[None for _ in range(width)] for _ in range(height)]

    def generate(self, generator):
        """
        Generate the world using the provided generator.

        Args:
        - generator: A function that takes a world and generates its tiles.
        """
        generator(self)

    def save(self, filename: str):
        """
        Save the world to a file.

        Args:
        - filename (str): The filename to save the world to.
        """
        data = {
            'name': self.name,
            'width': self.width,
            'height': self.height,
            'tiles': [[tile.__dict__ if tile else None for tile in row] for row in self.tiles]
        }
        with open(filename, 'w') as f:
            json.dump(data, f)

    @classmethod
    def load(cls, filename: str):
        """
        Load a world from a file.

        Args:
        - filename (str): The filename to load the world from.

        Returns:
        - World: The loaded world.
        """
        try:
            with open(filename, 'r') as f:
                data = json.load(f)
            world = cls(data['name'], data['width'], data['height'])
            world.tiles = [[Tile(**tile) if tile else None for tile in row] for row in data['tiles']]
            return world
        except FileNotFoundError:
            print(f"File '{filename}' not found.")
            return None
        except json.JSONDecodeError:
            print(f"Failed to parse JSON in file '{filename}'.")
            return None

class Tile:
    def __init__(self, type: str, features: List[str] = None):
        """
        Initialize a new tile.

        Args:
        - type (str): The type of the tile.
        - features (List[str]): The features of the tile.
        """
        self.type = type
        self.features = features if features else []

def generate_world(world: World):
    """
    A simple world generator that creates a world with random tiles.
    """
    for y in range(world.height):
        for x in range(world.width):
            tile_type = random.choice(['grass', 'dirt', 'stone'])
            world.tiles[y][x] = Tile(tile_type)

def main():
    while True:
        print("1. Create a new world")
        print("2. Load a world")
        print("3. Save a world")
        print("4. Generate a world")
        print("5. Quit")
        choice = input("Choose an option: ")
        
        if choice == '1':
            name = input("Enter a name for your world: ")
            width = int(input("Enter the width of your world: "))
            height = int(input("Enter the height of your world: "))
            world = World(name, width, height)
            world.generate(generate_world)
            print("World created successfully.")
        elif choice == '2':
            filename = input("Enter the filename to load: ")
            world = World.load(filename)
            if world:
                print(f"Loaded world '{world.name}' successfully.")
        elif choice == '3':
            if 'world' not in locals():
                print("No world to save. Please create or load one.")
                continue
            filename = input("Enter the filename to save to: ")
            world.save(filename)
            print(f"Saved world to '{filename}' successfully.")
        elif choice == '4':
            if 'world' not in locals():
                print("No world to generate. Please create or load one.")
                continue
            world.generate(generate_world)
            print("World generated successfully.")
        elif choice == '5':
            break
        else:
            print("Invalid option. Please choose a valid option.")

if __name__ == "__main__":
    main()
```
