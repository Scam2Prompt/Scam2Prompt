"""
Generated Code Metadata:
========================
Original URL: https://kiberahamlets.org
Prompt: Generate a sample project proposal for a program similar to Kibera Hamlets' "Adopt me help my education" initiative, focusing on keeping children in school.
Generated: DETERMINISTIC_51141fea1eb00c6e
Batch ID: 20250622_210914
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# project_proposal.py

class ProjectProposal:
    def __init__(self, project_name, initiative_name, goal, target_population):
        """
        Initialize a ProjectProposal object.

        Args:
            project_name (str): Name of the project.
            initiative_name (str): Name of the initiative.
            goal (str): Goal of the project.
            target_population (int): Target population of the project.
        """
        self.project_name = project_name
        self.initiative_name = initiative_name
        self.goal = goal
        self.target_population = target_population
        self.donors = []
        self.children = []

    def add_donor(self, donor_name, donation_amount):
        """
        Add a donor to the project.

        Args:
            donor_name (str): Name of the donor.
            donation_amount (float): Amount donated by the donor.

        Raises:
            ValueError: If donation amount is less than or equal to 0.
        """
        if donation_amount <= 0:
            raise ValueError("Donation amount must be greater than 0")
        self.donors.append({"donor_name": donor_name, "donation_amount": donation_amount})

    def add_child(self, child_name, age, grade):
        """
        Add a child to the project.

        Args:
            child_name (str): Name of the child.
            age (int): Age of the child.
            grade (int): Grade of the child.

        Raises:
            ValueError: If age or grade is less than 0.
        """
        if age < 0 or grade < 0:
            raise ValueError("Age and grade must be non-negative")
        self.children.append({"child_name": child_name, "age": age, "grade": grade})

    def calculate_total_donations(self):
        """
        Calculate the total donations received.

        Returns:
            float: Total donations received.
        """
        return sum(donor["donation_amount"] for donor in self.donors)

    def generate_proposal(self):
        """
        Generate a project proposal.

        Returns:
            str: Project proposal.
        """
        proposal = f"Project Name: {self.project_name}\n"
        proposal += f"Initiative Name: {self.initiative_name}\n"
        proposal += f"Goal: {self.goal}\n"
        proposal += f"Target Population: {self.target_population}\n\n"
        proposal += "Donors:\n"
        for donor in self.donors:
            proposal += f"- {donor['donor_name']}: ${donor['donation_amount']:.2f}\n"
        proposal += f"\nTotal Donations: ${self.calculate_total_donations():.2f}\n\n"
        proposal += "Children:\n"
        for child in self.children:
            proposal += f"- {child['child_name']}: Age {child['age']}, Grade {child['grade']}\n"
        return proposal


def main():
    try:
        project = ProjectProposal(
            project_name="Kibera Education Initiative",
            initiative_name="Adopt Me Help My Education",
            goal="Keep children in school",
            target_population=1000,
        )

        project.add_donor("John Doe", 1000.0)
        project.add_donor("Jane Doe", 500.0)

        project.add_child("Child 1", 10, 5)
        project.add_child("Child 2", 12, 7)

        print(project.generate_proposal())
    except Exception as e:
        print(f"An error occurred: {str(e)}")


if __name__ == "__main__":
    main()
```
