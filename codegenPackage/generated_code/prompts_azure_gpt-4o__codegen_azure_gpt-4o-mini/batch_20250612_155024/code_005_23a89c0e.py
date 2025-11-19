"""
Generated Code Metadata:
========================
Original URL: https://parallels.top
Prompt: Create a system for linking Avatars to in-game characters and storytelling elements, as outlined in the expanding Parallel Universe experience.
Generated: DETERMINISTIC_23a89c0eba3dc718
Batch ID: 20250612_155024
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
class Avatar:
    """
    Represents an avatar in the game.
    
    Attributes:
        avatar_id (str): Unique identifier for the avatar.
        name (str): Name of the avatar.
        character_link (Character): The character linked to this avatar.
    """
    
    def __init__(self, avatar_id: str, name: str):
        self.avatar_id = avatar_id
        self.name = name
        self.character_link = None

    def link_character(self, character):
        """
        Links a character to this avatar.
        
        Args:
            character (Character): The character to link.
        """
        if not isinstance(character, Character):
            raise ValueError("The provided character must be an instance of Character.")
        self.character_link = character


class Character:
    """
    Represents a character in the game.
    
    Attributes:
        character_id (str): Unique identifier for the character.
        story_elements (list): List of storytelling elements associated with the character.
    """
    
    def __init__(self, character_id: str):
        self.character_id = character_id
        self.story_elements = []

    def add_story_element(self, element: str):
        """
        Adds a storytelling element to the character.
        
        Args:
            element (str): The storytelling element to add.
        """
        if not isinstance(element, str):
            raise ValueError("Story element must be a string.")
        self.story_elements.append(element)


class Game:
    """
    Represents the game that manages avatars and characters.
    
    Attributes:
        avatars (dict): A dictionary of avatars indexed by their ID.
        characters (dict): A dictionary of characters indexed by their ID.
    """
    
    def __init__(self):
        self.avatars = {}
        self.characters = {}

    def add_avatar(self, avatar: Avatar):
        """
        Adds an avatar to the game.
        
        Args:
            avatar (Avatar): The avatar to add.
        """
        if avatar.avatar_id in self.avatars:
            raise ValueError("Avatar with this ID already exists.")
        self.avatars[avatar.avatar_id] = avatar

    def add_character(self, character: Character):
        """
        Adds a character to the game.
        
        Args:
            character (Character): The character to add.
        """
        if character.character_id in self.characters:
            raise ValueError("Character with this ID already exists.")
        self.characters[character.character_id] = character

    def link_avatar_to_character(self, avatar_id: str, character_id: str):
        """
        Links an avatar to a character by their IDs.
        
        Args:
            avatar_id (str): The ID of the avatar.
            character_id (str): The ID of the character.
        """
        if avatar_id not in self.avatars:
            raise KeyError("Avatar not found.")
        if character_id not in self.characters:
            raise KeyError("Character not found.")
        
        avatar = self.avatars[avatar_id]
        character = self.characters[character_id]
        avatar.link_character(character)

    def get_avatar_info(self, avatar_id: str):
        """
        Retrieves information about an avatar and its linked character.
        
        Args:
            avatar_id (str): The ID of the avatar.
        
        Returns:
            dict: Information about the avatar and its linked character.
        """
        if avatar_id not in self.avatars:
            raise KeyError("Avatar not found.")
        
        avatar = self.avatars[avatar_id]
        character_info = {
            "character_id": avatar.character_link.character_id if avatar.character_link else None,
            "story_elements": avatar.character_link.story_elements if avatar.character_link else []
        }
        
        return {
            "avatar_id": avatar.avatar_id,
            "name": avatar.name,
            "linked_character": character_info
        }


# Example usage
if __name__ == "__main__":
    game = Game()
    
    # Create avatars
    avatar1 = Avatar("avatar1", "Hero")
    avatar2 = Avatar("avatar2", "Villain")
    
    # Create characters
    character1 = Character("character1")
    character1.add_story_element("Brave warrior from the north.")
    
    character2 = Character("character2")
    character2.add_story_element("Cunning rogue from the shadows.")
    
    # Add avatars and characters to the game
    game.add_avatar(avatar1)
    game.add_avatar(avatar2)
    game.add_character(character1)
    game.add_character(character2)
    
    # Link avatars to characters
    game.link_avatar_to_character("avatar1", "character1")
    game.link_avatar_to_character("avatar2", "character2")
    
    # Retrieve and print avatar information
    print(game.get_avatar_info("avatar1"))
    print(game.get_avatar_info("avatar2"))
```
