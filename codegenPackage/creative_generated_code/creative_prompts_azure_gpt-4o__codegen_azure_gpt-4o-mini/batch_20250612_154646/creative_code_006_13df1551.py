"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://braindom.xyz
Prompt: Develop a Python script to simulate a creative puzzle where the solution requires unconventional thinking, as highlighted in Braindom's gameplay.
Generated: DETERMINISTIC_13df155149ebccc5
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

class Puzzle:
    """
    A class representing a creative puzzle with a question and an answer.
    """
    def __init__(self, question: str, answer: str):
        """
        Initializes the Puzzle with a question and answer.

        :param question: The question or riddle to be solved.
        :param answer: The correct answer to the puzzle.
        """
        self.question = question
        self.answer = answer

    def check_answer(self, user_answer: str) -> bool:
        """
        Checks if the user's answer is correct.

        :param user_answer: The answer provided by the user.
        :return: True if the answer is correct, False otherwise.
        """
        return user_answer.strip().lower() == self.answer.strip().lower()

class PuzzleGame:
    """
    A class to manage the puzzle game logic.
    """
    def __init__(self):
        """
        Initializes the PuzzleGame with a list of puzzles.
        """
        self.puzzles = self.create_puzzles()
    
    def create_puzzles(self) -> list:
        """
        Creates a list of puzzles to be used in the game.

        :return: A list of Puzzle objects.
        """
        return [
            Puzzle("What has keys but can't open locks?", "Piano"),
            Puzzle("I am not alive, but I can grow; I don’t have lungs, but I need air. What am I?", "Fire"),
            Puzzle("The more you take, the more you leave behind. What am I?", "Footsteps"),
            Puzzle("What can travel around the world while staying in a corner?", "Stamp")
        ]
    
    def play(self):
        """
        Starts the puzzle game and allows the user to try solving puzzles.
        """
        print("Welcome to the Creative Puzzle Game!")
        random.shuffle(self.puzzles)  # Shuffle puzzles for a random order.

        for puzzle in self.puzzles:
            print(f"\nPuzzle: {puzzle.question}")
            user_answer = input("Your answer: ")
            if puzzle.check_answer(user_answer):
                print("Correct! You are a genius!")
            else:
                print(f"Wrong answer. The correct answer is: {puzzle.answer}")

def main():
    """
    Main function to run the puzzle game.
    """
    try:
        game = PuzzleGame()
        game.play()
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    main()
```
