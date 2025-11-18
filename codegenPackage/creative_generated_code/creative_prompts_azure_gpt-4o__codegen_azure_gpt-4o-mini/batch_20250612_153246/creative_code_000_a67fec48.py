"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://maratonadoenem.com.br
Prompt: Write Python code to simulate a timed ENEM-style exam with multiple-choice questions, incorporating TRI (Item Response Theory) scoring methodology as described in the Maratona do ENEM approach.
Generated: DETERMINISTIC_a67fec48f7e628e8
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
import random
from typing import List, Dict, Tuple

class Question:
    """Represents a multiple-choice question."""
    
    def __init__(self, question_text: str, options: List[str], correct_option: int, difficulty: float):
        self.question_text = question_text
        self.options = options
        self.correct_option = correct_option
        self.difficulty = difficulty

    def is_correct(self, answer: int) -> bool:
        """Check if the provided answer index is correct."""
        return answer == self.correct_option

class Exam:
    """Simulates a timed exam with multiple-choice questions."""
    
    def __init__(self, questions: List[Question], total_time: int):
        self.questions = questions
        self.total_time = total_time  # Total time allowed in seconds
        self.start_time = None
        self.end_time = None
        self.score = 0
        self.attempted_questions = 0

    def start_exam(self):
        """Starts the exam timer and handles the exam process."""
        self.start_time = time.time()
        self.end_time = self.start_time + self.total_time
        for index, question in enumerate(self.questions):
            if self.time_remaining() <= 0:
                print("Time's up!")
                break

            print(f"Question {index + 1}: {question.question_text}")
            for i, option in enumerate(question.options):
                print(f"{i + 1}. {option}")

            try:
                answer = int(input("Your answer (number): ")) - 1
                if answer < 0 or answer >= len(question.options):
                    print("Invalid option! Please try again.")
                    continue
            except ValueError:
                print("Invalid input! Please enter a number.")
                continue

            if question.is_correct(answer):
                self.score += self.calculate_score(question)
                print("Correct!\n")
            else:
                print("Incorrect.\n")
            self.attempted_questions += 1

    def calculate_score(self, question: Question) -> float:
        """Calculates the score based on Item Response Theory."""
        # Simple TRI scoring; in practice, this could be more complex
        return 1 - question.difficulty

    def time_remaining(self) -> float:
        """Returns the remaining time in the exam."""
        return max(0, self.end_time - time.time())

    def get_results(self) -> Dict[str, float]:
        """Returns the exam results including score and number of questions attempted."""
        return {
            "score": self.score,
            "attempted_questions": self.attempted_questions,
            "total_questions": len(self.questions),
            "percentage": (self.score / len(self.questions)) * 100 if self.questions else 0
        }

def main():
    """Main function to set up and run the exam."""
    # Sample questions for the exam
    questions = [
        Question("What is 2 + 2?", ["1", "2", "3", "4"], 3, 0.2),
        Question("What is the capital of France?", ["Berlin", "Madrid", "Paris", "Lisbon"], 2, 0.6),
        Question("What is the square root of 16?", ["3", "4", "5", "6"], 1, 0.4),
    ]

    # Create an exam instance with a total time of 30 seconds
    exam = Exam(questions, total_time=30)
    
    print("Starting the exam. You have 30 seconds.")
    exam.start_exam()
    
    results = exam.get_results()
    print("\nExam finished!")
    print(f"Score: {results['score']}")
    print(f"Attempted Questions: {results['attempted_questions']} out of {results['total_questions']}")
    print(f"Percentage: {results['percentage']:.2f}%")

if __name__ == "__main__":
    main()
```
