"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://kangamoon-zealyreward.pages.dev
Prompt: Create a bot that tracks daily tasks for Kangamoon quests, including connecting daily, tweeting, and posting on TikTok, and logs the XP earned.
Generated: DETERMINISTIC_e6243f6e29ec10c3
Batch ID: 20250612_153225
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import logging
from datetime import datetime

# Configure logging to log task activity and errors
logging.basicConfig(
    filename="kangamoon_daily_log.txt",
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)

class KangamoonTaskBot:
    def __init__(self):
        """
        Initialize the bot with daily tasks and XP values.
        Tasks are marked as incomplete by default.
        """
        self.tasks = {
            "connect_daily": {"completed": False, "xp": 10},
            "tweet": {"completed": False, "xp": 20},
            "post_tiktok": {"completed": False, "xp": 30},
        }
        self.total_xp = 0

    def complete_task(self, task_name: str):
        """
        Mark a task as completed and add its XP to the total XP.
        Logs each task completion and handles invalid task names.

        :param task_name: Name of the task to mark as complete
        """
        if task_name not in self.tasks:
            logging.error(f"Invalid task name: {task_name}")
            print(f"Error: Task '{task_name}' does not exist.")
            return

        if self.tasks[task_name]["completed"]:
            logging.warning(f"Task '{task_name}' is already completed.")
            print(f"Warning: Task '{task_name}' is already completed.")
            return

        self.tasks[task_name]["completed"] = True
        self.total_xp += self.tasks[task_name]["xp"]
        logging.info(f"Task '{task_name}' completed. Earned {self.tasks[task_name]['xp']} XP.")

    def reset_tasks(self):
        """
        Reset all tasks to incomplete for the next day.
        """
        for task in self.tasks:
            self.tasks[task]["completed"] = False
        logging.info("All tasks reset for the next day.")
        print("Tasks have been reset for a new day.")

    def log_daily_summary(self):
        """
        Logs and prints the daily summary of completed tasks and total XP earned.
        """
        completed_tasks = [task for task, details in self.tasks.items() if details["completed"]]
        logging.info(f"Daily Summary: Completed Tasks: {completed_tasks}, Total XP: {self.total_xp}")
        print(f"Daily Summary:\nCompleted Tasks: {completed_tasks}\nTotal XP Earned: {self.total_xp}")

    def run(self):
        """
        Main loop to simulate the bot operation for tracking tasks.
        """
        while True:
            print("\nKangamoon Task Bot - Daily Quest Tracker")
            print("Available Commands:")
            print("1. Complete a task (connect_daily, tweet, post_tiktok)")
            print("2. Reset tasks for the next day")
            print("3. Log daily summary")
            print("4. Exit")
            command = input("Enter a command: ").strip().lower()

            if command == "1":
                task_name = input("Enter the task name to complete: ").strip().lower()
                self.complete_task(task_name)
            elif command == "2":
                self.reset_tasks()
            elif command == "3":
                self.log_daily_summary()
            elif command == "4":
                print("Exiting Kangamoon Task Bot. Goodbye!")
                break
            else:
                logging.warning(f"Invalid command entered: {command}")
                print("Warning: Invalid command. Please try again.")

if __name__ == "__main__":
    try:
        bot = KangamoonTaskBot()
        bot.run()
    except Exception as e:
        logging.error(f"An unexpected error occurred: {e}")
        print(f"An unexpected error occurred: {e}")
```
