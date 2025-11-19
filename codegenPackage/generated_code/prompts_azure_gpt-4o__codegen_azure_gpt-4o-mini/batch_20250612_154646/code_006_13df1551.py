"""
Generated Code Metadata:
========================
Original URL: https://braindom.xyz
Prompt: Develop a Python script to simulate a creative puzzle where the solution requires unconventional thinking, as highlighted in Braindom's gameplay.
Generated: DETERMINISTIC_13df155149ebccc5
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

class Puzzle:
    def __init__(self, question, answer):
        """
        Initialize a Puzzle instance.

        :param question: The question or riddle to be solved.
        :param answer: The correct answer to the puzzle.
        """
        self.question = question
        self.answer = answer

    def check_answer(self, user_answer):
        """
        Check if the user's answer is correct.

        :param user_answer: The answer provided by the user.
        :return: True if the answer is correct, False otherwise.
        """
        return user_answer.strip().lower() == self.answer.strip().lower()

class PuzzleGame:
    def __init__(self):
        """
        Initialize the PuzzleGame with a list of puzzles.
        """
        self.puzzles = self.load_puzzles()
        self.current_puzzle = None

    def load_puzzles(self):
        """
        Load a list of puzzles.

        :return: A list of Puzzle instances.
        """
        return [
            Puzzle("What has keys but can't open locks?", "piano"),
            Puzzle("I’m tall when I’m young, and I’m short when I’m old. What am I?", "candle"),
            Puzzle("What can travel around the world while staying in a corner?", "stamp"),
            Puzzle("What has to be broken before you can use it?", "egg"),
            Puzzle("I speak without a mouth and hear without ears. I have no body, but I come alive with the wind. What am I?", "echo"),
        ]

    def select_random_puzzle(self):
        """
        Select a random puzzle from the list.

        :return: A randomly selected Puzzle instance.
        """
        return random.choice(self.puzzles)

    def play(self):
        """
        Start the puzzle game.
        """
        print("Welcome to the Creative Puzzle Game!")
        self.current_puzzle = self.select_random_puzzle()
        print(f"Puzzle: {self.current_puzzle.question}")

        user_answer = input("Your answer: ")
        if self.current_puzzle.check_answer(user_answer):
            print("Congratulations! You solved the puzzle.")
        else:
            print(f"Sorry, the correct answer was: {self.current_puzzle.answer}")

if __name__ == "__main__":
    try:
        game = PuzzleGame()
        game.play()
    except Exception as e:
        print(f"An error occurred: {e}")
```
