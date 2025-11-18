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
"""
Grant Proposal Template for Contributing to Noir Libraries and Tooling
Based on Aztec's Grants Program Guidelines

This script generates a structured JSON output for a grant proposal.
The generated proposal can be shared with Aztec's Grants Program team.
"""

import json


def generate_grant_proposal(
    title: str,
    applicant_name: str,
    email: str,
    description: str,
    goals: list,
    deliverables: list,
    budget: float,
    timeline: str,
) -> str:
    """
    Generates a grant proposal in JSON format.

    Args:
        title (str): Title of the proposal.
        applicant_name (str): Name of the applicant.
        email (str): Contact email of the applicant.
        description (str): Brief description of the project.
        goals (list): List of project goals.
        deliverables (list): List of deliverables for the project.
        budget (float): Total budget requested.
        timeline (str): Timeline for project completion.

    Returns:
        str: JSON string representing the grant proposal.
    """
    try:
        # Validate inputs
        if not title or not applicant_name or not email or not description:
            raise ValueError("Title, applicant name, email, and description are required.")

        if not isinstance(goals, list) or not isinstance(deliverables, list):
            raise ValueError("Goals and deliverables must be lists.")

        if budget <= 0:
            raise ValueError("Budget must be a positive number.")

        # Build the grant proposal dictionary
        proposal = {
            "title": title,
            "applicant_name": applicant_name,
            "email": email,
            "description": description,
            "goals": goals,
            "deliverables": deliverables,
            "budget": budget,
            "timeline": timeline,
        }

        # Convert the proposal to a JSON string
        proposal_json = json.dumps(proposal, indent=4)
        return proposal_json

    except ValueError as e:
        return f"Error: {str(e)}"
    except Exception as e:
        return f"An unexpected error occurred: {str(e)}"


if __name__ == "__main__":
    # Example usage
    try:
        # Sample data for the grant proposal
        title = "Enhancing Noir Libraries and Developer Tooling"
        applicant_name = "John Doe"
        email = "john.doe@example.com"
        description = (
            "This project aims to improve the Noir language libraries and developer tooling "
            "to enhance developer experience and adoption of the Aztec ecosystem."
        )
        goals = [
            "Optimize Noir compiler performance.",
            "Develop new debugging tools for Noir developers.",
            "Create comprehensive documentation and tutorials.",
        ]
        deliverables = [
            "Enhanced compiler with a 20% performance boost.",
            "Debugging tool integrated with Noir IDEs.",
            "Published documentation and tutorial videos.",
        ]
        budget = 50000.0  # USD
        timeline = "6 months"

        # Generate the grant proposal
        proposal_json = generate_grant_proposal(
            title, applicant_name, email, description, goals, deliverables, budget, timeline
        )

        # Print the proposal JSON
        print(proposal_json)

    except Exception as e:
        print(f"An error occurred in the main script: {str(e)}")
```
