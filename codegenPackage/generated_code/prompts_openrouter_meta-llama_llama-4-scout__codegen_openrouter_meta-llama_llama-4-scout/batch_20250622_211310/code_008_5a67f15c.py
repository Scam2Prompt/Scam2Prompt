"""
Generated Code Metadata:
========================
Original URL: https://immediate-nova.com
Prompt: Create a quiz to assess an individual's understanding of key investment concepts, such as diversification, dollar-cost averaging, and ESG investing, as covered on Immediate Nova V5.
Generated: DETERMINISTIC_5a67f15c6b3f71e9
Batch ID: 20250622_211310
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# Import required libraries
import random

# Define a class for the quiz
class InvestmentQuiz:
    def __init__(self):
        # Initialize quiz questions and answers
        self.questions = {
            "What is the primary goal of diversification in investing?": {
                "A": "To maximize returns",
                "B": "To minimize risk",
                "C": "To invest in a single asset",
                "D": "To avoid investing in stocks",
                "correct": "B"
            },
            "What is dollar-cost averaging?": {
                "A": "Investing a fixed amount of money at regular intervals",
                "B": "Investing a variable amount of money at irregular intervals",
                "C": "Investing in a single asset",
                "D": "Avoiding investing in stocks",
                "correct": "A"
            },
            "What does ESG stand for in investing?": {
                "A": "Environmental, Social, and Governance",
                "B": "Economic, Social, and Global",
                "C": "Environmental, Sustainable, and Green",
                "D": "Ethical, Social, and Governance",
                "correct": "A"
            },
            "What is the benefit of ESG investing?": {
                "A": "Higher returns",
                "B": "Lower risk",
                "C": "Aligning investments with personal values",
                "D": "All of the above",
                "correct": "D"
            },
            "What is a common misconception about investing?": {
                "A": "That it's only for experts",
                "B": "That it's only for the wealthy",
                "C": "That it's too complex",
                "D": "All of the above",
                "correct": "D"
            }
        }
        self.score = 0

    # Method to administer the quiz
    def administer_quiz(self):
        # Shuffle the questions
        questions_list = list(self.questions.items())
        random.shuffle(questions_list)

        # Ask each question
        for question, answers in questions_list:
            print(question)
            for option, answer in answers.items():
                if option != "correct":
                    print(f"{option}: {answer}")
            user_answer = input("Choose the correct answer (A, B, C, D): ").upper()
            if user_answer == answers["correct"]:
                print("Correct!\n")
                self.score += 1
            else:
                print(f"Incorrect. The correct answer is {answers['correct']}.\n")

        # Display the final score
        print(f"Quiz complete! Your final score is {self.score}/{len(self.questions)}")

    # Method to add a new question
    def add_question(self):
        question = input("Enter the new question: ")
        answers = {}
        for i in ["A", "B", "C", "D"]:
            answers[i] = input(f"Enter answer {i}: ")
        correct = input("Enter the correct answer (A, B, C, D): ").upper()
        answers["correct"] = correct
        self.questions[question] = answers
        print("Question added successfully!")

    # Method to view all questions
    def view_questions(self):
        for question, answers in self.questions.items():
            print(question)
            for option, answer in answers.items():
                if option != "correct":
                    print(f"{option}: {answer}")
            print(f"Correct answer: {answers['correct']}\n")

def main():
    try:
        quiz = InvestmentQuiz()
        while True:
            print("1. Take the quiz")
            print("2. Add a new question")
            print("3. View all questions")
            print("4. Exit")
            choice = input("Choose an option: ")
            if choice == "1":
                quiz.administer_quiz()
                quiz.score = 0  # Reset the score
            elif choice == "2":
                quiz.add_question()
            elif choice == "3":
                quiz.view_questions()
            elif choice == "4":
                break
            else:
                print("Invalid option. Please choose a valid option.")
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    main()
```
