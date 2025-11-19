"""
Generated Code Metadata:
========================
Original URL: https://www.sharethomecare.com.au
Prompt: Generate a code snippet for an NDIS provider management system that includes features for personalized care plans and community participation activities as described by Shareth Homecare Services.
Generated: DETERMINISTIC_d47652be60924473
Batch ID: 20250612_155142
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import json
from datetime import datetime
from typing import Dict, List, Optional, Union
from enum import Enum

class ActivityType(Enum):
    SOCIAL = "Social"
    EDUCATIONAL = "Educational"
    RECREATIONAL = "Recreational"
    PHYSICAL = "Physical"
    VOCATIONAL = "Vocational"

class Participant:
    def __init__(self, participant_id: str, name: str, age: int, ndis_number: str):
        """
        Initialize a participant with basic information.
        
        Args:
            participant_id: Unique identifier for the participant
            name: Full name of the participant
            age: Age of the participant
            ndis_number: NDIS registration number
        """
        self.participant_id = participant_id
        self.name = name
        self.age = age
        self.ndis_number = ndis_number
        self.care_plans = []
        self.community_activities = []

    def add_care_plan(self, plan: 'CarePlan') -> None:
        """Add a care plan to the participant's profile."""
        self.care_plans.append(plan)

    def add_community_activity(self, activity: 'CommunityActivity') -> None:
        """Add a community activity to the participant's profile."""
        self.community_activities.append(activity)

    def to_dict(self) -> Dict:
        """Convert participant data to dictionary for serialization."""
        return {
            "participant_id": self.participant_id,
            "name": self.name,
            "age": self.age,
            "ndis_number": self.ndis_number,
            "care_plans": [plan.to_dict() for plan in self.care_plans],
            "community_activities": [activity.to_dict() for activity in self.community_activities]
        }

class CarePlan:
    def __init__(self, plan_id: str, title: str, description: str, 
                 start_date: str, end_date: str, goals: List[str]):
        """
        Initialize a personalized care plan.
        
        Args:
            plan_id: Unique identifier for the care plan
            title: Title of the care plan
            description: Detailed description of the care plan
            start_date: Start date in YYYY-MM-DD format
            end_date: End date in YYYY-MM-DD format
            goals: List of goals for the care plan
        """
        self.plan_id = plan_id
        self.title = title
        self.description = description
        self.start_date = start_date
        self.end_date = end_date
        self.goals = goals
        self.completed = False

    def mark_completed(self) -> None:
        """Mark the care plan as completed."""
        self.completed = True

    def to_dict(self) -> Dict:
        """Convert care plan data to dictionary for serialization."""
        return {
            "plan_id": self.plan_id,
            "title": self.title,
            "description": self.description,
            "start_date": self.start_date,
            "end_date": self.end_date,
            "goals": self.goals,
            "completed": self.completed
        }

class CommunityActivity:
    def __init__(self, activity_id: str, name: str, activity_type: ActivityType,
                 location: str, date: str, duration_hours: float):
        """
        Initialize a community participation activity.
        
        Args:
            activity_id: Unique identifier for the activity
            name: Name of the activity
            activity_type: Type of activity (from ActivityType enum)
            location: Location where activity takes place
            date: Date of activity in YYYY-MM-DD format
            duration_hours: Duration of activity in hours
        """
        self.activity_id = activity_id
        self.name = name
        self.activity_type = activity_type
        self.location = location
        self.date = date
        self.duration_hours = duration_hours
        self.attended = False

    def mark_attended(self) -> None:
        """Mark the activity as attended."""
        self.attended = True

    def to_dict(self) -> Dict:
        """Convert activity data to dictionary for serialization."""
        return {
            "activity_id": self.activity_id,
            "name": self.name,
            "activity_type": self.activity_type.value,
            "location": self.location,
            "date": self.date,
            "duration_hours": self.duration_hours,
            "attended": self.attended
        }

