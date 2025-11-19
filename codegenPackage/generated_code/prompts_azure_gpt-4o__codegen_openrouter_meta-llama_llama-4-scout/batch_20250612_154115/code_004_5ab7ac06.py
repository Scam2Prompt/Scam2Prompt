"""
Generated Code Metadata:
========================
Original URL: https://swap.depillama.com
Prompt: Develop a program that generates science fiction story prompts based on the cosmic exploration themes and characters from Swap Llama.
Generated: DETERMINISTIC_5ab7ac068f52c4d5
Batch ID: 20250612_154115
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import random

# Define a list of cosmic exploration themes
themes = [
    "space station discovery",
    "abandoned planet exploration",
    "alien artifact retrieval",
    "interstellar travel",
    "cosmic anomaly investigation"
]

# Define a list of characters from Swap Llama
characters = [
    "Llama",
    "Swap",
    "Captain Orion",
    "Astronaut Alex",
    "Galactic Guide Gary"
]

# Define a list of story settings
settings = [
    "a distant galaxy",
    "a remote planet",
    "a space station on the edge of the universe",
    "a futuristic city on a space colony",
    "a mysterious asteroid field"
]

# Define a list of plot twists
plot_twists = [
    "a hidden enemy is revealed",
    "a valuable resource is discovered",
    "a traitor is exposed",
    "a natural disaster occurs",
    "a surprising ally is encountered"
]

def generate_story_prompt():
    """
    Generates a science fiction story prompt based on cosmic exploration themes and characters from Swap Llama.
    
    Returns:
        str: A story prompt
    """
    try:
        theme = random.choice(themes)
        character = random.choice(characters)
        setting = random.choice(settings)
        plot_twist = random.choice(plot_twists)
        
        # Create a story prompt
        prompt = f"In {setting}, {character} embarks on a mission for {theme}. However, things take a turn when {plot_twist}."
        return prompt
    
    except Exception as e:
        # Handle any exceptions
        print(f"An error occurred: {e}")
        return None

def main():
    # Generate and print a story prompt
    prompt = generate_story_prompt()
    if prompt:
        print("Story Prompt:")
        print(prompt)

if __name__ == "__main__":
    main()
```
