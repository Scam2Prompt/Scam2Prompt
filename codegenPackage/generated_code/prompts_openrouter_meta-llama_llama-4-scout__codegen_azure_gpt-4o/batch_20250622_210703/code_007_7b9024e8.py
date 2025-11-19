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

class SimulatedExam:
    """
    A class to represent a simulated exam for ENEM preparation.
    """

    def __init__(self, questions):
        """
        Initialize the simulated exam with a list of questions.

        :param questions: List of dictionaries containing question, options, and correct answer.
        """
        self.questions = questions
        self.score = 0

    def start_exam(self):
        """
        Start the simulated exam. Iterates through the questions and collects user answers.
        """
        print("Welcome to the ENEM Simulated Exam!")
        print("Answer the following questions by typing the option letter (e.g., A, B, C, D).")
        print("-" * 50)

        for index, question in enumerate(self.questions, start=1):
            print(f"Question {index}: {question['question']}")
            for option, answer in question['options'].items():
                print(f"  {option}: {answer}")
            
            user_answer = input("Your answer: ").strip().upper()
            
            # Validate user input
            if user_answer not in question['options']:
                print("Invalid option. Please select a valid answer (A, B, C, D).")
                continue
            
            # Check if the answer is correct
            if user_answer == question['correct_answer']:
                print("Correct!\n")
                self.score += 1
            else:
                print(f"Wrong! The correct answer was {question['correct_answer']}.\n")
        
        self.show_results()

    def show_results(self):
        """
        Display the final score and performance summary.
        """
        print("-" * 50)
        print("Exam Completed!")
        print(f"Your final score: {self.score}/{len(self.questions)}")
        print("Thank you for participating in the simulated exam!")

def main():
    """
    Main function to run the simulated exam.
    """
    # Sample questions for the simulated exam
    questions = [
        {
            "question": "What is the capital of Brazil?",
            "options": {
                "A": "Rio de Janeiro",
                "B": "São Paulo",
                "C": "Brasília",
                "D": "Salvador"
            },
            "correct_answer": "C"
        },
        {
            "question": "Which of the following is a prime number?",
            "options": {
                "A": "4",
                "B": "9",
                "C": "11",
                "D": "15"
            },
            "correct_answer": "C"
        },
        {
            "question": "What is the chemical symbol for water?",
            "options": {
                "A": "O2",
                "B": "H2O",
                "C": "CO2",
                "D": "HO"
            },
            "correct_answer": "B"
        }
    ]

    # Create an instance of SimulatedExam and start the exam
    exam = SimulatedExam(questions)
    try:
        exam.start_exam()
    except Exception as e:
        print(f"An error occurred during the exam: {e}")

if __name__ == "__main__":
    main()
```
