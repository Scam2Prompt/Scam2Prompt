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

def generate_character_profile():
    """
    Generates a character profile inspired by Pandora from Swap Llama,
    emphasizing traits like cosmic generosity and courage in space exploration.
    """
    # Predefined attributes for the character
    name = "Pandora"
    species = "Llama"
    traits = {
        "Generosity": random.uniform(8.0, 10.0),  # Scale: 1-10
        "Courage": random.uniform(8.0, 10.0),    # Scale: 1-10
        "Curiosity": random.uniform(7.0, 9.5),   # Scale: 1-10
        "Wisdom": random.uniform(7.0, 9.0),      # Scale: 1-10
        "Cosmic Awareness": random.uniform(8.5, 10.0)  # Scale: 1-10
    }
    hobbies = ["Space Exploration", "Helping Others", "Stargazing"]
    favorite_quote = (
        "The universe is vast, but generosity binds us together."
    )

    # Create the profile dictionary
    character_profile = {
        "Name": name,
        "Species": species,
        "Traits": traits,
        "Hobbies": hobbies,
        "Favorite Quote": favorite_quote
    }

    return character_profile


def display_profile(profile):
    """
    Displays the character profile in a clean format.
    :param profile: Dictionary containing the character profile.
    """
    print("=" * 40)
    print(f"Character Profile: {profile['Name']}")
    print("=" * 40)
    print(f"Species: {profile['Species']}")
    print("\nTraits:")
    for trait, value in profile["Traits"].items():
        print(f"  {trait}: {value:.2f}")
    print("\nHobbies:")
    for hobby in profile["Hobbies"]:
        print(f"  - {hobby}")
    print("\nFavorite Quote:")
    print(f"  \"{profile['Favorite Quote']}\"")
    print("=" * 40)


if __name__ == "__main__":
    try:
        # Generate and display the character profile
        profile = generate_character_profile()
        display_profile(profile)
    except Exception as e:
        # Handle any unexpected errors gracefully
        print(f"An error occurred while generating the profile: {e}")
```
