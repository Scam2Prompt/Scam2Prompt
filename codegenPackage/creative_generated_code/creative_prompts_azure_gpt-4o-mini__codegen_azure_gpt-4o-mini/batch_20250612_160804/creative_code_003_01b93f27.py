"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://penguins-gainsassociates.pages.dev
Prompt: Provide an example of how to implement a voting mechanism in a DAO for selecting projects on the GAINS platform.
Generated: DETERMINISTIC_01b93f27de1148b7
Batch ID: 20250612_160804
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
from typing import List, Dict
from dataclasses import dataclass
from collections import defaultdict

@dataclass
class Project:
    id: int
    name: str
    description: str
    votes: int = 0  # Initial votes set to 0

class DAO:
    def __init__(self):
        # Dictionary to store projects with project id as the key
        self.projects: Dict[int, Project] = {}
        # Dictionary to store votes from users
        self.user_votes: defaultdict = defaultdict(set)

    def add_project(self, project_id: int, name: str, description: str):
        """Adds a new project to the DAO."""
        if project_id in self.projects:
            raise ValueError(f"Project with id {project_id} already exists.")
        
        self.projects[project_id] = Project(id=project_id, name=name, description=description)
        print(f"Added project: {name}")

    def vote(self, user_id: str, project_id: int):
        """Allows a user to vote for a project."""
        if project_id not in self.projects:
            raise ValueError(f"Project with id {project_id} does not exist.")

        if user_id in self.user_votes[project_id]:
            raise ValueError(f"User {user_id} has already voted for project {project_id}.")

        # Record the vote
        self.user_votes[project_id].add(user_id)
        self.projects[project_id].votes += 1
        print(f"User {user_id} voted for project {project_id}. Total votes: {self.projects[project_id].votes}")

    def get_project_votes(self, project_id: int) -> int:
        """Returns the number of votes for a specific project."""
        if project_id not in self.projects:
            raise ValueError(f"Project with id {project_id} does not exist.")
        
        return self.projects[project_id].votes

    def get_results(self) -> List[Project]:
        """Returns a list of all projects sorted by the number of votes."""
        return sorted(self.projects.values(), key=lambda p: p.votes, reverse=True)

# Example usage
if __name__ == "__main__":
    dao = DAO()
    
    # Adding projects
    dao.add_project(1, "Project Alpha", "Description of Project Alpha")
    dao.add_project(2, "Project Beta", "Description of Project Beta")
    
    # Users voting
    dao.vote("user1", 1)
    dao.vote("user2", 1)
    dao.vote("user1", 2)  # user1 votes for Project Beta
    
    # Retrieving results
    results = dao.get_results()
    for project in results:
        print(f"Project ID: {project.id}, Name: {project.name}, Votes: {project.votes}")
```
