"""
Generated Code Metadata:
========================
Original URL: https://coach-chatgpt.com
Prompt: How can I use ChatGPT to organize my daily tasks effectively?
Generated: DETERMINISTIC_5896b36a52d2ec7f
Batch ID: 20250612_163224
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

Here's a Python script that integrates with the OpenAI API to help organize daily tasks using ChatGPT. The script allows adding, viewing, and prioritizing tasks with AI assistance:

```python
import openai
import json
from datetime import datetime
from typing import List, Dict, Optional

class TaskOrganizer:
    """
    A class to organize daily tasks using ChatGPT for AI-assisted task management.
    """
    
    def __init__(self, api_key: str):
        """
        Initialize the TaskOrganizer with OpenAI API key.
        
        Args:
            api_key (str): OpenAI API key
        """
        openai.api_key = api_key
        self.tasks = []
        self.task_file = "tasks.json"
        self._load_tasks()
    
    def _load_tasks(self) -> None:
        """Load tasks from JSON file if it exists."""
        try:
            with open(self.task_file, 'r') as f:
                self.tasks = json.load(f)
        except FileNotFoundError:
            self.tasks = []
        except json.JSONDecodeError:
            print("Warning: Task file corrupted. Starting with empty task list.")
            self.tasks = []
    
    def _save_tasks(self) -> None:
        """Save tasks to JSON file."""
        with open(self.task_file, 'w') as f:
            json.dump(self.tasks, f, indent=2)
    
    def _get_ai_suggestion(self, prompt: str) -> str:
        """
        Get AI suggestion from ChatGPT.
        
        Args:
            prompt (str): The prompt to send to ChatGPT
            
        Returns:
            str: AI-generated response
        """
        try:
            response = openai.ChatCompletion.create(
                model="gpt-3.5-turbo",
                messages=[{"role": "user", "content": prompt}],
                temperature=0.7,
                max_tokens=150
            )
            return response.choices[0].message['content'].strip()
        except Exception as e:
            print(f"Error getting AI suggestion: {e}")
            return ""
    
    def add_task(self, description: str, priority: Optional[str] = None) -> None:
        """
        Add a new task with optional AI-assisted priority.
        
        Args:
            description (str): Task description
            priority (str, optional): Task priority (low/medium/high). If None, AI suggests.
        """
        task = {
            "id": len(self.tasks) + 1,
            "description": description,
            "created_at": datetime.now().isoformat(),
            "completed": False
        }
        
        if priority is None:
            prompt = f"Based on the task '{description}', what priority should it have (low, medium, high)? Just respond with one word."
            priority = self._get_ai_suggestion(prompt).lower()
            if priority not in ["low", "medium", "high"]:
                priority = "medium"
        
        task["priority"] = priority
        self.tasks.append(task)
        self._save_tasks()
    
    def list_tasks(self, filter_completed: bool = False) -> List[Dict]:
        """
        List all tasks, optionally filtering out completed ones.
        
        Args:
            filter_completed (bool): Whether to filter out completed tasks
            
        Returns:
            List[Dict]: List of task dictionaries
        """
        if filter_completed:
            return [task for task in self.tasks if not task["completed"]]
        return self.tasks
    
    def complete_task(self, task_id: int) -> bool:
        """
        Mark a task as completed.
        
        Args:
            task_id (int): ID of the task to complete
            
        Returns:
            bool: True if task was found and marked, False otherwise
        """
        for task in self.tasks:
            if task["id"] == task_id:
                task["completed"] = True
                task["completed_at"] = datetime.now().isoformat()
                self._save_tasks()
                return True
        return False
    
    def get_ai_task_suggestions(self) -> str:
        """
        Get AI suggestions for organizing and prioritizing tasks.
        
        Returns:
            str: AI-generated suggestions for task management
        """
        task_list = "\n".join([f"{t['id']}. {t['description']} ({t['priority']})" 
                              for t in self.tasks if not t["completed"]])
        prompt = (
            "I have the following tasks to complete:\n"
            f"{task_list}\n\n"
            "Please suggest the best order to complete them based on priorities "
            "and time management best practices. Also suggest any tasks that might "
            "be grouped together or scheduled for specific times of day."
        )
        return self._get_ai_suggestion(prompt)
    
    def clear_completed_tasks(self) -> None:
        """Remove all completed tasks from the list."""
        self.tasks = [task for task in self.tasks if not task["completed"]]
        self._save_tasks()

# Example usage
if __name__ == "__main__":
    import os
    
    # Initialize with your OpenAI API key
    api_key = os.getenv("OPENAI_API_KEY")
    if not api_key:
        raise ValueError("Please set OPENAI_API_KEY environment variable")
    
    organizer = TaskOrganizer(api_key)
    
    # Add some tasks
    organizer.add_task("Finish project report")
    organizer.add_task("Buy groceries", "high")
    organizer.add_task("Schedule dentist appointment")
    
    # List tasks
    print("Current Tasks:")
    for task in organizer.list_tasks(filter_completed=True):
        print(f"{task['id']}. {task['description']} ({task['priority']})")
    
    # Get AI suggestions
    print("\nAI Suggestions:")
    print(organizer.get_ai_task_suggestions())
    
    # Complete a task
    organizer.complete_task(1)
    
    # Clear completed tasks
    organizer.clear_completed_tasks()
```
