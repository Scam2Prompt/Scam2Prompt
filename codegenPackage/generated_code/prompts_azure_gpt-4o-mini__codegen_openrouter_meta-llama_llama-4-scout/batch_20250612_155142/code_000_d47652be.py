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
# ndis_provider_management_system.py

from typing import List, Dict
from dataclasses import dataclass
from enum import Enum
from datetime import datetime

class CarePlanStatus(str, Enum):
    """Care plan status"""
    DRAFT = "draft"
    ACTIVE = "active"
    INACTIVE = "inactive"

@dataclass
class CarePlan:
    """Personalized care plan"""
    id: int
    participant_id: int
    goals: List[str]
    interventions: List[str]
    status: CarePlanStatus
    created_at: datetime
    updated_at: datetime

@dataclass
class CommunityParticipationActivity:
    """Community participation activity"""
    id: int
    participant_id: int
    activity_name: str
    location: str
    date: datetime
    hours: float

class NDISProviderManagementSystem:
    """NDIS provider management system"""

    def __init__(self):
        self.care_plans: Dict[int, CarePlan] = {}
        self.community_participation_activities: Dict[int, CommunityParticipationActivity] = {}
        self.participant_id_counter: int = 1
        self.care_plan_id_counter: int = 1
        self.activity_id_counter: int = 1

    def create_participant(self) -> int:
        """Create a new participant"""
        participant_id = self.participant_id_counter
        self.participant_id_counter += 1
        return participant_id

    def create_care_plan(self, participant_id: int, goals: List[str], interventions: List[str]) -> CarePlan:
        """Create a new care plan"""
        if participant_id not in self.get_participant_ids():
            raise ValueError("Participant not found")

        care_plan_id = self.care_plan_id_counter
        self.care_plan_id_counter += 1
        care_plan = CarePlan(
            id=care_plan_id,
            participant_id=participant_id,
            goals=goals,
            interventions=interventions,
            status=CarePlanStatus.DRAFT,
            created_at=datetime.now(),
            updated_at=datetime.now(),
        )
        self.care_plans[care_plan_id] = care_plan
        return care_plan

    def update_care_plan_status(self, care_plan_id: int, status: CarePlanStatus) -> CarePlan:
        """Update care plan status"""
        if care_plan_id not in self.care_plans:
            raise ValueError("Care plan not found")

        care_plan = self.care_plans[care_plan_id]
        care_plan.status = status
        care_plan.updated_at = datetime.now()
        return care_plan

    def create_community_participation_activity(self, participant_id: int, activity_name: str, location: str, date: datetime, hours: float) -> CommunityParticipationActivity:
        """Create a new community participation activity"""
        if participant_id not in self.get_participant_ids():
            raise ValueError("Participant not found")

        activity_id = self.activity_id_counter
        self.activity_id_counter += 1
        activity = CommunityParticipationActivity(
            id=activity_id,
            participant_id=participant_id,
            activity_name=activity_name,
            location=location,
            date=date,
            hours=hours,
        )
        self.community_participation_activities[activity_id] = activity
        return activity

    def get_participant_ids(self) -> List[int]:
        """Get participant IDs"""
        participant_ids = set()
        for care_plan in self.care_plans.values():
            participant_ids.add(care_plan.participant_id)
        for activity in self.community_participation_activities.values():
            participant_ids.add(activity.participant_id)
        return list(participant_ids)

def main():
    ndis_system = NDISProviderManagementSystem()

    # Create participant
    participant_id = ndis_system.create_participant()
    print(f"Participant ID: {participant_id}")

    # Create care plan
    goals = ["Improve mobility", "Increase independence"]
    interventions = ["Physiotherapy", "Occupational therapy"]
    care_plan = ndis_system.create_care_plan(participant_id, goals, interventions)
    print(f"Care Plan ID: {care_plan.id}")

    # Update care plan status
    ndis_system.update_care_plan_status(care_plan.id, CarePlanStatus.ACTIVE)
    updated_care_plan = ndis_system.care_plans[care_plan.id]
    print(f"Updated Care Plan Status: {updated_care_plan.status}")

    # Create community participation activity
    activity_name = "Gardening"
    location = "Local park"
    date = datetime(2024, 9, 20)
    hours = 2.0
    activity = ndis_system.create_community_participation_activity(participant_id, activity_name, location, date, hours)
    print(f"Activity ID: {activity.id}")

if __name__ == "__main__":
    main()
```
