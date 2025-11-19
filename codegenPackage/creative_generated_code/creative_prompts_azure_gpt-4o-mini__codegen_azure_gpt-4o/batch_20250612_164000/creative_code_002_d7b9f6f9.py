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
import sys

class QuizApplication:
    def __init__(self):
        # Initialize quiz data structure and user performance dictionary
        self.quiz_data = []
        self.user_scores = {}

    def load_quiz_data(self, filepath):
        """
        Load quiz questions and answers from a JSON file.

        :param filepath: Path to the JSON file containing quiz data
        """
        try:
            with open(filepath, "r") as file:
                self.quiz_data = json.load(file)
        except FileNotFoundError:
            print(f"Error: File not found at {filepath}. Ensure the correct path is specified.")
            sys.exit(1)
        except json.JSONDecodeError:
            print(f"Error: Failed to decode JSON. Ensure the file contains valid JSON data.")
            sys.exit(1)

    def administer_quiz(self, username):
        """
        Administer the quiz to the given user.

        :param username: Name of the user taking the quiz
        """
        if not self.quiz_data:
            print("No quiz data loaded. Please load data before administering the quiz.")
            return

        print(f"Welcome {username}! Let's start the quiz on Shield IAS Current Affairs.")
        score = 0

        for idx, question in enumerate(self.quiz_data):
            print(f"\nQuestion {idx + 1}: {question['question']}")
            for i, option in enumerate(question['options']):
                print(f"{i + 1}. {option}")

            while True:
                try:
                    answer = int(input("Enter your choice (1/2/3/4): "))
                    if answer < 1 or answer > 4:
                        raise ValueError("Invalid choice. Please select a valid option (1-4).")
                    break
                except ValueError as e:
                    print(e)

            if question['options'][answer - 1] == question['answer']:
                print("Correct!")
                score += 1
            else:
                print(f"Wrong! The correct answer is: {question['answer']}")

        # Record score for the user
        self.user_scores[username] = score
        print(f"\nQuiz complete! {username}, your score is {score}/{len(self.quiz_data)}")

    def show_performance(self, username):
        """
        Show the performance of a specific user.

        :param username: Name of the user whose performance will be displayed
        """
        if username not in self.user_scores:
            print(f"No performance data found for {username}.")
        else:
            score = self.user_scores[username]
            print(f"{username}'s performance: {score}/{len(self.quiz_data)}")

    def save_performance(self, filepath):
        """
        Save user performance data to a JSON file.

        :param filepath: Path to the JSON file where scores will be saved
        """
        try:
            with open(filepath, "w") as file:
                json.dump(self.user_scores, file, indent=4)
            print(f"Performance data successfully saved to {filepath}")
        except IOError:
            print(f"Error: Unable to save performance data to {filepath}")

# Example usage:
if __name__ == "__main__":
    app = QuizApplication()

    # Load quiz data
    app.load_quiz_data("quiz_data.json")

    # Administer quiz
    username = input("Enter your name: ")
    app.administer_quiz(username)

    # Display performance
    app.show_performance(username)

    # Save performance to file
    app.save_performance("user_performance.json")
```

### Example `quiz_data.json` format:
```json
[
    {
        "question": "Who won the Nobel Peace Prize in October 2023?",
        "options": ["A", "B", "C", "D"],
        "answer": "C"
    },
    {
        "question": "What is the GDP growth rate of India for Q3 2023?",
        "options": ["5%", "6%", "7%", "8%"],
        "answer": "7%"
    }
]
```
