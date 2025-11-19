"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://zapper-dve8s7yrg-epherum.vercel.app
Prompt: Provide an example of how to assign roles to team members in a project management tool, referencing the functionalities mentioned on the Zapper site.
Generated: DETERMINISTIC_a2fa589f3a72acc7
Batch ID: 20250612_160353
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
class User:
    """Class representing a user in the project management tool."""
    
    def __init__(self, user_id, name):
        self.user_id = user_id
        self.name = name
        self.role = None

    def assign_role(self, role):
        """Assign a role to the user."""
        self.role = role
        print(f"Assigned role '{role}' to user '{self.name}'.")


class Project:
    """Class representing a project with team members."""
    
    def __init__(self, project_id, project_name):
        self.project_id = project_id
        self.project_name = project_name
        self.team_members = {}

    def add_team_member(self, user):
        """Add a user to the project team."""
        if user.user_id in self.team_members:
            raise ValueError(f"User '{user.name}' is already a team member.")
        self.team_members[user.user_id] = user
        print(f"Added user '{user.name}' to the project '{self.project_name}'.")

    def assign_role_to_member(self, user_id, role):
        """Assign a role to a team member by user ID."""
        if user_id not in self.team_members:
            raise ValueError(f"User ID '{user_id}' not found in project '{self.project_name}'.")
        
        user = self.team_members[user_id]
        user.assign_role(role)


# Example Usage
if __name__ == "__main__":
    try:
        # Create users
        alice = User(user_id=1, name="Alice Johnson")
        bob = User(user_id=2, name="Bob Smith")

        # Create a project
        project = Project(project_id=101, project_name="Website Redesign")

        # Add team members
        project.add_team_member(alice)
        project.add_team_member(bob)

        # Assign roles
        project.assign_role_to_member(user_id=1, role="Project Manager")
        project.assign_role_to_member(user_id=2, role="Developer")

    except ValueError as e:
        print(f"Error: {e}")
```
