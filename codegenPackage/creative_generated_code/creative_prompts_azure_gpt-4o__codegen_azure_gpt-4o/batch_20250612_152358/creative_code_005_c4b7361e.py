"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://venomonnetwork.pages.dev
Prompt: Generate code to launch the Crazy Camels game and track user progress in completing tasks for earning tokens.
Generated: DETERMINISTIC_c4b7361e18be6d88
Batch ID: 20250612_152358
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import json
import os

class CrazyCamelsGame:
    def __init__(self, user_data_file='user_data.json'):
        """
        Initialize the Crazy Camels game and load user data.

        :param user_data_file: Path to the file where user progress is stored
        """
        self.user_data_file = user_data_file
        self.user_data = {}
        self.tasks = [
            {"task_id": 1, "description": "Collect 5 water bottles", "tokens": 10},
            {"task_id": 2, "description": "Ride 3 camels", "tokens": 15},
            {"task_id": 3, "description": "Find the oasis", "tokens": 20}
        ]
        self._load_user_data()

    def _load_user_data(self):
        """
        Load user progress from a JSON file. If the file doesn't exist, initialize empty data.
        """
        try:
            if os.path.exists(self.user_data_file):
                with open(self.user_data_file, 'r') as file:
                    self.user_data = json.load(file)
            else:
                self.user_data = {}
        except Exception as e:
            print(f"Error loading user data: {e}")
            self.user_data = {}

    def _save_user_data(self):
        """
        Save user progress to a JSON file.
        """
        try:
            with open(self.user_data_file, 'w') as file:
                json.dump(self.user_data, file, indent=4)
        except Exception as e:
            print(f"Error saving user data: {e}")

    def start_game(self):
        """
        Start the Crazy Camels game.
        """
        print("Welcome to Crazy Camels!")
        user_name = input("Enter your username: ").strip()
        if user_name not in self.user_data:
            self.user_data[user_name] = {"tasks_completed": [], "tokens_earned": 0}

        print(f"Hello, {user_name}! Let's start tracking your progress.")
        self._game_loop(user_name)

    def _game_loop(self, user_name):
        """
        Main game loop for tracking tasks.
        """
        while True:
            print("\nTasks available:")
            for task in self.tasks:
                completed = task["task_id"] in self.user_data[user_name]["tasks_completed"]
                status = "Completed" if completed else "Pending"
                print(f"Task ID: {task['task_id']} | {task['description']} | Tokens: {task['tokens']} | Status: {status}")

            try:
                task_id = int(input("\nEnter the Task ID to mark as completed (or 0 to exit): "))
                if task_id == 0:
                    print("Exiting the game. Saving progress...")
                    self._save_user_data()
                    print("Progress saved. Goodbye!")
                    break

                task = next((t for t in self.tasks if t["task_id"] == task_id), None)
                if not task:
                    print("Invalid Task ID. Please try again.")
                    continue

                if task_id in self.user_data[user_name]["tasks_completed"]:
                    print("Task already completed. Choose another.")
                    continue

                # Mark task as completed
                self.user_data[user_name]["tasks_completed"].append(task_id)
                self.user_data[user_name]["tokens_earned"] += task["tokens"]
                print(f"Task '{task['description']}' completed! You earned {task['tokens']} tokens.")
            except ValueError:
                print("Invalid input. Please enter a valid Task ID.")
            except Exception as e:
                print(f"An unexpected error occurred: {e}")

            print(f"Total Tokens Earned: {self.user_data[user_name]['tokens_earned']}")

# Entry point for the application
if __name__ == "__main__":
    game = CrazyCamelsGame()
    game.start_game()
```
