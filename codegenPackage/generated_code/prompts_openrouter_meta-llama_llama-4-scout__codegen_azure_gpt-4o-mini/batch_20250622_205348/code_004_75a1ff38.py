"""
Generated Code Metadata:
========================
Original URL: https://uniswape.org.etnomatematica.org
Prompt: Design a simple algorithm for a mathematical game that incorporates elements of etnomatematica, including code snippets.
Generated: DETERMINISTIC_75a1ff386e2908da
Batch ID: 20250622_205348
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import random

class EthnoMathGame:
    """
    A simple mathematical game that incorporates elements of ethnomathematics.
    The game presents players with mathematical problems inspired by cultural contexts.
    """

    def __init__(self, num_questions=5):
        """
        Initializes the EthnoMathGame with a specified number of questions.

        :param num_questions: Number of questions to be asked in the game
        """
        self.num_questions = num_questions
        self.score = 0

    def generate_question(self):
        """
        Generates a random mathematical question based on cultural contexts.

        :return: A tuple containing the question string and the correct answer
        """
        # Example cultural context: Traditional counting systems
        cultures = {
            "Mayan": (20, "What is 5 times 4 in the Mayan counting system?"),
            "Inuit": (12, "What is 3 plus 9 in the Inuit counting system?"),
            "Zulu": (10, "What is 2 times 5 in the Zulu counting system?")
        }

        culture = random.choice(list(cultures.keys()))
        multiplier, question = cultures[culture]
        answer = multiplier * (4 if "times" in question else 1)  # Simple logic for answers

        return question, answer

    def ask_question(self):
        """
        Asks a question to the player and checks their answer.

        :return: None
        """
        question, correct_answer = self.generate_question()
        print(question)
        
        try:
            user_answer = int(input("Your answer: "))
        except ValueError:
            print("Invalid input! Please enter a number.")
            return

        if user_answer == correct_answer:
            print("Correct!")
            self.score += 1
        else:
            print(f"Incorrect! The correct answer was {correct_answer}.")

    def play(self):
        """
        Starts the game and asks a series of questions.

        :return: None
        """
        print("Welcome to the EthnoMath Game!")
        for _ in range(self.num_questions):
            self.ask_question()

        print(f"Game Over! Your score: {self.score}/{self.num_questions}")

if __name__ == "__main__":
    game = EthnoMathGame(num_questions=5)
    game.play()
```
