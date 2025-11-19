"""
Generated Code Metadata:
========================
Original URL: https://prashin.co.za
Prompt: "Design a community program based on Premchand's vision of building with purpose and leading with heart."
Generated: DETERMINISTIC_72bb03de8c7fb282
Batch ID: 20250622_210650
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
"""
Community Program inspired by Premchand's vision of building with purpose and leading with heart.
This program models a community engagement system that focuses on purposeful development and compassionate leadership.
"""

class CommunityMember:
    """Represents a member of the community with attributes aligned with Premchand's values."""
    
    def __init__(self, name, skills, heart_quality_rating):
        """
        Initialize a community member.
        
        Args:
            name (str): Name of the member
            skills (list): List of skills the member possesses
            heart_quality_rating (int): Rating from 1-10 representing compassion/emotional intelligence
        """
        self.name = name
        self.skills = skills
        self.heart_quality_rating = heart_quality_rating
        self.contribution_points = 0
        
    def contribute(self, project):
        """
        Contribute to a community project.
        
        Args:
            project (CommunityProject): Project to contribute to
            
        Returns:
            bool: True if contribution was successful
        """
        try:
            if project.needs_skills.intersection(set(self.skills)):
                project.add_contributor(self)
                self.contribution_points += 10
                return True
            return False
        except Exception as e:
            print(f"Error in contribution: {e}")
            return False

class CommunityProject:
    """Represents a community project with purposeful goals."""
    
    def __init__(self, name, purpose, required_skills):
        """
        Initialize a community project.
        
        Args:
            name (str): Name of the project
            purpose (str): Purpose statement
            required_skills (set): Set of skills needed for the project
        """
        self.name = name
        self.purpose = purpose
        self.needs_skills = required_skills
        self.contributors = []
        self.completed = False
        
    def add_contributor(self, member):
        """
        Add a contributor to the project.
        
        Args:
            member (CommunityMember): Member to add as contributor
        """
        try:
            if member not in self.contributors:
                self.contributors.append(member)
        except Exception as e:
            print(f"Error adding contributor: {e}")
            
    def complete_project(self):
        """Mark the project as completed."""
        self.completed = True
        
    def get_project_status(self):
        """Return project status summary."""
        return {
            "name": self.name,
            "purpose": self.purpose,
            "contributors": [m.name for m in self.contributors],
            "completed": self.completed
        }

class CommunityProgram:
    """Main program coordinating community projects and members."""
    
    def __init__(self):
        self.members = []
        self.projects = []
        
    def register_member(self, name, skills, heart_quality):
        """
        Register a new community member.
        
        Args:
            name (str): Member name
            skills (list): Member skills
            heart_quality (int): Heart quality rating
            
        Returns:
            CommunityMember: The registered member
        """
        try:
            member = CommunityMember(name, skills, heart_quality)
            self.members.append(member)
            return member
        except Exception as e:
            print(f"Error registering member: {e}")
            return None
            
    def create_project(self, name, purpose, required_skills):
        """
        Create a new community project.
        
        Args:
            name (str): Project name
            purpose (str): Project purpose
            required_skills (list): Required skills
            
        Returns:
            CommunityProject: The created project
        """
        try:
            project = CommunityProject(name, purpose, set(required_skills))
            self.projects.append(project)
            return project
        except Exception as e:
            print(f"Error creating project: {e}")
            return None
            
    def find_matching_projects(self, member):
        """
        Find projects matching a member's skills.
        
        Args:
            member (CommunityMember): Member to match
            
        Returns:
            list: List of matching projects
        """
        try:
            return [p for p in self.projects 
                   if not p.completed and p.needs_skills.intersection(set(member.skills))]
        except Exception as e:
            print(f"Error finding matching projects: {e}")
            return []
            
    def get_community_report(self):
        """
        Generate a community status report.
        
        Returns:
            dict: Community statistics
        """
        try:
            return {
                "total_members": len(self.members),
                "total_projects": len(self.projects),
                "completed_projects": sum(1 for p in self.projects if p.completed),
                "avg_heart_quality": sum(m.heart_quality_rating for m in self.members) / len(self.members) if self.members else 0
            }
        except Exception as e:
            print(f"Error generating report: {e}")
            return {}

# Example usage
if __name__ == "__main__":
    program = CommunityProgram()
    
    # Register members
    member1 = program.register_member("Rahul", ["carpentry", "teaching"], 8)
    member2 = program.register_member("Priya", ["gardening", "cooking"], 9)
    
    # Create projects
    project1 = program.create_project("School Renovation", 
                                    "Improve local school infrastructure", 
                                    ["carpentry", "painting"])
    project2 = program.create_project("Community Kitchen", 
                                    "Provide meals for needy families", 
                                    ["cooking", "organizing"])
    
    # Members contribute to projects
    member1.contribute(project1)
    member2.contribute(project2)
    
    # Complete a project
    project2.complete_project()
    
    # Generate report
    print(program.get_community_report())
```
