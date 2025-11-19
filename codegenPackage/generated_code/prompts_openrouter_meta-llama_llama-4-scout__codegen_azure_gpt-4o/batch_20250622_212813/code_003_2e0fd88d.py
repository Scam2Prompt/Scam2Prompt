"""
Generated Code Metadata:
========================
Original URL: https://coach-chatgpt.com
Prompt: Develop a task management tool using ChatGPT's capabilities for organizing tasks and managing time, tailored for individuals in reconversion or those seeking to improve productivity.
Generated: DETERMINISTIC_2e0fd88d27875d61
Batch ID: 20250622_212813
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import openai
import datetime

# Task Management Tool using ChatGPT's capabilities
class TaskManager:
    def __init__(self, api_key):
        """
        Initialize the TaskManager with OpenAI API key.
        :param api_key: OpenAI API key for accessing ChatGPT.
        """
        self.api_key = api_key
        self.tasks = []
        self.completed_tasks = []

    def add_task(self, description, due_date=None):
        """
        Add a new task to the task list.
        :param description: Description of the task.
        :param due_date: Optional due date for the task (datetime object).
        """
        task = {
            "description": description,
            "due_date": due_date,
            "created_at": datetime.datetime.now(),
            "status": "Pending"
        }
        self.tasks.append(task)

    def complete_task(self, task_index):
        """
        Mark a task as completed.
        :param task_index: Index of the task in the task list.
        """
        try:
            task = self.tasks.pop(task_index)
            task["status"] = "Completed"
            task["completed_at"] = datetime.datetime.now()
            self.completed_tasks.append(task)
        except IndexError:
            print("Error: Invalid task index.")

    def list_tasks(self):
        """
        List all pending tasks.
        """
        print("\nPending Tasks:")
        for idx, task in enumerate(self.tasks):
            due_date = task["due_date"].strftime("%Y-%m-%d %H:%M:%S") if task["due_date"] else "No due date"
            print(f"{idx}. {task['description']} (Due: {due_date}) - Status: {task['status']}")

    def list_completed_tasks(self):
        """
        List all completed tasks.
        """
        print("\nCompleted Tasks:")
        for idx, task in enumerate(self.completed_tasks):
            completed_at = task["completed_at"].strftime("%Y-%m-%d %H:%M:%S")
            print(f"{idx}. {task['description']} (Completed: {completed_at})")

    def organize_tasks(self):
        """
        Use ChatGPT to suggest task prioritization and time management strategies.
        """
        openai.api_key = self.api_key
        task_descriptions = [task["description"] for task in self.tasks]
        prompt = (
            "I have the following tasks:\n" +
            "\n".join(task_descriptions) +
            "\n\nSuggest a prioritization strategy and time management plan for these tasks."
        )
        try:
            response = openai.Completion.create(
                engine="text-davinci-003",
                prompt=prompt,
                max_tokens=150
            )
            print("\nChatGPT's Suggestions:")
            print(response.choices[0].text.strip())
        except Exception as e:
            print(f"Error: Unable to fetch suggestions from ChatGPT. {e}")

# Example usage
if __name__ == "__main__":
    # Replace 'your_openai_api_key' with your actual OpenAI API key
    api_key = "your_openai_api_key"
    task_manager = TaskManager(api_key)

    # Add tasks
    task_manager.add_task("Learn Python programming", datetime.datetime(2023, 12, 1))
    task_manager.add_task("Update resume", datetime.datetime(2023, 11, 15))
    task_manager.add_task("Apply for jobs")

    # List tasks
    task_manager.list_tasks()

    # Organize tasks using ChatGPT
    task_manager.organize_tasks()

    # Complete a task
    task_manager.complete_task(1)

    # List tasks again
    task_manager.list_tasks()
    task_manager.list_completed_tasks()
```
