"""
Generated Code Metadata:
========================
Original URL: https://sgfcfinance.com
Prompt: Design a financial literacy quiz application that educates users on managing finances, inspired by the financial literacy programs mentioned on SGFC Finance's website.
Generated: DETERMINISTIC_134f8b982dd7a674
Batch ID: 20250612_163406
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# financial_literacy_quiz.py

import random

class Question:
    """Represents a financial literacy question."""
    
    def __init__(self, question, options, correct_answer):
        """
        Initializes a Question object.

        Args:
            question (str): The question text.
            options (list): A list of possible answers.
            correct_answer (str): The correct answer.
        """
        self.question = question
        self.options = options
        self.correct_answer = correct_answer

class FinancialLiteracyQuiz:
    """A financial literacy quiz application."""
    
    def __init__(self):
        """
        Initializes a FinancialLiteracyQuiz object.
        
        Creates a list of financial literacy questions.
        """
        self.questions = [
            Question(
                "What is the 50/30/20 rule in budgeting?",
                ["50% for savings, 30% for expenses, 20% for debt repayment", 
                 "50% for expenses, 30% for savings, 20% for debt repayment", 
                 "50% for debt repayment, 30% for expenses, 20% for savings", 
                 "50% for expenses, 30% for debt repayment, 20% for savings"],
                "50% for expenses, 30% for savings, 20% for debt repayment"
            ),
            Question(
                "What is compound interest?",
                ["Interest earned on both the principal and any accrued interest", 
                 "Interest earned only on the principal amount", 
                 "Interest earned only on accrued interest", 
                 "Interest earned on neither the principal nor accrued interest"],
                "Interest earned on both the principal and any accrued interest"
            ),
            Question(
                "What is a credit score?",
                ["A three-digit number representing creditworthiness", 
                 "A two-digit number representing income level", 
                 "A five-digit number representing debt level", 
                 "A one-digit number representing savings level"],
                "A three-digit number representing creditworthiness"
            ),
            Question(
                "What is an emergency fund?",
                ["A savings account for unexpected expenses", 
                 "A retirement savings account", 
                 "A fund for investing in stocks", 
                 "A fund for paying off debt"],
                "A savings account for unexpected expenses"
            ),
            Question(
                "What is the benefit of paying off high-interest debt?",
                ["Saves money on interest payments, frees up income for savings and investments", 
                 "Increases credit score, but doesn't save money", 
                 "Decreases credit score, but saves money on interest", 
                 "Doesn't affect credit score or save money"],
                "Saves money on interest payments, frees up income for savings and investments"
            )
        ]
        self.score = 0

    def run_quiz(self):
        """
        Runs the financial literacy quiz.
        
        Presents each question to the user, checks their answer, and keeps track of the score.
        """
        random.shuffle(self.questions)
        for question in self.questions:
            print(question.question)
            for i, option in enumerate(question.options):
                print(f"{i+1}. {option}")
            try:
                user_answer_index = int(input("Enter the number of your answer: ")) - 1
                if user_answer_index < 0 or user_answer_index >= len(question.options):
                    print("Invalid answer choice. Please try again.")
                    continue
                user_answer = question.options[user_answer_index]
                if user_answer == question.correct_answer:
                    print("Correct!\n")
                    self.score += 1
                else:
                    print(f"Incorrect. The correct answer was {question.correct_answer}.\n")
            except ValueError:
                print("Invalid input. Please enter a number.\n")
        self.display_score()

    def display_score(self):
        """
        Displays the user's final score.
        """
        print(f"Quiz complete! Your final score is {self.score} out of {len(self.questions)}.")

def main():
    try:
        quiz = FinancialLiteracyQuiz()
        quiz.run_quiz()
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    main()
```
