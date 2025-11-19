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
# Import required libraries
import random

# Define a class for the chatbot
class ProcrastinationChatbot:
    def __init__(self):
        # Initialize a dictionary with strategies and guidance
        self.strategies = {
            "breaking_down_tasks": {
                "description": "Break down large tasks into smaller, manageable chunks.",
                "guidance": "Try to divide your task into smaller tasks that can be completed in a shorter amount of time."
            },
            "setting_deadlines": {
                "description": "Set specific deadlines for tasks and milestones.",
                "guidance": "Create a schedule with deadlines for each task to help you stay on track."
            },
            "eliminating_distractions": {
                "description": "Identify and eliminate distractions that prevent you from focusing.",
                "guidance": "Turn off notifications, log out of social media, and find a quiet workspace."
            },
            "using_the_2_minute_rule": {
                "description": "If a task can be done in less than 2 minutes, do it immediately.",
                "guidance": "If you have a task that can be completed quickly, do it right away to build momentum."
            }
        }

    # Method to provide guidance on a specific strategy
    def provide_guidance(self, strategy):
        try:
            if strategy in self.strategies:
                return self.strategies[strategy]["guidance"]
            else:
                return "Sorry, I couldn't find any guidance on that strategy."
        except Exception as e:
            return f"An error occurred: {str(e)}"

    # Method to list available strategies
    def list_strategies(self):
        try:
            strategies_list = list(self.strategies.keys())
            return strategies_list
        except Exception as e:
            return f"An error occurred: {str(e)}"

    # Method to provide a random strategy
    def provide_random_strategy(self):
        try:
            random_strategy = random.choice(list(self.strategies.keys()))
            return {
                "strategy": random_strategy,
                "description": self.strategies[random_strategy]["description"],
                "guidance": self.strategies[random_strategy]["guidance"]
            }
        except Exception as e:
            return f"An error occurred: {str(e)}"


# Define a function to interact with the chatbot
def interact_with_chatbot():
    chatbot = ProcrastinationChatbot()
    print("Welcome to the Procrastination Chatbot!")
    while True:
        print("\nOptions:")
        print("1. List strategies")
        print("2. Get guidance on a strategy")
        print("3. Get a random strategy")
        print("4. Quit")
        option = input("Choose an option: ")
        if option == "1":
            strategies = chatbot.list_strategies()
            if isinstance(strategies, list):
                print("\nAvailable strategies:")
                for strategy in strategies:
                    print(strategy)
            else:
                print(strategies)
        elif option == "2":
            strategy = input("Enter the name of the strategy: ").replace(" ", "_").lower()
            guidance = chatbot.provide_guidance(strategy)
            print("\nGuidance:")
            print(guidance)
        elif option == "3":
            random_strategy = chatbot.provide_random_strategy()
            if isinstance(random_strategy, dict):
                print("\nRandom strategy:")
                print(f"Strategy: {random_strategy['strategy']}")
                print(f"Description: {random_strategy['description']}")
                print(f"Guidance: {random_strategy['guidance']}")
            else:
                print(random_strategy)
        elif option == "4":
            print("Goodbye!")
            break
        else:
            print("Invalid option. Please choose a valid option.")

# Run the chatbot
if __name__ == "__main__":
    interact_with_chatbot()
```
