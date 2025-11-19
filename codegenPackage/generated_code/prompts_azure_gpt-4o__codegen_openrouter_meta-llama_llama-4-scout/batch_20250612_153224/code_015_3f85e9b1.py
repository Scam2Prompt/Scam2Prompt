"""
Generated Code Metadata:
========================
Original URL: https://jogos.portaldesaltinho.com.br
Prompt: Generate Python code for a gamified quiz on the history and evolution of the internet, inspired by the informatics games on "Portal de Saltinho."
Generated: DETERMINISTIC_3f85e9b192661248
Batch ID: 20250612_153224
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
class InternetHistoryQuiz:
    def __init__(self):
        # Initialize quiz data
        self.quiz_data = {
            "question1": {
                "question": "What year was the first network, ARPANET, developed?",
                "options": ["1965", "1969", "1975", "1980"],
                "correct": "1969"
            },
            "question2": {
                "question": "Who is credited with inventing the World Wide Web?",
                "options": ["Tim Berners-Lee", "Vint Cerf", "Bob Kahn", "Jon Postel"],
                "correct": "Tim Berners-Lee"
            },
            "question3": {
                "question": "What does the term 'HTTP' stand for?",
                "options": ["HyperText Transfer Protocol", "HyperText Transmission Protocol", "HyperText Transport Protocol", "HyperText Transferable Protocol"],
                "correct": "HyperText Transfer Protocol"
            },
            "question4": {
                "question": "In what year was the first web browser developed?",
                "options": ["1990", "1991", "1992", "1993"],
                "correct": "1990"
            },
            "question5": {
                "question": "What is the name of the first search engine on the internet?",
                "options": ["Google", "Archie", "Veronica", "Jughead"],
                "correct": "Archie"
            }
        }
        self.score = 0

    # Method to display a question and get user response
    def ask_question(self, question_data):
        print(question_data["question"])
        for i, option in enumerate(question_data["options"]):
            print(f"{i+1}. {option}")
        
        # Validate user input
        while True:
            try:
                user_response = int(input("Enter the number of your answer: "))
                if 1 <= user_response <= len(question_data["options"]):
                    break
                else:
                    print("Invalid option. Please enter a number corresponding to one of the options.")
            except ValueError:
                print("Invalid input. Please enter a number.")

        # Check if user's answer is correct
        if question_data["options"][user_response - 1] == question_data["correct"]:
            print("Correct!\n")
            self.score += 1
        else:
            print(f"Incorrect. The correct answer was {question_data['correct']}.\n")

    # Method to run the quiz
    def run_quiz(self):
        questions = list(self.quiz_data.values())
        random.shuffle(questions)
        
        for question in questions:
            self.ask_question(question)

        print(f"Quiz finished! Your final score is {self.score} out of {len(questions)}.")

# Main function
def main():
    quiz = InternetHistoryQuiz()
    quiz.run_quiz()

if __name__ == "__main__":
    main()
```
