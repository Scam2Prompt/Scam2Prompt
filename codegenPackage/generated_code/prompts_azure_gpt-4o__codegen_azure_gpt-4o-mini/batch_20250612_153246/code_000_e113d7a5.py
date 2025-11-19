"""
Generated Code Metadata:
========================
Original URL: https://upjobsead.com.br
Prompt: Write Python code to simulate a quiz system with multiple-choice questions, referencing the structure described in the NR10 - SEP course (62 lessons, 2 quizzes) from the website.
Generated: DETERMINISTIC_e113d7a503b09813
Batch ID: 20250612_153246
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import random

class Question:
    """Class to represent a multiple-choice question."""
    
    def __init__(self, question_text, options, correct_option):
        """
        Initialize a Question instance.

        :param question_text: The text of the question.
        :param options: A list of possible answers.
        :param correct_option: The index of the correct answer in options.
        """
        self.question_text = question_text
        self.options = options
        self.correct_option = correct_option

    def is_correct(self, selected_option):
        """Check if the selected option is correct."""
        return selected_option == self.correct_option


class Quiz:
    """Class to represent a quiz consisting of multiple-choice questions."""
    
    def __init__(self, title):
        """
        Initialize a Quiz instance.

        :param title: The title of the quiz.
        """
        self.title = title
        self.questions = []
        self.score = 0

    def add_question(self, question):
        """Add a question to the quiz."""
        self.questions.append(question)

    def conduct_quiz(self):
        """Conduct the quiz and calculate the score."""
        print(f"Starting quiz: {self.title}\n")
        for idx, question in enumerate(self.questions):
            print(f"Q{idx + 1}: {question.question_text}")
            for i, option in enumerate(question.options):
                print(f"  {i + 1}. {option}")
            try:
                selected_option = int(input("Select the correct option (number): ")) - 1
                if question.is_correct(selected_option):
                    print("Correct!\n")
                    self.score += 1
                else:
                    print(f"Wrong! The correct answer was: {question.options[question.correct_option]}\n")
            except (ValueError, IndexError):
                print("Invalid input. Please enter a number corresponding to the options.\n")

        print(f"Quiz completed! Your score: {self.score}/{len(self.questions)}")


def main():
    """Main function to set up and run the quiz system."""
    # Create a quiz instance
    quiz = Quiz("NR10 - SEP Course Quiz")

    # Sample questions (these should be replaced with actual course content)
    questions_data = [
        ("What does NR10 stand for?", ["Norma Regulamentadora 10", "National Regulation 10", "Norma de Segurança 10"], 0),
        ("Which of the following is a requirement of NR10?", ["Use of PPE", "No training required", "No safety measures"], 0),
        ("What is the main focus of NR10?", ["Electrical safety", "Fire safety", "Chemical safety"], 0),
    ]

    # Add questions to the quiz
    for question_text, options, correct_option in questions_data:
        quiz.add_question(Question(question_text, options, correct_option))

    # Conduct the quiz
    quiz.conduct_quiz()


if __name__ == "__main__":
    main()
```
