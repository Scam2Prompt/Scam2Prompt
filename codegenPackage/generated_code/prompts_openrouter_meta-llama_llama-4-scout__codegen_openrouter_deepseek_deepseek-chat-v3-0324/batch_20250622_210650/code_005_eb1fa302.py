"""
Generated Code Metadata:
========================
Original URL: https://canatechinstitute.ca
Prompt: "What are the benefits of using Scrum and Agile methodologies in software development, and how can they be applied in a real-world project?"
Generated: DETERMINISTIC_eb1fa302def6198a
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
This script demonstrates the application of Scrum and Agile methodologies 
in a software development project through a simulated project management system.
"""

from datetime import datetime, timedelta
from typing import List, Dict, Optional
import random

class UserStory:
    """Represents a user story in Agile development."""
    
    def __init__(self, id: int, description: str, points: int):
        self.id = id
        self.description = description
        self.points = points
        self.status = "Backlog"  # Backlog, To Do, In Progress, Done
        self.sprint_assigned: Optional[int] = None
    
    def update_status(self, new_status: str) -> None:
        """Update the status of the user story."""
        valid_statuses = ["Backlog", "To Do", "In Progress", "Done"]
        if new_status not in valid_statuses:
            raise ValueError(f"Invalid status. Must be one of {valid_statuses}")
        self.status = new_status
    
    def assign_to_sprint(self, sprint_id: int) -> None:
        """Assign the user story to a specific sprint."""
        self.sprint_assigned = sprint_id
        self.status = "To Do"
    
    def __str__(self) -> str:
        return f"US-{self.id}: {self.description} ({self.points} points) [{self.status}]"

class Sprint:
    """Represents a sprint in Scrum methodology."""
    
    def __init__(self, id: int, start_date: datetime, duration_days: int):
        self.id = id
        self.start_date = start_date
        self.duration_days = duration_days
        self.user_stories: List[UserStory] = []
        self.velocity: int = 0
    
    def add_user_story(self, user_story: UserStory) -> None:
        """Add a user story to the sprint."""
        if user_story.status != "To Do":
            raise ValueError("User story must be in 'To Do' status to be added to sprint")
        self.user_stories.append(user_story)
        self.velocity += user_story.points
    
    def complete_sprint(self) -> Dict[str, int]:
        """Complete the sprint and return metrics."""
        completed = sum(1 for us in self.user_stories if us.status == "Done")
        return {
            "total_stories": len(self.user_stories),
            "completed_stories": completed,
            "completion_percentage": int((completed / len(self.user_stories)) * 100),
            "velocity": self.velocity
        }
    
    def __str__(self) -> str:
        end_date = self.start_date + timedelta(days=self.duration_days)
        return f"Sprint {self.id} ({self.start_date.strftime('%Y-%m-%d')} to {end_date.strftime('%Y-%m-%d')})"

