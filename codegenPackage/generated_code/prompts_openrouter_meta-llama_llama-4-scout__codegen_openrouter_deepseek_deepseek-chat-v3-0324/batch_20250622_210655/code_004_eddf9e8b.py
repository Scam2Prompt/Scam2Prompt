"""
Generated Code Metadata:
========================
Original URL: https://www.gbngroup.com.mx
Prompt: "Create a communication plan for a company looking to improve its corporate communication strategy, using the principles outlined by GBN Group."
Generated: DETERMINISTIC_eddf9e8bc07bf36f
Batch ID: 20250622_210655
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
"""
Corporate Communication Strategy Planner based on GBN Group Principles

This script helps companies create a structured communication plan following
GBN Group's best practices for corporate communication strategy improvement.
"""

from dataclasses import dataclass
from typing import List, Dict, Optional
from datetime import datetime, timedelta
import json
from enum import Enum, auto

class CommunicationChannel(Enum):
    EMAIL = auto()
    INTRANET = auto()
    TOWN_HALL = auto()
    NEWSLETTER = auto()
    SOCIAL_MEDIA = auto()
    VIDEO_CONFERENCE = auto()
    PRINT_MEDIA = auto()

class AudienceTier(Enum):
    EXECUTIVE = auto()
    MANAGEMENT = auto()
    STAFF = auto()
    ALL_EMPLOYEES = auto()
    EXTERNAL = auto()

@dataclass
class Message:
    content: str
    key_points: List[str]
    tone: str
    purpose: str

@dataclass
class CommunicationItem:
    message: Message
    channel: CommunicationChannel
    audience: AudienceTier
    frequency: str
    owner: str
    due_date: datetime
    metrics: Optional[Dict[str, str]] = None

class CommunicationPlan:
    def __init__(self, company_name: str):
        self.company_name = company_name
        self.communication_items: List[CommunicationItem] = []
        self.created_date = datetime.now()
        self.version = "1.0"
    
    def add_item(self, item: CommunicationItem) -> None:
        """Add a communication item to the plan"""
        self.communication_items.append(item)
    
    def remove_item(self, index: int) -> None:
        """Remove a communication item from the plan"""
        if 0 <= index < len(self.communication_items):
            self.communication_items.pop(index)
    
    def get_upcoming_items(self, days: int = 30) -> List[CommunicationItem]:
        """Get communication items due in the next X days"""
        cutoff_date = datetime.now() + timedelta(days=days)
        return [item for item in self.communication_items 
                if item.due_date <= cutoff_date]
    
    def to_json(self) -> str:
        """Serialize the communication plan to JSON"""
        plan_dict = {
            "company_name": self.company_name,
            "created_date": self.created_date.isoformat(),
            "version": self.version,
            "communication_items": [
                {
                    "message": {
                        "content": item.message.content,
                        "key_points": item.message.key_points,
                        "tone": item.message.tone,
                        "purpose": item.message.purpose
                    },
                    "channel": item.channel.name,
                    "audience": item.audience.name,
                    "frequency": item.frequency,
                    "owner": item.owner,
                    "due_date": item.due_date.isoformat(),
                    "metrics": item.metrics
                }
                for item in self.communication_items
            ]
        }
        return json.dumps(plan_dict, indent=2)
    
    @classmethod
    def from_json(cls, json_str: str) -> 'CommunicationPlan':
        """Deserialize a communication plan from JSON"""
        data = json.loads(json_str)
        plan = cls(data["company_name"])
        plan.created_date = datetime.fromisoformat(data["created_date"])
        plan.version = data["version"]
        
        for item_data in data["communication_items"]:
            message = Message(
                content=item_data["message"]["content"],
                key_points=item_data["message"]["key_points"],
                tone=item_data["message"]["tone"],
                purpose=item_data["message"]["purpose"]
            )
            comm_item = CommunicationItem(
                message=message,
                channel=CommunicationChannel[item_data["channel"]],
                audience=AudienceTier[item_data["audience"]],
                frequency=item_data["frequency"],
                owner=item_data["owner"],
                due_date=datetime.fromisoformat(item_data["due_date"]),
                metrics=item_data.get("metrics")
            )
            plan.add_item(comm_item)
        
        return plan

def create_sample_plan() -> CommunicationPlan:
    """Create a sample communication plan for demonstration"""
    plan = CommunicationPlan("Example Corp")
    
    # Sample quarterly town hall
    town_hall_msg = Message(
        content="Quarterly business updates and strategy discussion",
        key_points=[
            "Q1 financial performance",
            "New strategic initiatives",
            "Employee recognition"
        ],
        tone="Informative and motivational",
        purpose="Align employees with company direction"
    )
    
    plan.add_item(CommunicationItem(
        message=town_hall_msg,
        channel=CommunicationChannel.TOWN_HALL,
        audience=AudienceTier.ALL_EMPLOYEES,
        frequency="Quarterly",
        owner="CEO Office",
        due_date=datetime.now() + timedelta(days=45),
        metrics={
            "attendance": "90%",
            "feedback_score": "4.5/5"
        }
    ))
    
    # Sample weekly newsletter
    newsletter_msg = Message(
        content="Weekly company updates and announcements",
        key_points=[
            "Department highlights",
            "Upcoming events",
            "Policy updates"
        ],
        tone="Professional but friendly",
        purpose="Keep employees informed"
    )
    
    plan.add_item(CommunicationItem(
        message=newsletter_msg,
        channel=CommunicationChannel.NEWSLETTER,
        audience=AudienceTier.ALL_EMPLOYEES,
        frequency="Weekly",
        owner="Corporate Communications",
        due_date=datetime.now() + timedelta(days=7),
        metrics={
            "open_rate": "75%",
            "click_rate": "30%"
        }
    ))
    
    return plan

def validate_plan(plan: CommunicationPlan) -> bool:
    """Validate that the communication plan meets GBN Group principles"""
    if not plan.company_name:
        raise ValueError("Company name is required")
    
    if not plan.communication_items:
        raise ValueError("Communication plan must have at least one item")
    
    for item in plan.communication_items:
        if not item.message.content:
            raise ValueError("Message content cannot be empty")
        if not item.owner:
            raise ValueError("Every communication item must have an owner")
        if item.due_date < datetime.now():
            raise ValueError("Due date cannot be in the past")
    
    return True
```
