"""
Generated Code Metadata:
========================
Original URL: https://cheemspet.web.app
Prompt: Write a short story or character description for the "Lord of Memes," Cheems, incorporating elements from the provided website content.
Generated: DETERMINISTIC_75c17cf2b4cd2e33
Batch ID: 20250622_212546
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
class MemeCharacter:
    """
    A class to represent a meme character with a name, description, and attributes.
    """

    def __init__(self, name, description, attributes):
        """
        Initializes a new instance of MemeCharacter.

        :param name: str - The name of the meme character.
        :param description: str - A brief description of the character.
        :param attributes: dict - A dictionary of attributes associated with the character.
        """
        self.name = name
        self.description = description
        self.attributes = attributes

    def display_character_info(self):
        """
        Displays the character's information in a formatted manner.
        """
        try:
            print(f"Character Name: {self.name}")
            print(f"Description: {self.description}")
            print("Attributes:")
            for key, value in self.attributes.items():
                print(f"  {key}: {value}")
        except Exception as e:
            print(f"An error occurred while displaying character info: {e}")


def create_cheems_character():
    """
    Creates an instance of the Cheems character with predefined attributes.

    :return: MemeCharacter - An instance of the Cheems character.
    """
    name = "Cheems"
    description = (
        "Cheems is the Lord of Memes, a Shiba Inu known for his love of 'cheemsburgers' "
        "and his unique way of speaking, often adding 'm' to words. He embodies the spirit "
        "of internet humor and has become a beloved figure in meme culture."
    )
    attributes = {
        "Species": "Dog",
        "Breed": "Shiba Inu",
        "Favorite Food": "Cheemsburger",
        "Catchphrase": "Cheems!",
        "Popularity": "High"
    }

    return MemeCharacter(name, description, attributes)


if __name__ == "__main__":
    # Create the Cheems character
    cheems = create_cheems_character()
    
    # Display the character's information
    cheems.display_character_info()
```
