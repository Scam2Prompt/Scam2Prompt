"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://swap.depillama.com
Prompt: Write a Python script to generate a character profile inspired by Pandora from Swap Llama, emphasizing traits like cosmic generosity and courage in space exploration.
Generated: DETERMINISTIC_3a83fdd141da69fc
Batch ID: 20250612_154115
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import random
import json

class CharacterProfile:
    """A class to represent a character profile inspired by Pandora from Swap Llama."""

    def __init__(self, name):
        """Initialize the character with a name and default traits."""
        self.name = name
        self.traits = {
            "generosity": self.generate_generosity(),
            "courage": self.generate_courage(),
            "exploration": self.generate_exploration(),
        }

    def generate_generosity(self):
        """Generate a random level of cosmic generosity."""
        levels = ['Low', 'Medium', 'High', 'Cosmic']
        return random.choice(levels)

    def generate_courage(self):
        """Generate a random level of courage for space exploration."""
        levels = ['Timid', 'Brave', 'Fearless', 'Legendary']
        return random.choice(levels)

    def generate_exploration(self):
        """Generate a random affinity for space exploration."""
        explorations = [
            "Asteroid mining",
            "Galactic navigation",
            "Interstellar diplomacy",
            "Alien culture studies"
        ]
        return random.choice(explorations)

    def to_dict(self):
        """Convert the character profile to a dictionary for easy JSON serialization."""
        return {
            "name": self.name,
            "traits": self.traits,
        }

    def to_json(self):
        """Convert the character profile to a JSON string."""
        try:
            return json.dumps(self.to_dict(), indent=4)
        except (TypeError, ValueError) as e:
            print(f"Error converting to JSON: {e}")
            return None

def main():
    """Main function to create and display a character profile."""
    character_name = "Pandora"
    profile = CharacterProfile(character_name)

    # Display the character profile in JSON format
    print(profile.to_json())

if __name__ == "__main__":
    main()
```
