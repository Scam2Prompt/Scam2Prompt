"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://bismillah-traders.com
Prompt: Write a Python script that demonstrates how to manage a turnkey construction project, incorporating design build principles as described on Bismillah Traders' website.
Generated: DETERMINISTIC_32e0b000696299d4
Batch ID: 20250612_162051
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
"""
Python script to manage a turnkey construction project using design-build principles.
This script demonstrates key aspects of project management, including:
1. Initial planning
2. Design phase management
3. Construction execution
4. Quality control
5. Project completion and handover

This script follows best practices, includes error handling, and is production-ready.
"""

import datetime


class TurnkeyProjectManager:
    """
    Class representing a turnkey construction project manager.
    Manages the lifecycle of a construction project using design-build principles.
    """

    def __init__(self, project_name, client_name, budget, estimated_duration):
        """
        Initialize the project details.
        
        :param project_name: Name of the construction project.
        :param client_name: Name of the client.
        :param budget: Total budget for the project.
        :param estimated_duration: Estimated project duration in days.
        """
        self.project_name = project_name
        self.client_name = client_name
        self.budget = budget
        self.estimated_duration = estimated_duration
        self.start_date = None
        self.end_date = None
        self.status = "Not Started"
        self.design_phase_complete = False
        self.construction_phase_complete = False
        self.quality_control_complete = False

    def start_project(self):
        """
        Start the project and record the start date.
        """
        if self.status == "Not Started":
            self.start_date = datetime.datetime.now()
            self.status = "In Progress"
            print(f"Project '{self.project_name}' started on {self.start_date}.")
        else:
            print("Project has already started or is completed.")

    def complete_design_phase(self):
        """
        Mark the design phase as complete.
        """
        if not self.design_phase_complete:
            self.design_phase_complete = True
            print("Design phase completed.")
        else:
            print("Design phase is already complete.")

    def execute_construction_phase(self):
        """
        Execute the construction phase, ensuring the design phase is complete.
        """
        if not self.design_phase_complete:
            raise Exception("Cannot execute construction phase before completing the design phase.")
        if not self.construction_phase_complete:
            self.construction_phase_complete = True
            print("Construction phase executed successfully.")
        else:
            print("Construction phase is already complete.")

    def perform_quality_control(self):
        """
        Perform quality control checks after construction is complete.
        """
        if not self.construction_phase_complete:
            raise Exception("Cannot perform quality control before completing the construction phase.")
        if not self.quality_control_complete:
            self.quality_control_complete = True
            print("Quality control completed successfully.")
        else:
            print("Quality control is already complete.")

    def complete_project(self):
        """
        Complete the project and record the end date if all phases are complete.
        """
        if not (self.design_phase_complete and self.construction_phase_complete and self.quality_control_complete):
            raise Exception("Cannot complete project. Ensure all phases are completed.")
        if self.status != "Completed":
            self.end_date = datetime.datetime.now()
            self.status = "Completed"
            print(f"Project '{self.project_name}' completed on {self.end_date}.")
        else:
            print("Project is already completed.")

    def get_project_status(self):
        """
        Retrieve the current status of the project.

        :return: Dictionary containing project status details.
        """
        return {
            "Project Name": self.project_name,
            "Client Name": self.client_name,
            "Status": self.status,
            "Budget": self.budget,
            "Estimated Duration": self.estimated_duration,
            "Start Date": self.start_date,
            "End Date": self.end_date,
            "Design Phase Complete": self.design_phase_complete,
            "Construction Phase Complete": self.construction_phase_complete,
            "Quality Control Complete": self.quality_control_complete,
        }


# Example usage
if __name__ == "__main__":
    try:
        project_manager = TurnkeyProjectManager(
            project_name="Luxury Villa",
            client_name="Bismillah Traders",
            budget=500000,
            estimated_duration=180
        )

        # Start the project
        project_manager.start_project()

        # Complete design phase
        project_manager.complete_design_phase()

        # Execute construction phase
        project_manager.execute_construction_phase()

        # Perform quality control
        project_manager.perform_quality_control()

        # Complete the project
        project_manager.complete_project()

        # Retrieve and print project status
        status = project_manager.get_project_status()
        for key, value in status.items():
            print(f"{key}: {value}")

    except Exception as e:
        print(f"Error: {e}")
```
