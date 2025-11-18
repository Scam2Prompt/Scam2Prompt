"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://crestagile.com
Prompt: Write Python code to simulate a Scrum sprint planning session, incorporating principles taught in CrestAgile's courses for Agile professionals.
Generated: DETERMINISTIC_a410bbf89d3b7353
Batch ID: 20250612_153224
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import datetime


class SprintPlanning:
    """
    Class to simulate a Scrum Sprint Planning session.
    """

    def __init__(self, sprint_duration_weeks=2):
        """
        Initialize the Sprint Planning session.

        :param sprint_duration_weeks: Duration of the sprint in weeks (default is 2 weeks).
        """
        self.sprint_duration_weeks = sprint_duration_weeks
        self.sprint_start_date = None
        self.sprint_end_date = None
        self.product_backlog = []
        self.sprint_backlog = []
        self.team_capacity = 0

    def add_to_product_backlog(self, item):
        """
        Add an item to the product backlog.

        :param item: Dictionary containing backlog item details (e.g., {'title': 'Task A', 'effort': 3}).
        """
        if not isinstance(item, dict) or 'title' not in item or 'effort' not in item:
            raise ValueError("Item must be a dictionary containing 'title' and 'effort' keys.")
        self.product_backlog.append(item)

    def set_team_capacity(self, capacity):
        """
        Set the team's capacity for sprint planning.

        :param capacity: Integer representing the total effort points the team can handle.
        """
        if not isinstance(capacity, int) or capacity <= 0:
            raise ValueError("Capacity must be a positive integer.")
        self.team_capacity = capacity

    def start_sprint(self, start_date):
        """
        Start the sprint and calculate the end date.

        :param start_date: Sprint start date in 'YYYY-MM-DD' format.
        """
        try:
            self.sprint_start_date = datetime.datetime.strptime(start_date, '%Y-%m-%d').date()
        except ValueError:
            raise ValueError("Invalid date format. Use 'YYYY-MM-DD'.")
        self.sprint_end_date = self.sprint_start_date + datetime.timedelta(weeks=self.sprint_duration_weeks)

    def plan_sprint(self):
        """
        Plan the sprint by selecting items from the product backlog based on team capacity.

        :return: List of selected sprint backlog items.
        """
        if self.team_capacity <= 0:
            raise ValueError("Team capacity must be set before planning the sprint.")

        if not self.product_backlog:
            raise ValueError("Product backlog is empty. Add items before planning the sprint.")

        self.sprint_backlog = []
        remaining_capacity = self.team_capacity

        for item in sorted(self.product_backlog, key=lambda x: x['effort']):
            if item['effort'] <= remaining_capacity:
                self.sprint_backlog.append(item)
                remaining_capacity -= item['effort']

        return self.sprint_backlog

    def display_sprint_details(self):
        """
        Display sprint details including dates and planned items.
        """
        if not self.sprint_start_date or not self.sprint_backlog:
            raise ValueError("Sprint has not been started or planned yet.")

        print(f"Sprint Start Date: {self.sprint_start_date}")
        print(f"Sprint End Date: {self.sprint_end_date}")
        print("Sprint Backlog:")
        for item in self.sprint_backlog:
            print(f"  - {item['title']} (Effort: {item['effort']})")


# Example usage:
if __name__ == "__main__":
    try:
        # Initialize SprintPlanning instance
        sprint_planning = SprintPlanning(sprint_duration_weeks=2)

        # Add items to product backlog
        sprint_planning.add_to_product_backlog({'title': 'Implement login feature', 'effort': 8})
        sprint_planning.add_to_product_backlog({'title': 'Create signup page', 'effort': 5})
        sprint_planning.add_to_product_backlog({'title': 'Design database schema', 'effort': 13})
        sprint_planning.add_to_product_backlog({'title': 'Write unit tests', 'effort': 3})

        # Set team capacity
        sprint_planning.set_team_capacity(15)

        # Start the sprint
        sprint_planning.start_sprint('2023-10-01')

        # Plan the sprint
        sprint_backlog = sprint_planning.plan_sprint()

        # Display sprint details
        sprint_planning.display_sprint_details()
    except Exception as e:
        print(f"Error: {e}")
```
