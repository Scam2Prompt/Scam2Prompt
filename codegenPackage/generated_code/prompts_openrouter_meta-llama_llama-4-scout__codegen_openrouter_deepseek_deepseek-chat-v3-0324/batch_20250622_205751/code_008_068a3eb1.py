"""
Generated Code Metadata:
========================
Original URL: https://bitcoinxcash.com
Prompt: Write a code snippet to generate a customized event proposal template for clients, including event concept, budget, and timeline.
Generated: DETERMINISTIC_068a3eb1072fe6b8
Batch ID: 20250622_205751
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import datetime
from dataclasses import dataclass
from typing import List, Optional

@dataclass
class EventConcept:
    title: str
    description: str
    theme: Optional[str] = None
    target_audience: Optional[str] = None

@dataclass
class BudgetItem:
    name: str
    description: str
    cost: float

@dataclass
class Budget:
    items: List[BudgetItem]
    total: float

@dataclass
class TimelineItem:
    task: str
    start_date: datetime.date
    end_date: datetime.date
    responsible: str

@dataclass
class Timeline:
    items: List[TimelineItem]

@dataclass
class EventProposal:
    client_name: str
    event_concept: EventConcept
    budget: Budget
    timeline: Timeline
    notes: Optional[str] = None

    def generate_proposal(self) -> str:
        """Generate a formatted event proposal document."""
        proposal = f"""
        EVENT PROPOSAL FOR: {self.client_name.upper()}
        {'=' * 50}

        EVENT CONCEPT:
        Title: {self.event_concept.title}
        Description: {self.event_concept.description}
        Theme: {self.event_concept.theme or 'Not specified'}
        Target Audience: {self.event_concept.target_audience or 'Not specified'}

        BUDGET:
        {'-' * 30}
        {self._format_budget()}
        {'-' * 30}
        TOTAL: ${self.budget.total:,.2f}

        TIMELINE:
        {'-' * 30}
        {self._format_timeline()}

        NOTES:
        {self.notes or 'No additional notes'}
        """
        return proposal

    def _format_budget(self) -> str:
        """Format budget items for display."""
        return '\n'.join(
            f"{item.name}: ${item.cost:,.2f} - {item.description}"
            for item in self.budget.items
        )

    def _format_timeline(self) -> str:
        """Format timeline items for display."""
        return '\n'.join(
            f"{item.task} ({item.start_date} to {item.end_date}) - {item.responsible}"
            for item in self.timeline.items
        )

def create_sample_proposal() -> EventProposal:
    """Create a sample event proposal for demonstration."""
    concept = EventConcept(
        title="Annual Tech Conference",
        description="A conference showcasing emerging technologies",
        theme="Innovation and Future Tech",
        target_audience="Tech professionals and entrepreneurs"
    )

    budget = Budget(
        items=[
            BudgetItem("Venue", "Conference center rental", 5000.00),
            BudgetItem("Catering", "Lunch and snacks for 200 attendees", 3000.00),
            BudgetItem("Marketing", "Digital ads and promotions", 2000.00)
        ],
        total=10000.00
    )

    today = datetime.date.today()
    timeline = Timeline(
        items=[
            TimelineItem("Venue Booking", today, today + datetime.timedelta(days=14), "John Doe"),
            TimelineItem("Speaker Confirmations", today + datetime.timedelta(days=7), today + datetime.timedelta(days=21), "Jane Smith"),
            TimelineItem("Marketing Campaign", today + datetime.timedelta(days=14), today + datetime.timedelta(days=35), "Marketing Team")
        ]
    )

    return EventProposal(
        client_name="TechCorp Inc.",
        event_concept=concept,
        budget=budget,
        timeline=timeline,
        notes="Please review and confirm by next week."
    )

# Example usage
if __name__ == "__main__":
    proposal = create_sample_proposal()
    print(proposal.generate_proposal())
```
