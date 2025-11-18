"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://jogos.portaldesaltinho.com.br
Prompt: Write Python code to create a gamified quiz about hardware and software, inspired by the interactive games on "Portal de Saltinho" for teaching computer science concepts.
Generated: DETERMINISTIC_8dbd1e7d71f3b02f
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

class QuizQuestion:
    """Class representing a single quiz question."""
    
    def __init__(self, question: str, options: list, answer: str):
        """
        Initialize the quiz question.

        :param question: The question text
        :param options: List of possible answers
        :param answer: Correct answer
        """
        self.question = question
        self.options = options
        self.answer = answer

    def check_answer(self, user_answer: str) -> bool:
        """Check if user's answer is correct.

        :param user_answer: The answer provided by the user
        :return: True if the answer is correct, False otherwise
        """
        return user_answer == self.answer

class Quiz:
    """Class to manage the quiz game."""

    def __init__(self, title: str):
        """
        Initialize the quiz.

        :param title: The title of the quiz
        """
        self.title = title
        self.questions = []
        self.score = 0

    def add_question(self, question: QuizQuestion):
        """Add a question to the quiz.

        :param question: The QuizQuestion object to add
        """
        self.questions.append(question)

    def play(self):
        """Conduct the quiz game."""
        print(f"Welcome to the {self.title}!")
        for idx, question in enumerate(self.questions, start=1):
            print(f"\nQuestion {idx}: {question.question}")
            for option in question.options:
                print(f"- {option}")

            user_answer = input("Your answer: ")
            if question.check_answer(user_answer):
                print("Correct!")
                self.score += 1
            else:
                print(f"Wrong! The correct answer was: {question.answer}")

        self.display_score()

    def display_score(self):
        """Display the final score."""
        total_questions = len(self.questions)
        print(f"\nQuiz completed! Your score: {self.score}/{total_questions}")

def main():
    """Main function to run the quiz."""
    # Create a new quiz
    hardware_software_quiz = Quiz("Hardware and Software Quiz")

    # Sample questions
    questions_data = [
        {
            "question": "What does CPU stand for?",
            "options": ["Central Processing Unit", "Computer Personal Unit", "Central Program Unit"],
            "answer": "Central Processing Unit"
        },
        {
            "question": "Which of the following is a type of software?",
            "options": ["Operating System", "Motherboard", "CPU"],
            "answer": "Operating System"
        },
        {
            "question": "What is RAM?",
            "options": ["Read Access Memory", "Random Access Memory", "Run Access Memory"],
            "answer": "Random Access Memory"
        },
        {
            "question": "Which device is used to input data?",
            "options": ["Monitor", "Keyboard", "Printer"],
            "answer": "Keyboard"
        },
        {
            "question": "What does BIOS stand for?",
            "options": ["Basic Input Output System", "Binary Input Output System", "Basic Integrated Operating System"],
            "answer": "Basic Input Output System"
        }
    ]

    # Add questions to the quiz
    for q in questions_data:
        quiz_question = QuizQuestion(q['question'], q['options'], q['answer'])
        hardware_software_quiz.add_question(quiz_question)

    # Start the quiz
    try:
        hardware_software_quiz.play()
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    main()
```
