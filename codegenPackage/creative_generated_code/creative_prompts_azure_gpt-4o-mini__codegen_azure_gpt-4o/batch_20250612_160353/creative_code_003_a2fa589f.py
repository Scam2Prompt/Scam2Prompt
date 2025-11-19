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
# Import necessary modules
from typing import List, Dict

class RoleAssignmentError(Exception):
    """Custom exception for role assignment errors."""
    pass

class ProjectManagementTool:
    """
    A class representing a project management tool for assigning roles to team members.
    """

    def __init__(self):
        """
        Initializes the project management tool with an empty list of team members and roles.
        """
        self.team_members = {}  # Dictionary to store team members and their assigned roles

    def add_team_member(self, member_name: str) -> None:
        """
        Adds a new team member to the project.
        
        :param member_name: Name of the team member to add
        :raises ValueError: If the team member already exists
        """
        if member_name in self.team_members:
            raise ValueError(f"Team member '{member_name}' already exists.")
        self.team_members[member_name] = None  # Initially, no role is assigned
        print(f"Team member '{member_name}' added successfully.")

    def assign_role(self, member_name: str, role: str) -> None:
        """
        Assigns a role to a team member.
        
        :param member_name: Name of the team member
        :param role: Role to assign to the team member
        :raises RoleAssignmentError: If the team member does not exist
        """
        if member_name not in self.team_members:
            raise RoleAssignmentError(f"Team member '{member_name}' does not exist.")
        self.team_members[member_name] = role
        print(f"Role '{role}' assigned to team member '{member_name}'.")

    def get_team_roles(self) -> Dict[str, str]:
        """
        Retrieves the current roles of all team members.
        
        :return: Dictionary mapping team members to their assigned roles
        """
        return self.team_members

# Example usage
if __name__ == "__main__":
    # Instantiate the project management tool
    project_tool = ProjectManagementTool()

    try:
        # Add team members
        project_tool.add_team_member("Alice")
        project_tool.add_team_member("Bob")
        
        # Assign roles
        project_tool.assign_role("Alice", "Project Manager")
        project_tool.assign_role("Bob", "Developer")
        
        # Retrieve and print team roles
        roles = project_tool.get_team_roles()
        print("Current team roles:")
        for member, role in roles.items():
            print(f"{member}: {role}")
    
    except (ValueError, RoleAssignmentError) as e:
        # Handle exceptions gracefully
        print(f"Error: {e}")
```
