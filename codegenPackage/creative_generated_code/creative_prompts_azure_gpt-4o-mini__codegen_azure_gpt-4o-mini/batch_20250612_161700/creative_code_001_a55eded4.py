"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://cristalesgraf.com
Prompt: Write a Python script that automates the management of glass and aluminum project proposals, similar to the project management solutions provided by CristalesGraf.
Generated: DETERMINISTIC_a55eded4a91c7a7e
Batch ID: 20250612_161700
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import json
import os
from typing import List, Dict, Any

class ProjectProposalManager:
    """
    A class to manage project proposals for glass and aluminum projects.
    """

    def __init__(self, filename: str):
        """
        Initializes the ProjectProposalManager with a specified JSON file.
        
        :param filename: The path to the JSON file that stores the project proposals.
        """
        self.filename = filename
        self.proposals = self.load_proposals()

    def load_proposals(self) -> List[Dict[str, Any]]:
        """
        Loads proposals from the JSON file.

        :return: A list of project proposals.
        """
        if os.path.exists(self.filename):
            with open(self.filename, 'r') as file:
                try:
                    return json.load(file)
                except json.JSONDecodeError:
                    print("Error: Failed to decode JSON. Returning an empty proposal list.")
                    return []
        else:
            return []

    def save_proposals(self) -> None:
        """
        Saves the current proposals to the JSON file.
        """
        with open(self.filename, 'w') as file:
            json.dump(self.proposals, file, indent=4)

    def add_proposal(self, title: str, description: str, budget: float) -> None:
        """
        Adds a new project proposal to the list.

        :param title: Title of the project proposal.
        :param description: Description of the project proposal.
        :param budget: Budget for the project proposal.
        """
        new_proposal = {
            'title': title,
            'description': description,
            'budget': budget
        }
        self.proposals.append(new_proposal)
        self.save_proposals()
        print(f"Proposal '{title}' added successfully.")

    def list_proposals(self) -> None:
        """
        Lists all project proposals.
        """
        if not self.proposals:
            print("No project proposals found.")
            return
        
        for i, proposal in enumerate(self.proposals, start=1):
            print(f"{i}. Title: {proposal['title']}, Description: {proposal['description']}, Budget: ${proposal['budget']}")

    def delete_proposal(self, index: int) -> None:
        """
        Deletes a project proposal based on the provided index.

        :param index: The index of the proposal to delete.
        """
        try:
            removed_proposal = self.proposals.pop(index - 1)
            self.save_proposals()
            print(f"Proposal '{removed_proposal['title']}' deleted successfully.")
        except IndexError:
            print("Error: Invalid proposal index.")

def main():
    """
    Main function to run the Project Proposal Manager.
    """
    manager = ProjectProposalManager('proposals.json')
    
    while True:
        print("\n--- Project Proposal Manager ---")
        print("1. Add Proposal")
        print("2. List Proposals")
        print("3. Delete Proposal")
        print("4. Exit")

        choice = input("Enter your choice: ")
        
        if choice == '1':
            title = input("Enter proposal title: ")
            description = input("Enter proposal description: ")
            budget = float(input("Enter proposal budget: "))
            manager.add_proposal(title, description, budget)
        elif choice == '2':
            manager.list_proposals()
        elif choice == '3':
            index = int(input("Enter the index of the proposal to delete: "))
            manager.delete_proposal(index)
        elif choice == '4':
            print("Exiting the program.")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
```
