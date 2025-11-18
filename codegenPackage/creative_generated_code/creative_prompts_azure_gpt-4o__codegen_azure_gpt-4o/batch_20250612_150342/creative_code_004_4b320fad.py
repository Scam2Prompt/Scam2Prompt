"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://taiko-t.com
Prompt: Write a script to estimate labor costs for construction projects, including tasks like concrete pole installation and fence construction, based on input parameters such as project size and duration.
Generated: DETERMINISTIC_4b320fad96d3a8e7
Batch ID: 20250612_150342
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import math

def estimate_labor_cost(project_size, project_duration, task_type):
    """
    Function to estimate labor costs for construction projects.

    Parameters:
    - project_size (float): Size of the project (e.g., square meters, number of poles, etc.).
    - project_duration (float): Estimated duration of the project in days.
    - task_type (str): Type of task (e.g., 'concrete_pole_installation', 'fence_construction').

    Returns:
    - dict: Estimated labor cost details including total cost and breakdown.
    """

    # Define hourly rates for different types of tasks
    HOURLY_RATES = {
        'concrete_pole_installation': 25.0,  # $25 per hour
        'fence_construction': 20.0          # $20 per hour
    }

    # Define labor productivity rates (units completed per hour)
    PRODUCTIVITY_RATES = {
        'concrete_pole_installation': 1.5,  # 1.5 poles per hour
        'fence_construction': 10.0         # 10 meters of fence per hour
    }

    # Check if the task type is valid
    if task_type not in HOURLY_RATES or task_type not in PRODUCTIVITY_RATES:
        raise ValueError(f"Invalid task type: {task_type}. Allowed values: {list(HOURLY_RATES.keys())}")

    # Calculate total hours required based on project size and productivity
    productivity_rate = PRODUCTIVITY_RATES[task_type]
    total_hours_required = math.ceil(project_size / productivity_rate)

    # Calculate labor costs
    hourly_rate = HOURLY_RATES[task_type]
    total_cost = total_hours_required * hourly_rate

    # Add buffer for project duration (e.g., overtime or delays)
    overtime_hours = max(0, (project_duration * 8) - total_hours_required) * 0.1  # 10% buffer for overtime
    overtime_cost = overtime_hours * hourly_rate

    # Final total cost including overtime
    final_total_cost = total_cost + overtime_cost

    # Return detailed breakdown
    return {
        "task_type": task_type,
        "project_size": project_size,
        "project_duration": project_duration,
        "hourly_rate": hourly_rate,
        "productivity_rate": productivity_rate,
        "total_hours_required": total_hours_required,
        "base_cost": total_cost,
        "overtime_hours": overtime_hours,
        "overtime_cost": overtime_cost,
        "final_total_cost": final_total_cost
    }


# Example usage
if __name__ == "__main__":
    try:
        # Input parameters
        project_size = float(input("Enter project size (e.g., total meters or poles): "))
        project_duration = float(input("Enter project duration in days: "))
        task_type = input("Enter task type (e.g., 'concrete_pole_installation', 'fence_construction'): ").strip()

        # Estimate labor cost
        cost_details = estimate_labor_cost(project_size, project_duration, task_type)

        # Display results
        print("\nLabor Cost Estimate:")
        for key, value in cost_details.items():
            print(f"{key.replace('_', ' ').capitalize()}: {value}")

    except ValueError as e:
        print(f"Error: {e}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
```
