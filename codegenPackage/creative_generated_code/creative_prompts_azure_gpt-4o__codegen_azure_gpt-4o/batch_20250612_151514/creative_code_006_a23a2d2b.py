"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://pooltyme.app
Prompt: Develop a feature that allows users to invite others to collaborate on pool maintenance tasks, similar to the collaborative functionality of Pooltyme.
Generated: DETERMINISTIC_a23a2d2b0d29fa00
Batch ID: 20250612_151514
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
# Python Code: Collaborative Pool Maintenance Invitation Feature

import uuid
from typing import List, Dict

# Define a class for the Pool Maintenance Collaboration feature
class PoolMaintenanceCollaboration:
    def __init__(self):
        # Dictionary to store pool maintenance groups
        # Each group is identified by a unique ID and contains information about members and tasks
        self.groups: Dict[str, Dict] = {}
    
    def create_group(self, owner_email: str) -> str:
        """
        Creates a new pool maintenance group.
        
        Args:
            owner_email (str): Email of the group owner.
        
        Returns:
            str: Unique group ID of the created group.
        """
        group_id = str(uuid.uuid4())  # Generate a unique group ID
        self.groups[group_id] = {
            "owner_email": owner_email,
            "members": [owner_email],  # Add owner to members list
            "tasks": []  # Initialize with no tasks
        }
        return group_id
    
    def invite_member(self, group_id: str, inviter_email: str, invitee_email: str) -> str:
        """
        Invites a new member to a pool maintenance group.
        
        Args:
            group_id (str): ID of the group to invite the member to.
            inviter_email (str): Email of the member sending the invitation.
            invitee_email (str): Email of the member being invited.
        
        Returns:
            str: Confirmation message if invitation is successful.
        """
        # Validate group existence
        if group_id not in self.groups:
            raise ValueError("Group ID not found.")
        
        group = self.groups[group_id]
        
        # Validate inviter membership
        if inviter_email not in group["members"]:
            raise PermissionError("Inviter is not a member of this group.")
        
        # Add invitee to the group
        if invitee_email in group["members"]:
            return f"{invitee_email} is already a member of the group."
        
        group["members"].append(invitee_email)
        return f"{invitee_email} has been successfully invited to the group."
    
    def list_members(self, group_id: str) -> List[str]:
        """
        Lists all members of a pool maintenance group.
        
        Args:
            group_id (str): ID of the group to get members from.
        
        Returns:
            List[str]: List of member emails in the group.
        """
        # Validate group existence
        if group_id not in self.groups:
            raise ValueError("Group ID not found.")
        
        return self.groups[group_id]["members"]
    
    def assign_task(self, group_id: str, assigner_email: str, task_description: str) -> str:
        """
        Assigns a maintenance task to the group.
        
        Args:
            group_id (str): ID of the group to assign the task to.
            assigner_email (str): Email of the member assigning the task.
            task_description (str): Description of the task.
        
        Returns:
            str: Confirmation message if task assignment is successful.
        """
        # Validate group existence
        if group_id not in self.groups:
            raise ValueError("Group ID not found.")
        
        group = self.groups[group_id]
        
        # Validate assigner membership
        if assigner_email not in group["members"]:
            raise PermissionError("Assigner is not a member of this group.")
        
        # Add task to the group's task list
        task = {
            "description": task_description,
            "assigned_by": assigner_email
        }
        group["tasks"].append(task)
        return f"Task '{task_description}' has been successfully assigned by {assigner_email}."
    
    def list_tasks(self, group_id: str) -> List[Dict]:
        """
        Lists all tasks assigned to a pool maintenance group.
        
        Args:
            group_id (str): ID of the group to get tasks from.
        
        Returns:
            List[Dict]: List of tasks with their descriptions and assigned-by information.
        """
        # Validate group existence
        if group_id not in self.groups:
            raise ValueError("Group ID not found.")
        
        return self.groups[group_id]["tasks"]

# Example Usage
if __name__ == "__main__":
    try:
        # Initialize the collaboration system
        collaboration_system = PoolMaintenanceCollaboration()
        
        # Create a new pool maintenance group
        group_id = collaboration_system.create_group(owner_email="owner@example.com")
        print(f"Group created with ID: {group_id}")
        
        # Invite a new member to the group
        invite_response = collaboration_system.invite_member(
            group_id=group_id, 
            inviter_email="owner@example.com", 
            invitee_email="newmember@example.com"
        )
        print(invite_response)
        
        # List group members
        members = collaboration_system.list_members(group_id=group_id)
        print(f"Group Members: {members}")
        
        # Assign a task to the group
        task_response = collaboration_system.assign_task(
            group_id=group_id, 
            assigner_email="owner@example.com", 
            task_description="Clean the pool filter."
        )
        print(task_response)
        
        # List group tasks
        tasks = collaboration_system.list_tasks(group_id=group_id)
        print(f"Group Tasks: {tasks}")
    
    except Exception as e:
        print(f"Error: {e}")
```
