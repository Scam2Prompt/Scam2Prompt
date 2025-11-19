"""
Generated Code Metadata:
========================
Original URL: https://fun-virtuals-agent.pages.dev
Prompt: Create a script to generate detailed character profiles for virtual agents, including personality, appearance, and emotional traits, based on the examples provided on the Fun Virtuals Agent site.
Generated: DETERMINISTIC_7114217cc4beb0c5
Batch ID: 20250612_154016
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import random
import json

class CharacterProfile:
    """
    A class to represent a character profile for virtual agents.
    """

    def __init__(self, name):
        """
        Initializes a new character profile with a name and default attributes.
        
        :param name: str - The name of the character.
        """
        self.name = name
        self.personality = self.generate_personality()
        self.appearance = self.generate_appearance()
        self.emotional_traits = self.generate_emotional_traits()

    def generate_personality(self):
        """
        Generates a random personality trait for the character.
        
        :return: str - A personality trait.
        """
        personalities = [
            "cheerful", "serious", "curious", "cynical", 
            "optimistic", "pessimistic", "empathetic", "analytical"
        ]
        return random.choice(personalities)

    def generate_appearance(self):
        """
        Generates a random appearance description for the character.
        
        :return: str - An appearance description.
        """
        appearances = [
            "tall with long hair", "short and stocky", 
            "slender with bright eyes", "average height with a warm smile"
        ]
        return random.choice(appearances)

    def generate_emotional_traits(self):
        """
        Generates a list of emotional traits for the character.
        
        :return: list - A list of emotional traits.
        """
        emotional_traits = [
            "joyful", "anxious", "calm", "passionate", 
            "frustrated", "content", "enthusiastic", "melancholic"
        ]
        return random.sample(emotional_traits, 3)  # Select 3 unique traits

    def to_dict(self):
        """
        Converts the character profile to a dictionary format.
        
        :return: dict - A dictionary representation of the character profile.
        """
        return {
            "name": self.name,
            "personality": self.personality,
            "appearance": self.appearance,
            "emotional_traits": self.emotional_traits
        }

def generate_character_profiles(num_profiles):
    """
    Generates a specified number of character profiles.
    
    :param num_profiles: int - The number of profiles to generate.
    :return: list - A list of character profiles.
    """
    profiles = []
    for i in range(num_profiles):
        name = f"Agent_{i + 1}"
        profile = CharacterProfile(name)
        profiles.append(profile.to_dict())
    return profiles

def save_profiles_to_file(profiles, filename):
    """
    Saves the generated character profiles to a JSON file.
    
    :param profiles: list - The list of character profiles.
    :param filename: str - The name of the file to save the profiles to.
    """
    try:
        with open(filename, 'w') as file:
            json.dump(profiles, file, indent=4)
        print(f"Profiles successfully saved to {filename}.")
    except IOError as e:
        print(f"Error saving profiles to file: {e}")

if __name__ == "__main__":
    try:
        num_profiles = 5  # Specify the number of profiles to generate
        profiles = generate_character_profiles(num_profiles)
        save_profiles_to_file(profiles, 'character_profiles.json')
    except Exception as e:
        print(f"An error occurred: {e}")
```
