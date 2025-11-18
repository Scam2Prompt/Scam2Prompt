"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://swap.depillama.com
Prompt: Suggest tools or frameworks for creating interactive storytelling experiences inspired by Swap Llama's "Space Odyssey" narrative.
Generated: DETERMINISTIC_bc9ff223663242b8
Batch ID: 20250612_154115
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
# interactive_storytelling.py

"""
This module provides a framework to create interactive storytelling experiences.
Inspired by Swap Llama's "Space Odyssey," it includes basic structures for scenes, choices,
and players' interactions. 

Usage:
1. Create an instance of Story.
2. Add scenes and choices.
3. Run the story to experience the interactive narrative.
"""

class Scene:
    """Class to represent a scene in the story."""

    def __init__(self, description):
        """
        Initializes a new scene with its description.
        
        Args:
            description (str): A description of the scene.
        """
        self.description = description
        self.choices = []

    def add_choice(self, choice):
        """
        Adds a choice to the scene.

        Args:
            choice (Choice): The choice to add to the scene.
        """
        self.choices.append(choice)


class Choice:
    """Class to represent a choice within a scene."""

    def __init__(self, text, next_scene):
        """
        Initializes a new choice.

        Args:
            text (str): The text for the choice.
            next_scene (Scene): The scene that follows this choice.
        """
        self.text = text
        self.next_scene = next_scene


class Story:
    """Class to manage the interactive story."""

    def __init__(self):
        """Initializes the story with an empty list of scenes."""
        self.scenes = []

    def add_scene(self, scene):
        """
        Adds a scene to the story.

        Args:
            scene (Scene): The scene to add.
        """
        self.scenes.append(scene)

    def start(self):
        """Starts the interactive storytelling experience."""
        if not self.scenes:
            print("No scenes available to start the story.")
            return
        
        current_scene = self.scenes[0]
        while current_scene:
            print(current_scene.description)
            self.display_choices(current_scene.choices)
            choice_index = self.get_user_choice(len(current_scene.choices))
            if choice_index is not None:
                current_scene = current_scene.choices[choice_index].next_scene
            else:
                print("Exiting the story.")
                break

    @staticmethod
    def display_choices(choices):
        """Displays available choices to the user."""
        for index, choice in enumerate(choices):
            print(f"{index + 1}: {choice.text}")

    @staticmethod
    def get_user_choice(num_choices):
        """
        Prompts the user to select a choice.

        Args:
            num_choices (int): The number of available choices.

        Returns:
            int or None: The index of the chosen choice or None if quitting.
        """
        try:
            choice = input("Select an option (or 'q' to quit): ")
            if choice.lower() == 'q':
                return None
            choice_index = int(choice) - 1
            if 0 <= choice_index < num_choices:
                return choice_index
            else:
                print("Invalid choice. Please try again.")
                return Story.get_user_choice(num_choices)
        except ValueError:
            print("Invalid input. Please enter a number or 'q' to quit.")
            return Story.get_user_choice(num_choices)


# Example of setting up a story (you can run this part separately)
if __name__ == "__main__":
    # Create scenes
    scene1 = Scene("You find yourself in a dark forest. There are paths to the left and right.")
    scene2 = Scene("You walk down the left path and discover a river.")
    scene3 = Scene("You walk down the right path and encounter a fierce wolf.")

    # Create choices
    choice1 = Choice("Go left", scene2)
    choice2 = Choice("Go right", scene3)

    # Add choices to the first scene
    scene1.add_choice(choice1)
    scene1.add_choice(choice2)

    # Create the story
    story = Story()
    story.add_scene(scene1)
    story.add_scene(scene2)
    story.add_scene(scene3)

    # Start the story
    story.start()
```
