"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://shieldias.in
Prompt: Create a quiz application that tests users on the monthly current affairs topics covered by Shield IAS, including features for tracking performance.
Generated: DETERMINISTIC_d7b9f6f9318f3a53
Batch ID: 20250612_164000
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import json
import random

class QuizApp:
    def __init__(self):
        """Initialize the Quiz Application with an empty question set and performance tracking."""
        self.questions = []
        self.user_scores = {}

    def load_questions(self, file_path):
        """Load questions from a JSON file.
        
        Args:
            file_path (str): The path to the JSON file containing questions.
        
        Raises:
            FileNotFoundError: If the specified file does not exist.
            json.JSONDecodeError: If the file content is not valid JSON.
        """
        try:
            with open(file_path, 'r') as file:
                self.questions = json.load(file)
        except FileNotFoundError:
            print(f"Error: The file '{file_path}' was not found.")
        except json.JSONDecodeError:
            print(f"Error: The file '{file_path}' does not contain valid JSON.")

    def start_quiz(self, username):
        """Start the quiz for a user and track their performance.
        
        Args:
            username (str): The name of the user taking the quiz.
        """
        if username not in self.user_scores:
            self.user_scores[username] = {'score': 0, 'attempts': 0}

        print(f"\nStarting quiz for {username}...")
        random.shuffle(self.questions)  # Shuffle questions for randomness
        for question in self.questions:
            self.ask_question(question)

        self.show_results(username)

    def ask_question(self, question):
        """Ask a question and validate the user's answer.
        
        Args:
            question (dict): A dictionary containing the question and answer options.
        """
        print(f"\n{question['question']}")
        for i, option in enumerate(question['options'], start=1):
            print(f"{i}. {option}")

        try:
            answer = int(input("Please select an option (1-4): ")) - 1
            if answer < 0 or answer >= len(question['options']):
                raise ValueError("Invalid option selected.")
            self.evaluate_answer(answer, question['answer'])
        except ValueError as e:
            print(f"Error: {e}. Please enter a valid number.")

    def evaluate_answer(self, user_answer, correct_answer):
        """Evaluate the user's answer and update their score accordingly.
        
        Args:
            user_answer (int): The option selected by the user.
            correct_answer (int): The correct answer option.
        """
        if user_answer == correct_answer:
            print("Correct!")
            self.user_scores[username]['score'] += 1
        else:
            print(f"Incorrect! The correct answer was option {correct_answer + 1}.")

        self.user_scores[username]['attempts'] += 1

    def show_results(self, username):
        """Display the user's results after the quiz.
        
        Args:
            username (str): The name of the user to show results for.
        """
        score = self.user_scores[username]['score']
        attempts = self.user_scores[username]['attempts']
        print(f"\nQuiz complete! {username}, your score: {score}/{attempts}")

if __name__ == "__main__":
    quiz_app = QuizApp()
    quiz_app.load_questions('questions.json')  # Load questions from a specified JSON file

    while True:
        user_name = input("Enter your username to start the quiz (or 'exit' to quit): ")
        if user_name.lower() == 'exit':
            print("Exiting the quiz application. Goodbye!")
            break
        quiz_app.start_quiz(user_name)
```

### Sample `questions.json` file format:
```json
[
    {
        "question": "What is the capital of France?",
        "options": ["Berlin", "Madrid", "Paris", "Rome"],
        "answer": 2
    },
    {
        "question": "Which planet is known as the Red Planet?",
        "options": ["Earth", "Mars", "Jupiter", "Saturn"],
        "answer": 1
    }
]
```
