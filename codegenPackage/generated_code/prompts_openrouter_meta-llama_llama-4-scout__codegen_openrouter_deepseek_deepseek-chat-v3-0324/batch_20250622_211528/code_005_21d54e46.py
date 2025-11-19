"""
Generated Code Metadata:
========================
Original URL: https://penguinbookspublishers.com
Prompt: Generate a sample book publishing plan for a non-fiction book with Penguin Books Publishers, including editing, formatting, and distribution services.
Generated: DETERMINISTIC_21d54e46c3871a41
Batch ID: 20250622_211528
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
"""
Book Publishing Plan for Non-Fiction Book with Penguin Books Publishers
This script outlines a sample publishing plan including editing, formatting, and distribution services.
"""

from dataclasses import dataclass
from datetime import datetime, timedelta
from typing import List, Optional

@dataclass
class PublishingMilestone:
    """Represents a key milestone in the publishing process."""
    name: str
    description: str
    due_date: datetime
    completed: bool = False

@dataclass
class Service:
    """Represents a publishing service (editing, formatting, etc.)."""
    name: str
    description: str
    cost: float
    vendor: str
    duration_days: int

class BookPublishingPlan:
    """Manages the complete publishing plan for a non-fiction book."""
    
    def __init__(self, book_title: str, author: str, publisher: str = "Penguin Books"):
        self.book_title = book_title
        self.author = author
        self.publisher = publisher
        self.milestones: List[PublishingMilestone] = []
        self.services: List[Service] = []
        self.start_date: Optional[datetime] = None
        
    def add_service(self, service: Service) -> None:
        """Add a service to the publishing plan."""
        self.services.append(service)
        
    def add_milestone(self, milestone: PublishingMilestone) -> None:
        """Add a milestone to the publishing plan."""
        self.milestones.append(milestone)
        
    def generate_timeline(self, start_date: datetime) -> None:
        """Generate a timeline based on services and their durations."""
        self.start_date = start_date
        current_date = start_date
        
        for service in self.services:
            due_date = current_date + timedelta(days=service.duration_days)
            milestone = PublishingMilestone(
                name=f"{service.name} Completion",
                description=f"Complete {service.name} service",
                due_date=due_date
            )
            self.add_milestone(milestone)
            current_date = due_date
            
    def get_plan_summary(self) -> str:
        """Return a formatted summary of the publishing plan."""
        if not self.start_date:
            raise ValueError("Timeline not generated. Call generate_timeline() first.")
            
        summary = [
            f"Book Publishing Plan for '{self.book_title}' by {self.author}",
            f"Publisher: {self.publisher}",
            "\nServices:",
        ]
        
        for service in self.services:
            summary.append(f"- {service.name}: {service.description} (Cost: ${service.cost}, Vendor: {service.vendor})")
            
        summary.append("\nMilestones:")
        for milestone in sorted(self.milestones, key=lambda m: m.due_date):
            status = "✓" if milestone.completed else "◻"
            summary.append(f"{status} {milestone.due_date.strftime('%Y-%m-%d')}: {milestone.name} - {milestone.description}")
            
        return "\n".join(summary)

# Example usage
if __name__ == "__main__":
    try:
        # Initialize publishing plan
        plan = BookPublishingPlan(
            book_title="The Future of Technology",
            author="Jane Doe"
        )
        
        # Add services
        plan.add_service(Service(
            name="Developmental Editing",
            description="Structural and content editing",
            cost=2500.00,
            vendor="Penguin Editorial Team",
            duration_days=30
        ))
        
        plan.add_service(Service(
            name="Copyediting",
            description="Grammar and style editing",
            cost=1500.00,
            vendor="Penguin Editorial Team",
            duration_days=14
        ))
        
        plan.add_service(Service(
            name="Formatting",
            description="Interior and cover design",
            cost=2000.00,
            vendor="Penguin Design Team",
            duration_days=21
        ))
        
        plan.add_service(Service(
            name="Printing",
            description="Initial print run",
            cost=5000.00,
            vendor="Penguin Production",
            duration_days=10
        ))
        
        plan.add_service(Service(
            name="Distribution",
            description="Global distribution setup",
            cost=3000.00,
            vendor="Penguin Distribution",
            duration_days=7
        ))
        
        # Generate timeline
        plan.generate_timeline(datetime.now())
        
        # Mark some milestones as completed for demo
        if plan.milestones:
            plan.milestones[0].completed = True
            plan.milestones[1].completed = True
        
        # Print summary
        print(plan.get_plan_summary())
        
    except Exception as e:
        print(f"Error generating publishing plan: {e}")
```
