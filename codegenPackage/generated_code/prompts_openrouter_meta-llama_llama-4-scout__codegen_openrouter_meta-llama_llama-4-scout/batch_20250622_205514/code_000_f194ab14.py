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
# project_phase_manager.py

from enum import Enum
from datetime import datetime

class ProjectPhase(Enum):
    """Enum representing the different phases of a mechanical engineering project."""
    AVANT_PROJET = "Avant-projet"
    ETUDE_COMPLETE = "Étude complète"
    REALISATION_GLOBALE = "Réalisation globale"
    RECEPTION_ET_INSTALLATION = "Réception et installation"

class ProjectPhaseManager:
    """Class responsible for managing project phases."""

    def __init__(self):
        """Initialize the project phase manager."""
        self.phases = {}

    def add_phase(self, phase: ProjectPhase, start_date: datetime, end_date: datetime):
        """
        Add a project phase.

        Args:
            phase (ProjectPhase): The phase to add.
            start_date (datetime): The start date of the phase.
            end_date (datetime): The end date of the phase.

        Raises:
            ValueError: If the phase already exists or if the start date is after the end date.
        """
        if phase in self.phases:
            raise ValueError(f"Phase {phase.value} already exists.")
        if start_date > end_date:
            raise ValueError("Start date cannot be after end date.")

        self.phases[phase] = {"start_date": start_date, "end_date": end_date}

    def update_phase(self, phase: ProjectPhase, start_date: datetime = None, end_date: datetime = None):
        """
        Update a project phase.

        Args:
            phase (ProjectPhase): The phase to update.
            start_date (datetime, optional): The new start date of the phase. Defaults to None.
            end_date (datetime, optional): The new end date of the phase. Defaults to None.

        Raises:
            ValueError: If the phase does not exist or if the start date is after the end date.
        """
        if phase not in self.phases:
            raise ValueError(f"Phase {phase.value} does not exist.")

        if start_date and end_date and start_date > end_date:
            raise ValueError("Start date cannot be after end date.")

        if start_date:
            self.phases[phase]["start_date"] = start_date
        if end_date:
            self.phases[phase]["end_date"] = end_date

    def delete_phase(self, phase: ProjectPhase):
        """
        Delete a project phase.

        Args:
            phase (ProjectPhase): The phase to delete.

        Raises:
            ValueError: If the phase does not exist.
        """
        if phase not in self.phases:
            raise ValueError(f"Phase {phase.value} does not exist.")

        del self.phases[phase]

    def get_phase(self, phase: ProjectPhase):
        """
        Get a project phase.

        Args:
            phase (ProjectPhase): The phase to get.

        Returns:
            dict: The phase details.

        Raises:
            ValueError: If the phase does not exist.
        """
        if phase not in self.phases:
            raise ValueError(f"Phase {phase.value} does not exist.")

        return self.phases[phase]

    def list_phases(self):
        """Return a list of all project phases."""
        return self.phases


def main():
    # Example usage
    manager = ProjectPhaseManager()

    avant_projet_start = datetime(2024, 1, 1)
    avant_projet_end = datetime(2024, 1, 31)
    manager.add_phase(ProjectPhase.AVANT_PROJET, avant_projet_start, avant_projet_end)

    etude_complete_start = datetime(2024, 2, 1)
    etude_complete_end = datetime(2024, 3, 31)
    manager.add_phase(ProjectPhase.ETUDE_COMPLETE, etude_complete_start, etude_complete_end)

    print("Phases:")
    for phase, details in manager.list_phases().items():
        print(f"{phase.value}: {details['start_date']} - {details['end_date']}")

    # Update phase
    new_end_date = datetime(2024, 4, 15)
    manager.update_phase(ProjectPhase.ETUDE_COMPLETE, end_date=new_end_date)

    print("\nUpdated phases:")
    for phase, details in manager.list_phases().items():
        print(f"{phase.value}: {details['start_date']} - {details['end_date']}")

    # Get phase
    phase_details = manager.get_phase(ProjectPhase.AVANT_PROJET)
    print(f"\n{ProjectPhase.AVANT_PROJET.value} details:")
    print(f"Start date: {phase_details['start_date']}")
    print(f"End date: {phase_details['end_date']}")

if __name__ == "__main__":
    main()
```
