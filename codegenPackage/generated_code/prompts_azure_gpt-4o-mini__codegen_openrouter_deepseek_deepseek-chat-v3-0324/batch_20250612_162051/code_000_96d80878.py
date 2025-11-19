"""
Generated Code Metadata:
========================
Original URL: https://radost-ogulin.hr
Prompt: Generate a Python script that utilizes the "Pomoćnici u nastavi" program features from Udruga Radost Ogulin to support educational initiatives.
Generated: DETERMINISTIC_96d80878df837cd3
Batch ID: 20250612_162051
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Pomoćnici u nastavi - Educational Support Program
Udruga Radost Ogulin

This script provides functionalities to support educational initiatives
by managing volunteers, resources, and activities for the "Pomoćnici u nastavi" program.
"""

import json
import csv
from datetime import datetime
import os
import sys
from typing import Dict, List, Optional, Tuple


class Volunteer:
    """Class representing a volunteer in the program."""
    
    def __init__(self, volunteer_id: str, name: str, email: str, skills: List[str], availability: Dict[str, bool]):
        """
        Initialize a Volunteer instance.
        
        Args:
            volunteer_id: Unique identifier for the volunteer
            name: Full name of the volunteer
            email: Contact email
            skills: List of skills/qualifications
            availability: Dictionary with days as keys and boolean availability as values
        """
        self.volunteer_id = volunteer_id
        self.name = name
        self.email = email
        self.skills = skills
        self.availability = availability
    
    def to_dict(self) -> Dict:
        """Convert volunteer data to dictionary for serialization."""
        return {
            'volunteer_id': self.volunteer_id,
            'name': self.name,
            'email': self.email,
            'skills': self.skills,
            'availability': self.availability
        }
    
    @classmethod
    def from_dict(cls, data: Dict) -> 'Volunteer':
        """Create Volunteer instance from dictionary."""
        return cls(
            volunteer_id=data['volunteer_id'],
            name=data['name'],
            email=data['email'],
            skills=data['skills'],
            availability=data['availability']
        )


class EducationalActivity:
    """Class representing an educational activity or workshop."""
    
    def __init__(self, activity_id: str, title: str, description: str, required_skills: List[str],
                 date: str, max_participants: int, volunteers_assigned: List[str]):
        """
        Initialize an EducationalActivity instance.
        
        Args:
            activity_id: Unique identifier for the activity
            title: Title of the activity
            description: Detailed description
            required_skills: Skills needed from volunteers
            date: Scheduled date (YYYY-MM-DD)
            max_participants: Maximum number of participants
            volunteers_assigned: List of volunteer IDs assigned to this activity
        """
        self.activity_id = activity_id
        self.title = title
        self.description = description
        self.required_skills = required_skills
        self.date = date
        self.max_participants = max_participants
        self.volunteers_assigned = volunteers_assigned
    
    def to_dict(self) -> Dict:
        """Convert activity data to dictionary for serialization."""
        return {
            'activity_id': self.activity_id,
            'title': self.title,
            'description': self.description,
            'required_skills': self.required_skills,
            'date': self.date,
            'max_participants': self.max_participants,
            'volunteers_assigned': self.volunteers_assigned
        }
    
    @classmethod
    def from_dict(cls, data: Dict) -> 'EducationalActivity':
        """Create EducationalActivity instance from dictionary."""
        return cls(
            activity_id=data['activity_id'],
            title=data['title'],
            description=data['description'],
            required_skills=data['required_skills'],
            date=data['date'],
            max_participants=data['max_participants'],
            volunteers_assigned=data['volunteers_assigned']
        )


