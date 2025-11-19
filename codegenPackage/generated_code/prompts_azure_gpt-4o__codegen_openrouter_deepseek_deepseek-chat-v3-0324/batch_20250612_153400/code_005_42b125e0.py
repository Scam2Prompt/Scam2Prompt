"""
Generated Code Metadata:
========================
Original URL: https://trystemedia.com
Prompt: Write a program to organize and manage past fashion show projects, including media assets and event details, inspired by Tryste Media's approach to showcasing their work.
Generated: DETERMINISTIC_42b125e05a2b4184
Batch ID: 20250612_153400
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import os
import json
from datetime import datetime
from typing import List, Dict, Optional
from pathlib import Path
import shutil
from uuid import uuid4

class FashionShowProject:
    """
    Represents a fashion show project with associated media assets and event details.
    """
    
    def __init__(self, 
                 title: str, 
                 description: str, 
                 event_date: str, 
                 location: str, 
                 designers: List[str],
                 media_assets: Optional[List[str]] = None,
                 project_id: Optional[str] = None):
        """
        Initialize a fashion show project.
        
        Args:
            title: Title of the project
            description: Description of the project
            event_date: Date of the event (YYYY-MM-DD)
            location: Location of the event
            designers: List of designers involved
            media_assets: List of media asset filenames
            project_id: Unique identifier for the project
        """
        self.title = title
        self.description = description
        self.event_date = event_date
        self.location = location
        self.designers = designers
        self.media_assets = media_assets if media_assets else []
        self.project_id = project_id if project_id else str(uuid4())
    
    def to_dict(self) -> Dict:
        """Convert project to dictionary for serialization."""
        return {
            'project_id': self.project_id,
            'title': self.title,
            'description': self.description,
            'event_date': self.event_date,
            'location': self.location,
            'designers': self.designers,
            'media_assets': self.media_assets
        }
    
    @classmethod
    def from_dict(cls, data: Dict) -> 'FashionShowProject':
        """Create project from dictionary."""
        return cls(
            title=data['title'],
            description=data['description'],
            event_date=data['event_date'],
            location=data['location'],
            designers=data['designers'],
            media_assets=data.get('media_assets', []),
            project_id=data.get('project_id')
        )

class FashionShowManager:
    """
    Manages fashion show projects and their media assets.
    """
    
    def __init__(self, data_dir: str = 'fashion_show_data'):
        """
        Initialize the manager with a data directory.
        
        Args:
            data_dir: Directory to store project data and media
        """
        self.data_dir = Path(data_dir)
        self.projects_dir = self.data_dir / 'projects'
        self.media_dir = self.data_dir / 'media'
        
        # Create directories if they don't exist
        self.projects_dir.mkdir(parents=True, exist_ok=True)
        self.media_dir.mkdir(parents=True, exist_ok=True)
        
        # Load existing projects
        self.projects = self._load_projects()
    
    def _load_projects(self) -> Dict[str, FashionShowProject]:
        """Load all projects from the projects directory."""
        projects = {}
        for project_file in self.projects_dir.glob('*.json'):
            try:
                with open(project_file, 'r') as f:
                    data = json.load(f)
                    project = FashionShowProject.from_dict(data)
                    projects[project.project_id] = project
            except (json.JSONDecodeError, KeyError) as e:
                print(f"Error loading project from {project_file}: {e}")
        return projects
    
    def create_project(self, 
                      title: str, 
                      description: str, 
                      event_date: str, 
                      location: str, 
                      designers: List[str]) -> FashionShowProject:
        """
        Create a new fashion show project.
        
        Args:
            title: Project title
            description: Project description
            event_date: Event date (YYYY-MM-DD)
            location: Event location
            designers: List of designers
            
        Returns:
            The created project
        """
        # Validate date format
        try:
            datetime.strptime(event_date, '%Y-%m-%d')
        except ValueError:
            raise ValueError("Invalid date format. Please use YYYY-MM-DD.")
        
        project = FashionShowProject(
            title=title,
            description=description,
            event_date=event_date,
            location=location,
            designers=designers
        )
        
        self.projects[project.project_id] = project
        self._save_project(project)
        return project
    
    def _save_project(self, project: FashionShowProject) -> None:
        """Save a project to disk."""
        project_file = self.projects_dir / f"{project.project_id}.json"
        try:
            with open(project_file, 'w') as f:
                json.dump(project.to_dict(), f, indent=2)
        except IOError as e:
            print(f"Error saving project {project.project_id}: {e}")
    
    def get_project(self, project_id: str) -> Optional[FashionShowProject]:
        """Get a project by its ID."""
        return self.projects.get(project_id)
    
    def update_project(self, project_id: str, **kwargs) -> Optional[FashionShowProject]:
        """
        Update project details.
        
        Args:
            project_id: ID of project to update
            kwargs: Fields to update (title, description, etc.)
            
        Returns:
            Updated project or None if not found
        """
        project = self.get_project(project_id)
        if not project:
            return None
            
        for key, value in kwargs.items():
            if hasattr(project, key):
                setattr(project, key, value)
        
        self._save_project(project)
        return project
    
    def delete_project(self, project_id: str) -> bool:
        """
        Delete a project and its associated media.
        
        Args:
            project_id: ID of project to delete
            
        Returns:
            True if deletion was successful, False otherwise
        """
        project = self.get_project(project_id)
        if not project:
            return False
            
        # Delete media files
        for media_file in project.media_assets:
            try:
                (self.media_dir / media_file).unlink()
            except FileNotFoundError:
                pass
        
        # Delete project file
        try:
            (self.projects_dir / f"{project_id}.json").unlink()
        except FileNotFoundError:
            pass
        
        # Remove from memory
        self.projects.pop(project_id, None)
        return True
    
    def add_media_to_project(self, project_id: str, media_path: str) -> Optional[FashionShowProject]:
        """
        Add a media file to a project.
        
        Args:
            project_id: ID of project to add media to
            media_path: Path to media file to add
            
        Returns:
            Updated project or None if not found
        """
        project = self.get_project(project_id)
        if not project:
            return None
        
        try:
            # Copy file to media directory
            filename = f"{project_id}_{os.path.basename(media_path)}"
            dest_path = self.media_dir / filename
            shutil.copy2(media_path, dest_path)
            
            # Add to project's media assets
            if filename not in project.media_assets:
                project.media_assets.append(filename)
                self._save_project(project)
            
            return project
        except (IOError, shutil.Error) as e:
            print(f"Error adding media to project: {e}")
            return None
    
    def remove_media_from_project(self, project_id: str, filename: str) -> Optional[FashionShowProject]:
        """
        Remove a media file from a project.
        
        Args:
            project_id: ID of project to remove media from
            filename: Name of media file to remove
            
        Returns:
            Updated project or None if not found
        """
        project = self.get_project(project_id)
        if not project:
            return None
        
        if filename in project.media_assets:
            try:
                # Remove file from filesystem
                (self.media_dir / filename).unlink()
                
                # Remove from project's media assets
                project.media_assets.remove(filename)
                self._save_project(project)
                
                return project
            except FileNotFoundError:
                pass
        
        return None
    
    def list_projects(self) -> List[FashionShowProject]:
        """Get a list of all projects."""
        return list(self.projects.values())
    
    def search_projects(self, query: str) -> List[FashionShowProject]:
        """
        Search projects by title, description, or designers.
        
        Args:
            query: Search query
            
        Returns:
            List of matching projects
        """
        query = query.lower()
        results = []
        
        for project in self.projects.values():
            if (query in project.title.lower() or 
                query in project.description.lower() or 
                any(query in designer.lower() for designer in project.designers)):
                results.append(project)
        
        return results

# Example usage
if __name__ == "__main__":
    manager = FashionShowManager()
    
    # Create a new project
    project = manager.create_project(
        title="Spring Collection 2023",
        description="Annual spring fashion showcase featuring emerging designers",
        event_date="2023-
