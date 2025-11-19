"""
Generated Code Metadata:
========================
Original URL: https://jogos.portaldesaltinho.com.br
Prompt: "Create a Python script to generate interactive math games for kids, similar to those found on the Portal de Saltinho website, focusing on addition and subtraction exercises."
Generated: DETERMINISTIC_b7eead91df7664a7
Batch ID: 20250622_210655
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import random

class MathGame:
    def __init__(self):
        """Initialize the MathGame with a score and a maximum number of questions."""
        self.score = 0
        self.max_questions = 5

    def generate_question(self):
        """Generate a random addition or subtraction question."""
        operation = random.choice(['+', '-'])
        num1 = random.randint(1, 20)
        num2 = random.randint(1, 20)

        if operation == '+':
            answer = num1 + num2
        else:
            # Ensure the result is non-negative for subtraction
            num1, num2 = max(num1, num2), min(num1, num2)
            answer = num1 - num2

        return f"What is {num1} {operation} {num2}?", answer

    def play_game(self):
        """Start the math game and ask a series of questions."""
        print("Welcome to the Math Game! Let's test your addition and subtraction skills.")
        
        for _ in range(self.max_questions):
            question, answer = self.generate_question()
            user_answer = self.get_user_answer(question)

            if user_answer is None:
                print("Exiting the game. Thank you for playing!")
                return

            if user_answer == answer:
                print("Correct! Well done.")
                self.score += 1
            else:
                print(f"Oops! The correct answer was {answer}.")

        self.display_score()

    def get_user_answer(self, question):
        """Prompt the user for an answer and handle potential errors."""
        while True:
            try:
                user_input = input(question + " (or type 'exit' to quit): ")
                if user_input.lower() == 'exit':
                    return None
                return int(user_input)
            except ValueError:
                print("Invalid input. Please enter a number.")

    def display_score(self):
        """Display the final score to the user."""
        print(f"Game over! Your final score is: {self.score}/{self.max_questions}")

if __name__ == "__main__":
    game = MathGame()
    game.play_game()
```
