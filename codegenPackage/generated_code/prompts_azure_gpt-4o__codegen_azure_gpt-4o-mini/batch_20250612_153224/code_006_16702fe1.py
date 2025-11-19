"""
Generated Code Metadata:
========================
Original URL: https://jogos.portaldesaltinho.com.br
Prompt: Develop a gamified quiz in Python to teach the functions of computer keyboard keys, referencing the interactive informatics games on "Portal de Saltinho."
Generated: DETERMINISTIC_16702fe1234d0620
Batch ID: 20250612_153224
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import random

class QuizGame:
    def __init__(self):
        """Initialize the quiz game with questions and score."""
        self.questions = {
            "What does the 'Enter' key do?": "Submits input or executes a command.",
            "What is the function of the 'Esc' key?": "Closes a dialog or exits a program.",
            "What does the 'Ctrl' key do?": "Used in combination with other keys for shortcuts.",
            "What is the purpose of the 'Alt' key?": "Used to access alternate functions of other keys.",
            "What does the 'Backspace' key do?": "Deletes the character to the left of the cursor.",
            "What is the function of the 'Tab' key?": "Moves the cursor to the next tab stop or field.",
            "What does the 'Shift' key do?": "Used to type capital letters or alternate characters.",
            "What is the purpose of the 'Delete' key?": "Deletes the character to the right of the cursor.",
            "What does the 'Space' key do?": "Inserts a space character.",
            "What is the function of the 'F1' key?": "Typically opens the help menu."
        }
        self.score = 0

    def ask_question(self):
        """Randomly select a question and return it with the correct answer."""
        question, answer = random.choice(list(self.questions.items()))
        return question, answer

    def play(self):
        """Main method to run the quiz game."""
        print("Welcome to the Keyboard Functions Quiz!")
        print("Type 'exit' to quit the game at any time.\n")

        while True:
            question, answer = self.ask_question()
            print(question)
            user_answer = input("Your answer: ").strip()

            if user_answer.lower() == 'exit':
                print("Thanks for playing! Your final score is:", self.score)
                break

            if user_answer.lower() == answer.lower():
                print("Correct!\n")
                self.score += 1
            else:
                print(f"Incorrect! The correct answer is: {answer}\n")

            print(f"Current Score: {self.score}\n")

if __name__ == "__main__":
    try:
        game = QuizGame()
        game.play()
    except Exception as e:
        print(f"An error occurred: {e}")
```
