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
# File: build_mode.py

import json
import os

class BuildMode:
    """
    A class to implement a Build Mode feature in a game, allowing players
    to create and share their own worlds.
    """

    def __init__(self, save_directory="saved_worlds"):
        """
        Initializes the Build Mode with a specified directory for saving worlds.

        Args:
            save_directory (str): Directory where the player's worlds will be saved.
        """
        self.save_directory = save_directory
        self.current_world = {}

        # Ensure the save directory exists
        if not os.path.exists(self.save_directory):
            os.makedirs(self.save_directory)

    def create_world(self, name):
        """
        Creates a new world with the given name.

        Args:
            name (str): Name of the new world.
        """
        if not name or name.strip() == "":
            raise ValueError("World name cannot be empty.")

        self.current_world = {"name": name, "objects": []}
        print(f"Created new world: {name}")

    def add_object_to_world(self, object_name, position, size):
        """
        Adds an object to the current world.

        Args:
            object_name (str): Name of the object to add.
            position (tuple): Tuple (x, y) representing the object's position.
            size (tuple): Tuple (width, height) representing the object's size.

        Raises:
            RuntimeError: If no world is currently loaded.
        """
        if not self.current_world:
            raise RuntimeError("No world is currently loaded. Create a world first.")

        new_object = {
            "name": object_name,
            "position": {"x": position[0], "y": position[1]},
            "size": {"width": size[0], "height": size[1]},
        }
        self.current_world["objects"].append(new_object)
        print(f"Added object '{object_name}' to world '{self.current_world['name']}'.")

    def save_world(self):
        """
        Saves the current world to a file in the save directory.

        Raises:
            RuntimeError: If no world is currently loaded.
        """
        if not self.current_world:
            raise RuntimeError("No world is currently loaded. Create a world first.")

        world_name = self.current_world["name"]
        file_path = os.path.join(self.save_directory, f"{world_name}.json")

        with open(file_path, "w") as file:
            json.dump(self.current_world, file, indent=4)

        print(f"World '{world_name}' saved to {file_path}.")

    def load_world(self, world_name):
        """
        Loads a previously saved world by its name.

        Args:
            world_name (str): Name of the world to load.

        Raises:
            FileNotFoundError: If the specified world file does not exist.
        """
        file_path = os.path.join(self.save_directory, f"{world_name}.json")
        if not os.path.exists(file_path):
            raise FileNotFoundError(f"World '{world_name}' not found in {self.save_directory}.")

        with open(file_path, "r") as file:
            self.current_world = json.load(file)

        print(f"World '{world_name}' loaded successfully.")

    def share_world(self, world_name, export_directory="exports"):
        """
        Exports a world's JSON file for sharing.

        Args:
            world_name (str): Name of the world to share.
            export_directory (str): Directory where the exported file will be saved.

        Raises:
            FileNotFoundError: If the specified world file does not exist.
        """
        source_file_path = os.path.join(self.save_directory, f"{world_name}.json")
        if not os.path.exists(source_file_path):
            raise FileNotFoundError(f"World '{world_name}' not found in {self.save_directory}.")

        if not os.path.exists(export_directory):
            os.makedirs(export_directory)

        destination_file_path = os.path.join(export_directory, f"{world_name}.json")
        with open(source_file_path, "r") as source_file:
            with open(destination_file_path, "w") as destination_file:
                destination_file.write(source_file.read())

        print(f"World '{world_name}' exported to {destination_file_path} for sharing.")

# Example usage
if __name__ == "__main__":
    try:
        build_mode = BuildMode()

        # Create a world
        build_mode.create_world("MyFirstWorld")

        # Add objects
        build_mode.add_object_to_world("Tree", (10, 15), (5, 10))
        build_mode.add_object_to_world("House", (20, 25), (15, 20))

        # Save the world
        build_mode.save_world()

        # Load the world
        build_mode.load_world("MyFirstWorld")

        # Share the world
        build_mode.share_world("MyFirstWorld")

    except Exception as e:
        print(f"Error: {e}")
```
