"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://anshsofttech.com
Prompt: Create a project proposal template for a software development project, incorporating Ansh Soft Tech's values of client-first solutions and tailored approaches.
Generated: DETERMINISTIC_e5264fd561cab69b
Batch ID: 20250612_151835
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import json
from datetime import datetime

class ProjectProposal:
    def __init__(self, client_name, project_title, project_description, timeline, budget):
        """
        Initializes a new ProjectProposal instance.

        :param client_name: Name of the client
        :param project_title: Title of the project
        :param project_description: Description of what the project involves
        :param timeline: Estimated timeline for project completion
        :param budget: Estimated budget for the project
        """
        self.client_name = client_name
        self.project_title = project_title
        self.project_description = project_description
        self.timeline = timeline
        self.budget = budget
        self.created_at = datetime.now()

    def to_dict(self):
        """
        Converts the ProjectProposal instance to a dictionary for easy serialization.

        :return: Dictionary representation of the project proposal
        """
        return {
            "client_name": self.client_name,
            "project_title": self.project_title,
            "project_description": self.project_description,
            "timeline": self.timeline,
            "budget": self.budget,
            "created_at": self.created_at.isoformat()
        }

    def save_to_file(self, filename):
        """
        Saves the project proposal to a JSON file.

        :param filename: Name of the file to save the proposal
        """
        try:
            with open(filename, 'w') as file:
                json.dump(self.to_dict(), file, indent=4)
            print(f"Project proposal saved to {filename}")
        except IOError as e:
            print(f"Error saving proposal to file: {e}")

def create_proposal():
    """
    Prompts user for project proposal details and creates a ProjectProposal instance.
    """
    client_name = input("Enter the client's name: ")
    project_title = input("Enter the project title: ")
    project_description = input("Enter the project description: ")
    timeline = input("Enter the estimated timeline: ")
    budget = input("Enter the estimated budget: ")

    proposal = ProjectProposal(client_name, project_title, project_description, timeline, budget)
    
    filename = f"{client_name.replace(' ', '_')}_proposal.json"
    proposal.save_to_file(filename)

if __name__ == "__main__":
    create_proposal()
```