class ScrumProject:
    """Manages a software project using Scrum methodology."""
    
    def __init__(self, name: str):
        self.name = name
        self.product_backlog: List[UserStory] = []
        self.sprints: List[Sprint] = []
        self.current_sprint: Optional[Sprint] = None
        self.team_capacity = 20  # Default team capacity in story points
    
    def add_user_story(self, description: str, points: int) -> UserStory:
        """Add a new user story to the product backlog."""
        story_id = len(self.product_backlog) + 1
        user_story = UserStory(story_id, description, points)
        self.product_backlog.append(user_story)
        return user_story
    
    def plan_sprint(self, start_date: datetime, duration_days: int = 14) -> Sprint:
        """Plan a new sprint."""
        sprint_id = len(self.sprints) + 1
        sprint = Sprint(sprint_id, start_date, duration_days)
        self.sprints.append(sprint)
        self.current_sprint = sprint
        return sprint
    
    def select_stories_for_sprint(self) -> None:
        """Select user stories for the current sprint based on team capacity."""
        if not self.current_sprint:
            raise ValueError("No active sprint to plan")
        
        available_points = self.team_capacity
        selected_stories = []
        
        # Prioritize stories by sorting backlog (simple random prioritization for demo)
        prioritized_backlog = sorted(
            self.product_backlog,
            key=lambda x: random.random() if x.status == "Backlog" else float('inf')
        )
        
        for story in prioritized_backlog:
            if story.status == "Backlog" and story.points <= available_points:
                story.assign_to_sprint(self.current_sprint.id)
                self.current_sprint.add_user_story(story)
                available_points -= story.points
                selected_stories.append(story)
                
                if available_points <= 0:
                    break
        
        return selected_stories
    
    def run_daily_standup(self) -> Dict[str, List[str]]:
        """Simulate a daily standup meeting."""
        if not self.current_sprint:
            raise ValueError("No active sprint for standup")
        
        updates = {
            "completed": [],
            "working_on": [],
            "blockers": []
        }
        
        for story in self.current_sprint.user_stories:
            if story.status == "Done":
                updates["completed"].append(str(story))
            elif story.status == "In Progress":
                updates["working_on"].append(str(story))
                # Randomly generate blockers for demo purposes
                if random.random() < 0.2:  # 20% chance of blocker
                    updates["blockers"].append(f"Blocked on {story.description}")
        
        return updates
    
    def complete_sprint(self) -> Dict:
        """Complete the current sprint and return metrics."""
        if not self.current_sprint:
            raise ValueError("No active sprint to complete")
        
        # Randomly mark some stories as done for demo purposes
        for story in self.current_sprint.user_stories:
            if story.status in ["To Do", "In Progress"]:
                if random.random() < 0.7:  # 70% chance of completion
                    story.update_status("Done")
        
        metrics = self.current_sprint.complete_sprint()
        self.current_sprint = None
        return metrics
    
    def generate_burndown_chart(self, sprint_id: int) -> Dict[int, int]:
        """Generate a simple burndown chart for a sprint."""
        sprint = next((s for s in self.sprints if s.id == sprint_id), None)
        if not sprint:
            raise ValueError(f"Sprint {sprint_id} not found")
        
        total_points = sprint.velocity
        days = sprint.duration_days
        remaining_points = total_points
        
        chart = {0: total_points}  # Day 0 is start of sprint
        
        # Simulate linear burndown for demo
        daily_burn = total_points / days
        
        for day in range(1, days + 1):
            remaining_points = max(0, remaining_points - daily_burn)
            chart[day] = int(remaining_points)
        
        return chart
    
    def __str__(self) -> str:
        return f"Scrum Project: {self.name}"

# Example usage
if __name__ == "__main__":
    # Create a new project
    project = ScrumProject("E-Commerce Platform")
    
    # Add user stories to the backlog
    stories = [
        ("As a user, I want to browse products", 3),
        ("As a user, I want to add items to cart", 5),
        ("As a user, I want to checkout", 8),
        ("As a user, I want to view order history", 5),
        ("As an admin, I want to manage products", 8),
        ("As an admin, I want to view reports", 5),
    ]
    
    for desc, points in stories:
        project.add_user_story(desc, points)
    
    # Plan a sprint
    sprint_start = datetime.now()
    sprint = project.plan_sprint(sprint_start)
    
    # Select stories for the sprint
    selected = project.select_stories_for_sprint()
    print(f"\nSelected {len(selected)} stories for Sprint {sprint.id}:")
    for story in selected:
        print(f" - {story}")
    
    # Simulate daily standups
    print("\nDaily Standup Updates:")
    for day in range(1, 4):  # Simulate 3 days
        print(f"\nDay {day}:")
        updates = project.run_daily_standup()
        print("Completed:", updates["completed"])
        print("Working on:", updates["working_on"])
        print("Blockers:", updates["blockers"] or "None")
    
    # Complete the sprint
    metrics = project.complete_sprint()
    print("\nSprint Metrics:")
    print(f"Stories completed: {metrics['completed_stories']}/{metrics['total_stories']} ({metrics['completion_percentage']}%)")
    print(f"Velocity: {metrics['velocity']} points")
    
    # Generate burndown chart
    print("\nBurndown Chart:")
    chart =
