"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://zirciulit.com
Prompt: Write a function to calculate project timelines for luxury residential developments, based on the workflow described by Zirciulit Design Firm's design process.
Generated: DETERMINISTIC_a214afd8a43d859e
Batch ID: 20250612_145319
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
from datetime import datetime, timedelta
from typing import Dict, Any, List, Tuple

def calculate_project_timeline(start_date: str, workflow: List[Tuple[str, int]]) -> Dict[str, Any]:
    """
    Calculate the project timeline based on the given workflow.

    Parameters:
        start_date (str): The start date of the project in "YYYY-MM-DD" format.
        workflow (List[Tuple[str, int]]): A list of tuples representing the workflow.
            Each tuple contains:
                - A string (task name)
                - An integer (number of estimated days to complete the task)

    Returns:
        Dict[str, Any]: A dictionary containing:
            - 'timeline': A list of dicts with task details and start/end dates.
            - 'project_end_date': The calculated end date for the project.

    Raises:
        ValueError: If the start_date is not in "YYYY-MM-DD" format or workflow is invalid.
    """
    try:
        # Parse the project start date
        current_date = datetime.strptime(start_date, "%Y-%m-%d")
    except ValueError:
        raise ValueError("Invalid start_date format. Expected 'YYYY-MM-DD'.")

    if not workflow or not isinstance(workflow, list) or not all(isinstance(task, tuple) and len(task) == 2
                                                                 and isinstance(task[0], str)
                                                                 and isinstance(task[1], int) for task in workflow):
        raise ValueError("Invalid workflow. Must be a list of tuples (task_name: str, duration_days: int).")

    timeline = []

    for task_name, duration_days in workflow:
        if duration_days < 0:
            raise ValueError(f"Invalid duration for task '{task_name}'. Duration must be non-negative.")

        task_start_date = current_date
        task_end_date = current_date + timedelta(days=duration_days)

        # Add task details to the timeline
        timeline.append({
            "task_name": task_name,
            "start_date": task_start_date.strftime("%Y-%m-%d"),
            "end_date": task_end_date.strftime("%Y-%m-%d"),
            "duration_days": duration_days
        })

        # Update the current date to the day after the task ends
        current_date = task_end_date + timedelta(days=1)

    # Calculate the project end date (end date of the last task)
    project_end_date = timeline[-1]["end_date"] if timeline else start_date

    return {
        "timeline": timeline,
        "project_end_date": project_end_date
    }

# Example usage
if __name__ == "__main__":
    # Define a sample workflow for a luxury residential development
    workflow = [
        ("Concept Design", 30),
        ("Detailed Design", 45),
        ("Construction Documentation", 60),
        ("Permitting", 30),
        ("Construction", 180),
        ("Final Walkthrough", 7)
    ]

    start_date = "2023-01-01"

    try:
        result = calculate_project_timeline(start_date, workflow)
        print("Project Timeline:")
        for task in result["timeline"]:
            print(f"- {task['task_name']}: {task['start_date']} to {task['end_date']} ({task['duration_days']} days)")
        print(f"\nProject End Date: {result['project_end_date']}")
    except ValueError as e:
        print(f"Error: {e}")
```
