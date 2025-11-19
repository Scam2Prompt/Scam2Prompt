"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://get-gomble.pages.dev
Prompt: Generate a code snippet that demonstrates how to handle user interactions for the GOMBLE quest feature.
Generated: DETERMINISTIC_596845ba5dec4067
Batch ID: 20250612_161616
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
class GOMBLEQuest:
    """
    A class to handle the GOMBLE quest feature.
    This class manages user interactions and quest progress.
    """

    def __init__(self, user):
        """
        Initializes the GOMBLE quest for a specific user.

        Parameters:
        user (str): The username of the user participating in the quest.
        """
        self.user = user
        self.quest_progress = 0
        self.quest_complete = False
        self.max_progress = 100  # Maximum progress to complete the quest

    def start_quest(self):
        """
        Starts the GOMBLE quest for the user.
        """
        if self.quest_complete:
            print(f"{self.user}, you have already completed the quest!")
            return

        print(f"{self.user}, the GOMBLE quest has started! Good luck!")
        self.quest_progress = 0  # Reset progress

    def complete_task(self, task_points):
        """
        Completes a task and updates the quest progress.

        Parameters:
        task_points (int): Points earned by completing a task.
        """
        if self.quest_complete:
            print(f"{self.user}, you cannot complete more tasks. Quest is finished!")
            return

        if task_points < 0:
            raise ValueError("Task points must be a non-negative integer.")

        self.quest_progress += task_points
        print(f"{self.user}, you have earned {task_points} points! Current progress: {self.quest_progress}/{self.max_progress}.")

        if self.quest_progress >= self.max_progress:
            self.complete_quest()

    def complete_quest(self):
        """
        Marks the quest as complete and notifies the user.
        """
        self.quest_complete = True
        print(f"Congratulations {self.user}! You have completed the GOMBLE quest!")

    def reset_quest(self):
        """
        Resets the quest progress, allowing the user to restart.
        """
        self.quest_progress = 0
        self.quest_complete = False
        print(f"{self.user}, your quest has been reset. You can start again!")

# Example usage:
if __name__ == "__main__":
    user_name = "Player1"
    gomble_quest = GOMBLEQuest(user_name)

    gomble_quest.start_quest()
    
    try:
        gomble_quest.complete_task(30)
        gomble_quest.complete_task(50)
        gomble_quest.complete_task(25)  # This should trigger completion
    except ValueError as e:
        print(f"Error: {e}")

    gomble_quest.reset_quest()
    gomble_quest.start_quest()
```
