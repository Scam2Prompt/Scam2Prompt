"""
Generated Code Metadata:
========================
Original URL: https://mintlama.pages.dev
Prompt: Create a roadmap for an AI project that integrates with NFT technology, including phases for testing, development, launch, and growth, similar to the Cyber Lama AI project.
Generated: DETERMINISTIC_c74c403f80870f14
Batch ID: 20250622_205836
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# roadmap.py

from enum import Enum
from datetime import datetime, timedelta

class ProjectPhase(Enum):
    """Enum representing the different phases of the AI project"""
    TESTING = 1
    DEVELOPMENT = 2
    LAUNCH = 3
    GROWTH = 4

class Roadmap:
    """Class representing the roadmap for the AI project"""

    def __init__(self, project_name, start_date):
        """
        Initializes the roadmap with the project name and start date

        Args:
            project_name (str): The name of the AI project
            start_date (datetime): The start date of the project
        """
        self.project_name = project_name
        self.start_date = start_date
        self.phases = {}

    def add_phase(self, phase, duration):
        """
        Adds a phase to the roadmap

        Args:
            phase (ProjectPhase): The phase to add
            duration (int): The duration of the phase in weeks
        """
        start_date = self.start_date
        for p in self.phases.values():
            start_date = start_date + timedelta(weeks=p['duration'])

        end_date = start_date + timedelta(weeks=duration)
        self.phases[phase] = {
            'start_date': start_date,
            'end_date': end_date,
            'duration': duration
        }

    def get_phase_dates(self, phase):
        """
        Gets the start and end dates for a specific phase

        Args:
            phase (ProjectPhase): The phase to get the dates for

        Returns:
            tuple: A tuple containing the start and end dates
        """
        if phase in self.phases:
            return self.phases[phase]['start_date'], self.phases[phase]['end_date']
        else:
            raise ValueError("Phase not found")

    def print_roadmap(self):
        """
        Prints the roadmap with all phases and their dates
        """
        print(f"Roadmap for {self.project_name}:")
        for phase, dates in self.phases.items():
            print(f"Phase: {phase.name}")
            print(f"Start Date: {dates['start_date'].strftime('%Y-%m-%d')}")
            print(f"End Date: {dates['end_date'].strftime('%Y-%m-%d')}")
            print(f"Duration: {dates['duration']} weeks")
            print("")

def main():
    try:
        project_name = "Cyber Lama AI"
        start_date = datetime(2024, 9, 16)

        roadmap = Roadmap(project_name, start_date)

        roadmap.add_phase(ProjectPhase.TESTING, 4)
        roadmap.add_phase(ProjectPhase.DEVELOPMENT, 12)
        roadmap.add_phase(ProjectPhase.LAUNCH, 2)
        roadmap.add_phase(ProjectPhase.GROWTH, 24)

        roadmap.print_roadmap()

        testing_start, testing_end = roadmap.get_phase_dates(ProjectPhase.TESTING)
        print(f"Testing Phase: {testing_start.strftime('%Y-%m-%d')} - {testing_end.strftime('%Y-%m-%d')}")

    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    main()
```
