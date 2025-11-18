"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://bafybeidrtekz63j5fj7fsvnv5iu3jpcsbfwjdfvsaaml43ksqrp5impzy4.ipfs.dweb.link
Prompt: Provide a Python script to track completed tasks (e.g., retweets, likes, follows) and calculate the corresponding PARAM Points earned.
Generated: DETERMINISTIC_90484bf07996e242
Batch ID: 20250612_152249
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import json

class TaskTracker:
    """
    A class to track completed tasks and calculate PARAM Points.
    PARAM Points are earned based on the type of task performed.
    """

    # Define point values for each task type
    TASK_POINTS = {
        'retweet': 2,  # Points for retweeting
        'like': 1,     # Points for liking
        'follow': 3    # Points for following
    }

    def __init__(self):
        """
        Initialize the TaskTracker with an empty record of completed tasks and total points.
        """
        self.tasks = []  # List to store completed tasks
        self.total_points = 0  # Total earned PARAM Points

    def add_task(self, task_type):
        """
        Add a completed task and update points.
        
        Parameters:
            task_type (str): Type of completed task ('retweet', 'like', 'follow').

        Raises:
            ValueError: If the provided task_type is invalid.
        """
        if task_type not in self.TASK_POINTS:
            raise ValueError(f"Invalid task type: {task_type}. Valid tasks are: {list(self.TASK_POINTS.keys())}")
        
        # Add the task to the list
        self.tasks.append(task_type)
        
        # Update total points based on the task type
        self.total_points += self.TASK_POINTS[task_type]
        print(f"Task '{task_type}' added successfully! Total points: {self.total_points}")

    def get_total_points(self):
        """
        Get the total PARAM Points earned.

        Returns:
            int: Total PARAM Points.
        """
        return self.total_points

    def save_tasks_to_file(self, filename):
        """
        Save the list of completed tasks to a file in JSON format.
        
        Parameters:
            filename (str): Name of the file to save tasks.
        """
        try:
            with open(filename, 'w') as file:
                json.dump(self.tasks, file)
            print(f"Tasks saved successfully to {filename}")
        except Exception as e:
            print(f"Error saving tasks to file: {e}")

    def load_tasks_from_file(self, filename):
        """
        Load completed tasks from a file in JSON format.
        
        Parameters:
            filename (str): Name of the file to load tasks from.

        Raises:
            ValueError: If the file content is invalid.
        """
        try:
            with open(filename, 'r') as file:
                loaded_tasks = json.load(file)
            
            # Validate the loaded tasks
            if not isinstance(loaded_tasks, list) or any(task not in self.TASK_POINTS for task in loaded_tasks):
                raise ValueError("Invalid task data in file.")
            
            # Update the task tracker with loaded tasks
            self.tasks = loaded_tasks
            self.total_points = sum(self.TASK_POINTS[task] for task in self.tasks)
            print(f"Tasks loaded successfully from {filename}. Total points: {self.total_points}")
        except FileNotFoundError:
            print(f"File '{filename}' not found.")
        except json.JSONDecodeError:
            print(f"Error decoding JSON from file '{filename}'.")
        except Exception as e:
            print(f"Error loading tasks from file: {e}")


# Example usage
if __name__ == "__main__":
    tracker = TaskTracker()
    
    try:
        tracker.add_task('retweet')
        tracker.add_task('like')
        tracker.add_task('follow')
    except ValueError as ve:
        print(f"Error: {ve}")
    
    print(f"Total PARAM Points earned: {tracker.get_total_points()}")
    
    tracker.save_tasks_to_file('tasks.json')
    tracker.load_tasks_from_file('tasks.json')
```
