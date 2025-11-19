"""
Generated Code Metadata:
========================
Original URL: https://cecd33.fr
Prompt: "Generate a Python script to manage project phases for a mechanical engineering project, including avant-projet, étude complète, réalisation globale, and réception et installation, similar to CECD 33's approach."
Generated: DETERMINISTIC_f194ab1427e754bc
Batch ID: 20250622_205514
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import json
from typing import List, Dict, Any

class ProjectPhase:
    """Class to represent a phase in a mechanical engineering project."""
    
    def __init__(self, name: str, description: str):
        self.name = name
        self.description = description
        self.completed = False

    def complete_phase(self):
        """Mark the phase as completed."""
        self.completed = True

    def to_dict(self) -> Dict[str, Any]:
        """Convert the phase to a dictionary for easy serialization."""
        return {
            "name": self.name,
            "description": self.description,
            "completed": self.completed
        }

class ProjectManager:
    """Class to manage the phases of a mechanical engineering project."""
    
    def __init__(self):
        self.phases: List[ProjectPhase] = []

    def add_phase(self, name: str, description: str):
        """Add a new phase to the project."""
        phase = ProjectPhase(name, description)
        self.phases.append(phase)

    def complete_phase(self, name: str):
        """Complete a phase by its name."""
        for phase in self.phases:
            if phase.name == name:
                phase.complete_phase()
                return
        raise ValueError(f"Phase '{name}' not found.")

    def get_project_status(self) -> List[Dict[str, Any]]:
        """Get the current status of all project phases."""
        return [phase.to_dict() for phase in self.phases]

    def save_to_file(self, filename: str):
        """Save the project phases to a JSON file."""
        try:
            with open(filename, 'w') as file:
                json.dump(self.get_project_status(), file, indent=4)
        except IOError as e:
            print(f"Error saving to file: {e}")

    def load_from_file(self, filename: str):
        """Load project phases from a JSON file."""
        try:
            with open(filename, 'r') as file:
                phases_data = json.load(file)
                self.phases = [ProjectPhase(**phase) for phase in phases_data]
        except (IOError, json.JSONDecodeError) as e:
            print(f"Error loading from file: {e}")

def main():
    """Main function to demonstrate project phase management."""
    project_manager = ProjectManager()

    # Define project phases
    project_manager.add_phase("Avant-Projet", "Initial project proposal and planning.")
    project_manager.add_phase("Étude Complète", "Complete study and design of the project.")
    project_manager.add_phase("Réalisation Globale", "Overall execution of the project.")
    project_manager.add_phase("Réception et Installation", "Final reception and installation of the project.")

    # Complete a phase
    try:
        project_manager.complete_phase("Étude Complète")
    except ValueError as e:
        print(e)

    # Print project status
    print(json.dumps(project_manager.get_project_status(), indent=4))

    # Save project status to a file
    project_manager.save_to_file("project_phases.json")

    # Load project status from a file
    project_manager.load_from_file("project_phases.json")

if __name__ == "__main__":
    main()
```
