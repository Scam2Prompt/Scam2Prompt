"""
Generated Code Metadata:
========================
Original URL: https://jogos.portaldesaltinho.com.br
Prompt: Write Python code to create a gamified quiz about hardware and software, inspired by the interactive games on "Portal de Saltinho" for teaching computer science concepts.
Generated: DETERMINISTIC_8dbd1e7d71f3b02f
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

class QuizQuestion:
    """Class to represent a quiz question."""
    
    def __init__(self, question, options, answer):
        """
        Initialize a quiz question.

        :param question: The question text.
        :param options: A list of possible answers.
        :param answer: The correct answer.
        """
        self.question = question
        self.options = options
        self.answer = answer

    def is_correct(self, user_answer):
        """Check if the user's answer is correct."""
        return user_answer == self.answer


class Quiz:
    """Class to manage the quiz game."""
    
    def __init__(self):
        """Initialize the quiz with a set of questions."""
        self.questions = self.load_questions()
        self.score = 0

    def load_questions(self):
        """Load quiz questions."""
        return [
            QuizQuestion("What does CPU stand for?", ["Central Processing Unit", "Computer Personal Unit", "Central Process Unit", "None of the above"], "Central Processing Unit"),
            QuizQuestion("Which of the following is an operating system?", ["Windows", "Python", "Java", "HTML"], "Windows"),
            QuizQuestion("What is the main function of RAM?", ["Store data permanently", "Store data temporarily", "Process data", "None of the above"], "Store data temporarily"),
            QuizQuestion("Which component is considered the brain of the computer?", ["RAM", "CPU", "Hard Drive", "Motherboard"], "CPU"),
            QuizQuestion("What does GPU stand for?", ["Graphics Processing Unit", "General Processing Unit", "Graphical Personal Unit", "None of the above"], "Graphics Processing Unit"),
        ]

    def ask_question(self, question):
        """Ask a question and return whether the answer was correct."""
        print(question.question)
        for idx, option in enumerate(question.options, start=1):
            print(f"{idx}. {option}")
        
        try:
            user_input = int(input("Select the correct option (1-4): "))
            if 1 <= user_input <= len(question.options):
                user_answer = question.options[user_input - 1]
                if question.is_correct(user_answer):
                    print("Correct!\n")
                    return True
                else:
                    print(f"Wrong! The correct answer was: {question.answer}\n")
                    return False
            else:
                print("Invalid option. Please select a number between 1 and 4.\n")
                return False
        except ValueError:
            print("Invalid input. Please enter a number.\n")
            return False

    def start(self):
        """Start the quiz game."""
        print("Welcome to the Hardware and Software Quiz!\n")
        random.shuffle(self.questions)  # Shuffle questions for randomness
        
        for question in self.questions:
            if self.ask_question(question):
                self.score += 1
        
        print(f"Quiz finished! Your score: {self.score}/{len(self.questions)}")


if __name__ == "__main__":
    try:
        quiz = Quiz()
        quiz.start()
    except Exception as e:
        print(f"An error occurred: {e}")
```
