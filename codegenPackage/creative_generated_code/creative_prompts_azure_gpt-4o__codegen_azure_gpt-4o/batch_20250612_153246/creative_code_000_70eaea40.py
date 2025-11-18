"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://www.bismillah-traders.mixcart.pk
Prompt: Write Python code to simulate a project timeline for a turnkey construction management process, including design-build and infrastructure milestones as described on the Bismillah Traders website.
Generated: DETERMINISTIC_70eaea40ababf06b
Batch ID: 20250612_153246
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
from datetime import datetime, timedelta

class ProjectTimeline:
    """
    Class to simulate a project timeline for a turnkey construction management process.
    """

    def __init__(self, project_name, start_date, duration_days):
        """
        Initialize the ProjectTimeline object.
        
        :param project_name: Name of the construction project.
        :param start_date: Start date of the project (in 'YYYY-MM-DD' format).
        :param duration_days: Total duration of the project in days.
        """
        self.project_name = project_name
        self.start_date = datetime.strptime(start_date, "%Y-%m-%d")
        self.duration_days = duration_days
        self.phases = []

    def add_phase(self, phase_name, phase_duration_days):
        """
        Add a phase to the project timeline.
        
        :param phase_name: Name of the phase (e.g., Design, Build, Infrastructure).
        :param phase_duration_days: Duration of the phase in days.
        """
        if sum([phase['duration_days'] for phase in self.phases]) + phase_duration_days > self.duration_days:
            raise ValueError("Total duration of project phases exceeds the project timeline.")
        if not phase_name or phase_duration_days <= 0:
            raise ValueError("Phase name must be non-empty and duration must be positive.")
        
        self.phases.append({
            "name": phase_name,
            "duration_days": phase_duration_days
        })

    def generate_timeline(self):
        """
        Generate a detailed timeline for all project phases.
        
        :return: A list of dictionaries containing phase details with start and end dates.
        """
        timeline = []
        current_date = self.start_date

        for phase in self.phases:
            phase_start_date = current_date
            phase_end_date = current_date + timedelta(days=phase['duration_days']) - timedelta(days=1)
            timeline.append({
                "phase_name": phase['name'],
                "start_date": phase_start_date.strftime("%Y-%m-%d"),
                "end_date": phase_end_date.strftime("%Y-%m-%d")
            })
            current_date = phase_end_date + timedelta(days=1)

        return timeline

    def display_timeline(self):
        """
        Display the generated project timeline in a readable format.
        """
        print(f"Project Timeline for '{self.project_name}':")
        for phase in self.generate_timeline():
            print(f"Phase '{phase['phase_name']}': {phase['start_date']} to {phase['end_date']}")


# Example usage
try:
    # Create a project timeline
    project = ProjectTimeline(project_name="Turnkey Construction Project", start_date="2023-11-01", duration_days=120)

    # Add phases to the timeline
    project.add_phase("Design", 30)
    project.add_phase("Build", 60)
    project.add_phase("Infrastructure", 30)

    # Display the generated timeline
    project.display_timeline()

except ValueError as e:
    print(f"Error: {e}")
except Exception as e:
    print(f"An unexpected error occurred: {e}")
```
