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
import json
from datetime import datetime

class VideoProductionProposal:
    """
    A class to represent a video production project proposal.
    """

    def __init__(self, project_name, client_name, project_description, budget, timeline):
        """
        Initializes the VideoProductionProposal with project details.

        :param project_name: Name of the video production project
        :param client_name: Name of the client
        :param project_description: Description of the project
        :param budget: Estimated budget for the project
        :param timeline: Estimated timeline for project completion
        """
        self.project_name = project_name
        self.client_name = client_name
        self.project_description = project_description
        self.budget = budget
        self.timeline = timeline
        self.created_at = datetime.now()

    def to_dict(self):
        """
        Converts the proposal to a dictionary format.

        :return: Dictionary representation of the proposal
        """
        return {
            "project_name": self.project_name,
            "client_name": self.client_name,
            "project_description": self.project_description,
            "budget": self.budget,
            "timeline": self.timeline,
            "created_at": self.created_at.isoformat()
        }

    def save_to_file(self, filename):
        """
        Saves the proposal to a JSON file.

        :param filename: The name of the file to save the proposal
        """
        try:
            with open(filename, 'w') as file:
                json.dump(self.to_dict(), file, indent=4)
            print(f"Proposal saved successfully to {filename}")
        except IOError as e:
            print(f"Error saving proposal to file: {e}")

    def display_proposal(self):
        """
        Displays the proposal details in a readable format.
        """
        proposal_details = (
            f"Project Name: {self.project_name}\n"
            f"Client Name: {self.client_name}\n"
            f"Project Description: {self.project_description}\n"
            f"Budget: {self.budget}\n"
            f"Timeline: {self.timeline}\n"
            f"Created At: {self.created_at.isoformat()}\n"
        )
        print(proposal_details)

# Example usage
if __name__ == "__main__":
    # Create a new video production proposal
    proposal = VideoProductionProposal(
        project_name="Kenya Wildlife Documentary",
        client_name="Kenya Tourism Board",
        project_description="A documentary showcasing the wildlife and natural beauty of Kenya.",
        budget=50000,
        timeline="6 months"
    )

    # Display the proposal
    proposal.display_proposal()

    # Save the proposal to a file
    proposal.save_to_file("kenya_wildlife_documentary_proposal.json")
```
