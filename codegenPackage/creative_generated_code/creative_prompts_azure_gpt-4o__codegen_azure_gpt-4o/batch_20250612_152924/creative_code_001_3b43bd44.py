"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://espinelycia.com
Prompt: Generate a script to simulate the construction process of sanitary networks, ensuring adherence to budget and timelines, as highlighted by Espinel y Cia's services.
Generated: DETERMINISTIC_3b43bd4454aae71f
Batch ID: 20250612_152924
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import datetime
import random

class ConstructionProject:
    """
    Class to simulate the construction process of sanitary networks.
    """
    def __init__(self, name, budget, timeline_days):
        """
        Initialize the construction project with a name, budget, and timeline.

        :param name: Name of the project
        :param budget: Total budget allocated for the project
        :param timeline_days: Number of days allocated for completion
        """
        self.name = name
        self.budget = budget
        self.timeline_days = timeline_days
        self.start_date = datetime.date.today()
        self.end_date = self.start_date + datetime.timedelta(days=timeline_days)
        self.expenses = 0
        self.progress = 0  # Progress in percentage
        self.status = "Not Started"

    def update_expenses(self, amount):
        """
        Update the expenses for the project.

        :param amount: Amount to add to expenses
        :raises ValueError: If expenses exceed the budget
        """
        if self.expenses + amount > self.budget:
            raise ValueError("Expenses exceed budget!")
        self.expenses += amount

    def update_progress(self, percentage):
        """
        Update the progress of the project.

        :param percentage: Percentage to add to current progress
        :raises ValueError: If progress exceeds 100%
        """
        if self.progress + percentage > 100:
            raise ValueError("Progress cannot exceed 100%!")
        self.progress += percentage
        if self.progress == 100:
            self.status = "Completed"

    def simulate_day(self):
        """
        Simulate a day of work on the project.
        Randomly increases expenses and progress to mimic real-world conditions.
        """
        if self.status == "Completed":
            return f"Project '{self.name}' is already completed."

        daily_expense = random.randint(100, 1000)  # Simulate daily expense
        daily_progress = random.uniform(1, 5)  # Simulate daily progress in percentage

        try:
            self.update_expenses(daily_expense)
        except ValueError as e:
            return f"Budget exceeded: {e}"

        try:
            self.update_progress(daily_progress)
        except ValueError as e:
            return f"Progress error: {e}"

        if datetime.date.today() >= self.end_date and self.progress < 100:
            self.status = "Overdue"

        return f"Day {datetime.date.today()}: Expenses updated, progress at {self.progress:.2f}%."

    def summary(self):
        """
        Provide a summary of the project's current state.

        :return: Dictionary summarizing the project details
        """
        return {
            "Project Name": self.name,
            "Budget": self.budget,
            "Expenses": self.expenses,
            "Timeline": f"{self.start_date} to {self.end_date}",
            "Progress": f"{self.progress:.2f}%",
            "Status": self.status
        }


# Main function to simulate the construction process
def main():
    # Initialize a sample project
    project = ConstructionProject(name="Sanitary Network Project", budget=50000, timeline_days=30)
    
    print(f"Starting project: {project.name}")
    print(f"Timeline: {project.start_date} to {project.end_date}")
    print(f"Budget: ${project.budget}")

    # Simulate construction over the timeline
    for day in range(project.timeline_days):
        result = project.simulate_day()
        print(result)
        if project.status == "Completed":
            break

    # Display final project summary
    print("\nFinal Project Summary:")
    for key, value in project.summary().items():
        print(f"{key}: {value}")


if __name__ == "__main__":
    main()
```
