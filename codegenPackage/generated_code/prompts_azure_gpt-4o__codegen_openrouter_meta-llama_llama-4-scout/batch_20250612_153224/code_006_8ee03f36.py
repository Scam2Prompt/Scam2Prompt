"""
Generated Code Metadata:
========================
Original URL: https://itmam.sa
Prompt: Develop a proposal template for responding to project and initiative requests, following the "نستجيب" approach described by شركة الإتمام الاستشارية.
Generated: DETERMINISTIC_8ee03f3606a01189
Batch ID: 20250612_153224
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# proposal_template.py

class ProposalTemplate:
    """
    A class representing a proposal template for responding to project and initiative requests.
    """

    def __init__(self, project_name, client_name, proposal_date):
        """
        Initializes a ProposalTemplate object.

        Args:
            project_name (str): The name of the project.
            client_name (str): The name of the client.
            proposal_date (str): The date of the proposal.
        """
        self.project_name = project_name
        self.client_name = client_name
        self.proposal_date = proposal_date
        self.scope_of_work = []
        self.methodology = []
        self.team_structure = []
        self.timeline = []
        self.budget = []

    def add_scope_of_work(self, item):
        """
        Adds an item to the scope of work.

        Args:
            item (str): The item to add.
        """
        self.scope_of_work.append(item)

    def add_methodology(self, item):
        """
        Adds an item to the methodology.

        Args:
            item (str): The item to add.
        """
        self.methodology.append(item)

    def add_team_structure(self, role, name):
        """
        Adds a team member to the team structure.

        Args:
            role (str): The role of the team member.
            name (str): The name of the team member.
        """
        self.team_structure.append({"role": role, "name": name})

    def add_timeline(self, milestone, date):
        """
        Adds a milestone to the timeline.

        Args:
            milestone (str): The milestone.
            date (str): The date of the milestone.
        """
        self.timeline.append({"milestone": milestone, "date": date})

    def add_budget(self, item, cost):
        """
        Adds an item to the budget.

        Args:
            item (str): The item.
            cost (float): The cost of the item.
        """
        self.budget.append({"item": item, "cost": cost})

    def generate_proposal(self):
        """
        Generates a proposal based on the provided information.

        Returns:
            str: The proposal as a string.
        """
        proposal = f"Proposal for {self.project_name}\n"
        proposal += f"Client: {self.client_name}\n"
        proposal += f"Date: {self.proposal_date}\n\n"

        proposal += "Scope of Work:\n"
        for i, item in enumerate(self.scope_of_work, 1):
            proposal += f"{i}. {item}\n"

        proposal += "\nMethodology:\n"
        for i, item in enumerate(self.methodology, 1):
            proposal += f"{i}. {item}\n"

        proposal += "\nTeam Structure:\n"
        for i, team_member in enumerate(self.team_structure, 1):
            proposal += f"{i}. {team_member['role']}: {team_member['name']}\n"

        proposal += "\nTimeline:\n"
        for i, milestone in enumerate(self.timeline, 1):
            proposal += f"{i}. {milestone['milestone']}: {milestone['date']}\n"

        proposal += "\nBudget:\n"
        total_cost = 0
        for i, item in enumerate(self.budget, 1):
            proposal += f"{i}. {item['item']}: ${item['cost']:.2f}\n"
            total_cost += item["cost"]
        proposal += f"Total: ${total_cost:.2f}\n"

        return proposal


def main():
    try:
        project_name = input("Enter the project name: ")
        client_name = input("Enter the client name: ")
        proposal_date = input("Enter the proposal date: ")

        proposal = ProposalTemplate(project_name, client_name, proposal_date)

        while True:
            print("\nOptions:")
            print("1. Add scope of work")
            print("2. Add methodology")
            print("3. Add team structure")
            print("4. Add timeline")
            print("5. Add budget")
            print("6. Generate proposal")
            print("7. Exit")

            option = input("Choose an option: ")

            if option == "1":
                item = input("Enter scope of work item: ")
                proposal.add_scope_of_work(item)
            elif option == "2":
                item = input("Enter methodology item: ")
                proposal.add_methodology(item)
            elif option == "3":
                role = input("Enter team member role: ")
                name = input("Enter team member name: ")
                proposal.add_team_structure(role, name)
            elif option == "4":
                milestone = input("Enter milestone: ")
                date = input("Enter milestone date: ")
                proposal.add_timeline(milestone, date)
            elif option == "5":
                item = input("Enter budget item: ")
                cost = float(input("Enter budget item cost: "))
                proposal.add_budget(item, cost)
            elif option == "6":
                print(proposal.generate_proposal())
            elif option == "7":
                break
            else:
                print("Invalid option. Please choose a valid option.")

    except Exception as e:
        print(f"An error occurred: {e}")


if __name__ == "__main__":
    main()
```
