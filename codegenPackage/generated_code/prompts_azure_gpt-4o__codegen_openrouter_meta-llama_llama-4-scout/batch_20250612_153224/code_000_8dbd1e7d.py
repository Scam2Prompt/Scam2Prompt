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
# Import required libraries
import random

# Define a class for Quiz questions
class Question:
    def __init__(self, question, options, answer):
        """
        Initialize a Question object.

        Args:
            question (str): The question text.
            options (list): A list of possible answers.
            answer (str): The correct answer.
        """
        self.question = question
        self.options = options
        self.answer = answer

# Define a class for the Quiz
class Quiz:
    def __init__(self):
        """
        Initialize a Quiz object with a list of questions.
        """
        self.questions = [
            Question("What is the brain of the computer?", ["CPU", "RAM", "GPU", "Motherboard"], "CPU"),
            Question("What is the primary function of RAM?", ["Storage", "Processing", "Memory", "Input/Output"], "Memory"),
            Question("What is an example of software?", ["Keyboard", "Mouse", "Operating System", "Monitor"], "Operating System"),
            Question("What is the function of a Graphics Card?", ["Processing", "Storage", "Graphics Rendering", "Sound Output"], "Graphics Rendering"),
            Question("What is an example of hardware?", ["Web Browser", "Operating System", "CPU", "Text Editor"], "CPU"),
        ]
        self.score = 0

    def ask_question(self, question):
        """
        Ask a question and check the user's answer.

        Args:
            question (Question): The question to ask.

        Returns:
            bool: True if the answer is correct, False otherwise.
        """
        print(question.question)
        for i, option in enumerate(question.options):
            print(f"{i+1}. {option}")
        user_answer = input("Enter the number of your answer: ")
        try:
            user_answer = int(user_answer)
            if user_answer < 1 or user_answer > len(question.options):
                raise ValueError
            if question.options[user_answer-1] == question.answer:
                print("Correct!\n")
                return True
            else:
                print(f"Incorrect. The correct answer is {question.answer}.\n")
                return False
        except (ValueError, IndexError):
            print("Invalid input. Please enter a number corresponding to an option.\n")
            return False

    def run_quiz(self):
        """
        Run the quiz and keep track of the score.
        """
        random_questions = random.sample(self.questions, len(self.questions))
        for question in random_questions:
            if self.ask_question(question):
                self.score += 1
        print(f"Quiz finished. Your final score is {self.score}/{len(self.questions)}")

# Run the quiz
if __name__ == "__main__":
    quiz = Quiz()
    quiz.run_quiz()
```
