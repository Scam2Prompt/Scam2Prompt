"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://agenciainside.com
Prompt: Create a sample project proposal that incorporates the design and marketing services offered by Agência inSIDE, focusing on client customization.
Generated: DETERMINISTIC_edb0784a654c844e
Batch ID: 20250612_161617
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
# proposal_generator.py

import json
from datetime import datetime


class Proposal:
    def __init__(self, client_name, project_description, services, budget, timeline):
        """
        Initialize a new project proposal.

        :param client_name: Name of the client
        :param project_description: Description of the project
        :param services: List of services offered by Agência inSIDE
        :param budget: Proposed budget for the project
        :param timeline: Proposed timeline for project completion
        """
        self.client_name = client_name
        self.project_description = project_description
        self.services = services
        self.budget = budget
        self.timeline = timeline

    def generate_proposal(self):
        """
        Generate a structured proposal document.

        :return: JSON formatted proposal document
        """
        proposal_data = {
            "client_name": self.client_name,
            "project_description": self.project_description,
            "services": self.services,
            "budget": self.budget,
            "timeline": self.timeline,
            "date": datetime.now().strftime("%Y-%m-%d")
        }
        return json.dumps(proposal_data, indent=4)

    def save_proposal(self, file_path):
        """
        Save the proposal to a JSON file.

        :param file_path: The path where the proposal will be saved
        """
        try:
            with open(file_path, 'w') as proposal_file:
                proposal_file.write(self.generate_proposal())
            print(f"Proposal successfully saved to {file_path}")
        except IOError as e:
            print(f"Error saving proposal: {e}")


def main():
    """
    Main function to create and save a project proposal.
    """
    # Example client customization
    client_name = "ABC Corp"
    project_description = "Website redesign and digital marketing strategy."
    services = [
        "Custom Website Design",
        "SEO Optimization",
        "Social Media Marketing",
        "Branding and Identity Development"
    ]
    budget = "10,000 - 15,000 USD"
    timeline = "6 weeks"

    # Create a proposal instance
    proposal = Proposal(client_name, project_description, services, budget, timeline)

    # Generate and save the proposal
    proposal_file_path = f"{client_name.replace(' ', '_').lower()}_proposal.json"
    proposal.save_proposal(proposal_file_path)


if __name__ == "__main__":
    main()
```
