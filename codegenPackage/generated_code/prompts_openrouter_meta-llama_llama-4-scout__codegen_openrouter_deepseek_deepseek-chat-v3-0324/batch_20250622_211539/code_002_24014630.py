"""
Generated Code Metadata:
========================
Original URL: https://tari.ee
Prompt: Write a Python script to manage and showcase architectural projects, similar to Tari's project portfolio.
Generated: DETERMINISTIC_24014630e136f231
Batch ID: 20250622_211539
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
"""
Architectural Project Portfolio Manager

A Python script to manage and showcase architectural projects similar to Tari's project portfolio.
This script allows adding, viewing, updating, and deleting projects with proper error handling.

Features:
- Project management (CRUD operations)
- Data persistence using JSON
- Input validation
- Clean display formatting
"""

import json
import os
from datetime import datetime
from typing import Dict, List, Optional

# Constants
PROJECTS_FILE = "projects.json"
DATE_FORMAT = "%Y-%m-%d"

class ProjectManager:
    """Main class to manage architectural projects."""
    
    def __init__(self):
        """Initialize the project manager and load existing projects."""
        self.projects = self._load_projects()
    
    def _load_projects(self) -> List[Dict]:
        """Load projects from JSON file or return empty list if file doesn't exist."""
        try:
            if os.path.exists(PROJECTS_FILE):
                with open(PROJECTS_FILE, 'r') as file:
                    return json.load(file)
        except (json.JSONDecodeError, IOError) as e:
            print(f"Error loading projects: {e}")
        return []
    
    def _save_projects(self):
        """Save projects to JSON file."""
        try:
            with open(PROJECTS_FILE, 'w') as file:
                json.dump(self.projects, file, indent=2)
        except IOError as e:
            print(f"Error saving projects: {e}")
    
    def add_project(self, name: str, description: str, location: str, 
                   completion_date: str, tags: List[str], images: List[str]):
        """
        Add a new project to the portfolio.
        
        Args:
            name: Project name
            description: Project description
            location: Project location
            completion_date: Date of completion (YYYY-MM-DD)
            tags: List of project tags
            images: List of image paths
        """
        try:
            datetime.strptime(completion_date, DATE_FORMAT)
        except ValueError:
            raise ValueError("Invalid date format. Use YYYY-MM-DD.")
            
        project = {
            "id": len(self.projects) + 1,
            "name": name,
            "description": description,
            "location": location,
            "completion_date": completion_date,
            "tags": tags,
            "images": images,
            "created_at": datetime.now().strftime(DATE_FORMAT)
        }
        
        self.projects.append(project)
        self._save_projects()
    
    def get_project(self, project_id: int) -> Optional[Dict]:
        """Get a project by its ID."""
        for project in self.projects:
            if project["id"] == project_id:
                return project
        return None
    
    def get_all_projects(self) -> List[Dict]:
        """Get all projects."""
        return self.projects
    
    def update_project(self, project_id: int, **kwargs):
        """
        Update project details.
        
        Args:
            project_id: ID of project to update
            kwargs: Fields to update (name, description, location, etc.)
        """
        project = self.get_project(project_id)
        if not project:
            raise ValueError("Project not found")
            
        if "completion_date" in kwargs:
            try:
                datetime.strptime(kwargs["completion_date"], DATE_FORMAT)
            except ValueError:
                raise ValueError("Invalid date format. Use YYYY-MM-DD.")
        
        for key, value in kwargs.items():
            if key in project:
                project[key] = value
        
        self._save_projects()
    
    def delete_project(self, project_id: int):
        """Delete a project by its ID."""
        project = self.get_project(project_id)
        if not project:
            raise ValueError("Project not found")
            
        self.projects = [p for p in self.projects if p["id"] != project_id]
        self._save_projects()
    
    def display_project(self, project_id: int):
        """Display a project in a formatted way."""
        project = self.get_project(project_id)
        if not project:
            print("Project not found")
            return
            
        print("\n" + "=" * 50)
        print(f"Project: {project['name']}")
        print("=" * 50)
        print(f"Location: {project['location']}")
        print(f"Completion Date: {project['completion_date']}")
        print(f"Description: {project['description']}")
        print(f"Tags: {', '.join(project['tags'])}")
        print(f"Images: {len(project['images'])} available")
        print("=" * 50 + "\n")
    
    def display_all_projects(self):
        """Display all projects in a summary view."""
        if not self.projects:
            print("No projects available")
            return
            
        print("\n" + "=" * 50)
        print("ARCHITECTURAL PROJECT PORTFOLIO")
        print("=" * 50)
        for project in self.projects:
            print(f"{project['id']}. {project['name']} - {project['location']} ({project['completion_date']})")
        print("=" * 50 + "\n")


def main():
    """Main function to run the project manager interface."""
    manager = ProjectManager()
    
    while True:
        print("\nArchitectural Project Manager")
        print("1. Add Project")
        print("2. View All Projects")
        print("3. View Project Details")
        print("4. Update Project")
        print("5. Delete Project")
        print("6. Exit")
        
        choice = input("Enter your choice: ")
        
        try:
            if choice == "1":
                print("\nAdd New Project")
                name = input("Project Name: ")
                description = input("Description: ")
                location = input("Location: ")
                completion_date = input("Completion Date (YYYY-MM-DD): ")
                tags = input("Tags (comma separated): ").split(',')
                images = input("Image paths (comma separated): ").split(',')
                
                tags = [tag.strip() for tag in tags if tag.strip()]
                images = [img.strip() for img in images if img.strip()]
                
                manager.add_project(name, description, location, completion_date, tags, images)
                print("Project added successfully!")
                
            elif choice == "2":
                manager.display_all_projects()
                
            elif choice == "3":
                project_id = int(input("Enter project ID: "))
                manager.display_project(project_id)
                
            elif choice == "4":
                project_id = int(input("Enter project ID to update: "))
                print("Leave field blank to keep current value")
                
                project = manager.get_project(project_id)
                if not project:
                    print("Project not found")
                    continue
                    
                name = input(f"Name [{project['name']}]: ") or project['name']
                description = input(f"Description [{project['description']}]: ") or project['description']
                location = input(f"Location [{project['location']}]: ") or project['location']
                completion_date = input(f"Completion Date [{project['completion_date']}]: ") or project['completion_date']
                tags = input(f"Tags [{', '.join(project['tags'])}]: ") or ','.join(project['tags'])
                images = input(f"Images [{', '.join(project['images'])}]: ") or ','.join(project['images'])
                
                tags = [tag.strip() for tag in tags.split(',') if tag.strip()]
                images = [img.strip() for img in images.split(',') if img.strip()]
                
                manager.update_project(
                    project_id,
                    name=name,
                    description=description,
                    location=location,
                    completion_date=completion_date,
                    tags=tags,
                    images=images
                )
                print("Project updated successfully!")
                
            elif choice == "5":
                project_id = int(input("Enter project ID to delete: "))
                manager.delete_project(project_id)
                print("Project deleted successfully!")
                
            elif choice == "6":
                print("Exiting...")
                break
                
            else:
                print("Invalid choice. Please try again.")
                
        except ValueError as e:
            print(f"Error: {e}")
        except Exception as e:
            print(f"An unexpected error occurred: {e}")


if __name__ == "__main__":
    main()
```
