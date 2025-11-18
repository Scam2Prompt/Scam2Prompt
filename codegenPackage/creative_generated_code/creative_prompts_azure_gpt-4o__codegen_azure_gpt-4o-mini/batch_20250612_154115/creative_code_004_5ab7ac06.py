"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://swap.depillama.com
Prompt: Develop a program that generates science fiction story prompts based on the cosmic exploration themes and characters from Swap Llama.
Generated: DETERMINISTIC_5ab7ac068f52c4d5
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

class StoryPromptGenerator:
    def __init__(self):
        # List of cosmic themes for the story prompts
        self.themes = [
            "intergalactic diplomacy",
            "alien civilizations encountering humans",
            "a cosmic anomaly threatening the universe",
            "the discovery of an ancient artifact in space",
            "space pirates and their treasure hunt",
            "a race against time to save a dying planet",
            "exploring the multiverse and parallel dimensions",
            "the first contact with a telepathic species",
            "a sentient spaceship on a quest for identity",
            "the ethics of terraforming a new world"
        ]

        # List of potential characters for the story prompts
        self.characters = [
            "a rogue scientist with a hidden agenda",
            "an alien ambassador trying to broker peace",
            "a young astronaut on their first mission",
            "a space explorer haunted by their past",
            "a robot with the ability to feel emotions",
            "a telepathic child with extraordinary powers",
            "a cynical captain of a salvage ship",
            "an artificial intelligence questioning its purpose",
            "a warrior from a lost civilization",
            "a diplomat from an advanced alien race"
        ]

    def generate_prompt(self):
        """
        Generates a random story prompt by selecting a theme and a character.
        
        Returns:
            str: A formatted story prompt.
        """
        try:
            theme = random.choice(self.themes)
            character = random.choice(self.characters)
            return f"Prompt: {character} encounters a challenge involving {theme}."
        except Exception as e:
            # Handle any unexpected errors that may occur
            return f"Error generating prompt: {str(e)}"

    def display_prompt(self):
        """
        Displays the generated story prompt to the user.
        """
        prompt = self.generate_prompt()
        print(prompt)


if __name__ == "__main__":
    # Create an instance of the StoryPromptGenerator
    prompt_generator = StoryPromptGenerator()
    
    # Generate and display a story prompt
    prompt_generator.display_prompt()
```
