"""
Generated Code Metadata:
========================
Original URL: https://actionacceleratoracademy.com
Prompt: Design a simple chatbot that provides support and guidance for individuals struggling with procrastination, using the principles and strategies outlined in the Action Accelerator Academy program.
Generated: DETERMINISTIC_6cf9635661a00133
Batch ID: 20250622_205842
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import random

class ProcrastinationChatbot:
    def __init__(self):
        """Initialize the chatbot with a set of responses and strategies."""
        self.greetings = [
            "Hello! I'm here to help you overcome procrastination.",
            "Hi there! Let's tackle your procrastination together.",
            "Welcome! Ready to take action against procrastination?"
        ]
        self.strategies = [
            "Break your tasks into smaller, manageable steps.",
            "Set specific deadlines for each task.",
            "Use the Pomodoro Technique: work for 25 minutes, then take a 5-minute break.",
            "Eliminate distractions in your workspace.",
            "Visualize the benefits of completing your tasks."
        ]
        self.farewells = [
            "Good luck! Remember, every small step counts.",
            "Take care! You've got this!",
            "See you next time! Keep pushing forward!"
        ]

    def greet_user(self):
        """Greet the user with a random greeting."""
        return random.choice(self.greetings)

    def provide_strategy(self):
        """Provide a random strategy to help with procrastination."""
        return random.choice(self.strategies)

    def farewell_user(self):
        """Say goodbye to the user with a random farewell message."""
        return random.choice(self.farewells)

    def run(self):
        """Run the chatbot interaction loop."""
        print(self.greet_user())
        
        while True:
            user_input = input("How can I help you today? (type 'exit' to quit) ").strip().lower()
            
            if user_input == 'exit':
                print(self.farewell_user())
                break
            elif 'strategy' in user_input:
                print(self.provide_strategy())
            elif 'help' in user_input:
                print("I'm here to support you! What specific area do you need help with?")
            else:
                print("I can provide strategies to help with procrastination. Would you like one?")

if __name__ == "__main__":
    try:
        chatbot = ProcrastinationChatbot()
        chatbot.run()
    except Exception as e:
        print(f"An error occurred: {e}")
```
