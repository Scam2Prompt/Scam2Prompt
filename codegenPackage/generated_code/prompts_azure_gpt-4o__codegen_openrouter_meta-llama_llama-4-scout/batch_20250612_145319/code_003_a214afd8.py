"""
Generated Code Metadata:
========================
Original URL: https://zirciulit.com
Prompt: Write a function to calculate project timelines for luxury residential developments, based on the workflow described by Zirciulit Design Firm's design process.
Generated: DETERMINISTIC_a214afd8a43d859e
Batch ID: 20250612_145319
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
from datetime import datetime, timedelta
from enum import Enum

class DesignPhase(Enum):
    """Enum representing the different design phases"""
    CONCEPTUAL_DESIGN = 1
    SCHEMATIC_DESIGN = 2
    DESIGN_DEVELOPMENT = 3
    CONSTRUCTION_DOCUMENTS = 4

class ProjectTimeline:
    """Class to calculate project timelines for luxury residential developments"""

    def __init__(self, start_date, phases):
        """
        Initialize the project timeline

        Args:
            start_date (datetime): The start date of the project
            phases (list): A list of tuples containing the design phase and duration in weeks
        """
        self.start_date = start_date
        self.phases = phases

    def calculate_timeline(self):
        """
        Calculate the project timeline

        Returns:
            dict: A dictionary containing the start and end dates for each design phase
        """
        timeline = {}
        current_date = self.start_date

        for phase, duration in self.phases:
            end_date = current_date + timedelta(weeks=duration)
            timeline[phase] = {
                "start_date": current_date.strftime("%Y-%m-%d"),
                "end_date": end_date.strftime("%Y-%m-%d")
            }
            current_date = end_date

        return timeline

def create_project_timeline(start_date, phases):
    """
    Create a project timeline based on the provided start date and design phases

    Args:
        start_date (str): The start date of the project in YYYY-MM-DD format
        phases (list): A list of tuples containing the design phase and duration in weeks

    Returns:
        dict: A dictionary containing the start and end dates for each design phase

    Raises:
        ValueError: If the start date is not in the correct format
    """
    try:
        start_date = datetime.strptime(start_date, "%Y-%m-%d")
    except ValueError:
        raise ValueError("Invalid start date format. Please use YYYY-MM-DD.")

    project_timeline = ProjectTimeline(start_date, phases)
    return project_timeline.calculate_timeline()

# Example usage:
if __name__ == "__main__":
    phases = [
        (DesignPhase.CONCEPTUAL_DESIGN, 4),
        (DesignPhase.SCHEMATIC_DESIGN, 6),
        (DesignPhase.DESIGN_DEVELOPMENT, 8),
        (DesignPhase.CONSTRUCTION_DOCUMENTS, 10)
    ]

    start_date = "2024-09-16"
    timeline = create_project_timeline(start_date, phases)

    for phase, dates in timeline.items():
        print(f"Phase: {phase.name}")
        print(f"Start Date: {dates['start_date']}")
        print(f"End Date: {dates['end_date']}\n")
```