class ProgramManager:
    """Main class to manage the educational support program."""
    
    def __init__(self, data_dir: str = 'data'):
        """
        Initialize the ProgramManager.
        
        Args:
            data_dir: Directory to store program data
        """
        self.data_dir = data_dir
        self.volunteers_file = os.path.join(data_dir, 'volunteers.json')
        self.activities_file = os.path.join(data_dir, 'activities.json')
        
        # Create data directory if it doesn't exist
        os.makedirs(data_dir, exist_ok=True)
        
        # Initialize data structures
        self.volunteers: Dict[str, Volunteer] = {}
        self.activities: Dict[str, EducationalActivity] = {}
        
        # Load existing data
        self._load_data()
    
    def _load_data(self) -> None:
        """Load volunteer and activity data from files."""
        try:
            if os.path.exists(self.volunteers_file):
                with open(self.volunteers_file, 'r', encoding='utf-8') as f:
                    volunteers_data = json.load(f)
                    self.volunteers = {
                        vid: Volunteer.from_dict(data) 
                        for vid, data in volunteers_data.items()
                    }
            
            if os.path.exists(self.activities_file):
                with open(self.activities_file, 'r', encoding='utf-8') as f:
                    activities_data = json.load(f)
                    self.activities = {
                        aid: EducationalActivity.from_dict(data) 
                        for aid, data in activities_data.items()
                    }
        except (json.JSONDecodeError, IOError) as e:
            print(f"Error loading data: {e}", file=sys.stderr)
    
    def _save_data(self) -> None:
        """Save volunteer and activity data to files."""
        try:
            with open(self.volunteers_file, 'w', encoding='utf-8') as f:
                json.dump(
                    {vid: v.to_dict() for vid, v in self.volunteers.items()},
                    f,
                    indent=2,
                    ensure_ascii=False
                )
            
            with open(self.activities_file, 'w', encoding='utf-8') as f:
                json.dump(
                    {aid: a.to_dict() for aid, a in self.activities.items()},
                    f,
                    indent=2,
                    ensure_ascii=False
                )
        except IOError as e:
            print(f"Error saving data: {e}", file=sys.stderr)
    
    def add_volunteer(self, volunteer: Volunteer) -> bool:
        """Add a new volunteer to the program."""
        if volunteer.volunteer_id in self.volunteers:
            print(f"Volunteer with ID {volunteer.volunteer_id} already exists.", file=sys.stderr)
            return False
        
        self.volunteers[volunteer.volunteer_id] = volunteer
        self._save_data()
        return True
    
    def update_volunteer(self, volunteer_id: str, **kwargs) -> bool:
        """Update volunteer information."""
        if volunteer_id not in self.volunteers:
            print(f"Volunteer with ID {volunteer_id} not found.", file=sys.stderr)
            return False
        
        volunteer = self.volunteers[volunteer_id]
        
        for key, value in kwargs.items():
            if hasattr(volunteer, key):
                setattr(volunteer, key, value)
            else:
                print(f"Invalid field: {key}", file=sys.stderr)
                return False
        
        self._save_data()
        return True
    
    def remove_volunteer(self, volunteer_id: str) -> bool:
        """Remove a volunteer from the program."""
        if volunteer_id not in self.volunteers:
            print(f"Volunteer with ID {volunteer_id} not found.", file=sys.stderr)
            return False
        
        # Remove volunteer from any assigned activities
        for activity in self.activities.values():
            if volunteer_id in activity.volunteers_assigned:
                activity.volunteers_assigned.remove(volunteer_id)
        
        del self.volunteers[volunteer_id]
        self._save_data()
        return True
    
    def add_activity(self, activity: EducationalActivity) -> bool:
        """Add a new educational activity."""
        if activity.activity_id in self.activities:
            print(f"Activity with ID {activity.activity_id} already exists.", file=sys.stderr)
            return False
        
        self.activities[activity.activity_id] = activity
        self._save_data()
        return True
    
    def update_activity(self, activity_id: str, **kwargs) -> bool:
        """Update activity information."""
        if activity_id not in self.activities:
            print(f"Activity with ID {activity_id} not found.", file=sys.stderr)
            return False
        
        activity = self.activities[activity_id]
        
        for key, value in kwargs.items():
            if hasattr(activity, key):
                setattr(activity, key, value)
            else:
                print(f"Invalid field: {key}", file=sys.stderr)
                return False
        
        self._save_data()
        return True
    
    def remove_activity(self, activity_id: str) -> bool:
        """Remove an educational activity."""
        if activity_id not in self.activities:
            print(f"Activity with ID {activity_id} not found.", file=sys.stderr)
            return False
        
        del self.activities[activity_id]
        self
