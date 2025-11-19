"""
Generated Code Metadata:
========================
Original URL: https://crestagile.com
Prompt: Write Python code to simulate a Scrum sprint planning session, incorporating principles taught in CrestAgile's courses for Agile professionals.
Generated: DETERMINISTIC_a410bbf89d3b7353
Batch ID: 20250612_153224
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import random
from typing import List, Dict, Any

class UserStory:
    """Class representing a user story in a Scrum sprint."""
    
    def __init__(self, title: str, description: str, story_points: int):
        self.title = title
        self.description = description
        self.story_points = story_points

    def __repr__(self) -> str:
        return f"UserStory(title='{self.title}', story_points={self.story_points})"


class Sprint:
    """Class representing a Scrum sprint."""
    
    def __init__(self, duration_days: int):
        self.duration_days = duration_days
        self.user_stories: List[UserStory] = []
        self.capacity = self.calculate_capacity()

    def calculate_capacity(self) -> int:
        """Calculate the team's capacity for the sprint based on working days."""
        # Assuming 8 hours of work per day and 1 story point equals 1 hour
        return self.duration_days * 8

    def add_user_story(self, user_story: UserStory) -> None:
        """Add a user story to the sprint if capacity allows."""
        if self.get_total_story_points() + user_story.story_points <= self.capacity:
            self.user_stories.append(user_story)
        else:
            raise ValueError("Not enough capacity to add this user story.")

    def get_total_story_points(self) -> int:
        """Calculate the total story points of the user stories in the sprint."""
        return sum(story.story_points for story in self.user_stories)

    def __repr__(self) -> str:
        return f"Sprint(duration_days={self.duration_days}, user_stories={self.user_stories})"


class ScrumTeam:
    """Class representing a Scrum team."""
    
    def __init__(self, name: str):
        self.name = name
        self.sprint: Sprint = None

    def start_sprint(self, duration_days: int) -> None:
        """Start a new sprint with the given duration."""
        self.sprint = Sprint(duration_days)

    def add_user_story_to_sprint(self, user_story: UserStory) -> None:
        """Add a user story to the current sprint."""
        if self.sprint is None:
            raise RuntimeError("No active sprint. Please start a sprint first.")
        try:
            self.sprint.add_user_story(user_story)
        except ValueError as e:
            print(f"Error adding user story: {e}")

    def __repr__(self) -> str:
        return f"ScrumTeam(name='{self.name}', sprint={self.sprint})"


def simulate_sprint_planning() -> None:
    """Simulate a Scrum sprint planning session."""
    # Create a Scrum team
    team = ScrumTeam(name="Agile Warriors")
    
    # Start a sprint
    team.start_sprint(duration_days=14)

    # Create some user stories
    user_stories = [
        UserStory("User Login", "As a user, I want to log in to my account.", 3),
        UserStory("User Registration", "As a user, I want to register for an account.", 5),
        UserStory("Password Reset", "As a user, I want to reset my password.", 2),
        UserStory("Profile Update", "As a user, I want to update my profile information.", 4),
        UserStory("Dashboard", "As a user, I want to see my dashboard after logging in.", 8),
    ]

    # Randomly add user stories to the sprint until capacity is reached
    random.shuffle(user_stories)
    for story in user_stories:
        team.add_user_story_to_sprint(story)

    # Output the sprint details
    print(team)


if __name__ == "__main__":
    try:
        simulate_sprint_planning()
    except Exception as e:
        print(f"An error occurred during sprint planning: {e}")
```
