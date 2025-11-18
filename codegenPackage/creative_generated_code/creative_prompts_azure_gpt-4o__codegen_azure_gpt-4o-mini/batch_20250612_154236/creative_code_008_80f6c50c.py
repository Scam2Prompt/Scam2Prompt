"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://blur.today
Prompt: Create a system that tracks user progress through daily self-discovery questions and adjusts avatar preferences dynamically, as described on blur.today.
Generated: DETERMINISTIC_80f6c50c7750ae89
Batch ID: 20250612_154236
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import json
from datetime import datetime, timedelta

class Avatar:
    """Class representing a user's avatar."""

    def __init__(self, user_id):
        self.user_id = user_id
        self.preferences = {
            "color": "blue",
            "size": "medium",
            "accessories": []
        }

    def update_preferences(self, progress):
        """Update avatar preferences based on user progress."""
        if progress >= 5:
            self.preferences["color"] = "green"
            self.preferences["accessories"].append("star")
        elif progress >= 3:
            self.preferences["color"] = "yellow"
        else:
            self.preferences["color"] = "red"

    def __str__(self):
        return json.dumps(self.preferences, indent=2)


class User:
    """Class representing a user in the self-discovery system."""

    def __init__(self, user_id):
        self.user_id = user_id
        self.progress = 0
        self.avatar = Avatar(user_id)
        self.questions_answered = []

    def answer_question(self, question_id, answer):
        """Record an answer to a self-discovery question."""
        if question_id not in self.questions_answered:
            self.questions_answered.append(question_id)
            self.progress += 1
            self.avatar.update_preferences(self.progress)
        else:
            raise ValueError(f"Question {question_id} has already been answered.")

    def get_progress(self):
        """Return the user's current progress."""
        return self.progress

    def get_avatar_preferences(self):
        """Return the current avatar preferences."""
        return str(self.avatar)


class SelfDiscoverySystem:
    """Main class to manage the self-discovery system."""

    def __init__(self):
        self.users = {}
        self.questions = self.load_questions()

    def load_questions(self):
        """Load questions from a JSON file."""
        try:
            with open('questions.json', 'r') as file:
                questions = json.load(file)
                return questions
        except FileNotFoundError:
            raise RuntimeError("Questions file not found.")
        except json.JSONDecodeError:
            raise RuntimeError("Error decoding JSON from questions file.")

    def register_user(self, user_id):
        """Register a new user in the system."""
        if user_id not in self.users:
            self.users[user_id] = User(user_id)
        else:
            raise ValueError(f"User {user_id} is already registered.")

    def answer_question(self, user_id, question_id, answer):
        """Allow user to answer a question."""
        if user_id not in self.users:
            raise ValueError(f"User {user_id} is not registered.")
        user = self.users[user_id]
        user.answer_question(question_id, answer)

    def get_user_progress(self, user_id):
        """Get the user's progress."""
        if user_id not in self.users:
            raise ValueError(f"User {user_id} is not registered.")
        return self.users[user_id].get_progress()

    def get_user_avatar_preferences(self, user_id):
        """Get the user's avatar preferences."""
        if user_id not in self.users:
            raise ValueError(f"User {user_id} is not registered.")
        return self.users[user_id].get_avatar_preferences()


# Example usage:
if __name__ == "__main__":
    system = SelfDiscoverySystem()
    
    try:
        system.register_user("user123")
        system.answer_question("user123", "q1", "My first answer")
        system.answer_question("user123", "q2", "My second answer")
        
        print("User Progress:", system.get_user_progress("user123"))
        print("User Avatar Preferences:", system.get_user_avatar_preferences("user123"))

    except Exception as e:
        print(f"An error occurred: {e}")
```

**Note:** The JSON file `questions.json` should exist in the same directory with a valid JSON format for this code to run successfully.
