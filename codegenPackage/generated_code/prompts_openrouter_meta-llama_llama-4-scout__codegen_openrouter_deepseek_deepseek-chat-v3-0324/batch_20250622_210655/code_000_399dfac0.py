"""
Generated Code Metadata:
========================
Original URL: https://oric.kinnaird.edu.pk
Prompt: Write a Python code to manage research projects and their funding for an institution like ORIC at Kinnaird College.
Generated: DETERMINISTIC_399dfac05d4dcfb1
Batch ID: 20250622_210655
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import json
from typing import List, Dict, Optional
from datetime import datetime
import os

class ResearchProject:
    """
    A class to represent a research project with its details and funding information.
    """
    
    def __init__(self, title: str, principal_investigator: str, start_date: str, 
                 end_date: str, total_budget: float, funding_sources: List[str]):
        """
        Initialize a ResearchProject instance.
        
        Args:
            title (str): Title of the research project.
            principal_investigator (str): Name of the principal investigator.
            start_date (str): Start date of the project in 'YYYY-MM-DD' format.
            end_date (str): End date of the project in 'YYYY-MM-DD' format.
            total_budget (float): Total budget allocated for the project.
            funding_sources (List[str]): List of funding sources for the project.
        """
        self.title = title
        self.principal_investigator = principal_investigator
        self.start_date = start_date
        self.end_date = end_date
        self.total_budget = total_budget
        self.funding_sources = funding_sources
        self.expenses = []
    
    def add_expense(self, description: str, amount: float, date: str):
        """
        Add an expense to the project.
        
        Args:
            description (str): Description of the expense.
            amount (float): Amount spent.
            date (str): Date of the expense in 'YYYY-MM-DD' format.
        """
        self.expenses.append({
            'description': description,
            'amount': amount,
            'date': date
        })
    
    def get_remaining_budget(self) -> float:
        """
        Calculate the remaining budget for the project.
        
        Returns:
            float: Remaining budget.
        """
        total_spent = sum(expense['amount'] for expense in self.expenses)
        return self.total_budget - total_spent
    
    def to_dict(self) -> Dict:
        """
        Convert the project details to a dictionary.
        
        Returns:
            Dict: Dictionary representation of the project.
        """
        return {
            'title': self.title,
            'principal_investigator': self.principal_investigator,
            'start_date': self.start_date,
            'end_date': self.end_date,
            'total_budget': self.total_budget,
            'funding_sources': self.funding_sources,
            'expenses': self.expenses
        }
    
    @classmethod
    def from_dict(cls, data: Dict) -> 'ResearchProject':
        """
        Create a ResearchProject instance from a dictionary.
        
        Args:
            data (Dict): Dictionary containing project details.
            
        Returns:
            ResearchProject: Instance of ResearchProject.
        """
        project = cls(
            title=data['title'],
            principal_investigator=data['principal_investigator'],
            start_date=data['start_date'],
            end_date=data['end_date'],
            total_budget=data['total_budget'],
            funding_sources=data['funding_sources']
        )
        project.expenses = data.get('expenses', [])
        return project

class ResearchProjectManager:
    """
    A class to manage multiple research projects and their funding.
    """
    
    def __init__(self, data_file: str = 'research_projects.json'):
        """
        Initialize the ResearchProjectManager.
        
        Args:
            data_file (str): Path to the JSON file to store project data.
        """
        self.data_file = data_file
        self.projects = []
        self.load_projects()
    
    def add_project(self, project: ResearchProject):
        """
        Add a new research project.
        
        Args:
            project (ResearchProject): Project to be added.
        """
        self.projects.append(project)
        self.save_projects()
    
    def get_project(self, title: str) -> Optional[ResearchProject]:
        """
        Retrieve a project by its title.
        
        Args:
            title (str): Title of the project to retrieve.
            
        Returns:
            Optional[ResearchProject]: The project if found, None otherwise.
        """
        for project in self.projects:
            if project.title == title:
                return project
        return None
    
    def delete_project(self, title: str) -> bool:
        """
        Delete a project by its title.
        
        Args:
            title (str): Title of the project to delete.
            
        Returns:
            bool: True if the project was deleted, False otherwise.
        """
        project = self.get_project(title)
        if project:
            self.projects.remove(project)
            self.save_projects()
            return True
        return False
    
    def save_projects(self):
        """
        Save all projects to the data file.
        """
        try:
            with open(self.data_file, 'w') as f:
                json.dump([project.to_dict() for project in self.projects], f, indent=4)
        except IOError as e:
            print(f"Error saving projects: {e}")
    
    def load_projects(self):
        """
        Load projects from the data file.
        """
        if not os.path.exists(self.data_file):
            return
        
        try:
            with open(self.data_file, 'r') as f:
                data = json.load(f)
                self.projects = [ResearchProject.from_dict(project) for project in data]
        except (IOError, json.JSONDecodeError) as e:
            print(f"Error loading projects: {e}")
    
    def get_all_projects(self) -> List[ResearchProject]:
        """
        Get all projects.
        
        Returns:
            List[ResearchProject]: List of all projects.
        """
        return self.projects
    
    def get_projects_by_investigator(self, investigator: str) -> List[ResearchProject]:
        """
        Get projects by principal investigator.
        
        Args:
            investigator (str): Name of the principal investigator.
            
        Returns:
            List[ResearchProject]: List of projects for the investigator.
        """
        return [project for project in self.projects 
                if project.principal_investigator == investigator]
    
    def get_projects_by_funding_source(self, funding_source: str) -> List[ResearchProject]:
        """
        Get projects by funding source.
        
        Args:
            funding_source (str): Name of the funding source.
            
        Returns:
            List[ResearchProject]: List of projects funded by the source.
        """
        return [project for project in self.projects 
                if funding_source in project.funding_sources]

# Example usage
if __name__ == "__main__":
    manager = ResearchProjectManager()
    
    # Add a new project
    project = ResearchProject(
        title="AI in Education",
        principal_investigator="Dr. Smith",
        start_date="2023-01-01",
        end_date="2023-12-31",
        total_budget=50000.0,
        funding_sources=["Kinnaird College", "HEC"]
    )
    manager.add_project(project)
    
    # Add an expense to the project
    project.add_expense("Hardware Purchase", 10000.0, "2023-02-15")
    manager.save_projects()
    
    # Retrieve and print all projects
    for p in manager.get_all_projects():
        print(f"Project: {p.title}, Remaining Budget: {p.get_remaining_budget()}")
```
