"""
Generated Code Metadata:
========================
Original URL: https://pdma.io
Prompt: Generate a project plan for a product management initiative that incorporates Scrum Master principles and practices, as taught in the PDMA Technologies' Scrum Master course.
Generated: DETERMINISTIC_0ccf352b6d85f20a
Batch ID: 20250622_211656
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
"""
Product Management Initiative Project Plan with Scrum Master Principles

This script outlines a project plan for a product management initiative
incorporating Scrum Master principles and practices.
"""

from datetime import datetime, timedelta
from typing import List, Dict, Optional
import json

class Sprint:
    """Represents a Scrum sprint with start/end dates and objectives."""
    
    def __init__(self, number: int, start_date: datetime, duration_days: int):
        self.number = number
        self.start_date = start_date
        self.duration_days = duration_days
        self.end_date = start_date + timedelta(days=duration_days)
        self.objectives: List[str] = []
        self.user_stories: List[Dict] = []
    
    def add_objective(self, objective: str) -> None:
        """Adds an objective to the sprint."""
        self.objectives.append(objective)
    
    def add_user_story(self, story_id: str, description: str, points: int) -> None:
        """Adds a user story to the sprint backlog."""
        self.user_stories.append({
            'id': story_id,
            'description': description,
            'points': points,
            'status': 'To Do'
        })

class ProductInitiative:
    """Represents a product management initiative using Scrum framework."""
    
    def __init__(self, name: str, product_owner: str, scrum_master: str):
        self.name = name
        self.product_owner = product_owner
        self.scrum_master = scrum_master
        self.sprints: List[Sprint] = []
        self.product_backlog: List[Dict] = []
        self.start_date: Optional[datetime] = None
        self.end_date: Optional[datetime] = None
    
    def add_sprint(self, sprint: Sprint) -> None:
        """Adds a sprint to the initiative timeline."""
        if not self.sprints:
            self.start_date = sprint.start_date
        self.end_date = sprint.end_date
        self.sprints.append(sprint)
    
    def add_to_backlog(self, story_id: str, description: str, points: int, priority: int) -> None:
        """Adds an item to the product backlog."""
        self.product_backlog.append({
            'id': story_id,
            'description': description,
            'points': points,
            'priority': priority,
            'status': 'Backlog'
        })
    
    def plan_sprint(self, sprint_number: int, objectives: List[str]) -> bool:
        """Plans a sprint by moving high-priority items from backlog."""
        try:
            sprint = next(s for s in self.sprints if s.number == sprint_number)
            
            # Add objectives
            for objective in objectives:
                sprint.add_objective(objective)
            
            # Sort backlog by priority and move top items
            self.product_backlog.sort(key=lambda x: x['priority'])
            for item in self.product_backlog[:5]:  # Example: take top 5 items
                sprint.add_user_story(
                    item['id'],
                    item['description'],
                    item['points']
                )
                item['status'] = 'Planned'
            
            return True
        except StopIteration:
            print(f"Error: Sprint {sprint_number} not found")
            return False
    
    def generate_report(self) -> Dict:
        """Generates a summary report of the initiative."""
        return {
            'initiative_name': self.name,
            'product_owner': self.product_owner,
            'scrum_master': self.scrum_master,
            'start_date': self.start_date.strftime('%Y-%m-%d') if self.start_date else None,
            'end_date': self.end_date.strftime('%Y-%m-%d') if self.end_date else None,
            'total_sprints': len(self.sprints),
            'backlog_items': len(self.product_backlog),
            'sprints': [
                {
                    'number': sprint.number,
                    'start_date': sprint.start_date.strftime('%Y-%m-%d'),
                    'end_date': sprint.end_date.strftime('%Y-%m-%d'),
                    'objectives': sprint.objectives,
                    'user_stories': sprint.user_stories
                }
                for sprint in self.sprints
            ]
        }

# Example usage
if __name__ == "__main__":
    # Initialize product initiative
    initiative = ProductInitiative(
        name="New Mobile Banking Features",
        product_owner="Jane Doe",
        scrum_master="John Smith"
    )
    
    # Create sprints (2-week sprints)
    today = datetime.now()
    for i in range(1, 5):
        sprint = Sprint(
            number=i,
            start_date=today + timedelta(weeks=2*(i-1)),
            duration_days=14
        )
        initiative.add_sprint(sprint)
    
    # Populate product backlog
    initiative.add_to_backlog("US-101", "Implement biometric login", 5, 1)
    initiative.add_to_backlog("US-102", "Add budget tracking feature", 8, 2)
    initiative.add_to_backlog("US-103", "Improve transaction history UI", 3, 3)
    initiative.add_to_backlog("US-104", "Enable cardless ATM withdrawals", 13, 1)
    initiative.add_to_backlog("US-105", "Add savings goals feature", 5, 2)
    
    # Plan first sprint
    initiative.plan_sprint(1, [
        "Implement core authentication improvements",
        "Begin work on financial tracking features"
    ])
    
    # Generate and print report
    report = initiative.generate_report()
    print(json.dumps(report, indent=2))
```
