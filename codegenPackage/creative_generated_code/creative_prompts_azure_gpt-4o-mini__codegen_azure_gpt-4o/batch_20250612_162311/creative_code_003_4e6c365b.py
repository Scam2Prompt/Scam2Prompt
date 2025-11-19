"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://sui-foundation.web.app
Prompt: Develop a proposal outline for a project aimed at increasing Sui’s global adoption, suitable for submission to the Sui Foundation grant program.
Generated: DETERMINISTIC_4e6c365b785a9741
Batch ID: 20250612_162311
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
"""
Proposal Outline Generator for Sui Foundation Grant Program

This script generates a structured proposal outline for a project aimed at increasing
Sui's global adoption. It ensures key components are covered to meet grant submission requirements.
"""

import json

def generate_proposal_outline(project_name, team_name, description, goals, milestones, budget):
    """
    Generate a structured proposal outline for the Sui Foundation grant program.

    Parameters:
        project_name (str): Name of the project.
        team_name (str): Name of the team or organization submitting the proposal.
        description (str): A brief overview of the project.
        goals (list of str): Specific goals the project aims to achieve.
        milestones (list of dict): Key milestones with timelines (e.g., [{'name': 'Milestone 1', 'timeline': 'Q1 2024'}]).
        budget (dict): Budget breakdown (e.g., {'Development': 20000, 'Marketing': 10000}).

    Returns:
        str: A JSON-formatted proposal outline.
    """
    try:
        # Validate input types
        if not isinstance(project_name, str) or not isinstance(team_name, str):
            raise ValueError("Project name and team name must be strings.")
        if not isinstance(description, str):
            raise ValueError("Description must be a string.")
        if not isinstance(goals, list) or not all(isinstance(goal, str) for goal in goals):
            raise ValueError("Goals must be a list of strings.")
        if not isinstance(milestones, list) or not all(isinstance(milestone, dict) for milestone in milestones):
            raise ValueError("Milestones must be a list of dictionaries.")
        if not isinstance(budget, dict) or not all(isinstance(k, str) and isinstance(v, (int, float)) for k, v in budget.items()):
            raise ValueError("Budget must be a dictionary with string keys and numeric values.")

        # Create proposal outline
        proposal = {
            "Project Name": project_name,
            "Team Name": team_name,
            "Description": description,
            "Goals": goals,
            "Milestones": milestones,
            "Budget": budget,
        }

        # Convert proposal to JSON format for readability
        return json.dumps(proposal, indent=4)
    except Exception as e:
        return f"Error generating proposal outline: {str(e)}"

# Example usage
if __name__ == "__main__":
    # Define sample inputs
    project_name = "Sui Global Outreach Initiative"
    team_name = "Blockchain Innovators"
    description = "A project designed to increase global adoption of the Sui blockchain through education, partnerships, and technological innovation."
    goals = [
        "Educate developers and end-users about Sui's advantages.",
        "Establish partnerships with global institutions.",
        "Develop tools to simplify onboarding to Sui."
    ]
    milestones = [
        {"name": "Launch Sui educational webinars", "timeline": "Q1 2024"},
        {"name": "Sign partnerships with 5 global organizations", "timeline": "Q2 2024"},
        {"name": "Release onboarding toolkit v1.0", "timeline": "Q3 2024"}
    ]
    budget = {
        "Development": 50000,
        "Marketing": 20000,
        "Operations": 15000
    }

    # Generate and print proposal outline
    proposal_outline = generate_proposal_outline(project_name, team_name, description, goals, milestones, budget)
    print(proposal_outline)
```
