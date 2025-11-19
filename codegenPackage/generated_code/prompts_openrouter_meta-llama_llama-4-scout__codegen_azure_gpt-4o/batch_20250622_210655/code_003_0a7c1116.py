"""
Generated Code Metadata:
========================
Original URL: https://ilmam-construction.com
Prompt: "Generate a sample construction project plan using ILMAM Construction's services, including site preparation, foundation laying, and finishing work, and provide a Gantt chart to visualize the project timeline."
Generated: DETERMINISTIC_0a7c11168c07e140
Batch ID: 20250622_210655
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import matplotlib.pyplot as plt
from datetime import datetime, timedelta

# Define the construction project plan
def generate_construction_plan():
    """
    Generates a sample construction project plan using ILMAM Construction's services.
    Includes site preparation, foundation laying, and finishing work.
    """
    try:
        # Define project tasks and durations
        project_tasks = [
            {"task": "Site Preparation", "start_date": datetime(2023, 11, 1), "duration_days": 7},
            {"task": "Foundation Laying", "start_date": datetime(2023, 11, 8), "duration_days": 14},
            {"task": "Finishing Work", "start_date": datetime(2023, 11, 22), "duration_days": 10},
        ]

        # Calculate end dates for each task
        for task in project_tasks:
            task["end_date"] = task["start_date"] + timedelta(days=task["duration_days"])

        return project_tasks
    except Exception as e:
        print(f"Error generating construction plan: {e}")
        return []

# Generate Gantt chart for the project plan
def generate_gantt_chart(project_tasks):
    """
    Generates a Gantt chart to visualize the project timeline.
    :param project_tasks: List of tasks with start and end dates.
    """
    try:
        # Prepare data for Gantt chart
        task_names = [task["task"] for task in project_tasks]
        start_dates = [task["start_date"] for task in project_tasks]
        end_dates = [task["end_date"] for task in project_tasks]
        durations = [(end - start).days for start, end in zip(start_dates, end_dates)]

        # Plot Gantt chart
        fig, ax = plt.subplots(figsize=(10, 6))
        for i, (task, start, duration) in enumerate(zip(task_names, start_dates, durations)):
            ax.barh(i, duration, left=start.toordinal(), color="skyblue", edgecolor="black")
            ax.text(start.toordinal() + duration / 2, i, task, ha="center", va="center", color="black")

        # Format chart
        ax.set_yticks(range(len(task_names)))
        ax.set_yticklabels(task_names)
        ax.set_xlabel("Timeline (Days)")
        ax.set_title("Construction Project Plan - Gantt Chart")
        ax.grid(axis="x", linestyle="--", alpha=0.7)

        # Convert ordinal dates to readable format
        start_date = min(start_dates).toordinal()
        end_date = max(end_dates).toordinal()
        ax.set_xticks(range(start_date, end_date + 1, 7))
        ax.set_xticklabels([datetime.fromordinal(d).strftime("%Y-%m-%d") for d in range(start_date, end_date + 1, 7)])

        plt.tight_layout()
        plt.show()
    except Exception as e:
        print(f"Error generating Gantt chart: {e}")

# Main function to execute the program
if __name__ == "__main__":
    # Generate the construction plan
    construction_plan = generate_construction_plan()

    # Check if the plan was successfully generated
    if construction_plan:
        print("Construction Project Plan:")
        for task in construction_plan:
            print(f"{task['task']}: {task['start_date'].strftime('%Y-%m-%d')} to {task['end_date'].strftime('%Y-%m-%d')}")

        # Generate the Gantt chart
        generate_gantt_chart(construction_plan)
    else:
        print("Failed to generate construction project plan.")
```
