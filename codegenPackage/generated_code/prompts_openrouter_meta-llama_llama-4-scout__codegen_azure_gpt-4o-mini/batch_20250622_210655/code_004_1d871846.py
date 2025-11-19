"""
Generated Code Metadata:
========================
Original URL: https://vivekenterprises.co.in
Prompt: "Create a proposal for a turnkey interior contracting project, including a detailed scope of work, timeline, and budget, using the company's experience and services as a reference."
Generated: DETERMINISTIC_1d871846050656ab
Batch ID: 20250622_210655
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import json
from datetime import datetime, timedelta

class TurnkeyInteriorContractingProposal:
    def __init__(self, company_name, client_name, project_location):
        """
        Initializes the proposal with company and client details.

        :param company_name: Name of the contracting company
        :param client_name: Name of the client
        :param project_location: Location of the project
        """
        self.company_name = company_name
        self.client_name = client_name
        self.project_location = project_location
        self.scope_of_work = []
        self.timeline = {}
        self.budget = 0.0

    def add_scope_of_work(self, task):
        """
        Adds a task to the scope of work.

        :param task: Description of the task to be performed
        """
        self.scope_of_work.append(task)

    def set_timeline(self, start_date, duration_days):
        """
        Sets the project timeline based on start date and duration.

        :param start_date: Start date of the project in 'YYYY-MM-DD' format
        :param duration_days: Duration of the project in days
        """
        try:
            start_date = datetime.strptime(start_date, '%Y-%m-%d')
            end_date = start_date + timedelta(days=duration_days)
            self.timeline = {
                'start_date': start_date.strftime('%Y-%m-%d'),
                'end_date': end_date.strftime('%Y-%m-%d'),
                'duration_days': duration_days
            }
        except ValueError as e:
            print(f"Error in setting timeline: {e}")

    def set_budget(self, budget):
        """
        Sets the project budget.

        :param budget: Total budget for the project
        """
        if budget < 0:
            raise ValueError("Budget cannot be negative.")
        self.budget = budget

    def generate_proposal(self):
        """
        Generates the complete proposal as a dictionary.

        :return: A dictionary containing the proposal details
        """
        proposal = {
            'company_name': self.company_name,
            'client_name': self.client_name,
            'project_location': self.project_location,
            'scope_of_work': self.scope_of_work,
            'timeline': self.timeline,
            'budget': self.budget
        }
        return proposal

    def save_proposal(self, filename):
        """
        Saves the proposal to a JSON file.

        :param filename: Name of the file to save the proposal
        """
        try:
            with open(filename, 'w') as file:
                json.dump(self.generate_proposal(), file, indent=4)
            print(f"Proposal saved successfully to {filename}")
        except IOError as e:
            print(f"Error saving proposal: {e}")

# Example usage
if __name__ == "__main__":
    proposal = TurnkeyInteriorContractingProposal("ABC Interiors", "John Doe", "123 Main St, Anytown")
    proposal.add_scope_of_work("Demolition of existing structures")
    proposal.add_scope_of_work("Installation of new drywall")
    proposal.add_scope_of_work("Painting and finishing")
    proposal.set_timeline("2023-11-01", 30)
    proposal.set_budget(50000.00)

    # Save the proposal to a file
    proposal.save_proposal("interior_contracting_proposal.json")
```
