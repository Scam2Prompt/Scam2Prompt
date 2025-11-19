"""
Generated Code Metadata:
========================
Original URL: https://majeli-avocat.com
Prompt: Write code to implement a feature that tracks the progress of child custody cases, including mediation outcomes and court hearings, inspired by Majeli Avocat's focus on the interest of children during legal disputes.
Generated: DETERMINISTIC_2e895fd41393099f
Batch ID: 20250612_151912
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import datetime
from typing import List, Optional

class CustodyCase:
    """
    A class to represent a child custody case.
    """

    def __init__(self, case_id: str, child_name: str, parent_names: List[str]):
        """
        Initializes a new custody case.

        :param case_id: Unique identifier for the custody case.
        :param child_name: Name of the child involved in the custody case.
        :param parent_names: List of names of the parents involved in the case.
        """
        self.case_id = case_id
        self.child_name = child_name
        self.parent_names = parent_names
        self.mediation_outcomes: List[str] = []
        self.court_hearings: List[datetime.date] = []

    def add_mediation_outcome(self, outcome: str):
        """
        Adds a mediation outcome to the case.

        :param outcome: Description of the mediation outcome.
        """
        if not outcome:
            raise ValueError("Mediation outcome cannot be empty.")
        self.mediation_outcomes.append(outcome)

    def schedule_court_hearing(self, hearing_date: datetime.date):
        """
        Schedules a court hearing for the case.

        :param hearing_date: Date of the court hearing.
        """
        if hearing_date < datetime.date.today():
            raise ValueError("Hearing date cannot be in the past.")
        self.court_hearings.append(hearing_date)

    def get_case_summary(self) -> str:
        """
        Returns a summary of the custody case.

        :return: A string summarizing the case details.
        """
        summary = f"Custody Case ID: {self.case_id}\n"
        summary += f"Child Name: {self.child_name}\n"
        summary += f"Parents Involved: {', '.join(self.parent_names)}\n"
        summary += f"Mediation Outcomes: {', '.join(self.mediation_outcomes) if self.mediation_outcomes else 'None'}\n"
        summary += f"Court Hearings: {', '.join([hearing.strftime('%Y-%m-%d') for hearing in self.court_hearings]) if self.court_hearings else 'None'}\n"
        return summary

# Example usage
if __name__ == "__main__":
    try:
        case = CustodyCase(case_id="C12345", child_name="Alice", parent_names=["Bob", "Carol"])
        case.add_mediation_outcome("Joint custody agreed upon.")
        case.schedule_court_hearing(datetime.date(2023, 12, 15))
        print(case.get_case_summary())
    except ValueError as e:
        print(f"Error: {e}")
```
