"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://azt3c-st.webflow.io
Prompt: Provide an example of a grant proposal for contributing to Noir libraries and tooling, based on Aztec's Grants Program guidelines.
Generated: DETERMINISTIC_19977ac3d319e171
Batch ID: 20250612_154842
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
class GrantProposal:
    """
    A class to represent a grant proposal for contributing to Noir libraries and tooling.
    """

    def __init__(self, applicant_name, project_title, project_description, budget, timeline):
        """
        Initializes the GrantProposal instance.

        :param applicant_name: Name of the applicant
        :param project_title: Title of the proposed project
        :param project_description: Description of the project objectives and outcomes
        :param budget: Proposed budget for the project
        :param timeline: Timeline for project completion
        """
        self.applicant_name = applicant_name
        self.project_title = project_title
        self.project_description = project_description
        self.budget = budget
        self.timeline = timeline

    def validate(self):
        """
        Validates the grant proposal data.

        :raises ValueError: If any of the required fields are empty or if the budget is negative
        """
        if not self.applicant_name or not self.project_title or not self.project_description:
            raise ValueError("Applicant name, project title, and project description cannot be empty.")
        if self.budget < 0:
            raise ValueError("Budget cannot be negative.")

    def generate_proposal(self):
        """
        Generates a formatted string of the grant proposal.

        :return: A string representation of the grant proposal
        """
        return (f"Grant Proposal:\n"
                f"Applicant Name: {self.applicant_name}\n"
                f"Project Title: {self.project_title}\n"
                f"Project Description: {self.project_description}\n"
                f"Budget: ${self.budget:.2f}\n"
                f"Timeline: {self.timeline}")

def main():
    """
    Main function to create a grant proposal and display it.
    """
    try:
        # Example data for the grant proposal
        applicant_name = "John Doe"
        project_title = "Enhancing Noir Libraries"
        project_description = ("This project aims to enhance existing Noir libraries by adding new features "
                               "and improving documentation for better usability.")
        budget = 15000.00  # Example budget
        timeline = "6 months"

        # Create an instance of GrantProposal
        proposal = GrantProposal(applicant_name, project_title, project_description, budget, timeline)

        # Validate the proposal
        proposal.validate()

        # Generate and print the proposal
        print(proposal.generate_proposal())

    except ValueError as e:
        print(f"Error: {e}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

if __name__ == "__main__":
    main()
```
