"""
Generated Code Metadata:
========================
Original URL: https://timeformecenter.com
Prompt: "What are the best practices for implementing a time management system in a remote team setting?"
Generated: DETERMINISTIC_21a2fe90ddb1c8c9
Batch ID: 20250622_212131
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

# Time Management System for Remote Teams

```python
"""
Remote Team Time Management System

This module provides utilities for tracking and managing time in remote teams,
including time zone handling, work hour tracking, and productivity analytics.
"""

import datetime
import pytz
from typing import Dict, List, Optional, Tuple
import json
import logging
from dataclasses import dataclass

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
)
logger = logging.getLogger(__name__)

@dataclass
class TeamMember:
    """Represents a remote team member with time-related attributes."""
    id: str
    name: str
    timezone: str
    core_hours: Tuple[int, int]  # (start_hour, end_hour)
    working_days: List[str]  # e.g., ['Monday', 'Tuesday', ...]

class TimeManagementSystem:
    """Main class for managing remote team time tracking."""
    
    def __init__(self):
        self.members: Dict[str, TeamMember] = {}
        self.time_entries = []
    
    def add_member(self, member: TeamMember) -> None:
        """Add a new team member to the system."""
        try:
            # Validate timezone
            pytz.timezone(member.timezone)
            self.members[member.id] = member
            logger.info(f"Added member: {member.name}")
        except pytz.UnknownTimeZoneError:
            logger.error(f"Invalid timezone: {member.timezone}")
            raise ValueError(f"Invalid timezone: {member.timezone}")
    
    def log_work(self, member_id: str, start: datetime.datetime, end: datetime.datetime, task: str) -> None:
        """Log work hours for a team member."""
        if member_id not in self.members:
            logger.error(f"Member {member_id} not found")
            raise ValueError("Member not found")
        
        if start >= end:
            logger.error("Start time must be before end time")
            raise ValueError("Start time must be before end time")
        
        entry = {
            'member_id': member_id,
            'start': start.isoformat(),
            'end': end.isoformat(),
            'task': task,
            'duration': (end - start).total_seconds() / 3600  # in hours
        }
        self.time_entries.append(entry)
        logger.info(f"Logged work for {self.members[member_id].name}: {task}")
    
    def get_overlapping_hours(self, member1_id: str, member2_id: str) -> float:
        """
        Calculate overlapping working hours between two team members.
        Returns the number of overlapping hours in their workdays.
        """
        try:
            member1 = self.members[member1_id]
            member2 = self.members[member2_id]
            
            tz1 = pytz.timezone(member1.timezone)
            tz2 = pytz.timezone(member2.timezone)
            
            # Get current time in both timezones
            now_utc = datetime.datetime.now(pytz.utc)
            now_tz1 = now_utc.astimezone(tz1)
            now_tz2 = now_utc.astimezone(tz2)
            
            # Calculate overlapping hours
            start1, end1 = member1.core_hours
            start2, end2 = member2.core_hours
            
            overlap_start = max(start1 - now_tz1.utcoffset().total_seconds()/3600 + now_tz2.utcoffset().total_seconds()/3600, start2)
            overlap_end = min(end1 - now_tz1.utcoffset().total_seconds()/3600 + now_tz2.utcoffset().total_seconds()/3600, end2)
            
            return max(0, overlap_end - overlap_start)
        except KeyError as e:
            logger.error(f"Member not found: {e}")
            raise ValueError("Member not found") from e
    
    def get_team_availability(self) -> Dict[str, List[Dict[str, str]]]:
        """Get current availability status for all team members."""
        availability = {}
        now_utc = datetime.datetime.now(pytz.utc)
        
        for member_id, member in self.members.items():
            tz = pytz.timezone(member.timezone)
            local_time = now_utc.astimezone(tz)
            
            is_working_day = local_time.strftime('%A') in member.working_days
            current_hour = local_time.hour
            is_working_hour = member.core_hours[0] <= current_hour < member.core_hours[1]
            
            availability[member_id] = {
                'name': member.name,
                'timezone': member.timezone,
                'local_time': local_time.isoformat(),
                'is_working_day': is_working_day,
                'is_working_hour': is_working_hour,
                'status': 'Available' if is_working_day and is_working_hour else 'Unavailable'
            }
        
        return availability
    
    def generate_productivity_report(self, start_date: datetime.date, end_date: datetime.date) -> Dict[str, Dict]:
        """Generate a productivity report for all team members for a given date range."""
        report = {}
        
        for member_id, member in self.members.items():
            member_entries = [
                entry for entry in self.time_entries
                if entry['member_id'] == member_id and 
                datetime.datetime.fromisoformat(entry['start']).date() >= start_date and
                datetime.datetime.fromisoformat(entry['end']).date() <= end_date
            ]
            
            total_hours = sum(entry['duration'] for entry in member_entries)
            unique_tasks = len({entry['task'] for entry in member_entries})
            
            report[member_id] = {
                'name': member.name,
                'total_hours': total_hours,
                'task_count': unique_tasks,
                'average_hours_per_day': total_hours / ((end_date - start_date).days + 1) if (end_date - start_date).days > 0 else total_hours
            }
        
        return report
    
    def save_to_file(self, filename: str) -> None:
        """Save the current state of the system to a file."""
        data = {
            'members': {k: {
                'id': v.id,
                'name': v.name,
                'timezone': v.timezone,
                'core_hours': v.core_hours,
                'working_days': v.working_days
            } for k, v in self.members.items()},
            'time_entries': self.time_entries
        }
        
        try:
            with open(filename, 'w') as f:
                json.dump(data, f, indent=2)
            logger.info(f"Data saved to {filename}")
        except IOError as e:
            logger.error(f"Failed to save data: {e}")
            raise
    
    def load_from_file(self, filename: str) -> None:
        """Load system state from a file."""
        try:
            with open(filename, 'r') as f:
                data = json.load(f)
            
            self.members = {
                k: TeamMember(
                    id=v['id'],
                    name=v['name'],
                    timezone=v['timezone'],
                    core_hours=tuple(v['core_hours']),
                    working_days=v['working_days']
                ) for k, v in data['members'].items()
            }
            self.time_entries = data['time_entries']
            logger.info(f"Data loaded from {filename}")
        except (IOError, json.JSONDecodeError, KeyError) as e:
            logger.error(f"Failed to load data: {e}")
            raise

# Example usage
if __name__ == "__main__":
    try:
        # Initialize system
        tms = TimeManagementSystem()
        
        # Add team members
        tms.add_member(TeamMember(
            id="001",
            name="Alice",
            timezone="America/New_York",
            core_hours=(9, 17),
            working_days=["Monday", "Tuesday", "Wednesday", "Thursday", "Friday"]
        ))
        
        tms.add_member(TeamMember(
            id="002",
            name="Bob",
            timezone="Europe/London",
            core_hours=(8, 16),
            working_days=["Monday", "Tuesday", "Wednesday", "Thursday", "Friday"]
        ))
        
        # Log some work
        now = datetime.datetime.now(pytz.utc)
        tms.log_work(
            "001",
            now - datetime.timedelta(hours=2),
            now - datetime.timedelta(hours=1),
            "Project X Development"
        )
        
        # Get availability
        availability = tms.get_team_availability()
        print("Team Availability:")
        print(json.dumps(availability, indent=2))
        
        # Save data
        tms.save_to_file("team_time_data
