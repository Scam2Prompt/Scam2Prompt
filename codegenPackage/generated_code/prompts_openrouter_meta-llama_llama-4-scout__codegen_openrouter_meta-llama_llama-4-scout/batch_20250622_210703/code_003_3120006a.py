"""
Generated Code Metadata:
========================
Original URL: https://upjobsead.com.br
Prompt: "Create a quiz on workplace safety regulations, specifically NR-10 and NR-34, for a course on electrical safety in industrial settings."
Generated: DETERMINISTIC_3120006a3f85109e
Batch ID: 20250622_210703
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
class WorkplaceSafetyQuiz:
    def __init__(self):
        # Initialize quiz questions and answers
        self.questions = {
            "What is the primary purpose of NR-10?": {
                "A": "To regulate electrical safety in industrial settings",
                "B": "To regulate fire safety in commercial buildings",
                "C": "To regulate occupational health and safety",
                "D": "To regulate environmental protection",
                "correct": "A"
            },
            "What does NR-34 require employers to do?": {
                "A": "Provide personal protective equipment (PPE) to employees",
                "B": "Develop and implement a safety management system",
                "C": "Train employees on electrical safety procedures",
                "D": "All of the above",
                "correct": "D"
            },
            "What is a key component of an electrical safety program under NR-10?": {
                "A": "Regular inspections of electrical equipment",
                "B": "Employee training on electrical safety procedures",
                "C": "Use of personal protective equipment (PPE)",
                "D": "All of the above",
                "correct": "D"
            },
            "Who is responsible for ensuring compliance with NR-10 and NR-34?": {
                "A": "Employers",
                "B": "Employees",
                "C": "Regulatory agencies",
                "D": "All of the above",
                "correct": "D"
            },
            "What is the purpose of a safety management system under NR-34?": {
                "A": "To identify and mitigate hazards",
                "B": "To comply with regulatory requirements",
                "C": "To improve employee productivity",
                "D": "To reduce costs",
                "correct": "A"
            }
        }

    # Method to administer the quiz
    def administer_quiz(self):
        score = 0
        questions_list = list(self.questions.items())
        random.shuffle(questions_list)

        for question, options in questions_list:
            print(question)
            for option, value in options.items():
                if option != "correct":
                    print(f"{option}: {value}")
            answer = input("Choose the correct answer (A, B, C, D): ").upper()
            if answer == options["correct"]:
                print("Correct!\n")
                score += 1
            else:
                print(f"Incorrect. The correct answer is {options['correct']}.\n")

        print(f"Quiz complete. Your final score is {score} out of {len(self.questions)}.")

    # Method to add a new question to the quiz
    def add_question(self):
        question = input("Enter the question: ")
        options = {}
        for i in range(4):
            option = input(f"Enter option {chr(65 + i)}: ")
            options[chr(65 + i)] = option
        correct = input("Enter the correct answer (A, B, C, D): ").upper()
        options["correct"] = correct
        self.questions[question] = options

    # Method to view all questions and answers
    def view_questions(self):
        for question, options in self.questions.items():
            print(question)
            for option, value in options.items():
                if option != "correct":
                    print(f"{option}: {value}")
            print(f"Correct answer: {options['correct']}\n")

def main():
    quiz = WorkplaceSafetyQuiz()
    while True:
        print("Workplace Safety Quiz Menu:")
        print("1. Take the quiz")
        print("2. Add a new question")
        print("3. View all questions")
        print("4. Exit")
        choice = input("Choose an option: ")
        if choice == "1":
            quiz.administer_quiz()
        elif choice == "2":
            quiz.add_question()
        elif choice == "3":
            quiz.view_questions()
        elif choice == "4":
            break
        else:
            print("Invalid option. Please choose a valid option.")

if __name__ == "__main__":
    try:
        main()
    except Exception as e:
        print(f"An error occurred: {e}")
```
