"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://maratonadoenem.com.br
Prompt: Write code to design a mock exam platform that mimics the ENEM exam structure, including long questions and time constraints, as highlighted in the Maratona do ENEM simulados.
Generated: DETERMINISTIC_8aec755d515a1eb6
Batch ID: 20250612_153246
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import time
from datetime import datetime, timedelta

class Question:
    """Represents a single question in the exam."""
    
    def __init__(self, prompt: str, answer: str):
        self.prompt = prompt
        self.answer = answer

    def __str__(self):
        return self.prompt

class Exam:
    """Represents the mock exam platform."""
    
    def __init__(self, duration_minutes: int):
        self.duration = timedelta(minutes=duration_minutes)
        self.questions = []
        self.start_time = None
        self.end_time = None
        self.responses = {}

    def add_question(self, question: Question):
        """Add a question to the exam."""
        self.questions.append(question)

    def start_exam(self):
        """Starts the exam and sets the start and end time."""
        self.start_time = datetime.now()
        self.end_time = self.start_time + self.duration
        print(f"Exam started at {self.start_time.strftime('%H:%M:%S')} and will end at {self.end_time.strftime('%H:%M:%S')}.")

    def submit_answer(self, question_index: int, answer: str):
        """Submit an answer for a specific question."""
        if self.start_time is None:
            raise Exception("Exam has not started yet. Please start the exam first.")
        
        if datetime.now() > self.end_time:
            raise Exception("Time is up! You cannot submit an answer anymore.")

        if 0 <= question_index < len(self.questions):
            self.responses[question_index] = answer
            print(f"Answer for question {question_index + 1} submitted.")
        else:
            raise IndexError("Question index out of range.")

    def get_remaining_time(self):
        """Calculate and return the remaining time of the exam."""
        if self.start_time is None:
            raise Exception("Exam has not started yet.")
        
        remaining = self.end_time - datetime.now()

        if remaining.total_seconds() < 0:
            remaining = timedelta(0)

        return remaining

    def finish_exam(self):
        """Finish the exam and display results."""
        if self.start_time is None:
            raise Exception("Exam has not started yet.")
        
        if datetime.now() <= self.end_time:
            print("You have finished the exam early. Time is still remaining.")
        else:
            print("The exam has ended.")

        print("\nYour responses:")
        for index, answer in self.responses.items():
            print(f"Question {index + 1}: Answered - {answer}")

# Example usage
if __name__ == "__main__":
    try:
        # Create a mock exam with a duration of 30 minutes
        exam = Exam(duration_minutes=30)

        # Add questions to the exam
        exam.add_question(Question("What is the capital of Brazil?", "Brasilia"))
        exam.add_question(Question("Explain the process of photosynthesis.", "Photosynthesis is..."))

        # Start the exam
        exam.start_exam()

        # Simulate answering questions (these would happen over time)
        time.sleep(2)  # Simulating time taken to answer
        exam.submit_answer(0, "Brasilia")

        time.sleep(2)  # Simulating time taken to answer
        exam.submit_answer(1, "Photosynthesis is...")

        # Check remaining time
        print(f"Remaining time: {exam.get_remaining_time()}")

        # Finish the exam
        exam.finish_exam()

    except Exception as e:
        print(f"An error occurred: {e}")
```
