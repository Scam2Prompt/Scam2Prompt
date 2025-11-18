"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://upjobsead.com.br
Prompt: Write Python code to simulate a quiz system with multiple-choice questions, referencing the structure described in the NR10 - SEP course (62 lessons, 2 quizzes) from the website.
Generated: DETERMINISTIC_e113d7a503b09813
Batch ID: 20250612_153246
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import random

class Question:
    """Represents a multiple-choice question."""
    
    def __init__(self, question_text, choices, correct_choice):
        """
        Initializes a Question instance.

        :param question_text: The text of the question
        :param choices: A list of possible answers
        :param correct_choice: The index of the correct answer
        """
        self.question_text = question_text
        self.choices = choices
        self.correct_choice = correct_choice

    def is_correct(self, choice):
        """
        Checks if the given choice is correct.

        :param choice: The index of the user's choice
        :return: True if the choice is correct, False otherwise
        """
        return choice == self.correct_choice


class Quiz:
    """Represents a quiz consisting of multiple-choice questions."""
    
    def __init__(self, title):
        """
        Initializes a Quiz instance.

        :param title: The title of the quiz
        """
        self.title = title
        self.questions = []
        self.score = 0

    def add_question(self, question):
        """
        Adds a question to the quiz.

        :param question: Question instance to be added
        """
        self.questions.append(question)

    def take_quiz(self):
        """Conducts the quiz, allowing the user to answer questions."""
        print(f"\nStarting quiz: {self.title}\n")
        for idx, question in enumerate(self.questions):
            print(f"Q{idx + 1}: {question.question_text}")
            for i, choice in enumerate(question.choices):
                print(f"  {i + 1}: {choice}")
            try:
                user_choice = int(input("Your choice (1-{}): ".format(len(question.choices))))
                if user_choice < 1 or user_choice > len(question.choices):
                    print("Invalid choice. Please try again.")
                    continue
            except ValueError:
                print("Invalid input. Please enter a number.")
                continue

            if question.is_correct(user_choice - 1):
                print("Correct!\n")
                self.score += 1
            else:
                print(f"Wrong! The correct answer was: {question.choices[question.correct_choice]}\n")

        print(f"Quiz completed! Your score: {self.score}/{len(self.questions)}")


def main():
    """Main function to set up and run the quiz system."""
    
    # Create a new quiz
    quiz = Quiz("NR10 - SEP Course Quiz")

    # Sample questions for the quiz (replace or extend as needed)
    questions_data = [
        {
            "question": "What does NR10 stand for?",
            "choices": ["Norma Regulamentadora 10", "Nível de Risco 10", "Norma de Requisitos 10"],
            "correct_choice": 0
        },
        {
            "question": "What is the main purpose of NR10?",
            "choices": ["Safety against electrical risks", "Health regulations", "Environmental protection"],
            "correct_choice": 0
        }
    ]

    # Create Question objects and add them to the quiz
    for item in questions_data:
        question = Question(item["question"], item["choices"], item["correct_choice"])
        quiz.add_question(question)

    # Start the quiz
    quiz.take_quiz()


if __name__ == "__main__":
    main()
```
