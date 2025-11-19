"""
Generated Code Metadata:
========================
Original URL: https://potencia.in
Prompt: Write Python code to simulate a periodic test system for JEE/NEET preparation, incorporating difficulty levels and performance tracking, as described in Potencia Academy's approach.
Generated: DETERMINISTIC_35a65c5734d3f36f
Batch ID: 20250612_142620
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import random
import json
from datetime import datetime

class Question:
    """Class to represent a question in the test system."""
    
    def __init__(self, question_text, options, correct_answer, difficulty_level):
        self.question_text = question_text
        self.options = options
        self.correct_answer = correct_answer
        self.difficulty_level = difficulty_level

    def is_correct(self, answer):
        """Check if the provided answer is correct."""
        return answer == self.correct_answer


class Test:
    """Class to represent a test consisting of multiple questions."""
    
    def __init__(self, questions):
        self.questions = questions
        self.score = 0
        self.total_questions = len(questions)
        self.start_time = None
        self.end_time = None

    def start_test(self):
        """Start the test and record the start time."""
        self.start_time = datetime.now()
        print("Test started!")

    def end_test(self):
        """End the test and record the end time."""
        self.end_time = datetime.now()
        print("Test ended!")

    def take_test(self):
        """Conduct the test by asking questions to the user."""
        self.start_test()
        for question in self.questions:
            print(f"\n{question.question_text}")
            for idx, option in enumerate(question.options, start=1):
                print(f"{idx}. {option}")
            try:
                user_answer = int(input("Select the correct option (1-4): ")) - 1
                if question.is_correct(question.options[user_answer]):
                    print("Correct answer!")
                    self.score += 1
                else:
                    print("Incorrect answer.")
            except (ValueError, IndexError):
                print("Invalid input. Please select a valid option.")
        self.end_test()
        self.display_results()

    def display_results(self):
        """Display the results of the test."""
        print(f"\nYour score: {self.score}/{self.total_questions}")
        print(f"Test duration: {self.end_time - self.start_time}")


class PerformanceTracker:
    """Class to track and store performance data."""
    
    def __init__(self, filename='performance_data.json'):
        self.filename = filename
        self.load_performance_data()

    def load_performance_data(self):
        """Load performance data from a JSON file."""
        try:
            with open(self.filename, 'r') as file:
                self.performance_data = json.load(file)
        except (FileNotFoundError, json.JSONDecodeError):
            self.performance_data = {}

    def save_performance_data(self):
        """Save performance data to a JSON file."""
        with open(self.filename, 'w') as file:
            json.dump(self.performance_data, file, indent=4)

    def update_performance(self, user_id, score):
        """Update the performance data for a user."""
        if user_id not in self.performance_data:
            self.performance_data[user_id] = []
        self.performance_data[user_id].append({
            'score': score,
            'date': datetime.now().isoformat()
        })
        self.save_performance_data()


def create_sample_questions():
    """Create a sample set of questions for the test."""
    return [
        Question("What is the capital of France?", ["Berlin", "Madrid", "Paris", "Rome"], "Paris", "Easy"),
        Question("What is 2 + 2?", ["3", "4", "5", "6"], "4", "Easy"),
        Question("What is the derivative of x^2?", ["x", "2x", "x^2", "2"], "2x", "Medium"),
        Question("What is the integral of 1/x?", ["ln(x)", "x", "1/x^2", "e^x"], "ln(x)", "Medium"),
        Question("What is the value of pi?", ["3.14", "3.15", "3.16", "3.17"], "3.14", "Hard"),
    ]


def main():
    """Main function to run the periodic test system."""
    questions = create_sample_questions()
    test = Test(questions)
    user_id = input("Enter your user ID: ")
    performance_tracker = PerformanceTracker()

    test.take_test()
    performance_tracker.update_performance(user_id, test.score)


if __name__ == "__main__":
    main()
```
