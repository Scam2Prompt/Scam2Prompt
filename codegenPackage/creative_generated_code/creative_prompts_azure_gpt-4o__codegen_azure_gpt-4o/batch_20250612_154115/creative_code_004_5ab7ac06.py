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

def generate_scifi_prompt():
    """
    Generates a random science fiction story prompt based on cosmic exploration themes 
    and characters from Swap Llama.

    Returns:
        str: A science fiction story prompt.
    """
    # Define lists of cosmic themes, characters, and plot elements
    themes = [
        "a quest to explore the edge of the known universe",
        "searching for habitable planets in a distant galaxy",
        "encountering mysterious cosmic phenomena",
        "a mission to recover lost alien artifacts",
        "an interstellar race against time"
    ]
    
    characters = [
        "a daring space pilot", 
        "a brilliant but eccentric astrophysicist",
        "an adventurous Swap Llama explorer",
        "a rogue AI with a hidden agenda",
        "a wise alien diplomat"
    ]
    
    challenges = [
        "facing hostile alien creatures",
        "navigating through a deadly asteroid field",
        "decoding cryptic messages from an ancient civilization",
        "overcoming internal crew conflicts",
        "dealing with a malfunctioning spaceship"
    ]
    
    # Randomly select one item from each category to form a story prompt
    theme = random.choice(themes)
    character = random.choice(characters)
    challenge = random.choice(challenges)
    
    # Combine the selected elements into a coherent story prompt
    prompt = f"In a story about {theme}, {character} must overcome {challenge}."
    return prompt


def main():
    """
    Main function to generate and display science fiction story prompts.
    """
    try:
        # Generate and display 5 random story prompts
        print("Science Fiction Story Prompts:\n")
        for _ in range(5):
            prompt = generate_scifi_prompt()
            print(f"- {prompt}")
    except Exception as e:
        # Handle unexpected errors
        print(f"An error occurred while generating story prompts: {e}")

        
if __name__ == "__main__":
    # Entry point of the program
    main()
```
