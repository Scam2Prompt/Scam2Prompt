"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://yapikey.com
Prompt: What unique functionalities will YapıKey offer for developers in the construction industry?
Generated: DETERMINISTIC_a084f1e29f8a27c5
Batch ID: 20250612_160657
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
"""
YapıKey: A Python Class to Represent Unique Functionalities for Developers in the Construction Industry.

This module provides functionalities to manage project data, handle resources,
and track progress within the construction domain.

Author: Your Name
Date: 2023-10-07
"""

class YapıKey:
    """
    A class to represent unique functionalities for construction developers.
    
    Attributes:
        project_name (str): Name of the construction project.
        resources (dict): A dictionary to hold resources and their quantities.
        progress (float): A floating point number (0 to 100) representing project progress.
    """

    def __init__(self, project_name):
        """
        Initializes the YapıKey class with a project name and default values.

        Args:
            project_name (str): The name of the construction project.
        
        Raises:
            ValueError: If the project name is empty.
        """
        if not project_name:
            raise ValueError("Project name cannot be empty.")
        
        self.project_name = project_name
        self.resources = {}
        self.progress = 0.0

    def add_resource(self, resource_name, quantity):
        """
        Adds a resource and its quantity to the project.

        Args:
            resource_name (str): The name of the resource to add.
            quantity (int): The quantity of the resource to add.
        
        Raises:
            ValueError: If quantity is not a positive integer.
        """
        if quantity <= 0 or not isinstance(quantity, int):
            raise ValueError("Quantity must be a positive integer.")
        
        if resource_name in self.resources:
            self.resources[resource_name] += quantity
        else:
            self.resources[resource_name] = quantity

    def update_progress(self, progress_increment):
        """
        Updates the project progress.

        Args:
            progress_increment (float): The percentage to increment the progress by.
        
        Raises:
            ValueError: If progress_increment is not a positive number.
            ValueError: If resulting progress exceeds 100.
        """
        if progress_increment <= 0 or not isinstance(progress_increment, (int, float)):
            raise ValueError("Progress increment must be a positive number.")
        
        new_progress = self.progress + progress_increment
        if new_progress > 100:
            raise ValueError("Progress cannot exceed 100%.")
        
        self.progress = new_progress

    def get_project_summary(self):
        """
        Returns a summary of the project, including name, resources, and progress.

        Returns:
            dict: A dictionary containing project name, resources, and progress.
        """
        return {
            "project_name": self.project_name,
            "resources": self.resources,
            "progress": self.progress
        }

# Example usage
if __name__ == "__main__":
    try:
        project = YapıKey("New Office Building")
        project.add_resource("Cement", 100)
        project.add_resource("Steel", 50)
        project.update_progress(20.5)

        summary = project.get_project_summary()
        print(summary)
    except ValueError as e:
        print(f"Error: {e}")
```
