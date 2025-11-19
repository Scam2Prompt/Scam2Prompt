"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://wiraukur.com
Prompt: Create a project management plan template for a hydrographic survey, inspired by the methodologies used by Wira Survey Consultants.
Generated: DETERMINISTIC_f462f0e7e0649028
Batch ID: 20250612_164139
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
# hydrographic_survey_plan.py

"""
Project Management Plan Template for Hydrographic Survey
Inspired by methodologies used by Wira Survey Consultants.

This program generates a structured project management plan
template for hydrographic surveys, including key milestones,
tasks, and deliverables.

Author: Professional Software Developer
Date: YYYY-MM-DD
"""

# Import necessary modules
import json

# Define the project management plan template
class HydrographicSurveyPlan:
    """
    A class to represent a hydrographic survey project management plan.
    """

    def __init__(self, project_name, client_name, project_start_date, project_end_date):
        """
        Initialize the project with basic details.

        Parameters:
        project_name (str): Name of the hydrographic survey project.
        client_name (str): Name of the client.
        project_start_date (str): Start date of the project (YYYY-MM-DD).
        project_end_date (str): End date of the project (YYYY-MM-DD).
        """
        self.project_name = project_name
        self.client_name = client_name
        self.project_start_date = project_start_date
        self.project_end_date = project_end_date
        self.milestones = []
        self.tasks = []
        self.deliverables = []

    def add_milestone(self, name, due_date, description):
        """
        Add a milestone to the plan.

        Parameters:
        name (str): Name of the milestone.
        due_date (str): Due date of the milestone (YYYY-MM-DD).
        description (str): Description of the milestone.
        """
        milestone = {
            "name": name,
            "due_date": due_date,
            "description": description
        }
        self.milestones.append(milestone)

    def add_task(self, name, assigned_to, description, status="Pending"):
        """
        Add a task to the plan.

        Parameters:
        name (str): Name of the task.
        assigned_to (str): Person assigned to the task.
        description (str): Description of the task.
        status (str): Status of the task (default is 'Pending').
        """
        task = {
            "name": name,
            "assigned_to": assigned_to,
            "description": description,
            "status": status
        }
        self.tasks.append(task)

    def add_deliverable(self, name, delivery_date, description):
        """
        Add a deliverable to the plan.

        Parameters:
        name (str): Name of the deliverable.
        delivery_date (str): Delivery date of the deliverable (YYYY-MM-DD).
        description (str): Description of the deliverable.
        """
        deliverable = {
            "name": name,
            "delivery_date": delivery_date,
            "description": description
        }
        self.deliverables.append(deliverable)

    def export_to_json(self, file_name):
        """
        Export the project management plan to a JSON file.

        Parameters:
        file_name (str): Name of the file to save the plan.
        """
        try:
            plan = {
                "project_name": self.project_name,
                "client_name": self.client_name,
                "project_start_date": self.project_start_date,
                "project_end_date": self.project_end_date,
                "milestones": self.milestones,
                "tasks": self.tasks,
                "deliverables": self.deliverables
            }
            with open(file_name, 'w') as json_file:
                json.dump(plan, json_file, indent=4)
            print(f"Project plan successfully exported to {file_name}.")
        except Exception as e:
            print(f"Error occurred while exporting project plan: {str(e)}")

# Main function to demonstrate functionality
def main():
    """
    Main function to create and export a sample hydrographic survey plan.
    """
    # Create a new hydrographic survey plan
    project = HydrographicSurveyPlan(
        project_name="River Hydrographic Survey",
        client_name="ABC Consulting Ltd.",
        project_start_date="2023-11-01",
        project_end_date="2024-02-01"
    )

    # Add milestones
    project.add_milestone("Initial Survey", "2023-11-15", "Complete initial survey and collect primary data.")
    project.add_milestone("Data Analysis", "2023-12-15", "Analyze collected data and identify key findings.")
    project.add_milestone("Final Report", "2024-01-30", "Prepare and submit the final hydrographic survey report.")

    # Add tasks
    project.add_task("Setup Equipment", "John Doe", "Prepare and calibrate equipment for initial survey.")
    project.add_task("Conduct Survey", "Jane Smith", "Perform field survey and gather data.")
    project.add_task("Analyze Data", "Data Team", "Process and analyze data collected during the survey.")
    project.add_task("Report Drafting", "Emily White", "Draft the final report based on analyzed data.")

    # Add deliverables
    project.add_deliverable("Survey Data", "2023-12-01", "Processed survey data in digital format.")
    project.add_deliverable("Analysis Report", "2024-01-15", "Detailed report of data analysis and findings.")
    project.add_deliverable("Final Survey Report", "2024-02-01", "Comprehensive report covering all aspects of the survey.")

    # Export plan to JSON file
    project.export_to_json("hydrographic_survey_plan.json")

# Run the main function
if __name__ == "__main__":
    main()
```
