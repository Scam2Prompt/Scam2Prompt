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
import json
import os

class WorldBuilder:
    """
    A class to represent a game world builder for creating and sharing custom worlds.
    """

    def __init__(self, save_directory='worlds'):
        """
        Initializes the WorldBuilder with a specified save directory.

        Args:
            save_directory (str): The directory where worlds will be saved.
        """
        self.save_directory = save_directory
        self.worlds = []

        # Create the save directory if it doesn't exist
        os.makedirs(self.save_directory, exist_ok=True)

    def create_world(self, name, terrain, objects):
        """
        Creates a new world with the given parameters.

        Args:
            name (str): The name of the world.
            terrain (str): The type of terrain for the world.
            objects (list): A list of objects to include in the world.

        Returns:
            dict: A dictionary representing the created world.
        """
        world = {
            'name': name,
            'terrain': terrain,
            'objects': objects
        }
        self.worlds.append(world)
        return world

    def save_world(self, world):
        """
        Saves the specified world to a JSON file.

        Args:
            world (dict): The world to save.

        Raises:
            IOError: If there is an error saving the file.
        """
        file_path = os.path.join(self.save_directory, f"{world['name']}.json")
        try:
            with open(file_path, 'w') as file:
                json.dump(world, file, indent=4)
            print(f"World '{world['name']}' saved successfully.")
        except IOError as e:
            print(f"Error saving world '{world['name']}': {e}")

    def load_world(self, name):
        """
        Loads a world from a JSON file.

        Args:
            name (str): The name of the world to load.

        Returns:
            dict: The loaded world.

        Raises:
            FileNotFoundError: If the world file does not exist.
        """
        file_path = os.path.join(self.save_directory, f"{name}.json")
        try:
            with open(file_path, 'r') as file:
                world = json.load(file)
            print(f"World '{name}' loaded successfully.")
            return world
        except FileNotFoundError:
            print(f"World '{name}' not found.")
            raise
        except json.JSONDecodeError as e:
            print(f"Error loading world '{name}': {e}")
            raise

    def list_worlds(self):
        """
        Lists all saved worlds in the save directory.

        Returns:
            list: A list of world names.
        """
        return [f[:-5] for f in os.listdir(self.save_directory) if f.endswith('.json')]

# Example usage
if __name__ == "__main__":
    builder = WorldBuilder()

    # Create a new world
    new_world = builder.create_world("Tropical Paradise", "Tropical", ["Palm Tree", "Beach", "Coconut"])
    
    # Save the new world
    builder.save_world(new_world)

    # List all worlds
    print("Available worlds:", builder.list_worlds())

    # Load a world
    try:
        loaded_world = builder.load_world("Tropical Paradise")
        print("Loaded World:", loaded_world)
    except FileNotFoundError:
        print("Could not load the world.")
```
