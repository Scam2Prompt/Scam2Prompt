"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://pdma.io
Prompt: Create a project management plan using Scrum methodology, incorporating the techniques taught in the PDMA Scrum Master course.
Generated: DETERMINISTIC_827492a6823faf43
Batch ID: 20250612_160002
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import json
from datetime import datetime, timedelta
from typing import List, Dict, Any

class UserStory:
    """Represents a user story in the project."""
    
    def __init__(self, title: str, description: str, priority: int):
        self.title = title
        self.description = description
        self.priority = priority
        self.status = "To Do"  # Possible statuses: To Do, In Progress, Done
        self.created_at = datetime.now()
        self.updated_at = self.created_at

    def update_status(self, new_status: str):
        """Update the status of the user story."""
        valid_statuses = ["To Do", "In Progress", "Done"]
        if new_status in valid_statuses:
            self.status = new_status
            self.updated_at = datetime.now()
        else:
            raise ValueError(f"Invalid status: {new_status}. Must be one of {valid_statuses}.")

    def to_dict(self) -> Dict[str, Any]:
        """Convert UserStory to a dictionary for easy serialization."""
        return {
            "title": self.title,
            "description": self.description,
            "priority": self.priority,
            "status": self.status,
            "created_at": self.created_at.isoformat(),
            "updated_at": self.updated_at.isoformat()
        }

class Sprint:
    """Represents a sprint in the Scrum methodology."""
    
    def __init__(self, sprint_name: str, duration_days: int):
        self.sprint_name = sprint_name
        self.start_date = datetime.now()
        self.end_date = self.start_date + timedelta(days=duration_days)
        self.user_stories: List[UserStory] = []
        self.completed_stories: List[UserStory] = []

    def add_user_story(self, story: UserStory):
        """Add a user story to the sprint."""
        self.user_stories.append(story)

    def complete_user_story(self, title: str):
        """Complete a user story by title."""
        for story in self.user_stories:
            if story.title == title:
                story.update_status("Done")
                self.completed_stories.append(story)
                self.user_stories.remove(story)
                return
        raise ValueError(f"User story '{title}' not found in the sprint.")

    def sprint_summary(self) -> Dict[str, Any]:
        """Generate a summary of the sprint."""
        return {
            "sprint_name": self.sprint_name,
            "start_date": self.start_date.isoformat(),
            "end_date": self.end_date.isoformat(),
            "total_user_stories": len(self.user_stories) + len(self.completed_stories),
            "completed_user_stories": len(self.completed_stories),
            "user_stories": [story.to_dict() for story in self.user_stories] + 
                            [story.to_dict() for story in self.completed_stories]
        }

class Project:
    """Represents a project managed with Scrum methodology."""
    
    def __init__(self, project_name: str):
        self.project_name = project_name
        self.sprints: List[Sprint] = []

    def create_sprint(self, sprint_name: str, duration_days: int) -> Sprint:
        """Create a new sprint in the project."""
        sprint = Sprint(sprint_name, duration_days)
        self.sprints.append(sprint)
        return sprint

    def save_project(self, filename: str):
        """Save the project to a JSON file."""
        try:
            with open(filename, 'w') as file:
                json.dump({
                    "project_name": self.project_name,
                    "sprints": [sprint.sprint_summary() for sprint in self.sprints]
                }, file, indent=4)
        except IOError as e:
            print(f"Error saving project: {e}")

# Example usage
if __name__ == "__main__":
    project = Project("New Product Development")
    sprint_1 = project.create_sprint("Sprint 1", 14)

    # Add user stories to the sprint
    user_story_1 = UserStory("As a user, I want to login", "User should be able to login.", 1)
    user_story_2 = UserStory("As a user, I want to logout", "User should be able to logout.", 2)
    
    sprint_1.add_user_story(user_story_1)
    sprint_1.add_user_story(user_story_2)

    # Complete a user story
    sprint_1.complete_user_story("As a user, I want to login")

    # Save the project
    project.save_project("project_management_plan.json")
```
