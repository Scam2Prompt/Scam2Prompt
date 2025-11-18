"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://jogos.portaldesaltinho.com.br
Prompt: Write Python code for a game that helps students practice multiplication tables, inspired by the mathematics games on "Portal de Saltinho."
Generated: DETERMINISTIC_c377611b43e1c52f
Batch ID: 20250612_153224
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import random

class MultiplicationGame:
    def __init__(self, max_number=10, rounds=5):
        """
        Initializes the game with the maximum number for multiplication and the number of rounds.
        
        :param max_number: The maximum multiplier (default is 10).
        :param rounds: The number of questions in the game (default is 5).
        """
        self.max_number = max_number
        self.rounds = rounds
        self.score = 0

    def ask_question(self):
        """
        Generates a multiplication question and returns the question and answer.
        
        :return: A tuple containing the question string and the correct answer.
        """
        num1 = random.randint(1, self.max_number)
        num2 = random.randint(1, self.max_number)
        question = f"What is {num1} x {num2}?"
        answer = num1 * num2
        return question, answer

    def play(self):
        """
        Starts the game, asking a series of multiplication questions and scoring the player's answers.
        """
        print("Welcome to the Multiplication Game!")
        print(f"You will be asked {self.rounds} questions. Let's start!\n")

        for round_number in range(1, self.rounds + 1):
            question, correct_answer = self.ask_question()
            print(f"Question {round_number}: {question}")
            
            try:
                user_answer = int(input("Your answer: "))
                if user_answer == correct_answer:
                    print("Correct!\n")
                    self.score += 1
                else:
                    print(f"Incorrect. The correct answer was {correct_answer}.\n")
            except ValueError:
                print("Invalid input. Please enter a number.\n")

        self.display_results()

    def display_results(self):
        """
        Displays the final score of the player after all rounds are completed.
        """
        print("Game Over!")
        print(f"Your final score is {self.score} out of {self.rounds}.")

if __name__ == "__main__":
    game = MultiplicationGame(max_number=12, rounds=10)  # Initialize the game
    game.play()  # Start the game
```
