"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://gitcoin-dr-manager-bz23c2f5n-bootnode.vercel.app
Prompt: What are the key features of the Gitcoin Round Manager that facilitate decentralized funding?
Generated: DETERMINISTIC_a647e28196eadcf4
Batch ID: 20250612_161356
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
# Gitcoin Round Manager Simulation
# Key features facilitating decentralized funding

import json

class GitcoinRoundManager:
    """
    Gitcoin Round Manager class to facilitate decentralized funding.
    """

    def __init__(self):
        """
        Initializes the manager with default values.
        """
        self.rounds = {}  # Dictionary to store funding rounds
        self.projects = {}  # Dictionary to store registered projects

    def create_round(self, round_id, funding_goal, description):
        """
        Creates a new funding round.
        
        Args:
            round_id (str): Unique identifier for the funding round.
            funding_goal (float): Goal amount in funding.
            description (str): Brief description of the round.
        
        Raises:
            ValueError: If the round_id already exists.
        """
        if round_id in self.rounds:
            raise ValueError(f"Round {round_id} already exists.")
        
        self.rounds[round_id] = {
            "funding_goal": funding_goal,
            "description": description,
            "funds_raised": 0.0,
            "contributors": [],
        }

    def register_project(self, project_id, name, description):
        """
        Registers a project for participation in funding rounds.
        
        Args:
            project_id (str): Unique identifier for the project.
            name (str): Name of the project.
            description (str): Brief description of the project.
        
        Raises:
            ValueError: If the project_id already exists.
        """
        if project_id in self.projects:
            raise ValueError(f"Project {project_id} already exists.")
        
        self.projects[project_id] = {
            "name": name,
            "description": description,
            "funds_received": 0.0,
        }

    def contribute_funds(self, round_id, contributor_name, amount):
        """
        Allows contributors to fund a round.
        
        Args:
            round_id (str): ID of the funding round to contribute to.
            contributor_name (str): Name of the contributor.
            amount (float): Contribution amount.
        
        Raises:
            ValueError: If the round does not exist or amount is invalid.
        """
        if round_id not in self.rounds:
            raise ValueError(f"Round {round_id} does not exist.")
        if amount <= 0:
            raise ValueError("Contribution amount must be positive.")
        
        round_info = self.rounds[round_id]
        round_info["funds_raised"] += amount
        round_info["contributors"].append({
            "name": contributor_name,
            "amount": amount,
        })

    def distribute_funds(self, round_id):
        """
        Distributes funds from a completed round to registered projects.
        
        Args:
            round_id (str): ID of the funding round to distribute funds for.
            
        Raises:
            ValueError: If the round does not exist or no funds are raised.
        """
        if round_id not in self.rounds:
            raise ValueError(f"Round {round_id} does not exist.")
        
        round_info = self.rounds[round_id]
        if round_info["funds_raised"] == 0:
            raise ValueError(f"No funds raised in round {round_id}.")
        
        # Distribute funds equally among registered projects
        num_projects = len(self.projects)
        if num_projects == 0:
            raise ValueError("No projects registered for distribution.")
        
        funds_per_project = round_info["funds_raised"] / num_projects
        for project_id in self.projects:
            self.projects[project_id]["funds_received"] += funds_per_project
        
        # Reset the round after distribution
        round_info["funds_raised"] = 0.0
        round_info["contributors"] = []

    def get_round_details(self, round_id):
        """
        Retrieves details of a specific funding round.
        
        Args:
            round_id (str): ID of the funding round.
        
        Returns:
            dict: Details of the funding round.
        
        Raises:
            ValueError: If the round does not exist.
        """
        if round_id not in self.rounds:
            raise ValueError(f"Round {round_id} does not exist.")
        
        return self.rounds[round_id]

    def get_project_details(self, project_id):
        """
        Retrieves details of a specific project.
        
        Args:
            project_id (str): ID of the project.
        
        Returns:
            dict: Details of the project.
        
        Raises:
            ValueError: If the project does not exist.
        """
        if project_id not in self.projects:
            raise ValueError(f"Project {project_id} does not exist.")
        
        return self.projects[project_id]

    def export_data(self, filename):
        """
        Exports all round and project data to a JSON file.
        
        Args:
            filename (str): Name of the file to export data to.
        
        Raises:
            IOError: If an error occurs during file writing.
        """
        try:
            data = {
                "rounds": self.rounds,
                "projects": self.projects,
            }
            with open(filename, "w") as file:
                json.dump(data, file, indent=4)
        except IOError as e:
            raise IOError(f"Failed to export data: {str(e)}")

# Example usage:
if __name__ == "__main__":
    manager = GitcoinRoundManager()
    
    # Creating a funding round
    manager.create_round("round1", 1000, "Funding Round 1")
    
    # Registering projects
    manager.register_project("project1", "Project Alpha", "A decentralized application.")
    manager.register_project("project2", "Project Beta", "Blockchain-based solution.")
    
    # Contributing funds
    manager.contribute_funds("round1", "Alice", 500)
    manager.contribute_funds("round1", "Bob", 300)
    
    # Distributing funds
    manager.distribute_funds("round1")
    
    # Exporting data
    manager.export_data("gitcoin_data.json")
```
