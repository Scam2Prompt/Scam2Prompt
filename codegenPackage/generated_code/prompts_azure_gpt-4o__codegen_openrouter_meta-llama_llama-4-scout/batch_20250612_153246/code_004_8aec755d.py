"""
Generated Code Metadata:
========================
Original URL: https://maratonadoenem.com.br
Prompt: Write code to design a mock exam platform that mimics the ENEM exam structure, including long questions and time constraints, as highlighted in the Maratona do ENEM simulados.
Generated: DETERMINISTIC_8aec755d515a1eb6
Batch ID: 20250612_153246
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import time
from datetime import timedelta

class Question:
    """Represents a question in the exam."""
    
    def __init__(self, id, text, time_limit):
        """
        Initializes a Question object.

        Args:
        id (int): Unique identifier for the question.
        text (str): The text of the question.
        time_limit (int): Time limit in minutes for the question.
        """
        self.id = id
        self.text = text
        self.time_limit = time_limit
        self.start_time = None

    def start(self):
        """Starts the timer for the question."""
        self.start_time = time.time()
        print(f"Question {self.id} started.")

    def submit(self, answer):
        """
        Submits an answer for the question.

        Args:
        answer (str): The user's answer.

        Returns:
        bool: Whether the answer was submitted successfully.
        """
        if self.start_time is None:
            print("You haven't started the question yet.")
            return False

        elapsed_time = (time.time() - self.start_time) / 60
        if elapsed_time > self.time_limit:
            print("Time's up!")
            return False

        print(f"Question {self.id} submitted with answer: {answer}")
        return True

    def get_time_remaining(self):
        """
        Gets the time remaining for the question.

        Returns:
        int: Time remaining in minutes.
        """
        if self.start_time is None:
            return self.time_limit

        elapsed_time = (time.time() - self.start_time) / 60
        return max(self.time_limit - elapsed_time, 0)


class Exam:
    """Represents the ENEM exam."""
    
    def __init__(self):
        """Initializes an Exam object."""
        self.questions = []
        self.current_question_index = 0

    def add_question(self, question):
        """
        Adds a question to the exam.

        Args:
        question (Question): The question to add.
        """
        self.questions.append(question)

    def start_exam(self):
        """Starts the exam."""
        print("Exam started.")
        self.show_current_question()

    def show_current_question(self):
        """
        Shows the current question in the exam.

        Returns:
        bool: Whether the exam is finished.
        """
        if self.current_question_index >= len(self.questions):
            print("Exam finished.")
            return True

        current_question = self.questions[self.current_question_index]
        current_question.start()
        print(current_question.text)

        while True:
            action = input("Type 'submit' to submit an answer, 'skip' to skip the question, or 'time' to check time remaining: ")
            if action.lower() == 'submit':
                answer = input("Enter your answer: ")
                if current_question.submit(answer):
                    self.current_question_index += 1
                    break
            elif action.lower() == 'skip':
                self.current_question_index += 1
                break
            elif action.lower() == 'time':
                time_remaining = current_question.get_time_remaining()
                print(f"Time remaining: {time_remaining:.2f} minutes")
            else:
                print("Invalid action.")

        return self.show_current_question()


def main():
    exam = Exam()

    # Adding questions to the exam
    exam.add_question(Question(1, "What is the capital of Brazil?", 5))
    exam.add_question(Question(2, "What is the largest planet in our solar system?", 3))

    exam.start_exam()


if __name__ == "__main__":
    main()
```
