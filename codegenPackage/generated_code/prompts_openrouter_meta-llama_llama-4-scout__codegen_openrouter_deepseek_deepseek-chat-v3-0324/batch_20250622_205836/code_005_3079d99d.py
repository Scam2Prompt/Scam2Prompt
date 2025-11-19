"""
Generated Code Metadata:
========================
Original URL: https://alphaonlineservices.com
Prompt: "Develop a web development project plan for a custom website using agile methodologies, prioritizing user experience and functionality, as per Alpha Online Services' web development services."
Generated: DETERMINISTIC_3079d99dbcdd627d
Batch ID: 20250622_205836
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
"""
Web Development Project Plan for Alpha Online Services
Agile-based project plan for custom website development
"""

from datetime import datetime, timedelta
from typing import List, Dict, Optional

class UserStory:
    """Represents a user story in agile development"""
    def __init__(self, id: str, title: str, description: str, priority: int, 
                 story_points: int, acceptance_criteria: List[str]):
        self.id = id
        self.title = title
        self.description = description
        self.priority = priority
        self.story_points = story_points
        self.acceptance_criteria = acceptance_criteria
        self.status = "Backlog"
        
    def update_status(self, new_status: str) -> None:
        """Update the status of the user story"""
        valid_statuses = ["Backlog", "To Do", "In Progress", "Review", "Done"]
        if new_status not in valid_statuses:
            raise ValueError(f"Invalid status. Must be one of: {valid_statuses}")
        self.status = new_status

class Sprint:
    """Represents an agile sprint"""
    def __init__(self, id: int, start_date: datetime, end_date: datetime):
        self.id = id
        self.start_date = start_date
        self.end_date = end_date
        self.user_stories: List[UserStory] = []
        
    def add_user_story(self, user_story: UserStory) -> None:
        """Add a user story to the sprint"""
        self.user_stories.append(user_story)
        
    def remove_user_story(self, user_story_id: str) -> None:
        """Remove a user story from the sprint"""
        self.user_stories = [us for us in self.user_stories if us.id != user_story_id]
        
    def total_story_points(self) -> int:
        """Calculate total story points in the sprint"""
        return sum(us.story_points for us in self.user_stories)

class Project:
    """Main project class for managing the web development"""
    def __init__(self, name: str, description: str, start_date: datetime):
        self.name = name
        self.description = description
        self.start_date = start_date
        self.sprints: List[Sprint] = []
        self.user_stories: Dict[str, UserStory] = {}
        self.current_sprint: Optional[Sprint] = None
        
    def create_sprint(self, duration_days: int = 14) -> Sprint:
        """Create a new sprint"""
        sprint_id = len(self.sprints) + 1
        start_date = self._calculate_next_sprint_start()
        end_date = start_date + timedelta(days=duration_days)
        sprint = Sprint(sprint_id, start_date, end_date)
        self.sprints.append(sprint)
        return sprint
        
    def _calculate_next_sprint_start(self) -> datetime:
        """Calculate start date for next sprint"""
        if not self.sprints:
            return self.start_date
        return self.sprints[-1].end_date + timedelta(days=1)
        
    def add_user_story(self, user_story: UserStory) -> None:
        """Add a user story to the project backlog"""
        if user_story.id in self.user_stories:
            raise ValueError(f"User story with ID {user_story.id} already exists")
        self.user_stories[user_story.id] = user_story
        
    def plan_sprint(self, sprint: Sprint, user_story_ids: List[str]) -> None:
        """Plan user stories for a sprint"""
        for us_id in user_story_ids:
            if us_id not in self.user_stories:
                raise ValueError(f"User story {us_id} not found")
            sprint.add_user_story(self.user_stories[us_id])
            
    def start_sprint(self, sprint_id: int) -> None:
        """Mark a sprint as current"""
        sprint = next((s for s in self.sprints if s.id == sprint_id), None)
        if not sprint:
            raise ValueError(f"Sprint with ID {sprint_id} not found")
        self.current_sprint = sprint
        
    def complete_sprint(self) -> None:
        """Complete the current sprint"""
        if not self.current_sprint:
            raise ValueError("No active sprint to complete")
        self.current_sprint = None
        
    def generate_report(self) -> Dict:
        """Generate project status report"""
        completed_stories = sum(1 for us in self.user_stories.values() if us.status == "Done")
        in_progress_stories = sum(1 for us in self.user_stories.values() if us.status == "In Progress")
        
        return {
            "project_name": self.name,
            "total_user_stories": len(self.user_stories),
            "completed_stories": completed_stories,
            "in_progress_stories": in_progress_stories,
            "current_sprint": self.current_sprint.id if self.current_sprint else None,
            "total_sprints": len(self.sprints)
        }

# Example usage
if __name__ == "__main__":
    # Initialize project
    project = Project(
        name="Alpha Online Services Website",
        description="Custom website development with focus on UX and functionality",
        start_date=datetime.now()
    )
    
    # Create user stories
    us1 = UserStory(
        id="US-001",
        title="Homepage Design",
        description="As a user, I want an attractive homepage",
        priority=1,
        story_points=5,
        acceptance_criteria=["Mobile responsive", "Loads under 2s"]
    )
    
    us2 = UserStory(
        id="US-002",
        title="Contact Form",
        description="As a user, I want to contact the company",
        priority=2,
        story_points=3,
        acceptance_criteria=["Form validation", "Success message"]
    )
    
    project.add_user_story(us1)
    project.add_user_story(us2)
    
    # Plan first sprint
    sprint1 = project.create_sprint()
    project.plan_sprint(sprint1, ["US-001", "US-002"])
    project.start_sprint(sprint1.id)
    
    # Update story status
    us1.update_status("In Progress")
    us2.update_status("Done")
    
    # Generate report
    print(project.generate_report())
```
