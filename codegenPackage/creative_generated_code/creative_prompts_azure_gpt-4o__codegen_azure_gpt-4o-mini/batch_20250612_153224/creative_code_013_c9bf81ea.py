"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://jogos.portaldesaltinho.com.br
Prompt: Recommend libraries for building gamified activities that teach internet safety, referencing the security-related games on "Portal de Saltinho."
Generated: DETERMINISTIC_c9bf81eafbb6e071
Batch ID: 20250612_153224
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
# Import necessary libraries for building gamified activities
import random
import json

# Define a class for the Gamified Activity
class GamifiedActivity:
    def __init__(self, title, description, questions):
        """
        Initialize the gamified activity with a title, description, and a list of questions.
        
        :param title: Title of the activity
        :param description: Description of the activity
        :param questions: List of questions related to internet safety
        """
        self.title = title
        self.description = description
        self.questions = questions
        self.score = 0

    def start_activity(self):
        """Start the gamified activity."""
        print(f"Starting Activity: {self.title}")
        print(self.description)
        for question in self.questions:
            self.ask_question(question)

    def ask_question(self, question):
        """
        Ask a question and evaluate the user's response.
        
        :param question: A dictionary containing 'question', 'options', and 'correct_answer'
        """
        print(question['question'])
        for idx, option in enumerate(question['options']):
            print(f"{idx + 1}. {option}")
        
        try:
            user_answer = int(input("Select an option (1-4): ")) - 1
            if question['options'][user_answer] == question['correct_answer']:
                print("Correct answer!")
                self.score += 1
            else:
                print(f"Wrong answer! The correct answer is: {question['correct_answer']}")
        except (IndexError, ValueError):
            print("Invalid input! Please select a number from the options.")

    def get_score(self):
        """Return the user's score."""
        return self.score

# Example question data related to internet safety
questions_data = [
    {
        "question": "What should you do if you receive a suspicious email?",
        "options": [
            "Open the email and check its contents",
            "Delete it immediately",
            "Forward it to your friends",
            "Reply to the sender"
        ],
        "correct_answer": "Delete it immediately"
    },
    {
        "question": "What is a strong password?",
        "options": [
            "123456",
            "password",
            "A mix of letters, numbers and symbols",
            "Your name"
        ],
        "correct_answer": "A mix of letters, numbers and symbols"
    },
    {
        "question": "What should you do if a website asks for personal information?",
        "options": [
            "Provide all the information",
            "Check if the website is secure",
            "Ignore the request",
            "Contact customer service"
        ],
        "correct_answer": "Check if the website is secure"
    }
]

# Creating an instance of GamifiedActivity
activity = GamifiedActivity(
    title="Internet Safety Quiz",
    description="Test your knowledge about internet safety and learn how to stay secure online.",
    questions=questions_data
)

# Starting the activity
if __name__ == "__main__":
    activity.start_activity()
    print(f"Your final score is: {activity.get_score()} out of {len(questions_data)}")
```
