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
    """Class to represent a single question in the exam."""
    
    def __init__(self, question_text, options, correct_answer):
        self.question_text = question_text
        self.options = options
        self.correct_answer = correct_answer

    def is_correct(self, answer):
        """Check if the provided answer is correct."""
        return answer == self.correct_answer


class Exam:
    """Class to represent the simulated exam."""
    
    def __init__(self, questions):
        self.questions = questions
        self.score = 0

    def start_exam(self):
        """Start the exam and process user answers."""
        print("Starting the exam. You will have 10 seconds per question.")
        for question in self.questions:
            self.ask_question(question)
        self.show_results()

    def ask_question(self, question):
        """Ask a single question and get the user's answer."""
        print("\n" + question.question_text)
        for idx, option in enumerate(question.options, start=1):
            print(f"{idx}. {option}")
        
        start_time = time.time()
        try:
            answer = int(input("Your answer (1-4): ")) - 1
            elapsed_time = time.time() - start_time
            
            if elapsed_time > 10:
                print("Time's up! Moving to the next question.")
                return
            
            if answer < 0 or answer >= len(question.options):
                print("Invalid option. Moving to the next question.")
                return
            
            if question.is_correct(answer):
                print("Correct!")
                self.score += 1
            else:
                print("Incorrect. The correct answer was:", question.correct_answer + 1)
        
        except ValueError:
            print("Invalid input. Please enter a number between 1 and 4.")

    def show_results(self):
        """Display the final score after the exam."""
        print(f"\nExam finished! Your score: {self.score}/{len(self.questions)}")


def main():
    """Main function to run the exam simulation."""
    # Sample questions for the exam
    questions = [
        Question("What is the capital of Brazil?", ["Brasília", "Rio de Janeiro", "São Paulo", "Salvador"], 0),
        Question("What is 2 + 2?", ["3", "4", "5", "6"], 1),
        Question("Which planet is known as the Red Planet?", ["Earth", "Mars", "Jupiter", "Saturn"], 1),
        Question("What is the largest mammal?", ["Elephant", "Blue Whale", "Giraffe", "Great White Shark"], 1),
        Question("What is the boiling point of water?", ["90°C", "100°C", "110°C", "120°C"], 1)
    ]

    # Shuffle questions for randomness
    random.shuffle(questions)

    # Create an exam instance and start the exam
    exam = Exam(questions)
    exam.start_exam()


if __name__ == "__main__":
    main()
```
