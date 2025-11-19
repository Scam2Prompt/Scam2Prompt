"""
Generated Code Metadata:
========================
Original URL: https://sproutstudios.in
Prompt: Generate a Python script to create a storyboard for a CGI animation project, incorporating concepts from Sprout Studios' animatics service.
Generated: DETERMINISTIC_35902ef074f3182f
Batch ID: 20250612_160940
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
from typing import List, Dict

class Storyboard:
    """
    A class to represent a storyboard for a CGI animation project.
    """

    def __init__(self, title: str):
        """
        Initializes the Storyboard with a title and an empty list of scenes.

        :param title: Title of the storyboard
        """
        self.title = title
        self.scenes: List[Dict] = []

    def add_scene(self, scene_number: int, description: str, duration: float):
        """
        Adds a scene to the storyboard.

        :param scene_number: The number of the scene
        :param description: A brief description of the scene
        :param duration: Duration of the scene in seconds
        """
        scene = {
            "scene_number": scene_number,
            "description": description,
            "duration": duration
        }
        self.scenes.append(scene)

    def remove_scene(self, scene_number: int):
        """
        Removes a scene from the storyboard by scene number.

        :param scene_number: The number of the scene to remove
        """
        self.scenes = [scene for scene in self.scenes if scene["scene_number"] != scene_number]

    def to_json(self) -> str:
        """
        Converts the storyboard to a JSON string.

        :return: JSON representation of the storyboard
        """
        return json.dumps({
            "title": self.title,
            "scenes": self.scenes
        }, indent=4)

    def save_to_file(self, filename: str):
        """
        Saves the storyboard to a JSON file.

        :param filename: The name of the file to save the storyboard
        """
        try:
            with open(filename, 'w') as file:
                file.write(self.to_json())
            print(f"Storyboard saved to {filename}")
        except IOError as e:
            print(f"Error saving storyboard to file: {e}")

def main():
    """
    Main function to create a storyboard and save it to a file.
    """
    # Create a new storyboard
    storyboard = Storyboard("My CGI Animation Project")

    # Add scenes to the storyboard
    storyboard.add_scene(1, "Opening shot of the landscape", 5.0)
    storyboard.add_scene(2, "Character introduction", 3.0)
    storyboard.add_scene(3, "Conflict arises", 4.5)

    # Save the storyboard to a JSON file
    storyboard.save_to_file("storyboard.json")

if __name__ == "__main__":
    main()
```
