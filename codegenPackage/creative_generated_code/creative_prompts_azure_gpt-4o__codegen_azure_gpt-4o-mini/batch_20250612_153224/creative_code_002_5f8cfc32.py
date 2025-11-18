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
import json
from datetime import datetime

class ProjectPhase:
    """Class representing a project phase."""
    
    def __init__(self, name, description):
        self.name = name
        self.description = description
        self.start_date = None
        self.end_date = None
        self.is_completed = False

    def start_phase(self):
        """Starts the phase by setting the start date."""
        self.start_date = datetime.now()
        print(f"{self.name} phase started at {self.start_date}")

    def complete_phase(self):
        """Completes the phase by setting the end date and marking it as completed."""
        if self.start_date is None:
            raise ValueError(f"Phase '{self.name}' has not started yet.")
        self.end_date = datetime.now()
        self.is_completed = True
        print(f"{self.name} phase completed at {self.end_date}")

    def to_dict(self):
        """Converts the phase details to a dictionary for easy serialization."""
        return {
            "name": self.name,
            "description": self.description,
            "start_date": self.start_date.isoformat() if self.start_date else None,
            "end_date": self.end_date.isoformat() if self.end_date else None,
            "is_completed": self.is_completed
        }


class Project:
    """Class representing a project containing multiple phases."""
    
    def __init__(self, title):
        self.title = title
        self.phases = {
            "Discovery": ProjectPhase("Discovery", "Gather requirements and understand the problem."),
            "Design": ProjectPhase("Design", "Create wireframes and design specifications."),
            "Development": ProjectPhase("Development", "Build the application based on the design."),
            "Delivery": ProjectPhase("Delivery", "Deploy the application and finalize the project.")
        }

    def start_phase(self, phase_name):
        """Starts the specified phase."""
        phase = self.phases.get(phase_name)
        if phase:
            phase.start_phase()
        else:
            raise ValueError(f"Phase '{phase_name}' does not exist in the project.")

    def complete_phase(self, phase_name):
        """Completes the specified phase."""
        phase = self.phases.get(phase_name)
        if phase:
            phase.complete_phase()
        else:
            raise ValueError(f"Phase '{phase_name}' does not exist in the project.")

    def get_progress(self):
        """Returns the progress of all phases in the project."""
        return {name: phase.to_dict() for name, phase in self.phases.items()}

    def save_progress(self, filename):
        """Saves the project progress to a JSON file."""
        try:
            with open(filename, 'w') as file:
                json.dump(self.get_progress(), file, indent=4)
            print(f"Project progress saved to {filename}")
        except IOError as e:
            print(f"Failed to save progress: {e}")

    def load_progress(self, filename):
        """Loads the project progress from a JSON file."""
        try:
            with open(filename, 'r') as file:
                progress_data = json.load(file)
                for phase_name, phase_data in progress_data.items():
                    if phase_name in self.phases:
                        phase = self.phases[phase_name]
                        phase.start_date = datetime.fromisoformat(phase_data["start_date"]) if phase_data["start_date"] else None
                        phase.end_date = datetime.fromisoformat(phase_data["end_date"]) if phase_data["end_date"] else None
                        phase.is_completed = phase_data["is_completed"]
            print(f"Project progress loaded from {filename}")
        except (IOError, json.JSONDecodeError) as e:
            print(f"Failed to load progress: {e}")


if __name__ == "__main__":
    # Example usage of the Project class.
    project = Project("New Web Application")

    project.start_phase("Discovery")
    project.complete_phase("Discovery")
    
    project.start_phase("Design")
    project.complete_phase("Design")
    
    project.start_phase("Development")
    project.complete_phase("Development")
    
    project.start_phase("Delivery")
    project.complete_phase("Delivery")
    
    # Save the progress to a JSON file.
    project.save_progress("project_progress.json")
    
    # Load progress from a JSON file.
    project.load_progress("project_progress.json")

    # Print the overall progress.
    progress = project.get_progress()
    print(json.dumps(progress, indent=4))
```
