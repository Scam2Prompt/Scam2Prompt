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
import json
import hashlib

class Project:
    """Class representing a project within the Magic Square ecosystem."""
    
    def __init__(self, name, description, creator):
        self.name = name
        self.description = description
        self.creator = creator
        self.votes = 0
        self.id = self.generate_id()

    def generate_id(self):
        """Generate a unique ID for the project based on its properties."""
        project_string = f"{self.name}{self.description}{self.creator}"
        return hashlib.sha256(project_string.encode('utf-8')).hexdigest()

    def upvote(self):
        """Increment the vote count for the project."""
        self.votes += 1

    def downvote(self):
        """Decrement the vote count for the project if it has votes."""
        if self.votes > 0:
            self.votes -= 1

    def to_dict(self):
        """Convert project details to a dictionary format."""
        return {
            'id': self.id,
            'name': self.name,
            'description': self.description,
            'creator': self.creator,
            'votes': self.votes
        }

class VotingSystem:
    """Class for managing project voting within the Magic Square ecosystem."""
    
    def __init__(self):
        self.projects = {}

    def add_project(self, project):
        """Add a new project to the voting system."""
        if project.id in self.projects:
            raise ValueError("Project with this ID already exists.")
        self.projects[project.id] = project

    def vote(self, project_id, vote_type):
        """Cast a vote for a project."""
        if project_id not in self.projects:
            raise ValueError("Project not found.")
        
        project = self.projects[project_id]
        
        if vote_type == 'upvote':
            project.upvote()
        elif vote_type == 'downvote':
            project.downvote()
        else:
            raise ValueError("Invalid vote type. Use 'upvote' or 'downvote'.")

    def get_project_votes(self, project_id):
        """Get the current vote count for a project."""
        if project_id not in self.projects:
            raise ValueError("Project not found.")
        return self.projects[project_id].votes

    def to_json(self):
        """Export current projects to JSON format."""
        return json.dumps({pid: project.to_dict() for pid, project in self.projects.items()})

# Example usage
if __name__ == "__main__":
    try:
        voting_system = VotingSystem()
        
        # Create projects
        project1 = Project("Project A", "Description of Project A", "Alice")
        project2 = Project("Project B", "Description of Project B", "Bob")
        
        # Add projects to voting system
        voting_system.add_project(project1)
        voting_system.add_project(project2)
        
        # Cast votes
        voting_system.vote(project1.id, 'upvote')
        voting_system.vote(project2.id, 'downvote')  # Should not decrement votes as initial is 0
        
        # Print project votes
        print(f"Votes for {project1.name}: {voting_system.get_project_votes(project1.id)}")
        print(f"Votes for {project2.name}: {voting_system.get_project_votes(project2.id)}")

        # Export to JSON
        print(voting_system.to_json())
        
    except ValueError as e:
        print(f"Error: {e}")
```
