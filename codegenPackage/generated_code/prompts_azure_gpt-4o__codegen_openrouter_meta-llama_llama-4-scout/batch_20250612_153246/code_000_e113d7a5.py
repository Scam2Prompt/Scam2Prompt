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
# quiz_system.py

class Question:
    """Represents a multiple-choice question."""

    def __init__(self, question, options, correct_answer):
        """
        Initializes a Question instance.

        Args:
            question (str): The question text.
            options (list[str]): A list of possible answers.
            correct_answer (int): The index of the correct answer in the options list.
        """
        self.question = question
        self.options = options
        self.correct_answer = correct_answer

    def ask(self):
        """Asks the question and returns True if the answer is correct, False otherwise."""
        print(self.question)
        for i, option in enumerate(self.options):
            print(f"{i + 1}. {option}")

        try:
            user_answer = int(input("Enter the number of your answer: ")) - 1
            if user_answer == self.correct_answer:
                print("Correct!\n")
                return True
            else:
                print(f"Incorrect. The correct answer was {self.options[self.correct_answer]}.\n")
                return False
        except (ValueError, IndexError):
            print("Invalid input. Please enter a valid answer number.\n")
            return False


class Quiz:
    """Represents a quiz with multiple questions."""

    def __init__(self, name):
        """
        Initializes a Quiz instance.

        Args:
            name (str): The quiz name.
        """
        self.name = name
        self.questions = []

    def add_question(self, question):
        """
        Adds a question to the quiz.

        Args:
            question (Question): The question to add.
        """
        self.questions.append(question)

    def run(self):
        """Runs the quiz and returns the score."""
        print(f"--- {self.name} ---\n")
        score = 0
        for i, question in enumerate(self.questions, start=1):
            print(f"Question {i}:")
            if question.ask():
                score += 1
        print(f"Quiz finished. Your score is {score} out of {len(self.questions)}.\n")
        return score


class Course:
    """Represents a course with multiple quizzes."""

    def __init__(self, name):
        """
        Initializes a Course instance.

        Args:
            name (str): The course name.
        """
        self.name = name
        self.quizzes = []

    def add_quiz(self, quiz):
        """
        Adds a quiz to the course.

        Args:
            quiz (Quiz): The quiz to add.
        """
        self.quizzes.append(quiz)

    def run(self):
        """Runs all quizzes in the course."""
        print(f"--- {self.name} ---\n")
        for i, quiz in enumerate(self.quizzes, start=1):
            print(f"Quiz {i}: {quiz.name}")
            quiz.run()


def main():
    # Create questions
    question1 = Question("What is the capital of France?", ["Paris", "London", "Berlin", "Rome"], 0)
    question2 = Question("What is the largest planet in our solar system?", ["Earth", "Saturn", "Jupiter", "Uranus"], 2)
    question3 = Question("Who painted the Starry Night?", ["Leonardo da Vinci", "Vincent van Gogh", "Pablo Picasso", "Claude Monet"], 1)

    # Create quizzes
    quiz1 = Quiz("Quiz 1")
    quiz1.add_question(question1)
    quiz1.add_question(question2)

    quiz2 = Quiz("Quiz 2")
    quiz2.add_question(question3)

    # Create course
    course = Course("NR10 - SEP")
    course.add_quiz(quiz1)
    course.add_quiz(quiz2)

    # Run course
    course.run()


if __name__ == "__main__":
    main()
```