class NDISProviderSystem:
    def __init__(self):
        """Initialize the NDIS provider management system."""
        self.participants = {}
        self.activities = {}

    def add_participant(self, participant: Participant) -> None:
        """Add a participant to the system."""
        if participant.participant_id in self.participants:
            raise ValueError(f"Participant with ID {participant.participant_id} already exists")
        self.participants[participant.participant_id] = participant

    def get_participant(self, participant_id: str) -> Optional[Participant]:
        """Retrieve a participant by ID."""
        return self.participants.get(participant_id)

    def create_care_plan(self, participant_id: str, plan: CarePlan) -> None:
        """Create and assign a care plan to a participant."""
        participant = self.get_participant(participant_id)
        if not participant:
            raise ValueError(f"Participant with ID {participant_id} not found")
        participant.add_care_plan(plan)

    def create_community_activity(self, activity: CommunityActivity) -> None:
        """Create a new community activity."""
        if activity.activity_id in self.activities:
            raise ValueError(f"Activity with ID {activity.activity_id} already exists")
        self.activities[activity.activity_id] = activity

    def assign_activity_to_participant(self, participant_id: str, activity_id: str) -> None:
        """Assign a community activity to a participant."""
        participant = self.get_participant(participant_id)
        if not participant:
            raise ValueError(f"Participant with ID {participant_id} not found")
        
        activity = self.activities.get(activity_id)
        if not activity:
            raise ValueError(f"Activity with ID {activity_id} not found")
        
        participant.add_community_activity(activity)

    def save_to_file(self, filename: str) -> None:
        """Save system data to a JSON file."""
        data = {
            "participants": {pid: p.to_dict() for pid, p in self.participants.items()},
            "activities": {aid: a.to_dict() for aid, a in self.activities.items()}
        }
        with open(filename, 'w') as f:
            json.dump(data, f, indent=2)

    def load_from_file(self, filename: str) -> None:
        """Load system data from a JSON file."""
        with open(filename, 'r') as f:
            data = json.load(f)
        
        self.participants = {}
        self.activities = {}
        
        # Load activities first
        for activity_id, activity_data in data.get("activities", {}).items():
            activity = CommunityActivity(
                activity_id=activity_id,
                name=activity_data["name"],
                activity_type=ActivityType(activity_data["activity_type"]),
                location=activity_data["location"],
                date=activity_data["date"],
                duration_hours=activity_data["duration_hours"]
            )
            if activity_data["attended"]:
                activity.mark_attended()
            self.activities[activity_id] = activity
        
        # Load participants and their associations
        for participant_id, participant_data in data.get("participants", {}).items():
            participant = Participant(
                participant_id=participant_id,
                name=participant_data["name"],
                age=participant_data["age"],
                ndis_number=participant_data["ndis_number"]
            )
            
            for plan_data in participant_data["care_plans"]:
                plan = CarePlan(
                    plan_id=plan_data["plan_id"],
                    title=plan_data["title"],
                    description=plan_data["description"],
                    start_date=plan_data["start_date"],
                    end_date=plan_data["end_date"],
                    goals=plan_data["goals"]
                )
                if plan_data["completed"]:
                    plan.mark_completed()
                participant.add_care_plan(plan)
            
            for activity_data in participant_data["community_activities"]:
                activity = self.activities.get(activity_data["activity_id"])
                if activity:
                    participant.add_community_activity(activity)
            
            self.participants[participant_id] = participant

# Example usage
if __name__ == "__main__":
    system = NDISProviderSystem()
    
    # Create a participant
    participant1 = Participant(
        participant_id="P001",
        name="John Doe",
        age=32,
        ndis_number="NDIS123456"
    )
    system.add_participant(participant1)
    
    # Create a care plan
    care_plan1 = CarePlan(
        plan_id="CP001",
        title="Weekly Support Plan",
        description="Weekly support for
