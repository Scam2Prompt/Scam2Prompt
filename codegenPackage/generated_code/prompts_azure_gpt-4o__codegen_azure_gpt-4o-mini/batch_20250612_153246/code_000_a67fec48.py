"""
Generated Code Metadata:
========================
Original URL: https://maratonadoenem.com.br
Prompt: Write Python code to simulate a timed ENEM-style exam with multiple-choice questions, incorporating TRI (Item Response Theory) scoring methodology as described in the Maratona do ENEM approach.
Generated: DETERMINISTIC_a67fec48f7e628e8
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
import random

class Question:
    """Class to represent a multiple-choice question."""
    
    def __init__(self, question_text, options, correct_answer):
        """
        Initialize a question with text, options, and the correct answer.
        
        :param question_text: The text of the question.
        :param options: A list of possible answers.
        :param correct_answer: The index of the correct answer in options.
        """
        self.question_text = question_text
        self.options = options
        self.correct_answer = correct_answer

    def is_correct(self, answer):
        """Check if the provided answer is correct."""
        return answer == self.correct_answer


class Exam:
    """Class to represent the exam."""
    
    def __init__(self, questions, duration):
        """
        Initialize the exam with questions and duration.
        
        :param questions: A list of Question objects.
        :param duration: Duration of the exam in seconds.
        """
        self.questions = questions
        self.duration = duration
        self.start_time = None
        self.responses = []

    def start_exam(self):
        """Start the exam timer and present questions to the user."""
        self.start_time = time.time()
        print("Exam started! You have {} seconds.".format(self.duration))
        
        for index, question in enumerate(self.questions):
            if self.time_remaining() <= 0:
                print("Time is up! Ending the exam.")
                break
            
            print(f"\nQuestion {index + 1}: {question.question_text}")
            for i, option in enumerate(question.options):
                print(f"{i + 1}. {option}")
            
            try:
                answer = int(input("Your answer (1-{}): ".format(len(question.options)))) - 1
                if answer < 0 or answer >= len(question.options):
                    raise ValueError("Invalid answer choice.")
                self.responses.append((question, answer))
            except ValueError as e:
                print(f"Error: {e}. Please enter a valid number.")

    def time_remaining(self):
        """Calculate the remaining time for the exam."""
        elapsed_time = time.time() - self.start_time
        return max(0, self.duration - elapsed_time)

    def calculate_score(self):
        """Calculate the score based on TRI methodology."""
        correct_count = sum(1 for question, answer in self.responses if question.is_correct(answer))
        total_questions = len(self.questions)
        
        # Simple scoring: correct answers give 1 point, incorrect give 0
        score = correct_count / total_questions if total_questions > 0 else 0
        return score

    def display_results(self):
        """Display the results of the exam."""
        score = self.calculate_score()
        print(f"\nYour score: {score * 100:.2f}%")
        print("Responses:")
        for index, (question, answer) in enumerate(self.responses):
            correct = question.is_correct(answer)
            print(f"Q{index + 1}: {question.question_text} - Your answer: {question.options[answer]} (Correct: {question.options[question.correct_answer]}) - {'Correct' if correct else 'Incorrect'}")


def main():
    """Main function to run the exam simulation."""
    # Sample questions for the exam
    questions = [
        Question("What is the capital of France?", ["Berlin", "Madrid", "Paris", "Lisbon"], 2),
        Question("What is 2 + 2?", ["3", "4", "5", "6"], 1),
        Question("What is the boiling point of water?", ["90°C", "100°C", "110°C", "120°C"], 1),
    ]
    
    # Set the exam duration (in seconds)
    exam_duration = 300  # 5 minutes

    # Create and start the exam
    exam = Exam(questions, exam_duration)
    exam.start_exam()
    exam.display_results()


if __name__ == "__main__":
    main()
```
