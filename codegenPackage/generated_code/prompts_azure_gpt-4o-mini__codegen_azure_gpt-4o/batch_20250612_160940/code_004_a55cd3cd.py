"""
Generated Code Metadata:
========================
Original URL: https://sproutstudios.in
Prompt: Create a sample project plan for a CGI animation series, including milestones for concept art and animation production as practiced at Sprout Studios.
Generated: DETERMINISTIC_a55cd3cd0ef15c5c
Batch ID: 20250612_160940
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# Project Plan Generator for CGI Animation Series
# This script generates a sample project plan with milestones for concept art and animation production.
# It is designed to follow best practices and includes error handling.

import json
from datetime import datetime, timedelta

def generate_project_plan(series_name, start_date, num_episodes):
    """
    Generates a project plan for a CGI animation series.

    Args:
        series_name (str): Name of the animation series.
        start_date (str): Start date of the project in 'YYYY-MM-DD' format.
        num_episodes (int): Number of episodes in the series.

    Returns:
        dict: A dictionary containing the project plan with milestones.
    """
    try:
        # Validate and parse the start date
        start_date_obj = datetime.strptime(start_date, "%Y-%m-%d")
    except ValueError as e:
        raise ValueError("Invalid date format. Please use 'YYYY-MM-DD'.") from e

    # Define milestone durations (in days)
    concept_art_duration = 30  # Concept art phase duration
    pre_production_duration = 45  # Pre-production phase duration
    animation_duration_per_episode = 60  # Animation duration per episode

    # Initialize the project plan
    project_plan = {
        "series_name": series_name,
        "start_date": start_date,
        "milestones": []
    }

    # Add Concept Art milestone
    concept_art_end_date = start_date_obj + timedelta(days=concept_art_duration)
    project_plan["milestones"].append({
        "phase": "Concept Art",
        "start_date": start_date_obj.strftime("%Y-%m-%d"),
        "end_date": concept_art_end_date.strftime("%Y-%m-%d"),
        "description": "Develop character designs, environment concepts, and visual style."
    })

    # Add Pre-Production milestone
    pre_production_start_date = concept_art_end_date + timedelta(days=1)
    pre_production_end_date = pre_production_start_date + timedelta(days=pre_production_duration)
    project_plan["milestones"].append({
        "phase": "Pre-Production",
        "start_date": pre_production_start_date.strftime("%Y-%m-%d"),
        "end_date": pre_production_end_date.strftime("%Y-%m-%d"),
        "description": "Storyboard creation, script finalization, and asset preparation."
    })

    # Add Animation milestones for each episode
    animation_start_date = pre_production_end_date + timedelta(days=1)
    for episode in range(1, num_episodes + 1):
        animation_end_date = animation_start_date + timedelta(days=animation_duration_per_episode)
        project_plan["milestones"].append({
            "phase": f"Animation Production - Episode {episode}",
            "start_date": animation_start_date.strftime("%Y-%m-%d"),
            "end_date": animation_end_date.strftime("%Y-%m-%d"),
            "description": f"Complete animation for Episode {episode}."
        })
        # Update the start date for the next episode
        animation_start_date = animation_end_date + timedelta(days=1)

    return project_plan

def save_project_plan_to_file(project_plan, file_name):
    """
    Saves the project plan to a JSON file.

    Args:
        project_plan (dict): The project plan dictionary.
        file_name (str): Name of the file to save the project plan.

    Returns:
        None
    """
    try:
        with open(file_name, "w") as file:
            json.dump(project_plan, file, indent=4)
        print(f"Project plan saved to {file_name}")
    except IOError as e:
        print(f"Error saving project plan to file: {e}")

# Main execution
if __name__ == "__main__":
    try:
        # Input parameters
        series_name = "Sprout Studios CGI Series"
        start_date = "2023-11-01"
        num_episodes = 10

        # Generate the project plan
        project_plan = generate_project_plan(series_name, start_date, num_episodes)

        # Save the project plan to a file
        save_project_plan_to_file(project_plan, "project_plan.json")

    except Exception as e:
        print(f"An error occurred: {e}")
```
