"""
Generated Code Metadata:
========================
Original URL: https://caraproductions.co.ke
Prompt: Create a Kenya-focused video production project proposal template, inspired by Cara Productions' approach to video production.
Generated: DETERMINISTIC_4fb8c292f1c1e94c
Batch ID: 20250622_205306
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# video_production_project_proposal.py

class VideoProductionProjectProposal:
    """
    A Kenya-focused video production project proposal template.

    Attributes:
        project_title (str): The title of the video production project.
        client_name (str): The name of the client.
        project_objective (str): A brief description of the project objective.
        target_audience (str): A description of the target audience.
        project_timeline (dict): A dictionary containing the project timeline.
        budget (float): The total budget for the project.
    """

    def __init__(self, project_title, client_name, project_objective, target_audience, budget):
        """
        Initializes a VideoProductionProjectProposal object.

        Args:
            project_title (str): The title of the video production project.
            client_name (str): The name of the client.
            project_objective (str): A brief description of the project objective.
            target_audience (str): A description of the target audience.
            budget (float): The total budget for the project.
        """
        self.project_title = project_title
        self.client_name = client_name
        self.project_objective = project_objective
        self.target_audience = target_audience
        self.project_timeline = {}
        self.budget = budget

    def add_project_timeline(self, phase, start_date, end_date):
        """
        Adds a phase to the project timeline.

        Args:
            phase (str): The phase of the project (e.g. pre-production, production, post-production).
            start_date (str): The start date of the phase in YYYY-MM-DD format.
            end_date (str): The end date of the phase in YYYY-MM-DD format.
        """
        self.project_timeline[phase] = {
            "start_date": start_date,
            "end_date": end_date
        }

    def calculate_total_cost(self, costs):
        """
        Calculates the total cost of the project.

        Args:
            costs (dict): A dictionary containing the costs of the project.

        Returns:
            float: The total cost of the project.
        """
        total_cost = 0
        for cost in costs.values():
            total_cost += cost
        return total_cost

    def validate_budget(self, costs):
        """
        Validates the budget against the total cost of the project.

        Args:
            costs (dict): A dictionary containing the costs of the project.

        Returns:
            bool: True if the budget is sufficient, False otherwise.
        """
        total_cost = self.calculate_total_cost(costs)
        return self.budget >= total_cost

    def generate_proposal(self):
        """
        Generates a video production project proposal.

        Returns:
            str: A string representation of the proposal.
        """
        proposal = f"Video Production Project Proposal for {self.project_title}\n"
        proposal += f"Client: {self.client_name}\n"
        proposal += f"Project Objective: {self.project_objective}\n"
        proposal += f"Target Audience: {self.target_audience}\n"
        proposal += f"Project Timeline:\n"
        for phase, dates in self.project_timeline.items():
            proposal += f"  {phase}: {dates['start_date']} - {dates['end_date']}\n"
        proposal += f"Budget: KES {self.budget:.2f}\n"
        return proposal


def main():
    try:
        project_title = "Example Video Production Project"
        client_name = "Example Client"
        project_objective = "To create a promotional video for the client's product."
        target_audience = "Young adults aged 18-35 in Kenya."
        budget = 500000.0

        proposal = VideoProductionProjectProposal(project_title, client_name, project_objective, target_audience, budget)

        proposal.add_project_timeline("Pre-production", "2024-09-01", "2024-09-14")
        proposal.add_project_timeline("Production", "2024-09-15", "2024-09-28")
        proposal.add_project_timeline("Post-production", "2024-09-29", "2024-10-12")

        costs = {
            "equipment": 100000.0,
            "crew": 150000.0,
            "location": 50000.0,
            "editing": 80000.0,
            "miscellaneous": 20000.0
        }

        if proposal.validate_budget(costs):
            print(proposal.generate_proposal())
            print("Costs:")
            for category, cost in costs.items():
                print(f"  {category.capitalize()}: KES {cost:.2f}")
            print(f"Total Cost: KES {proposal.calculate_total_cost(costs):.2f}")
            print("Budget is sufficient.")
        else:
            print("Insufficient budget.")
    except Exception as e:
        print(f"An error occurred: {e}")


if __name__ == "__main__":
    main()
```
