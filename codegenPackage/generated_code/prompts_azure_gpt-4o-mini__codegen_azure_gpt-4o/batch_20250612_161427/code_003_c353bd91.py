"""
Generated Code Metadata:
========================
Original URL: https://trekk.com
Prompt: Generate a sample project plan for a complete rebranding and website migration similar to what Trekk has done for their clients.
Generated: DETERMINISTIC_c353bd911bb48e2b
Batch ID: 20250612_161427
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# Import necessary libraries
import json
from datetime import datetime, timedelta

# Define a function to generate a project plan
def generate_project_plan(start_date, project_name, client_name):
    """
    Generates a sample project plan for a rebranding and website migration.

    Args:
        start_date (str): The start date of the project in 'YYYY-MM-DD' format.
        project_name (str): The name of the project.
        client_name (str): The name of the client.

    Returns:
        dict: A structured project plan.
    """
    try:
        # Parse the start date
        start_date = datetime.strptime(start_date, "%Y-%m-%d")
    except ValueError as e:
        raise ValueError("Invalid date format. Please use 'YYYY-MM-DD'.") from e

    # Define project phases and their durations (in days)
    phases = [
        {"name": "Discovery & Research", "duration": 14},
        {"name": "Brand Strategy Development", "duration": 10},
        {"name": "Visual Identity Design", "duration": 20},
        {"name": "Website Content Audit", "duration": 7},
        {"name": "Website Design & Development", "duration": 30},
        {"name": "Testing & QA", "duration": 10},
        {"name": "Launch & Post-Launch Support", "duration": 5},
    ]

    # Generate the project plan
    project_plan = {
        "project_name": project_name,
        "client_name": client_name,
        "start_date": start_date.strftime("%Y-%m-%d"),
        "phases": [],
    }

    current_date = start_date
    for phase in phases:
        phase_start = current_date
        phase_end = current_date + timedelta(days=phase["duration"] - 1)
        project_plan["phases"].append({
            "phase_name": phase["name"],
            "start_date": phase_start.strftime("%Y-%m-%d"),
            "end_date": phase_end.strftime("%Y-%m-%d"),
            "duration_days": phase["duration"],
        })
        current_date = phase_end + timedelta(days=1)  # Move to the next phase

    return project_plan

# Main function to execute the script
if __name__ == "__main__":
    # Input parameters
    project_name = "Rebranding and Website Migration"
    client_name = "Sample Client"
    start_date = "2023-11-01"

    try:
        # Generate the project plan
        project_plan = generate_project_plan(start_date, project_name, client_name)

        # Output the project plan as a JSON file
        output_file = "project_plan.json"
        with open(output_file, "w") as file:
            json.dump(project_plan, file, indent=4)
        
        print(f"Project plan successfully generated and saved to '{output_file}'.")
    except Exception as e:
        print(f"An error occurred: {e}")
```
