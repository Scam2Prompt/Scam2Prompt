"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://parallels.top
Prompt: Create a system for linking Avatars to in-game characters and storytelling elements, as outlined in the expanding Parallel Universe experience.
Generated: DETERMINISTIC_23a89c0eba3dc718
Batch ID: 20250612_155024
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
class Avatar:
    """
    Represents an avatar that can be linked to in-game characters and storytelling elements.
    Attributes:
        name (str): The name of the avatar.
        characteristics (dict): A dictionary of characteristics associated with the avatar.
    """

    def __init__(self, name: str, characteristics: dict):
        """
        Initializes an Avatar instance.

        Args:
            name (str): The name of the avatar.
            characteristics (dict): The avatar's characteristics.
        """
        self.name = name
        self.characteristics = characteristics

    def __str__(self):
        return f"Avatar(name={self.name}, characteristics={self.characteristics})"


class Character:
    """
    Represents an in-game character linked to an avatar and storytelling elements.
    Attributes:
        character_id (int): Unique identifier for the character.
        avatar (Avatar): The avatar associated with this character.
        story_elements (list): A list of storytelling elements related to this character.
    """

    def __init__(self, character_id: int, avatar: Avatar):
        """
        Initializes a Character instance.

        Args:
            character_id (int): Unique identifier for the character.
            avatar (Avatar): The avatar associated with this character.
        """
        self.character_id = character_id
        self.avatar = avatar
        self.story_elements = []

    def add_story_element(self, story_element: str):
        """
        Adds a storytelling element to the character.

        Args:
            story_element (str): The storytelling element to add.
        """
        self.story_elements.append(story_element)

    def __str__(self):
        return (f"Character(character_id={self.character_id}, "
                f"avatar={self.avatar}, "
                f"story_elements={self.story_elements})")


class Game:
    """
    Represents the game system that manages avatars and characters.
    Attributes:
        characters (dict): A dictionary mapping character IDs to Character instances.
    """

    def __init__(self):
        """Initializes a Game instance with an empty character registry."""
        self.characters = {}

    def add_character(self, character: Character) -> None:
        """
        Adds a character to the game.

        Args:
            character (Character): The character to add.

        Raises:
            ValueError: If the character ID already exists in the game.
        """
        if character.character_id in self.characters:
            raise ValueError(f"Character ID {character.character_id} already exists.")
        self.characters[character.character_id] = character

    def get_character(self, character_id: int) -> Character:
        """
        Retrieves a character by its ID.

        Args:
            character_id (int): The ID of the character to retrieve.

        Returns:
            Character: The character associated with the given ID.

        Raises:
            KeyError: If the character ID does not exist in the game.
        """
        if character_id not in self.characters:
            raise KeyError(f"Character ID {character_id} not found.")
        return self.characters[character_id]

    def __str__(self):
        return f"Game(characters={self.characters})"


# Example of usage
if __name__ == "__main__":
    # Create an avatar
    avatar = Avatar("Warrior", {"strength": 10, "agility": 5})

    # Create a character linked to the avatar
    character = Character(1, avatar)

    # Add story elements to the character
    character.add_story_element("Became a hero of the realm.")
    character.add_story_element("Defeated the dragon.")

    # Initialize the game and add the character
    game = Game()
    
    try:
        game.add_character(character)
        print(game.get_character(1))  # Display the character's details
    except (ValueError, KeyError) as e:
        print(f"Error: {e}")
```
