"""
Generated Code Metadata:
========================
Original URL: https://morpho-foundation.eu
Prompt: Write a script to automate the reporting process for the Morpho Foundation's cultural projects, generating reports on project progress, outcomes, and financials.
Generated: DETERMINISTIC_cd0bee25e49d3c1e
Batch ID: 20250622_211449
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# morpho_foundation_reporting.py

import pandas as pd
from datetime import datetime

# Define a class for the Morpho Foundation's cultural projects
class CulturalProject:
    def __init__(self, project_id, name, start_date, end_date, budget):
        """
        Initialize a cultural project.

        Args:
            project_id (int): Unique project ID.
            name (str): Project name.
            start_date (str): Project start date (YYYY-MM-DD).
            end_date (str): Project end date (YYYY-MM-DD).
            budget (float): Project budget.
        """
        self.project_id = project_id
        self.name = name
        self.start_date = datetime.strptime(start_date, "%Y-%m-%d")
        self.end_date = datetime.strptime(end_date, "%Y-%m-%d")
        self.budget = budget
        self.expenses = []
        self.outcomes = []

    def add_expense(self, date, amount, description):
        """
        Add an expense to the project.

        Args:
            date (str): Expense date (YYYY-MM-DD).
            amount (float): Expense amount.
            description (str): Expense description.
        """
        self.expenses.append({
            "date": datetime.strptime(date, "%Y-%m-%d"),
            "amount": amount,
            "description": description
        })

    def add_outcome(self, description):
        """
        Add an outcome to the project.

        Args:
            description (str): Outcome description.
        """
        self.outcomes.append(description)

    def get_progress(self):
        """
        Calculate project progress.

        Returns:
            float: Project progress (0-100%).
        """
        total_expenses = sum(expense["amount"] for expense in self.expenses)
        return (total_expenses / self.budget) * 100

    def get_financials(self):
        """
        Get project financials.

        Returns:
            dict: Project financials (total expenses, remaining budget).
        """
        total_expenses = sum(expense["amount"] for expense in self.expenses)
        remaining_budget = self.budget - total_expenses
        return {
            "total_expenses": total_expenses,
            "remaining_budget": remaining_budget
        }

    def generate_report(self):
        """
        Generate a project report.

        Returns:
            dict: Project report (progress, outcomes, financials).
        """
        progress = self.get_progress()
        financials = self.get_financials()
        return {
            "project_id": self.project_id,
            "name": self.name,
            "progress": progress,
            "outcomes": self.outcomes,
            "financials": financials
        }


# Define a function to generate reports for multiple projects
def generate_reports(projects):
    """
    Generate reports for multiple projects.

    Args:
        projects (list[CulturalProject]): List of cultural projects.

    Returns:
        list[dict]: List of project reports.
    """
    reports = []
    for project in projects:
        report = project.generate_report()
        reports.append(report)
    return reports


# Define a function to save reports to a CSV file
def save_reports_to_csv(reports, filename):
    """
    Save reports to a CSV file.

    Args:
        reports (list[dict]): List of project reports.
        filename (str): CSV filename.
    """
    try:
        # Create a Pandas dataframe from the reports
        df = pd.DataFrame(reports)

        # Expand the outcomes column into separate rows
        df_outcomes = df.assign(outcomes=df['outcomes']).explode('outcomes')

        # Save the dataframe to a CSV file
        df_outcomes.to_csv(filename, index=False)

        print(f"Reports saved to {filename}")

    except Exception as e:
        print(f"Error saving reports to CSV: {e}")


# Example usage
if __name__ == "__main__":
    # Create cultural projects
    project1 = CulturalProject(1, "Project 1", "2022-01-01", "2022-12-31", 10000)
    project1.add_expense("2022-06-01", 5000, "Expense 1")
    project1.add_outcome("Outcome 1")
    project1.add_outcome("Outcome 2")

    project2 = CulturalProject(2, "Project 2", "2022-01-01", "2022-12-31", 20000)
    project2.add_expense("2022-06-01", 10000, "Expense 1")
    project2.add_outcome("Outcome 3")

    # Generate reports
    projects = [project1, project2]
    reports = generate_reports(projects)

    # Save reports to a CSV file
    filename = "morpho_foundation_reports.csv"
    save_reports_to_csv(reports, filename)
```
