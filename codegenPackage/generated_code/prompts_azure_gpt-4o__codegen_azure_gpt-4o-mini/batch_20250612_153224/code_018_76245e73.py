"""
Generated Code Metadata:
========================
Original URL: https://jogos.portaldesaltinho.com.br
Prompt: Create Python code for a gamified quiz that tests knowledge of Microsoft Word shortcuts, inspired by the informatics games on "Portal de Saltinho."
Generated: DETERMINISTIC_76245e73c05bcdf2
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
    
    def __init__(self, question: str, options: list, answer: str):
        """
        Initialize a quiz question.

        :param question: The quiz question text.
        :param options: A list of possible answers.
        :param answer: The correct answer.
        """
        self.question = question
        self.options = options
        self.answer = answer

    def is_correct(self, user_answer: str) -> bool:
        """Check if the user's answer is correct."""
        return user_answer.strip().lower() == self.answer.strip().lower()


class Quiz:
    """Class to manage the quiz game."""
    
    def __init__(self):
        """Initialize the quiz with questions."""
        self.questions = self.load_questions()
        self.score = 0

    def load_questions(self) -> list:
        """Load quiz questions."""
        return [
            QuizQuestion("What is the shortcut for 'Copy' in Microsoft Word?", ["Ctrl+C", "Ctrl+V", "Ctrl+X"], "Ctrl+C"),
            QuizQuestion("What is the shortcut for 'Paste' in Microsoft Word?", ["Ctrl+C", "Ctrl+V", "Ctrl+X"], "Ctrl+V"),
            QuizQuestion("What is the shortcut for 'Undo' in Microsoft Word?", ["Ctrl+Z", "Ctrl+Y", "Ctrl+A"], "Ctrl+Z"),
            QuizQuestion("What is the shortcut for 'Save' in Microsoft Word?", ["Ctrl+S", "Ctrl+P", "Ctrl+N"], "Ctrl+S"),
            QuizQuestion("What is the shortcut for 'Select All' in Microsoft Word?", ["Ctrl+A", "Ctrl+S", "Ctrl+D"], "Ctrl+A"),
        ]

    def ask_question(self, question: QuizQuestion) -> None:
        """Ask a question and get the user's answer."""
        print(question.question)
        for idx, option in enumerate(question.options, start=1):
            print(f"{idx}. {option}")
        
        try:
            user_input = int(input("Select the correct option (1-3): "))
            if 1 <= user_input <= len(question.options):
                user_answer = question.options[user_input - 1]
                if question.is_correct(user_answer):
                    print("Correct!\n")
                    self.score += 1
                else:
                    print(f"Wrong! The correct answer was: {question.answer}\n")
            else:
                print("Invalid option. Please select a number from the list.\n")
        except ValueError:
            print("Invalid input. Please enter a number.\n")

    def start_quiz(self) -> None:
        """Start the quiz game."""
        print("Welcome to the Microsoft Word Shortcuts Quiz!\n")
        random.shuffle(self.questions)  # Shuffle questions for randomness
        for question in self.questions:
            self.ask_question(question)
        
        print(f"Quiz finished! Your score: {self.score}/{len(self.questions)}")


if __name__ == "__main__":
    try:
        quiz = Quiz()
        quiz.start_quiz()
    except Exception as e:
        print(f"An error occurred: {e}")
```
