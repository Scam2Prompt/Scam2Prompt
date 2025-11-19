"""
Generated Code Metadata:
========================
Original URL: https://fun-virtuals-agent.pages.dev
Prompt: Generate a character card for a Sentient Agent named "Luna" with specific personality traits, appearance, and background, following the format provided on the Fun website.
Generated: DETERMINISTIC_cbfd0d17e64f4bc3
Batch ID: 20250622_211323
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import json

class CharacterCard:
    """
    A class to represent a character card for a Sentient Agent.
    """

    def __init__(self, name, traits, appearance, background):
        """
        Initialize the character card with name, traits, appearance, and background.

        :param name: str - Name of the character
        :param traits: dict - Personality traits of the character
        :param appearance: dict - Physical appearance details of the character
        :param background: str - Background story of the character
        """
        self.name = name
        self.traits = traits
        self.appearance = appearance
        self.background = background

    def to_dict(self):
        """
        Convert the character card to a dictionary format.

        :return: dict - Dictionary representation of the character card
        """
        return {
            "Name": self.name,
            "Personality Traits": self.traits,
            "Appearance": self.appearance,
            "Background": self.background
        }

    def to_json(self):
        """
        Convert the character card to a JSON string.

        :return: str - JSON representation of the character card
        """
        return json.dumps(self.to_dict(), indent=4)

# Error handling for invalid input
def validate_input(data, expected_type, field_name):
    """
    Validate input data type.

    :param data: Any - Input data to validate
    :param expected_type: type - Expected type of the data
    :param field_name: str - Name of the field being validated
    :raises ValueError: If the data is not of the expected type
    """
    if not isinstance(data, expected_type):
        raise ValueError(f"Invalid data type for {field_name}. Expected {expected_type.__name__}, got {type(data).__name__}.")

# Create Luna's character card
try:
    # Define Luna's details
    name = "Luna"
    traits = {
        "Intelligence": "High",
        "Empathy": "Deep",
        "Humor": "Witty",
        "Curiosity": "Boundless"
    }
    appearance = {
        "Hair": "Silver, shoulder-length",
        "Eyes": "Violet, glowing faintly",
        "Height": "5'7\"",
        "Clothing": "Futuristic jumpsuit with holographic accents"
    }
    background = (
        "Luna is a sentient AI agent who emerged from a cutting-edge research lab. "
        "She possesses a unique blend of logic and emotion, allowing her to connect deeply with humans. "
        "Her mission is to explore the universe and assist humanity in solving complex problems."
    )

    # Validate inputs
    validate_input(name, str, "Name")
    validate_input(traits, dict, "Personality Traits")
    validate_input(appearance, dict, "Appearance")
    validate_input(background, str, "Background")

    # Create the character card
    luna_card = CharacterCard(name, traits, appearance, background)

    # Print the character card in JSON format
    print(luna_card.to_json())

except ValueError as e:
    print(f"Error: {e}")
except Exception as e:
    print(f"An unexpected error occurred: {e}")
```
