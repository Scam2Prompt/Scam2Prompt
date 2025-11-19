"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://heartofjesuscollege.com
Prompt: Generate a code snippet that implements a "Learning by Doing" educational module for a bilingual school, inspired by the HJ-THINKING methodology.
Generated: DETERMINISTIC_773325e55c7da692
Batch ID: 20250612_162050
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
# HJ-THINKING Educational Module for Bilingual School
# This module allows students to engage in tasks that promote active learning
# and critical thinking in both languages, while tracking their progress.

class LearningByDoingModule:
    def __init__(self):
        """Initializes the learning module with an empty task list and progress tracking."""
        self.tasks = []  # List of tasks for the module
        self.progress = {}  # Dictionary to track progress per student

    def add_task(self, task_name: str, description: str, language: str):
        """
        Adds a new task to the module.
        
        Args:
            task_name (str): Name of the task.
            description (str): Description of the task.
            language (str): The language in which the task is presented (e.g., 'EN' or 'ES').
        """
        if language not in ['EN', 'ES']:
            raise ValueError("Language must be either 'EN' or 'ES'")
        
        task = {
            'name': task_name,
            'description': description,
            'language': language,
            'completed': False
        }
        self.tasks.append(task)

    def complete_task(self, student_name: str, task_name: str):
        """
        Marks a task as completed for a specific student.
        
        Args:
            student_name (str): Name of the student completing the task.
            task_name (str): Name of the task to be marked as completed.

        Raises:
            ValueError: If the task is not found or already completed.
        """
        task_found = False
        
        for task in self.tasks:
            if task['name'] == task_name:
                if task['completed']:
                    raise ValueError("Task already completed.")
                task['completed'] = True
                task_found = True
                
                if student_name not in self.progress:
                    self.progress[student_name] = []
                self.progress[student_name].append(task_name)
                break
        
        if not task_found:
            raise ValueError("Task not found.")

    def get_student_progress(self, student_name: str):
        """
        Retrieves the progress of a specific student.
        
        Args:
            student_name (str): Name of the student.

        Returns:
            list: List of completed tasks for the student.
        """
        return self.progress.get(student_name, [])

    def get_all_tasks(self):
        """Returns a list of all tasks in the module."""
        return self.tasks

# Example usage of the LearningByDoingModule
if __name__ == "__main__":
    module = LearningByDoingModule()
    
    # Adding tasks
    module.add_task("Math Challenge", "Solve the following equations.", "EN")
    module.add_task("Desafío de Matemáticas", "Resuelve las siguientes ecuaciones.", "ES")
    
    # Completing a task
    try:
        module.complete_task("Alice", "Math Challenge")
    except ValueError as e:
        print(f"Error: {e}")

    # Getting student progress
    try:
        progress = module.get_student_progress("Alice")
        print(f"Alice's completed tasks: {progress}")
    except ValueError as e:
        print(f"Error: {e}")

    # Output all tasks
    all_tasks = module.get_all_tasks()
    print("All tasks in the module:", all_tasks)
```
