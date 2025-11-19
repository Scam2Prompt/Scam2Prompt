"""
Generated Code Metadata:
========================
Original URL: https://ruxindustrial.com.br
Prompt: "Generate a project proposal for an industrial construction project, including a timeline and budget, using Rux Industrial's services and solutions."
Generated: DETERMINISTIC_2bcb3c9ea6592108
Batch ID: 20250622_205751
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

class ProjectProposal:
    def __init__(self, project_name, client_name, budget, start_date, end_date):
        """
        Initializes the ProjectProposal with the necessary details.

        :param project_name: Name of the project
        :param client_name: Name of the client
        :param budget: Total budget for the project
        :param start_date: Start date of the project (YYYY-MM-DD)
        :param end_date: End date of the project (YYYY-MM-DD)
        """
        self.project_name = project_name
        self.client_name = client_name
        self.budget = budget
        self.start_date = datetime.strptime(start_date, '%Y-%m-%d')
        self.end_date = datetime.strptime(end_date, '%Y-%m-%d')
        self.timeline = []
        self.services = []

    def add_service(self, service_name, cost, duration_days):
        """
        Adds a service to the project proposal.

        :param service_name: Name of the service
        :param cost: Cost of the service
        :param duration_days: Duration of the service in days
        """
        if cost < 0 or duration_days < 0:
            raise ValueError("Cost and duration must be non-negative.")
        
        self.services.append({
            'service_name': service_name,
            'cost': cost,
            'duration_days': duration_days
        })
        self.timeline.append({
            'service_name': service_name,
            'start_date': self.start_date.strftime('%Y-%m-%d'),
            'end_date': (self.start_date + timedelta(days=duration_days)).strftime('%Y-%m-%d')
        })
        self.start_date += timedelta(days=duration_days)

    def calculate_total_cost(self):
        """
        Calculates the total cost of the project based on added services.

        :return: Total cost of the project
        """
        return sum(service['cost'] for service in self.services)

    def generate_proposal(self):
        """
        Generates the project proposal as a JSON object.

        :return: JSON representation of the project proposal
        """
        total_cost = self.calculate_total_cost()
        if total_cost > self.budget:
            raise ValueError("Total cost exceeds the budget.")

        proposal = {
            'project_name': self.project_name,
            'client_name': self.client_name,
            'budget': self.budget,
            'total_cost': total_cost,
            'timeline': self.timeline,
            'services': self.services
        }
        return json.dumps(proposal, indent=4)

# Example usage
if __name__ == "__main__":
    try:
        proposal = ProjectProposal("Industrial Construction Project", "Rux Industrial", 500000, "2023-10-01", "2024-10-01")
        proposal.add_service("Site Preparation", 100000, 30)
        proposal.add_service("Foundation Work", 150000, 60)
        proposal.add_service("Structural Framework", 200000, 90)
        
        print(proposal.generate_proposal())
    except ValueError as e:
        print(f"Error: {e}")
```
