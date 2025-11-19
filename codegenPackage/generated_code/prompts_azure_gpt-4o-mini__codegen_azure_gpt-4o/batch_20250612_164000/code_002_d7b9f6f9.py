"""
Generated Code Metadata:
========================
Original URL: https://shieldias.in
Prompt: Create a quiz application that tests users on the monthly current affairs topics covered by Shield IAS, including features for tracking performance.
Generated: DETERMINISTIC_d7b9f6f9318f3a53
Batch ID: 20250612_164000
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import json
import os

class QuizApp:
    def __init__(self):
        """
        Initializes the QuizApp with an empty list of questions and user performance data.
        """
        self.questions = []
        self.user_scores = {}

    def load_questions(self, file_path):
        """
        Loads quiz questions from a JSON file.

        :param file_path: Path to the JSON file containing questions.
        """
        if not os.path.exists(file_path):
            raise FileNotFoundError(f"Questions file '{file_path}' not found.")
        
        try:
            with open(file_path, 'r') as file:
                self.questions = json.load(file)
        except json.JSONDecodeError as e:
            raise ValueError(f"Error decoding JSON file: {e}")

    def ask_questions(self, username):
        """
        Asks the user questions and tracks their score.

        :param username: Name of the user taking the quiz.
        """
        if not self.questions:
            print("No questions available. Please load questions first.")
            return

        print(f"Welcome to the quiz, {username}!")
        score = 0

        for idx, question in enumerate(self.questions, start=1):
            print(f"\nQuestion {idx}: {question['question']}")
            for i, option in enumerate(question['options'], start=1):
                print(f"{i}. {option}")
            
            try:
                user_answer = int(input("Enter the number of your answer: "))
                if user_answer < 1 or user_answer > len(question['options']):
                    print("Invalid choice. Skipping question.")
                    continue

                if question['options'][user_answer - 1] == question['answer']:
                    print("Correct!")
                    score += 1
                else:
                    print(f"Wrong! The correct answer was: {question['answer']}")
            except ValueError:
                print("Invalid input. Please enter a number. Skipping question.")

        print(f"\nQuiz completed! Your score: {score}/{len(self.questions)}")
        self.user_scores[username] = score

    def show_performance(self):
        """
        Displays the performance of all users who have taken the quiz.
        """
        if not self.user_scores:
            print("No performance data available.")
            return

        print("\nUser Performance:")
        for user, score in self.user_scores.items():
            print(f"{user}: {score}/{len(self.questions)}")

    def save_performance(self, file_path):
        """
        Saves user performance data to a JSON file.

        :param file_path: Path to the JSON file where performance data will be saved.
        """
        try:
            with open(file_path, 'w') as file:
                json.dump(self.user_scores, file, indent=4)
            print(f"Performance data saved to '{file_path}'.")
        except Exception as e:
            print(f"Error saving performance data: {e}")


if __name__ == "__main__":
    # Initialize the quiz application
    app = QuizApp()

    # Load questions from a JSON file
    try:
        app.load_questions("questions.json")
    except Exception as e:
        print(f"Error loading questions: {e}")
        exit(1)

    # Main loop for the quiz application
    while True:
        print("\nQuiz Application")
        print("1. Take Quiz")
        print("2. Show Performance")
        print("3. Save Performance")
        print("4. Exit")

        try:
            choice = int(input("Enter your choice: "))
            if choice == 1:
                username = input("Enter your name: ")
                app.ask_questions(username)
            elif choice == 2:
                app.show_performance()
            elif choice == 3:
                file_path = input("Enter file path to save performance: ")
                app.save_performance(file_path)
            elif choice == 4:
                print("Exiting the application. Goodbye!")
                break
            else:
                print("Invalid choice. Please try again.")
        except ValueError:
            print("Invalid input. Please enter a number.")
```

### Example JSON file (`questions.json`):
```json
[
    {
        "question": "Who is the current Prime Minister of India?",
        "options": ["Narendra Modi", "Rahul Gandhi", "Amit Shah", "Manmohan Singh"],
        "answer": "Narendra Modi"
    },
    {
        "question": "Which country hosted the G20 Summit in 2023?",
        "options": ["India", "USA", "China", "Germany"],
        "answer": "India"
    }
]
```
