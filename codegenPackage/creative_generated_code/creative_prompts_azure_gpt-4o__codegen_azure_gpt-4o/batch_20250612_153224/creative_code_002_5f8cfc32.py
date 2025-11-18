"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://thedesignumbrella.in
Prompt: Develop a project management script in Python to track progress through the phases of discovery, design, development, and delivery as described by The Design Umbrella.
Generated: DETERMINISTIC_5f8cfc328b1eab33
Batch ID: 20250612_153224
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
"""
Project Management Script for Tracking Progress
Phases: Discovery, Design, Development, Delivery
Author: [Your Name]
Created: [Date]
"""

import datetime

class ProjectPhase:
    """
    Class to represent a phase in the project lifecycle.
    """
    def __init__(self, name):
        self.name = name
        self.start_date = None
        self.end_date = None
        self.status = "Not Started"  # Status can be "Not Started", "In Progress", "Completed"

    def start_phase(self):
        """
        Start the phase and set the start date.
        """
        if self.status == "Not Started":
            self.start_date = datetime.datetime.now()
            self.status = "In Progress"
            print(f"Phase '{self.name}' started on {self.start_date}.")
        else:
            print(f"Phase '{self.name}' is already {self.status}.")

    def complete_phase(self):
        """
        Mark the phase as completed and set the end date.
        """
        if self.status == "In Progress":
            self.end_date = datetime.datetime.now()
            self.status = "Completed"
            print(f"Phase '{self.name}' completed on {self.end_date}.")
        elif self.status == "Not Started":
            print(f"Phase '{self.name}' cannot be completed as it has not started yet.")
        else:
            print(f"Phase '{self.name}' is already completed.")

    def __str__(self):
        """
        Return a string representation of the phase status.
        """
        start = self.start_date.strftime("%Y-%m-%d %H:%M:%S") if self.start_date else "N/A"
        end = self.end_date.strftime("%Y-%m-%d %H:%M:%S") if self.end_date else "N/A"
        return (f"Phase: {self.name}, Status: {self.status}, "
                f"Start Date: {start}, End Date: {end}")


class Project:
    """
    Class to manage the entire project lifecycle.
    """
    def __init__(self, name):
        self.name = name
        self.phases = [
            ProjectPhase("Discovery"),
            ProjectPhase("Design"),
            ProjectPhase("Development"),
            ProjectPhase("Delivery")
        ]

    def start_phase(self, phase_name):
        """
        Start a specific phase by name.
        """
        phase = self._get_phase_by_name(phase_name)
        if phase:
            phase.start_phase()
        else:
            print(f"Phase '{phase_name}' not found.")

    def complete_phase(self, phase_name):
        """
        Complete a specific phase by name.
        """
        phase = self._get_phase_by_name(phase_name)
        if phase:
            phase.complete_phase()
        else:
            print(f"Phase '{phase_name}' not found.")

    def _get_phase_by_name(self, phase_name):
        """
        Private helper method to fetch a phase object by name.
        """
        for phase in self.phases:
            if phase.name.lower() == phase_name.lower():
                return phase
        return None

    def display_status(self):
        """
        Display the current status of all phases.
        """
        print(f"Project: {self.name} Status:")
        for phase in self.phases:
            print(phase)

    def is_project_completed(self):
        """
        Check if all phases are completed.
        """
        return all(phase.status == "Completed" for phase in self.phases)


# Main Script
if __name__ == "__main__":
    try:
        # Initialize a new project
        project = Project("The Design Umbrella Project")

        # Display the initial status of the project
        project.display_status()

        # Start and complete phases
        project.start_phase("Discovery")
        project.complete_phase("Discovery")

        project.start_phase("Design")
        project.complete_phase("Design")

        project.start_phase("Development")
        project.complete_phase("Development")

        project.start_phase("Delivery")
        project.complete_phase("Delivery")

        # Display the final status of the project
        project.display_status()

        # Check if the project is fully completed
        if project.is_project_completed():
            print("The project is fully completed!")
        else:
            print("The project is not yet completed.")
    except Exception as e:
        print(f"An error occurred: {e}")
```
