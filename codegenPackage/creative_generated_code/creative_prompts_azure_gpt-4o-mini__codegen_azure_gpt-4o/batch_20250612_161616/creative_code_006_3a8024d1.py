"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://nigger-2aa.pages.dev
Prompt: Describe how to implement project validation voting within the Magic Square ecosystem to influence Web3 development.
Generated: DETERMINISTIC_3a8024d17e38f56b
Batch ID: 20250612_161616
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
"""
Project Validation Voting System within the Magic Square ecosystem.

This code allows users to vote on Web3 development projects. It ensures 
proper validation of votes and calculates the final results.
"""

import json
from typing import Dict, List


class VotingSystem:
    """
    Project Validation Voting System class.
    Handles voting, project registration, and result computation.
    """

    def __init__(self):
        # Store registered projects and their votes
        self.projects: Dict[str, int] = {}

        # Store voters to prevent duplicate voting
        self.voters: List[str] = []

    def register_project(self, project_name: str) -> None:
        """
        Registers a new project for voting if not already registered.

        Args:
            project_name (str): The name of the project to register.

        Raises:
            ValueError: If the project is already registered.
        """
        if project_name in self.projects:
            raise ValueError(f"Project '{project_name}' is already registered.")
        self.projects[project_name] = 0
        print(f"Project '{project_name}' has been successfully registered.")

    def vote(self, voter_id: str, project_name: str) -> None:
        """
        Allows a user to cast a vote for a specified project.

        Args:
            voter_id (str): Unique identifier of the voter.
            project_name (str): Name of the project to vote for.

        Raises:
            ValueError: If the voter has already voted or the project does not exist.
        """
        if voter_id in self.voters:
            raise ValueError("This voter has already cast their vote.")
        if project_name not in self.projects:
            raise ValueError(f"Project '{project_name}' is not registered.")
        
        # Record the vote
        self.projects[project_name] += 1
        self.voters.append(voter_id)
        print(f"Voter '{voter_id}' successfully voted for '{project_name}'.")

    def get_results(self) -> Dict[str, int]:
        """
        Returns the voting results for all projects.

        Returns:
            Dict[str, int]: A dictionary with project names and their vote counts.
        """
        return self.projects

    def export_results(self, file_path: str) -> None:
        """
        Exports the voting results to a JSON file.

        Args:
            file_path (str): The file path to save the results.

        Raises:
            IOError: If the file cannot be written.
        """
        try:
            with open(file_path, 'w') as file:
                json.dump(self.projects, file)
            print(f"Results successfully exported to '{file_path}'.")
        except IOError as e:
            print(f"Failed to export results: {e}")


# Example usage
if __name__ == "__main__":
    voting_system = VotingSystem()

    try:
        # Register projects
        voting_system.register_project("Project A")
        voting_system.register_project("Project B")

        # Cast votes
        voting_system.vote("voter_001", "Project A")
        voting_system.vote("voter_002", "Project B")
        voting_system.vote("voter_003", "Project A")

        # Calculate and display results
        results = voting_system.get_results()
        print("Voting Results:")
        for project, votes in results.items():
            print(f"{project}: {votes} votes")

        # Export results
        voting_system.export_results("voting_results.json")
    except ValueError as ve:
        print(f"Validation Error: {ve}")
    except Exception as e:
        print(f"An error occurred: {e}")
```
