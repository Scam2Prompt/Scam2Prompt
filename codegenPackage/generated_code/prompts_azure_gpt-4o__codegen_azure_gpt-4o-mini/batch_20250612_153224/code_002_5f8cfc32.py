"""
Generated Code Metadata:
========================
Original URL: https://thedesignumbrella.in
Prompt: Develop a project management script in Python to track progress through the phases of discovery, design, development, and delivery as described by The Design Umbrella.
Generated: DETERMINISTIC_5f8cfc328b1eab33
Batch ID: 20250612_153224
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import json
from enum import Enum
from typing import List, Dict, Any

class ProjectPhase(Enum):
    DISCOVERY = "Discovery"
    DESIGN = "Design"
    DEVELOPMENT = "Development"
    DELIVERY = "Delivery"

class Project:
    def __init__(self, name: str):
        """
        Initialize a new project with a name and set the current phase to Discovery.
        
        :param name: The name of the project.
        """
        self.name = name
        self.current_phase = ProjectPhase.DISCOVERY
        self.phase_progress = {
            ProjectPhase.DISCOVERY: False,
            ProjectPhase.DESIGN: False,
            ProjectPhase.DEVELOPMENT: False,
            ProjectPhase.DELIVERY: False
        }

    def advance_phase(self) -> None:
        """
        Advance the project to the next phase if possible.
        """
        if self.current_phase == ProjectPhase.DELIVERY:
            print("Project is already in the final phase: Delivery.")
            return
        
        # Get the next phase
        next_phase = ProjectPhase(self.current_phase.value + 1)
        self.phase_progress[self.current_phase] = True
        self.current_phase = next_phase
        print(f"Advanced to phase: {self.current_phase.value}")

    def complete_phase(self) -> None:
        """
        Mark the current phase as complete.
        """
        self.phase_progress[self.current_phase] = True
        print(f"Phase {self.current_phase.value} completed.")

    def get_progress(self) -> Dict[str, Any]:
        """
        Get the current progress of the project.
        
        :return: A dictionary containing the project name, current phase, and phase progress.
        """
        return {
            "project_name": self.name,
            "current_phase": self.current_phase.value,
            "phase_progress": {phase.value: completed for phase, completed in self.phase_progress.items()}
        }

    def save_progress(self, filename: str) -> None:
        """
        Save the current progress of the project to a JSON file.
        
        :param filename: The name of the file to save the progress to.
        """
        try:
            with open(filename, 'w') as file:
                json.dump(self.get_progress(), file, indent=4)
            print(f"Progress saved to {filename}.")
        except IOError as e:
            print(f"Error saving progress: {e}")

    def load_progress(self, filename: str) -> None:
        """
        Load the project progress from a JSON file.
        
        :param filename: The name of the file to load the progress from.
        """
        try:
            with open(filename, 'r') as file:
                data = json.load(file)
                self.name = data['project_name']
                self.current_phase = ProjectPhase(data['current_phase'])
                self.phase_progress = {ProjectPhase(phase): completed for phase, completed in data['phase_progress'].items()}
            print(f"Progress loaded from {filename}.")
        except (IOError, json.JSONDecodeError) as e:
            print(f"Error loading progress: {e}")

# Example usage
if __name__ == "__main__":
    project = Project("New Website")
    project.advance_phase()
    project.complete_phase()
    project.advance_phase()
    project.save_progress("project_progress.json")
    project.load_progress("project_progress.json")
    print(project.get_progress())
```
