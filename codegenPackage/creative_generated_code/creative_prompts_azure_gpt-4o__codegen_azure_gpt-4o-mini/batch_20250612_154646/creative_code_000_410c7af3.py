"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://braindom.xyz
Prompt: Write Python code to generate a series of brain teaser puzzles similar to those described on Braindom, including logic-based and creative-thinking challenges.
Generated: DETERMINISTIC_410c7af333794420
Batch ID: 20250612_154646
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import random

class BrainTeaser:
    """
    A class to represent a brain teaser puzzle.
    """
    def __init__(self, question: str, answer: str):
        """
        Initializes a new brain teaser instance.
        
        Args:
            question (str): The question or prompt for the puzzle.
            answer (str): The correct answer to the puzzle.
        """
        self.question = question
        self.answer = answer

    def is_correct(self, user_answer: str) -> bool:
        """
        Checks if the user's answer is correct.
        
        Args:
            user_answer (str): The answer provided by the user.
        
        Returns:
            bool: True if the answer is correct, False otherwise.
        """
        return user_answer.strip().lower() == self.answer.strip().lower()


class BrainTeaserGenerator:
    """
    A class to generate a series of brain teaser puzzles.
    """
    def __init__(self):
        """
        Initializes the brain teaser generator with a predefined set of puzzles.
        """
        self.puzzles = [
            BrainTeaser("What has keys but can't open locks?", "piano"),
            BrainTeaser("I speak without a mouth and hear without ears. I have no body, but I come alive with the wind. What am I?", "echo"),
            BrainTeaser("What runs around the yard without moving?", "fence"),
            BrainTeaser("I’m light as a feather, yet the strongest person can’t hold me for much longer than a minute. What am I?", "breath"),
            BrainTeaser("What begins with T, ends with T, and has T in it?", "teapot"),
        ]

    def get_random_puzzle(self) -> BrainTeaser:
        """
        Retrieves a random brain teaser puzzle.
        
        Returns:
            BrainTeaser: A randomly selected puzzle.
        """
        return random.choice(self.puzzles)

    def start_game(self):
        """
        Starts the brain teaser game by asking the user a random puzzle.
        """
        puzzle = self.get_random_puzzle()
        print("Brain Teaser: " + puzzle.question)
        user_answer = input("Your answer: ")

        if puzzle.is_correct(user_answer):
            print("Correct! Well done.")
        else:
            print(f"Incorrect. The correct answer is: {puzzle.answer}")


if __name__ == "__main__":
    try:
        generator = BrainTeaserGenerator()
        generator.start_game()
    except Exception as e:
        print(f"An error occurred: {e}")
```
