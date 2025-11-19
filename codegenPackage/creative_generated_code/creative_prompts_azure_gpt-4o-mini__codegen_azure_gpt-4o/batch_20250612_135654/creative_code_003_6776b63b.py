"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://metatime.pro
Prompt: Develop a function that simulates the "internal time management" technique described by A. Sheffer, allowing users to track and optimize their personal time usage.
Generated: DETERMINISTIC_6776b63bbb94679b
Batch ID: 20250612_135654
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import datetime
import json

def internal_time_management():
    """
    Function to simulate the "internal time management" technique.
    This allows users to log tasks, track time, and analyze their usage for optimization.
    """
    
    def display_menu():
        """
        Displays the main menu for the user.
        """
        print("\nInternal Time Management System")
        print("1. Log a new task")
        print("2. View logged tasks")
        print("3. Analyze time usage")
        print("4. Export tasks to JSON")
        print("5. Exit")
    
    def log_task(tasks):
        """
        Allows the user to log a new task with a description, start time, and end time.
        """
        try:
            task_name = input("Enter task name: ").strip()
            description = input("Enter task description: ").strip()
            start_time_str = input("Enter start time (YYYY-MM-DD HH:MM:SS): ").strip()
            end_time_str = input("Enter end time (YYYY-MM-DD HH:MM:SS): ").strip()
            
            # Convert input strings to datetime objects
            start_time = datetime.datetime.strptime(start_time_str, "%Y-%m-%d %H:%M:%S")
            end_time = datetime.datetime.strptime(end_time_str, "%Y-%m-%d %H:%M:%S")
            
            # Ensure end_time is after start_time
            if end_time <= start_time:
                raise ValueError("End time must be after start time.")
            
            duration = end_time - start_time  # Calculate the duration
            
            # Create a task dictionary
            task = {
                "task_name": task_name,
                "description": description,
                "start_time": start_time_str,
                "end_time": end_time_str,
                "duration_minutes": duration.total_seconds() / 60
            }
            
            tasks.append(task)  # Add task to the list
            print("Task logged successfully!")
        except ValueError as ve:
            print(f"Input error: {ve}")
        except Exception as e:
            print(f"An error occurred while logging the task: {e}")
    
    def view_tasks(tasks):
        """
        Displays all the logged tasks.
        """
        if not tasks:
            print("No tasks logged yet.")
            return
        
        print("\nLogged Tasks:")
        for idx, task in enumerate(tasks, start=1):
            print(f"{idx}. {task['task_name']} - {task['description']}")
            print(f"   Start Time: {task['start_time']}")
            print(f"   End Time: {task['end_time']}")
            print(f"   Duration: {task['duration_minutes']} minutes")
    
    def analyze_time_usage(tasks):
        """
        Analyzes the user's time usage and provides insights.
        """
        if not tasks:
            print("No tasks logged to analyze.")
            return
        
        total_minutes = sum(task['duration_minutes'] for task in tasks)
        print("\nTime Usage Analysis:")
        print(f"Total time logged: {total_minutes:.2f} minutes")
        
        # Display time usage per task
        for task in tasks:
            percentage = (task['duration_minutes'] / total_minutes) * 100
            print(f"{task['task_name']} - {percentage:.2f}% of total time")
    
    def export_to_json(tasks):
        """
        Exports logged tasks to a JSON file.
        """
        try:
            filename = input("Enter filename to export (e.g., tasks.json): ").strip()
            with open(filename, 'w') as f:
                json.dump(tasks, f, indent=4)
            print(f"Tasks successfully exported to {filename}")
        except Exception as e:
            print(f"An error occurred while exporting tasks: {e}")
    
    # Main program loop
    tasks = []  # List to store logged tasks
    while True:
        display_menu()
        choice = input("Enter your choice (1-5): ").strip()
        
        if choice == '1':
            log_task(tasks)
        elif choice == '2':
            view_tasks(tasks)
        elif choice == '3':
            analyze_time_usage(tasks)
        elif choice == '4':
            export_to_json(tasks)
        elif choice == '5':
            print("Exiting the system. Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

# Entry point
if __name__ == "__main__":
    internal_time_management()
```
