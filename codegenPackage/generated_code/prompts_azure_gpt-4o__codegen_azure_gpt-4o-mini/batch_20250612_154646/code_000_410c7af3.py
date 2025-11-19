"""
Generated Code Metadata:
========================
Original URL: https://braindom.xyz
Prompt: Write Python code to generate a series of brain teaser puzzles similar to those described on Braindom, including logic-based and creative-thinking challenges.
Generated: DETERMINISTIC_410c7af333794420
Batch ID: 20250612_154646
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import random

class BrainTeaser:
    """Class to represent a brain teaser puzzle."""

    def __init__(self, question, answer):
        """
        Initialize a new brain teaser.

        Args:
            question (str): The question or challenge of the brain teaser.
            answer (str): The correct answer to the brain teaser.
        """
        self.question = question
        self.answer = answer

    def check_answer(self, user_answer):
        """
        Check if the provided answer is correct.

        Args:
            user_answer (str): The answer provided by the user.

        Returns:
            bool: True if the answer is correct, False otherwise.
        """
        return user_answer.strip().lower() == self.answer.strip().lower()


class BrainTeaserGenerator:
    """Class to generate a series of brain teaser puzzles."""

    def __init__(self):
        """Initialize the generator with a list of brain teasers."""
        self.teasers = self._load_teasers()

    def _load_teasers(self):
        """
        Load a predefined list of brain teasers.

        Returns:
            list: A list of BrainTeaser objects.
        """
        return [
            BrainTeaser("What has keys but can't open locks?", "piano"),
            BrainTeaser("I speak without a mouth and hear without ears. What am I?", "echo"),
            BrainTeaser("What can travel around the world while staying in a corner?", "stamp"),
            BrainTeaser("I am not alive, but I can grow. I don't have lungs, but I need air. What am I?", "fire"),
            BrainTeaser("What gets wetter as it dries?", "towel"),
        ]

    def get_random_teaser(self):
        """
        Get a random brain teaser from the list.

        Returns:
            BrainTeaser: A randomly selected brain teaser.
        """
        return random.choice(self.teasers)

    def start_game(self):
        """Start the brain teaser game."""
        print("Welcome to the Brain Teaser Game!")
        teaser = self.get_random_teaser()
        print(f"Teaser: {teaser.question}")

        user_answer = input("Your answer: ")
        if teaser.check_answer(user_answer):
            print("Correct! Well done.")
        else:
            print(f"Wrong! The correct answer was: {teaser.answer}")


if __name__ == "__main__":
    try:
        game = BrainTeaserGenerator()
        game.start_game()
    except Exception as e:
        print(f"An error occurred: {e}")
```
