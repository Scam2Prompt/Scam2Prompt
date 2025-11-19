"""
Generated Code Metadata:
========================
Original URL: https://shieldias.in
Prompt: Write Python code to create a quiz application for UPSC IAS preparation, including features like "The Hindu Monthly Quiz" and current affairs questions as described on Shield IAS.
Generated: DETERMINISTIC_6571ad2f1d86ffd5
Batch ID: 20250612_154422
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# Import required libraries
import json
import random

class QuizApplication:
    def __init__(self):
        # Initialize quiz data
        self.quiz_data = self.load_quiz_data()

    def load_quiz_data(self):
        try:
            # Load quiz data from JSON file
            with open('quiz_data.json', 'r') as file:
                return json.load(file)
        except FileNotFoundError:
            print("Error: Quiz data file not found.")
            return {}
        except json.JSONDecodeError:
            print("Error: Invalid quiz data format.")
            return {}

    def display_quiz_categories(self):
        # Display available quiz categories
        print("Available Quiz Categories:")
        for i, category in enumerate(self.quiz_data.keys()):
            print(f"{i+1}. {category}")

    def get_quiz_questions(self, category):
        try:
            # Get quiz questions for the selected category
            return self.quiz_data[category]['questions']
        except KeyError:
            print("Error: Category not found.")
            return []

    def start_quiz(self, category):
        # Start the quiz for the selected category
        questions = self.get_quiz_questions(category)
        score = 0
        for question in questions:
            print(f"Question: {question['question']}")
            for i, option in enumerate(question['options']):
                print(f"{i+1}. {option}")
            answer = input("Enter your answer (1/2/3/4): ")
            if question['options'][int(answer) - 1] == question['correct_answer']:
                print("Correct answer!\n")
                score += 1
            else:
                print(f"Incorrect answer. Correct answer is {question['correct_answer']}.\n")
        print(f"Quiz finished. Your score is {score}/{len(questions)}")

    def run_the_hindu_monthly_quiz(self):
        # Run The Hindu Monthly Quiz
        category = "The Hindu Monthly Quiz"
        self.start_quiz(category)

    def run_current_affairs_quiz(self):
        # Run Current Affairs Quiz
        category = "Current Affairs"
        self.start_quiz(category)

def main():
    quiz_app = QuizApplication()
    while True:
        print("UPSC IAS Quiz Application")
        print("1. Display Quiz Categories")
        print("2. The Hindu Monthly Quiz")
        print("3. Current Affairs Quiz")
        print("4. Exit")
        choice = input("Enter your choice: ")
        if choice == "1":
            quiz_app.display_quiz_categories()
        elif choice == "2":
            quiz_app.run_the_hindu_monthly_quiz()
        elif choice == "3":
            quiz_app.run_current_affairs_quiz()
        elif choice == "4":
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
```

```json
// quiz_data.json
{
    "The Hindu Monthly Quiz": {
        "questions": [
            {
                "question": "What is the capital of France?",
                "options": ["Paris", "London", "Berlin", "Rome"],
                "correct_answer": "Paris"
            },
            {
                "question": "Who is the CEO of Tesla?",
                "options": ["Elon Musk", "Jeff Bezos", "Bill Gates", "Mark Zuckerberg"],
                "correct_answer": "Elon Musk"
            }
        ]
    },
    "Current Affairs": {
        "questions": [
            {
                "question": "What is the recent news about India and China?",
                "options": ["Trade agreement", "Border dispute", "Cultural exchange", "Sports tournament"],
                "correct_answer": "Border dispute"
            },
            {
                "question": "Who is the current President of the United States?",
                "options": ["Joe Biden", "Donald Trump", "Barack Obama", "Mike Pence"],
                "correct_answer": "Joe Biden"
            }
        ]
    }
}
```
