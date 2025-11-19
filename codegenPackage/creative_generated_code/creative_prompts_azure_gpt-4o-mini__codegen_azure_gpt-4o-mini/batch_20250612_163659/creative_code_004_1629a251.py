"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://iqratechpoint.pages.dev
Prompt: How can gamification techniques be applied using IQRA Token to enhance user engagement in educational games?
Generated: DETERMINISTIC_1629a251d292ce59
Batch ID: 20250612_163659
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
# Import necessary libraries
import random
import json

class User:
    """Class to represent a user in the gamification system."""
    
    def __init__(self, username):
        self.username = username
        self.score = 0
        self.iqra_tokens = 0
        self.level = 1

    def earn_tokens(self, amount):
        """Method to earn IQRA tokens based on performance."""
        if amount < 0:
            raise ValueError("Amount of tokens earned must be non-negative.")
        self.iqra_tokens += amount
        print(f"{self.username} earned {amount} IQRA tokens. Total: {self.iqra_tokens}")

    def spend_tokens(self, amount):
        """Method to spend IQRA tokens."""
        if amount < 0:
            raise ValueError("Amount of tokens spent must be non-negative.")
        if amount > self.iqra_tokens:
            raise ValueError("Not enough IQRA tokens to spend.")
        self.iqra_tokens -= amount
        print(f"{self.username} spent {amount} IQRA tokens. Remaining: {self.iqra_tokens}")

    def update_score(self, points):
        """Update the user's score and handle level up."""
        if points < 0:
            raise ValueError("Points added must be non-negative.")
        self.score += points
        print(f"{self.username} scored {points} points. Total score: {self.score}")
        self.check_level_up()

    def check_level_up(self):
        """Check if the user qualifies for a level up."""
        level_threshold = 100 * self.level
        if self.score >= level_threshold:
            self.level += 1
            print(f"Congratulations {self.username}! You leveled up to Level {self.level}.")

class Game:
    """Class to represent the educational game."""
    
    def __init__(self, title):
        self.title = title
        self.questions = self.load_questions()

    def load_questions(self):
        """Load game questions from a JSON file."""
        try:
            with open('questions.json', 'r') as file:
                return json.load(file)
        except FileNotFoundError:
            raise FileNotFoundError("Questions file not found.")
        except json.JSONDecodeError:
            raise ValueError("Error decoding JSON from questions file.")

    def ask_question(self, user):
        """Ask a random question to the user and process their answer."""
        question = random.choice(self.questions)
        print(f"Question: {question['question']}")
        user_answer = input("Your answer: ")

        if user_answer.lower() == question['answer'].lower():
            user.update_score(10)  # Earning points for correct answer
            user.earn_tokens(5)     # Earning tokens for correct answer
        else:
            print("Wrong answer. Try again!")

def main():
    """Main function to run the game."""
    print("Welcome to the IQRA Token Game!")
    
    # Create a user
    username = input("Enter your username: ")
    user = User(username)

    # Create a game instance
    game = Game(title="Educational Quiz Game")

    # Start the game loop
    while True:
        try:
            game.ask_question(user)
            continue_playing = input("Do you want to continue playing? (yes/no): ").strip().lower()
            if continue_playing != 'yes':
                break
        except Exception as e:
            print(f"An error occurred: {e}")

    print(f"Thanks for playing, {user.username}! Your final score: {user.score}, IQRA tokens: {user.iqra_tokens}, Level: {user.level}")

if __name__ == "__main__":
    main()
```
