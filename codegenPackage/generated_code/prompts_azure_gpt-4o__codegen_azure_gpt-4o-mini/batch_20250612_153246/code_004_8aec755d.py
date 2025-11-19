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
    """Class to represent a single question in the exam."""
    
    def __init__(self, question_text, options=None, correct_answer=None):
        """
        Initialize a question with text, options, and the correct answer.
        
        :param question_text: The text of the question.
        :param options: A list of possible answers (for multiple choice).
        :param correct_answer: The correct answer for validation.
        """
        self.question_text = question_text
        self.options = options or []
        self.correct_answer = correct_answer

    def is_correct(self, answer):
        """Check if the provided answer is correct."""
        return answer == self.correct_answer


class Exam:
    """Class to represent the exam structure and logic."""
    
    def __init__(self, duration_minutes):
        """
        Initialize the exam with a specified duration.
        
        :param duration_minutes: Duration of the exam in minutes.
        """
        self.questions = []
        self.duration = timedelta(minutes=duration_minutes)
        self.start_time = None
        self.end_time = None

    def add_question(self, question):
        """Add a question to the exam."""
        if not isinstance(question, Question):
            raise ValueError("Only Question instances can be added.")
        self.questions.append(question)

    def start_exam(self):
        """Start the exam timer."""
        self.start_time = time.time()
        self.end_time = self.start_time + self.duration.total_seconds()

    def time_remaining(self):
        """Calculate the remaining time for the exam."""
        if self.start_time is None:
            raise RuntimeError("Exam has not been started yet.")
        remaining = self.end_time - time.time()
        return max(0, remaining)

    def is_time_up(self):
        """Check if the exam time is up."""
        return time.time() >= self.end_time

    def take_exam(self):
        """Simulate taking the exam."""
        if self.start_time is not None:
            raise RuntimeError("Exam is already in progress.")
        
        self.start_exam()
        answers = []
        
        for question in self.questions:
            if self.is_time_up():
                print("Time is up! You cannot answer more questions.")
                break
            
            print(question.question_text)
            if question.options:
                for idx, option in enumerate(question.options):
                    print(f"{idx + 1}. {option}")
            
            answer = input("Your answer: ")
            answers.append(answer)

        return answers


class ExamPlatform:
    """Class to represent the mock exam platform."""
    
    def __init__(self):
        """Initialize the exam platform."""
        self.exams = []

    def create_exam(self, duration_minutes):
        """Create a new exam with a specified duration."""
        exam = Exam(duration_minutes)
        self.exams.append(exam)
        return exam

    def list_exams(self):
        """List all created exams."""
        return self.exams


# Example usage
if __name__ == "__main__":
    platform = ExamPlatform()
    
    # Create a new exam with a 30-minute duration
    exam = platform.create_exam(30)
    
    # Add questions to the exam
    exam.add_question(Question("What is the capital of France?", ["Berlin", "Madrid", "Paris", "Lisbon"], "Paris"))
    exam.add_question(Question("What is 2 + 2?", [], "4"))  # Long answer question
    
    # Start the exam and take it
    try:
        answers = exam.take_exam()
        print("Your answers:", answers)
    except Exception as e:
        print(f"An error occurred: {e}")
```
