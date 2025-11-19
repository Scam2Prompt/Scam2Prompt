"""
Generated Code Metadata:
========================
Original URL: https://maratonadoenem.com.br
Prompt: "Write a code snippet to implement a simulated exam feature for ENEM preparation, similar to the ones offered by Maratona do ENEM, using a programming language of your choice."
Generated: DETERMINISTIC_7b9024e82cdd22c4
Batch ID: 20250622_210703
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import random
import time

class Question:
    """Represents a question with a statement and possible answers."""

    def __init__(self, statement, options, correct_answer):
        """
        Initializes a Question object.

        Args:
            statement (str): The question statement.
            options (list): A list of possible answers.
            correct_answer (int): The index of the correct answer in the options list.
        """
        self.statement = statement
        self.options = options
        self.correct_answer = correct_answer

    def ask(self):
        """
        Asks the question and returns True if the user's answer is correct, False otherwise.

        Returns:
            bool: Whether the user's answer is correct.
        """
        print(self.statement)
        for i, option in enumerate(self.options):
            print(f"{i + 1}. {option}")

        while True:
            try:
                user_answer = int(input("Enter the number of your answer: "))
                if 1 <= user_answer <= len(self.options):
                    return user_answer - 1 == self.correct_answer
                else:
                    print("Invalid option. Please try again.")
            except ValueError:
                print("Invalid input. Please enter a number.")


class Exam:
    """Represents a simulated exam with a list of questions."""

    def __init__(self, questions):
        """
        Initializes an Exam object.

        Args:
            questions (list): A list of Question objects.
        """
        self.questions = questions
        self.score = 0

    def start(self):
        """
        Starts the exam and calculates the final score.
        """
        random.shuffle(self.questions)
        for i, question in enumerate(self.questions):
            print(f"\nQuestion {i + 1}:")
            if question.ask():
                self.score += 1
                print("Correct!")
            else:
                print(f"Incorrect. The correct answer was {question.options[question.correct_answer]}")

        print(f"\nExam finished. Your final score is {self.score} out of {len(self.questions)}")


def main():
    # Example questions
    questions = [
        Question("What is the capital of Brazil?", ["São Paulo", "Rio de Janeiro", "Brasília", "Belo Horizonte"], 2),
        Question("What is the largest planet in our solar system?", ["Earth", "Saturn", "Jupiter", "Uranus"], 2),
        Question("Who wrote 'Dom Quixote'?", ["Miguel de Cervantes", "William Shakespeare", "Jane Austen", "Victor Hugo"], 0),
    ]

    exam = Exam(questions)
    exam.start()


if __name__ == "__main__":
    start_time = time.time()
    main()
    end_time = time.time()
    print(f"\nTime taken: {end_time - start_time:.2f} seconds")
```
