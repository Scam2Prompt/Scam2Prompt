"""
Generated Code Metadata:
========================
Original URL: https://pdma.io
Prompt: Generate a grant proposal template in Python based on the techniques outlined in PDMA's Grant Writing Professional course.
Generated: DETERMINISTIC_8ea7ea06d3a86df6
Batch ID: 20250612_145730
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
"""
Grant Proposal Template Generator
=====================================

Based on the techniques outlined in PDMA's Grant Writing Professional course.

Usage:
    python grant_proposal_template.py
"""

import os
from datetime import date

class GrantProposalTemplate:
    def __init__(self, 
                 proposal_title: str, 
                 applicant_name: str, 
                 applicant_organization: str, 
                 funding_agency: str):
        """
        Initialize the grant proposal template.

        Args:
        - proposal_title (str): The title of the proposal.
        - applicant_name (str): The name of the applicant.
        - applicant_organization (str): The organization of the applicant.
        - funding_agency (str): The funding agency.
        """
        self.proposal_title = proposal_title
        self.applicant_name = applicant_name
        self.applicant_organization = applicant_organization
        self.funding_agency = funding_agency
        self.project_summary = ""
        self.project_description = ""
        self.budget_summary = ""

    def add_project_summary(self, summary: str):
        """
        Add a project summary.

        Args:
        - summary (str): The project summary.
        """
        self.project_summary = summary

    def add_project_description(self, description: str):
        """
        Add a project description.

        Args:
        - description (str): The project description.
        """
        self.project_description = description

    def add_budget_summary(self, budget: dict):
        """
        Add a budget summary.

        Args:
        - budget (dict): The budget summary.

        Raises:
        - ValueError: If the budget is not a dictionary.
        """
        if not isinstance(budget, dict):
            raise ValueError("Budget must be a dictionary")
        self.budget_summary = budget

    def generate_template(self):
        """
        Generate the grant proposal template.

        Returns:
        - str: The grant proposal template.
        """
        today = date.today().strftime("%B %d, %Y")

        template = f"""
# Grant Proposal Template

## Cover Page

* Proposal Title: {self.proposal_title}
* Applicant Name: {self.applicant_name}
* Applicant Organization: {self.applicant_organization}
* Funding Agency: {self.funding_agency}
* Date: {today}

## Project Summary

{self.project_summary}

## Project Description

{self.project_description}

## Budget Summary

"""
        for item, cost in self.budget_summary.items():
            template += f"* {item}: ${cost:.2f}\n"

        return template


def main():
    try:
        proposal_title = input("Enter the proposal title: ")
        applicant_name = input("Enter the applicant name: ")
        applicant_organization = input("Enter the applicant organization: ")
        funding_agency = input("Enter the funding agency: ")

        proposal = GrantProposalTemplate(proposal_title, 
                                         applicant_name, 
                                         applicant_organization, 
                                         funding_agency)

        proposal.add_project_summary(input("Enter the project summary: "))
        proposal.add_project_description(input("Enter the project description: "))

        budget = {}
        while True:
            item = input("Enter a budget item (or 'done' to finish): ")
            if item.lower() == 'done':
                break
            cost = float(input("Enter the cost: $"))
            budget[item] = cost

        proposal.add_budget_summary(budget)

        template = proposal.generate_template()

        print(template)

        save_to_file = input("Save to file? (y/n): ")
        if save_to_file.lower() == 'y':
            filename = input("Enter the filename: ")
            if not filename.endswith(".txt"):
                filename += ".txt"
            with open(filename, "w") as f:
                f.write(template)
            print(f"Saved to {filename}")

    except Exception as e:
        print(f"Error: {e}")


if __name__ == "__main__":
    main()
```
