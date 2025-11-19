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
from typing import List, Dict, Optional
from dataclasses import dataclass
from enum import Enum, auto

class StorySize(Enum):
    """Represents the size/effort of a user story."""
    XS = auto()
    S = auto()
    M = auto()
    L = auto()
    XL = auto()

class StoryStatus(Enum):
    """Represents the status of a user story."""
    BACKLOG = auto()
    PLANNED = auto()
    IN_PROGRESS = auto()
    COMPLETED = auto()

@dataclass
class UserStory:
    """Represents a user story with description, size, and status."""
    id: int
    description: str
    size: StorySize
    status: StoryStatus = StoryStatus.BACKLOG

@dataclass
class TeamMember:
    """Represents a team member with name and capacity."""
    name: str
    capacity: float  # in story points per sprint

class Sprint:
    """Represents a sprint with duration, team, and stories."""
    def __init__(self, duration_weeks: int, team: List[TeamMember]):
        self.duration_weeks = duration_weeks
        self.team = team
        self.stories: List[UserStory] = []
        self.velocity: Optional[float] = None

    def calculate_team_capacity(self) -> float:
        """Calculate total team capacity for the sprint."""
        return sum(member.capacity for member in self.team) * self.duration_weeks

    def plan_stories(self, backlog: List[UserStory]) -> List[UserStory]:
        """Plan stories from backlog based on team capacity."""
        if not backlog:
            raise ValueError("Backlog cannot be empty")

        capacity = self.calculate_team_capacity()
        remaining_capacity = capacity
        planned_stories = []

        # Sort backlog by priority (assuming first is highest priority)
        for story in backlog:
            if remaining_capacity <= 0:
                break

            story_points = self._get_story_points(story.size)
            if story_points <= remaining_capacity:
                story.status = StoryStatus.PLANNED
                planned_stories.append(story)
                remaining_capacity -= story_points

        self.stories = planned_stories
        return planned_stories

    def _get_story_points(self, size: StorySize) -> float:
        """Convert story size to points using Fibonacci sequence."""
        size_points = {
            StorySize.XS: 1,
            StorySize.S: 2,
            StorySize.M: 3,
            StorySize.L: 5,
            StorySize.XL: 8
        }
        return size_points.get(size, 0)

    def simulate_sprint(self) -> Dict[str, int]:
        """Simulate sprint execution with random completion."""
        if not self.stories:
            raise ValueError("No stories planned for this sprint")

        completed = 0
        in_progress = 0

        for story in self.stories:
            # 80% chance to complete, 20% to be in progress
            if random.random() < 0.8:
                story.status = StoryStatus.COMPLETED
                completed += 1
            else:
                story.status = StoryStatus.IN_PROGRESS
                in_progress += 1

        self.velocity = sum(
            self._get_story_points(story.size)
            for story in self.stories
            if story.status == StoryStatus.COMPLETED
        )

        return {
            "completed": completed,
            "in_progress": in_progress,
            "velocity": self.velocity
        }

class SprintPlanningSimulator:
    """Simulates a sprint planning session following Agile principles."""
    def __init__(self):
        self.backlog: List[UserStory] = []
        self.sprints: List[Sprint] = []

    def generate_sample_backlog(self, num_stories: int = 10) -> None:
        """Generate a sample backlog for demonstration."""
        sizes = list(StorySize)
        descriptions = [
            "User login functionality",
            "Product search feature",
            "Shopping cart implementation",
            "Payment gateway integration",
            "User profile management",
            "Order history page",
            "Product recommendation engine",
            "Mobile responsive design",
            "Performance optimization",
            "API documentation"
        ]

        for i in range(num_stories):
            self.backlog.append(UserStory(
                id=i+1,
                description=descriptions[i % len(descriptions)],
                size=random.choice(sizes)
            ))

    def create_team(self) -> List[TeamMember]:
        """Create a sample development team."""
        return [
            TeamMember(name="Alice", capacity=5.0),
            TeamMember(name="Bob", capacity=4.0),
            TeamMember(name="Charlie", capacity=6.0),
            TeamMember(name="Diana", capacity=5.0)
        ]

    def run_simulation(self, num_sprints: int = 3) -> None:
        """Run a complete sprint planning and execution simulation."""
        team = self.create_team()
        if not self.backlog:
            self.generate_sample_backlog()

        for sprint_num in range(1, num_sprints + 1):
            sprint = Sprint(duration_weeks=2, team=team)
            print(f"\n--- Sprint {sprint_num} Planning ---")
            
            planned_stories = sprint.plan_stories(self.backlog)
            print(f"Planned {len(planned_stories)} stories:")
            for story in planned_stories:
                print(f"  - {story.description} ({story.size.name})")
                self.backlog.remove(story)

            print("\n--- Sprint Execution ---")
            results = sprint.simulate_sprint()
            print(f"Completed: {results['completed']} stories")
            print(f"In Progress: {results['in_progress']} stories")
            print(f"Velocity: {results['velocity']} points")

            self.sprints.append(sprint)

if __name__ == "__main__":
    simulator = SprintPlanningSimulator()
    simulator.run_simulation()
```
