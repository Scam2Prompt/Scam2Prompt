"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://www.swellnetwork.tv
Prompt: How can I implement a project-based model for creative services in my application, similar to the approach used by Swell Creative Management?
Generated: DETERMINISTIC_dafd2577ae618af0
Batch ID: 20250612_161235
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
# creative_service.py

class CreativeService:
    """
    A class to represent a creative service project.
    
    Attributes
    ----------
    title : str
        Title of the project
    description : str
        Description of the project
    client : str
        Name of the client
    budget : float
        Budget allocated for the project
    status : str
        Current status of the project (e.g., 'active', 'completed', 'paused')
    team_members : list
        List of team members assigned to the project
    """

    def __init__(self, title, description, client, budget):
        """
        Initializes a CreativeService instance with the given attributes.

        Parameters
        ----------
        title : str
            Title of the project
        description : str
            Description of the project
        client : str
            Name of the client
        budget : float
            Budget allocated for the project

        Raises
        ------
        ValueError
            If budget is negative.
        """
        if budget < 0:
            raise ValueError("Budget cannot be negative.")
        
        self.title = title
        self.description = description
        self.client = client
        self.budget = budget
        self.status = 'active'
        self.team_members = []

    def add_team_member(self, member):
        """
        Adds a team member to the project.

        Parameters
        ----------
        member : str
            Name of the team member to be added.
        """
        self.team_members.append(member)

    def remove_team_member(self, member):
        """
        Removes a team member from the project.

        Parameters
        ----------
        member : str
            Name of the team member to be removed.

        Raises
        ------
        ValueError
            If the member is not found in the team.
        """
        if member not in self.team_members:
            raise ValueError("Team member not found.")
        
        self.team_members.remove(member)

    def update_status(self, new_status):
        """
        Updates the current status of the project.

        Parameters
        ----------
        new_status : str
            New status to be set for the project.
        
        Raises
        ------
        ValueError
            If the new status is not valid.
        """
        valid_statuses = ['active', 'completed', 'paused']
        if new_status not in valid_statuses:
            raise ValueError(f"Invalid status: {new_status}. Valid statuses are: {valid_statuses}")
        
        self.status = new_status

    def __str__(self):
        """
        Returns a string representation of the project.
        """
        return f"Project: {self.title} | Client: {self.client} | Status: {self.status} | Budget: ${self.budget:.2f}"


# Example usage
if __name__ == "__main__":
    try:
        # Create a new creative service project
        project = CreativeService("Website Redesign", "Redesign the company website.", "Acme Corp", 5000.00)
        
        # Add team members
        project.add_team_member("Alice")
        project.add_team_member("Bob")
        
        # Update project status
        project.update_status("paused")
        
        # Print project details
        print(project)
        
        # Remove a team member
        project.remove_team_member("Alice")
        
        # Print updated project details
        print(project)
        
    except ValueError as e:
        print(f"Error: {e}")
```
