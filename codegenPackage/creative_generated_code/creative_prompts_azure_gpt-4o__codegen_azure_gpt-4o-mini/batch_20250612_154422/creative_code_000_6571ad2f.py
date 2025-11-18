"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://shieldias.in
Prompt: Write Python code to create a quiz application for UPSC IAS preparation, including features like "The Hindu Monthly Quiz" and current affairs questions as described on Shield IAS.
Generated: DETERMINISTIC_6571ad2f1d86ffd5
Batch ID: 20250612_154422
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
from typing import List, Dict, Any

class QuizApplication:
    def __init__(self):
        self.questions = []
        self.load_questions()

    def load_questions(self) -> None:
        """Load questions from a JSON file."""
        try:
            with open('questions.json', 'r') as file:
                self.questions = json.load(file)
        except FileNotFoundError:
            print("Error: questions.json file not found.")
        except json.JSONDecodeError:
            print("Error: Invalid JSON format in questions.json.")

    def start_quiz(self) -> None:
        """Start the quiz and administer questions to the user."""
        if not self.questions:
            print("No questions available to start the quiz.")
            return
        
        score = 0
        total_questions = len(self.questions)
        random.shuffle(self.questions)  # Shuffle questions for randomness

        for idx, question in enumerate(self.questions):
            self.ask_question(question)
            user_answer = input("Your answer: ")
            if self.check_answer(question['answer'], user_answer):
                print("Correct!")
                score += 1
            else:
                print(f"Incorrect! The correct answer was: {question['answer']}")
            print()  # New line for better readability

        self.display_score(score, total_questions)

    def ask_question(self, question: Dict[str, Any]) -> None:
        """Display a question and its options."""
        print(f"Q{question['id']}: {question['question']}")
        for option in question['options']:
            print(option)

    def check_answer(self, correct_answer: str, user_answer: str) -> bool:
        """Check if the user's answer is correct."""
        return correct_answer.lower() == user_answer.lower()

    def display_score(self, score: int, total: int) -> None:
        """Display the final score to the user."""
        print(f"You scored {score} out of {total}!")

if __name__ == "__main__":
    quiz_app = QuizApplication()
    quiz_app.start_quiz()
```

```json
// questions.json
[
    {
        "id": 1,
        "question": "What is the capital of India?",
        "options": ["A) New Delhi", "B) Mumbai", "C) Kolkata", "D) Chennai"],
        "answer": "A) New Delhi"
    },
    {
        "id": 2,
        "question": "Who is known as the Father of the Nation in India?",
        "options": ["A) Jawaharlal Nehru", "B) Mahatma Gandhi", "C) Sardar Patel", "D) B.R. Ambedkar"],
        "answer": "B) Mahatma Gandhi"
    }
]
``` 

This code sets up a basic quiz application that loads questions from a JSON file and allows users to answer them, providing feedback and score at the end. Make sure to create a `questions.json` file with the appropriate data format as shown above.
