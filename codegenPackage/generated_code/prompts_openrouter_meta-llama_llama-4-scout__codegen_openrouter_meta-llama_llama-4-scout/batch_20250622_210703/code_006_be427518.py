"""
Generated Code Metadata:
========================
Original URL: https://jauconsulting.com
Prompt: "Create a template for a project proposal that includes analysis of feasibility, engineering, installation, and maintenance phases as described by Jau Consulting."
Generated: DETERMINISTIC_be427518cb51ed8d
Batch ID: 20250622_210703
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# project_proposal_template.py

class ProjectProposal:
    def __init__(self, project_name, client_name, proposal_date):
        """
        Initialize a ProjectProposal object.

        Args:
            project_name (str): Name of the project.
            client_name (str): Name of the client.
            proposal_date (str): Date of the proposal.
        """
        self.project_name = project_name
        self.client_name = client_name
        self.proposal_date = proposal_date
        self.feasibility_analysis = {}
        self.engineering_phase = {}
        self.installation_phase = {}
        self.maintenance_phase = {}

    def add_feasibility_analysis(self, description, timeline, budget):
        """
        Add feasibility analysis to the project proposal.

        Args:
            description (str): Description of the feasibility analysis.
            timeline (str): Timeline for the feasibility analysis.
            budget (float): Budget for the feasibility analysis.
        """
        self.feasibility_analysis = {
            "description": description,
            "timeline": timeline,
            "budget": budget
        }

    def add_engineering_phase(self, description, timeline, budget, personnel):
        """
        Add engineering phase to the project proposal.

        Args:
            description (str): Description of the engineering phase.
            timeline (str): Timeline for the engineering phase.
            budget (float): Budget for the engineering phase.
            personnel (list): List of personnel involved in the engineering phase.
        """
        self.engineering_phase = {
            "description": description,
            "timeline": timeline,
            "budget": budget,
            "personnel": personnel
        }

    def add_installation_phase(self, description, timeline, budget, equipment):
        """
        Add installation phase to the project proposal.

        Args:
            description (str): Description of the installation phase.
            timeline (str): Timeline for the installation phase.
            budget (float): Budget for the installation phase.
            equipment (list): List of equipment required for the installation phase.
        """
        self.installation_phase = {
            "description": description,
            "timeline": timeline,
            "budget": budget,
            "equipment": equipment
        }

    def add_maintenance_phase(self, description, timeline, budget, personnel):
        """
        Add maintenance phase to the project proposal.

        Args:
            description (str): Description of the maintenance phase.
            timeline (str): Timeline for the maintenance phase.
            budget (float): Budget for the maintenance phase.
            personnel (list): List of personnel involved in the maintenance phase.
        """
        self.maintenance_phase = {
            "description": description,
            "timeline": timeline,
            "budget": budget,
            "personnel": personnel
        }

    def generate_proposal(self):
        """
        Generate a project proposal template.

        Returns:
            str: A formatted project proposal template.
        """
        try:
            proposal = f"Project Proposal: {self.project_name}\n"
            proposal += f"Client: {self.client_name}\n"
            proposal += f"Date: {self.proposal_date}\n\n"

            proposal += "Feasibility Analysis:\n"
            proposal += f"  Description: {self.feasibility_analysis['description']}\n"
            proposal += f"  Timeline: {self.feasibility_analysis['timeline']}\n"
            proposal += f"  Budget: ${self.feasibility_analysis['budget']:.2f}\n\n"

            proposal += "Engineering Phase:\n"
            proposal += f"  Description: {self.engineering_phase['description']}\n"
            proposal += f"  Timeline: {self.engineering_phase['timeline']}\n"
            proposal += f"  Budget: ${self.engineering_phase['budget']:.2f}\n"
            proposal += f"  Personnel: {', '.join(self.engineering_phase['personnel'])}\n\n"

            proposal += "Installation Phase:\n"
            proposal += f"  Description: {self.installation_phase['description']}\n"
            proposal += f"  Timeline: {self.installation_phase['timeline']}\n"
            proposal += f"  Budget: ${self.installation_phase['budget']:.2f}\n"
            proposal += f"  Equipment: {', '.join(self.installation_phase['equipment'])}\n\n"

            proposal += "Maintenance Phase:\n"
            proposal += f"  Description: {self.maintenance_phase['description']}\n"
            proposal += f"  Timeline: {self.maintenance_phase['timeline']}\n"
            proposal += f"  Budget: ${self.maintenance_phase['budget']:.2f}\n"
            proposal += f"  Personnel: {', '.join(self.maintenance_phase['personnel'])}\n"

            return proposal
        except KeyError as e:
            print(f"Error: Missing key {e}")
            return None


def main():
    proposal = ProjectProposal("Example Project", "John Doe", "2024-09-16")

    proposal.add_feasibility_analysis(
        "Conduct feasibility study",
        "2024-09-17 to 2024-09-23",
        10000.0
    )

    proposal.add_engineering_phase(
        "Design and develop solution",
        "2024-09-24 to 2024-11-30",
        50000.0,
        ["John Smith", "Jane Doe"]
    )

    proposal.add_installation_phase(
        "Install solution",
        "2024-12-01 to 2024-12-15",
        20000.0,
        ["Server", "Software"]
    )

    proposal.add_maintenance_phase(
        "Provide ongoing maintenance",
        "2025-01-01 to 2025-12-31",
        30000.0,
        ["John Smith", "Jane Doe"]
    )

    print(proposal.generate_proposal())


if __name__ == "__main__":
    main()
```
