"""
Generated Code Metadata:
========================
Original URL: https://simonscat.pages.dev
Prompt: Write a Python script to create a simple quiz that determines which Simon's Cat character a user is, based on a few easy questions.
Generated: DETERMINISTIC_459b38d53889add9
Batch ID: 20250622_204621
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import sys

class Quiz:
    def __init__(self):
        self.questions = [
            {
                "question": "What do you enjoy doing the most?",
                "options": ["Sleeping", "Playing", "Eating", "Chasing"],
                "answers": {
                    "Sleeping": "Simon’s Cat",
                    "Playing": "Hunky Dory",
                    "Eating": "The Kitten",
                    "Chasing": "The Dog"
                }
            },
            {
                "question": "How do you react when you see a bird?",
                "options": ["Ignore it", "Watch it closely", "Try to catch it", "Bark at it"],
                "answers": {
                    "Ignore it": "Simon’s Cat",
                    "Watch it closely": "Hunky Dory",
                    "Try to catch it": "The Kitten",
                    "Bark at it": "The Dog"
                }
            },
            {
                "question": "What is your favorite snack?",
                "options": ["Fish", "Catnip", "Chicken", "Dog food"],
                "answers": {
                    "Fish": "Simon’s Cat",
                    "Catnip": "Hunky Dory",
                    "Chicken": "The Kitten",
                    "Dog food": "The Dog"
                }
            }
        ]
        self.results = {}

    def run_quiz(self):
        """Run the quiz and collect user responses."""
        print("Welcome to the Simon's Cat Character Quiz!")
        for q in self.questions:
            self.ask_question(q)

        self.determine_character()

    def ask_question(self, question):
        """Ask a question and collect the user's answer."""
        print(f"\n{question['question']}")
        for idx, option in enumerate(question['options'], start=1):
            print(f"{idx}. {option}")

        try:
            answer_index = int(input("Choose an option (1-4): ")) - 1
            if answer_index < 0 or answer_index >= len(question['options']):
                raise ValueError("Invalid option selected.")
            answer = question['options'][answer_index]
            self.results[answer] = self.results.get(answer, 0) + 1
        except ValueError as e:
            print(f"Error: {e}. Please enter a valid number.")
            sys.exit(1)

    def determine_character(self):
        """Determine the character based on the user's answers."""
        if not self.results:
            print("No answers were recorded.")
            return

        # Find the character with the highest score
        character = max(self.results, key=self.results.get)
        print(f"\nYou are most like: {self.results[character]}!")

if __name__ == "__main__":
    quiz = Quiz()
    quiz.run_quiz()
```
