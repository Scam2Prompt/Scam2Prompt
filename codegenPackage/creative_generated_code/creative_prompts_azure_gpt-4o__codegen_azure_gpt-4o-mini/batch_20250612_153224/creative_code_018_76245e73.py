"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://jogos.portaldesaltinho.com.br
Prompt: Create Python code for a gamified quiz that tests knowledge of Microsoft Word shortcuts, inspired by the informatics games on "Portal de Saltinho."
Generated: DETERMINISTIC_76245e73c05bcdf2
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
    """Class to represent a quiz question."""
    
    def __init__(self, question, options, answer):
        self.question = question
        self.options = options
        self.answer = answer

    def is_correct(self, user_answer):
        """Check if the provided answer is correct."""
        return self.answer == user_answer

class Quiz:
    """Class to manage the quiz game."""
    
    def __init__(self):
        self.questions = []
        self.score = 0
        self.current_question_index = 0

    def load_questions(self):
        """Load quiz questions into the quiz."""
        self.questions = [
            QuizQuestion(
                "What shortcut opens the 'Save As' dialog?",
                ["Ctrl + S", "Ctrl + A", "F12", "Ctrl + O"],
                "F12"
            ),
            QuizQuestion(
                "What shortcut is used to copy selected text?",
                ["Ctrl + X", "Ctrl + C", "Ctrl + V", "Ctrl + P"],
                "Ctrl + C"
            ),
            QuizQuestion(
                "Which shortcut will paste the copied text?",
                ["Ctrl + X", "Ctrl + C", "Ctrl + V", "Ctrl + Z"],
                "Ctrl + V"
            ),
            QuizQuestion(
                "What shortcut will undo the last action?",
                ["Ctrl + Z", "Ctrl + Y", "Ctrl + A", "Ctrl + S"],
                "Ctrl + Z"
            ),
            QuizQuestion(
                "What key combination will select all text in a document?",
                ["Ctrl + A", "Ctrl + S", "Ctrl + P", "Ctrl + C"],
                "Ctrl + A"
            )
        ]
        random.shuffle(self.questions)  # Shuffle questions for randomness

    def ask_question(self):
        """Ask the current question to the user and get their answer."""
        if self.current_question_index >= len(self.questions):
            print("No more questions available.")
            return False

        question = self.questions[self.current_question_index]
        print(f"\nQuestion {self.current_question_index + 1}: {question.question}")
        for idx, option in enumerate(question.options, start=1):
            print(f"{idx}. {option}")

        try:
            user_input = int(input("Select your answer (1-4): ")) - 1
            if user_input < 0 or user_input >= len(question.options):
                raise ValueError("Invalid choice. Please select a number between 1 and 4.")
            
            if question.is_correct(question.options[user_input]):
                print("Correct answer!")
                self.score += 1
            else:
                print(f"Wrong answer! The correct answer was: {question.answer}")
            
            self.current_question_index += 1
            return True
        except ValueError as e:
            print(f"Error: {e}")
            return True  # Continue asking questions

    def show_score(self):
        """Display the user's final score."""
        print(f"\nYour final score is: {self.score} out of {len(self.questions)}")

def main():
    """Main function to run the quiz."""
    quiz = Quiz()
    quiz.load_questions()

    print("Welcome to the Microsoft Word Shortcuts Quiz!")
    
    while quiz.ask_question():
        pass

    quiz.show_score()

if __name__ == "__main__":
    main()
```
