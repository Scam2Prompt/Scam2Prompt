"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://fun-virtuals-agent.pages.dev
Prompt: Create a script to generate detailed character profiles for virtual agents, including personality, appearance, and emotional traits, based on the examples provided on the Fun Virtuals Agent site.
Generated: DETERMINISTIC_7114217cc4beb0c5
Batch ID: 20250612_154016
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import random

# Constants for generating profiles
PERSONALITY_TRAITS = [
    "optimistic", "pessimistic", "adventurous", "calm", "extroverted",
    "introverted", "creative", "analytical", "empathetic", "assertive"
]

APPEARANCE_FEATURES = [
    "blonde hair", "brown hair", "black hair", "red hair", "curly hair",
    "straight hair", "blue eyes", "green eyes", "brown eyes", "slim build",
    "athletic build", "tall", "short", "freckles", "glasses"
]

EMOTIONAL_TRAITS = [
    "cheerful", "moody", "resilient", "sensitive", "stoic",
    "temperamental", "calm under pressure", "easily stressed",
    "kind-hearted", "determined"
]

# Function to generate a random character profile
def generate_character_profile(name):
    """
    Generate a detailed character profile for virtual agents.

    Args:
        name (str): The name of the virtual agent.

    Returns:
        dict: A dictionary containing the character's name, personality,
              appearance, and emotional traits.
    """
    try:
        # Randomly select traits for the character
        personality = random.choice(PERSONALITY_TRAITS)
        appearance = random.sample(APPEARANCE_FEATURES, 3)  # Select 3 features
        emotional_traits = random.sample(EMOTIONAL_TRAITS, 2)  # Select 2 traits

        # Create the profile as a dictionary
        profile = {
            "name": name,
            "personality": personality,
            "appearance": appearance,
            "emotional_traits": emotional_traits
        }

        return profile
    except Exception as e:
        # Handle unexpected errors
        return {"error": f"An error occurred while generating the profile: {e}"}

# Function to display the character profile
def display_character_profile(profile):
    """
    Display the character profile in a user-friendly format.

    Args:
        profile (dict): The character profile dictionary.
    """
    if "error" in profile:
        print(profile["error"])
        return

    print("\nCharacter Profile")
    print("=================")
    print(f"Name: {profile['name']}")
    print(f"Personality: {profile['personality']}")
    print(f"Appearance: {', '.join(profile['appearance'])}")
    print(f"Emotional Traits: {', '.join(profile['emotional_traits'])}")

# Main entry point of the script
if __name__ == "__main__":
    try:
        # Prompt user for the character's name
        agent_name = input("Enter the name of the virtual agent: ").strip()

        # Validate that the name is not empty
        if not agent_name:
            raise ValueError("The name of the virtual agent cannot be empty.")

        # Generate and display the profile
        profile = generate_character_profile(agent_name)
        display_character_profile(profile)
    except ValueError as ve:
        # Handle specific input validation error
        print(f"Input Error: {ve}")
    except Exception as e:
        # Handle other unexpected errors gracefully
        print(f"An unexpected error occurred: {e}")
```
