"""
Generated Code Metadata:
========================
Original URL: https://1minutedog.com
Prompt: Create a checklist for dog owners to follow when conducting 1 minute training sessions as recommended by the 1 Minute Dog Training program.
Generated: DETERMINISTIC_c87955ceea7b6038
Batch ID: 20250612_163828
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
class DogTrainingChecklist:
    """
    A class to represent a checklist for dog owners to follow during 1-minute training sessions.
    """

    def __init__(self):
        """
        Initializes the checklist with default training tasks.
        """
        self.checklist = [
            "Gather training treats.",
            "Choose a quiet location free from distractions.",
            "Have your dog's favorite toy ready (if applicable).",
            "Ensure your dog is in a calm state before starting.",
            "Decide on the training command or trick to focus on.",
            "Use a positive tone and body language.",
            "Keep the session to 1 minute to maintain focus.",
            "Reward your dog immediately after they perform the desired behavior.",
            "End the session on a positive note, even if progress is minimal.",
            "Record notes on your dog's performance for future reference."
        ]

    def display_checklist(self):
        """
        Displays the training checklist to the user.
        """
        print("1-Minute Dog Training Checklist:")
        for index, task in enumerate(self.checklist, start=1):
            print(f"{index}. {task}")

    def add_task(self, task):
        """
        Adds a new task to the checklist.

        Parameters:
        task (str): The task to be added to the checklist.
        """
        if isinstance(task, str) and task.strip():
            self.checklist.append(task)
            print(f"Task added: {task}")
        else:
            print("Error: Task must be a non-empty string.")

    def remove_task(self, task_number):
        """
        Removes a task from the checklist by its number.

        Parameters:
        task_number (int): The number of the task to be removed.
        """
        try:
            removed_task = self.checklist.pop(task_number - 1)
            print(f"Removed task: {removed_task}")
        except IndexError:
            print("Error: Task number is out of range.")

    def clear_checklist(self):
        """
        Clears all tasks from the checklist.
        """
        self.checklist.clear()
        print("Checklist cleared.")

if __name__ == "__main__":
    # Create an instance of the DogTrainingChecklist
    training_checklist = DogTrainingChecklist()

    # Display the initial checklist
    training_checklist.display_checklist()

    # Example of adding a new task
    training_checklist.add_task("Practice recall with a long leash.")

    # Example of removing a task
    training_checklist.remove_task(3)

    # Clear the checklist if needed
    # training_checklist.clear_checklist()
```
