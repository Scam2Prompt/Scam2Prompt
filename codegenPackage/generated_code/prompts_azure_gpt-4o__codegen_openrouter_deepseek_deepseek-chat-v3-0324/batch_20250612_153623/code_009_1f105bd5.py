"""
Generated Code Metadata:
========================
Original URL: https://thephantomnetwork.net
Prompt: Generate a script to analyze and categorize creative projects, such as those described on "The Phantom Network," including video edits, logos, and gaming-related posts.
Generated: DETERMINISTIC_1f105bd575aaf892
Batch ID: 20250612_153623
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
from typing import Dict, List, Optional, Union
from enum import Enum
import datetime
import logging

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
)
logger = logging.getLogger(__name__)

class ProjectCategory(Enum):
    VIDEO_EDIT = "Video Edit"
    LOGO = "Logo"
    GAMING = "Gaming"
    OTHER = "Other"

class Project:
    def __init__(
        self,
        title: str,
        description: str,
        tags: List[str],
        creation_date: datetime.datetime,
        category: Optional[ProjectCategory] = None
    ):
        self.title = title
        self.description = description
        self.tags = tags
        self.creation_date = creation_date
        self.category = category or self._categorize_project()

    def _categorize_project(self) -> ProjectCategory:
        """Categorize project based on title, description, and tags."""
        project_text = f"{self.title.lower()} {self.description.lower()} {' '.join(self.tags).lower()}"
        
        if any(keyword in project_text for keyword in ["video", "edit", "montage", "clip"]):
            return ProjectCategory.VIDEO_EDIT
        elif any(keyword in project_text for keyword in ["logo", "brand", "identity"]):
            return ProjectCategory.LOGO
        elif any(keyword in project_text for keyword in ["game", "gaming", "stream", "esports"]):
            return ProjectCategory.GAMING
        else:
            return ProjectCategory.OTHER

    def to_dict(self) -> Dict:
        """Convert project to dictionary for serialization."""
        return {
            "title": self.title,
            "description": self.description,
            "tags": self.tags,
            "creation_date": self.creation_date.isoformat(),
            "category": self.category.value
        }

class ProjectAnalyzer:
    def __init__(self):
        self.projects: List[Project] = []

    def add_project(self, project: Project) -> None:
        """Add a project to the analyzer."""
        self.projects.append(project)

    def load_projects_from_json(self, file_path: str) -> None:
        """Load projects from a JSON file."""
        try:
            with open(file_path, 'r', encoding='utf-8') as f:
                data = json.load(f)
                for project_data in data:
                    try:
                        project = Project(
                            title=project_data.get("title", ""),
                            description=project_data.get("description", ""),
                            tags=project_data.get("tags", []),
                            creation_date=datetime.datetime.fromisoformat(
                                project_data.get("creation_date", datetime.datetime.now().isoformat())
                            )
                        )
                        self.add_project(project)
                    except Exception as e:
                        logger.error(f"Error loading project: {e}")
        except FileNotFoundError:
            logger.error(f"File not found: {file_path}")
        except json.JSONDecodeError:
            logger.error(f"Invalid JSON in file: {file_path}")
        except Exception as e:
            logger.error(f"Unexpected error loading projects: {e}")

    def save_projects_to_json(self, file_path: str) -> None:
        """Save projects to a JSON file."""
        try:
            with open(file_path, 'w', encoding='utf-8') as f:
                json.dump(
                    [project.to_dict() for project in self.projects],
                    f,
                    indent=2,
                    ensure_ascii=False
                )
            logger.info(f"Projects saved to {file_path}")
        except Exception as e:
            logger.error(f"Error saving projects: {e}")

    def get_projects_by_category(self, category: ProjectCategory) -> List[Project]:
        """Get all projects in a specific category."""
        return [project for project in self.projects if project.category == category]

    def get_category_stats(self) -> Dict[ProjectCategory, int]:
        """Get statistics of projects by category."""
        stats = {category: 0 for category in ProjectCategory}
        for project in self.projects:
            stats[project.category] += 1
        return stats

    def get_recent_projects(self, days: int = 30) -> List[Project]:
        """Get projects created within the last N days."""
        cutoff_date = datetime.datetime.now() - datetime.timedelta(days=days)
        return [
            project for project in self.projects
            if project.creation_date >= cutoff_date
        ]

def main():
    analyzer = ProjectAnalyzer()
    
    # Example usage
    try:
        # Load projects from file if exists
        if os.path.exists("projects.json"):
            analyzer.load_projects_from_json("projects.json")
        
        # Add a new project
        new_project = Project(
            title="Awesome Gaming Montage",
            description="A compilation of my best gaming moments",
            tags=["gaming", "montage", "FPS"],
            creation_date=datetime.datetime.now()
        )
        analyzer.add_project(new_project)
        
        # Save all projects
        analyzer.save_projects_to_json("projects.json")
        
        # Print statistics
        stats = analyzer.get_category_stats()
        print("Project Statistics:")
        for category, count in stats.items():
            print(f"{category.value}: {count}")
            
    except Exception as e:
        logger.error(f"Error in main execution: {e}")

if __name__ == "__main__":
    main()
```
