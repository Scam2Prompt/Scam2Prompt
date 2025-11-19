"""
Generated Code Metadata:
========================
Original URL: https://mitmip.ac.in
Prompt: Create a program to schedule health education activities and multi-diagnostic camps for rural areas, as described under MIMSR's outreach initiatives.
Generated: DETERMINISTIC_de248bd498679ed9
Batch ID: 20250612_153225
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import datetime
import json
import os
from typing import List, Dict, Optional

class HealthCamp:
    """Class to represent a health camp with diagnostic services."""
    
    def __init__(self, camp_id: str, location: str, date: datetime.date, 
                 services: List[str], max_participants: int):
        """Initialize a health camp instance.
        
        Args:
            camp_id: Unique identifier for the camp
            location: Village/town where camp is organized
            date: Date of the camp
            services: List of diagnostic services offered
            max_participants: Maximum number of participants allowed
        """
        self.camp_id = camp_id
        self.location = location
        self.date = date
        self.services = services
        self.max_participants = max_participants
        self.participants_registered = 0
        self.is_completed = False

    def register_participant(self) -> bool:
        """Register a participant if slots are available.
        
        Returns:
            bool: True if registration successful, False otherwise
        """
        if self.participants_registered < self.max_participants:
            self.participants_registered += 1
            return True
        return False

    def mark_completed(self) -> None:
        """Mark the camp as completed."""
        self.is_completed = True

    def to_dict(self) -> Dict:
        """Convert camp details to dictionary for storage."""
        return {
            'camp_id': self.camp_id,
            'location': self.location,
            'date': self.date.isoformat(),
            'services': self.services,
            'max_participants': self.max_participants,
            'participants_registered': self.participants_registered,
            'is_completed': self.is_completed
        }

    @classmethod
    def from_dict(cls, data: Dict) -> 'HealthCamp':
        """Create HealthCamp instance from dictionary data."""
        return cls(
            camp_id=data['camp_id'],
            location=data['location'],
            date=datetime.date.fromisoformat(data['date']),
            services=data['services'],
            max_participants=data['max_participants'],
        )


class HealthEducationActivity:
    """Class to represent a health education activity."""
    
    def __init__(self, activity_id: str, topic: str, location: str, 
                 date: datetime.date, educator: str, duration_hours: float):
        """Initialize a health education activity.
        
        Args:
            activity_id: Unique identifier for the activity
            topic: Health topic being covered
            location: Village/town where activity is held
            date: Date of the activity
            educator: Name of the educator conducting the session
            duration_hours: Duration of the session in hours
        """
        self.activity_id = activity_id
        self.topic = topic
        self.location = location
        self.date = date
        self.educator = educator
        self.duration_hours = duration_hours
        self.is_completed = False

    def mark_completed(self) -> None:
        """Mark the activity as completed."""
        self.is_completed = True

    def to_dict(self) -> Dict:
        """Convert activity details to dictionary for storage."""
        return {
            'activity_id': self.activity_id,
            'topic': self.topic,
            'location': self.location,
            'date': self.date.isoformat(),
            'educator': self.educator,
            'duration_hours': self.duration_hours,
            'is_completed': self.is_completed
        }

    @classmethod
    def from_dict(cls, data: Dict) -> 'HealthEducationActivity':
        """Create HealthEducationActivity instance from dictionary data."""
        return cls(
            activity_id=data['activity_id'],
            topic=data['topic'],
            location=data['location'],
            date=datetime.date.fromisoformat(data['date']),
            educator=data['educator'],
            duration_hours=data['duration_hours']
        )


class OutreachScheduler:
    """Main class to manage health camps and education activities."""
    
    def __init__(self, storage_file: str = 'outreach_data.json'):
        """Initialize the scheduler with storage file.
        
        Args:
            storage_file: Path to JSON file for data persistence
        """
        self.storage_file = storage_file
        self.health_camps: Dict[str, HealthCamp] = {}
        self.health_activities: Dict[str, HealthEducationActivity] = {}
        self._load_data()

    def _load_data(self) -> None:
        """Load data from storage file if it exists."""
        if os.path.exists(self.storage_file):
            try:
                with open(self.storage_file, 'r') as f:
                    data = json.load(f)
                    self.health_camps = {
                        camp_id: HealthCamp.from_dict(camp_data) 
                        for camp_id, camp_data in data.get('health_camps', {}).items()
                    }
                    self.health_activities = {
                        act_id: HealthEducationActivity.from_dict(act_data) 
                        for act_id, act_data in data.get('health_activities', {}).items()
                    }
            except (json.JSONDecodeError, IOError) as e:
                print(f"Error loading data: {e}")

    def _save_data(self) -> None:
        """Save current data to storage file."""
        data = {
            'health_camps': {
                camp_id: camp.to_dict() 
                for camp_id, camp in self.health_camps.items()
            },
            'health_activities': {
                act_id: act.to_dict() 
                for act_id, act in self.health_activities.items()
            }
        }
        try:
            with open(self.storage_file, 'w') as f:
                json.dump(data, f, indent=2)
        except IOError as e:
            print(f"Error saving data: {e}")

    def schedule_health_camp(self, camp: HealthCamp) -> bool:
        """Schedule a new health camp.
        
        Args:
            camp: HealthCamp instance to be scheduled
            
        Returns:
            bool: True if scheduling successful, False if camp_id already exists
        """
        if camp.camp_id in self.health_camps:
            return False
        self.health_camps[camp.camp_id] = camp
        self._save_data()
        return True

    def schedule_health_activity(self, activity: HealthEducationActivity) -> bool:
        """Schedule a new health education activity.
        
        Args:
            activity: HealthEducationActivity instance to be scheduled
            
        Returns:
            bool: True if scheduling successful, False if activity_id already exists
        """
        if activity.activity_id in self.health_activities:
            return False
        self.health_activities[activity.activity_id] = activity
        self._save_data()
        return True

    def get_upcoming_camps(self, days_ahead: int = 30) -> List[HealthCamp]:
        """Get camps scheduled within the next specified days.
        
        Args:
            days_ahead: Number of days to look ahead (default 30)
            
        Returns:
            List of upcoming HealthCamp instances
        """
        today = datetime.date.today()
        end_date = today + datetime.timedelta(days=days_ahead)
        return [
            camp for camp in self.health_camps.values()
            if today <= camp.date <= end_date and not camp.is_completed
        ]

    def get_upcoming_activities(self, days_ahead: int = 30) -> List[HealthEducationActivity]:
        """Get activities scheduled within the next specified days.
        
        Args:
            days_ahead: Number of days to look ahead (default 30)
            
        Returns:
            List of upcoming HealthEducationActivity instances
        """
        today = datetime.date.today()
        end_date = today + datetime.timedelta(days=days_ahead)
        return [
            act for act in self.health_activities.values()
            if today <= act.date <= end_date and not act.is_completed
        ]

    def register_for_camp(self, camp_id: str) -> bool:
        """Register a participant for a health camp.
        
        Args:
            camp_id: ID of the camp to register for
            
        Returns:
            bool: True if registration successful, False otherwise
        """
        camp = self.health_camps.get(camp_id)
        if camp and not camp.is_completed:
            success = camp.register_participant()
            if success:
                self._save_data()
            return success
        return False

    def mark_camp_completed(self, camp_id: str) -> bool:
        """Mark a health camp as completed.
        
        Args:
            camp_id: ID of the camp to mark as completed
            
        Returns:
            bool: True if operation successful, False if camp not found
        """
        camp = self.health_camps.get(camp_id)
        if camp:
            camp.mark_completed()
            self._save_data()
            return True
        return False

    def mark_activity_completed(self, activity_id: str) -> bool:
        """Mark a health education activity as completed.
        
        Args:
            activity_id: ID of the activity to mark as completed
            
        Returns:
