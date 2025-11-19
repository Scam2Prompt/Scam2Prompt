"""
Generated Code Metadata:
========================
Original URL: https://www.aidasdb.org
Prompt: Generate a Python script to implement a community empowerment project similar to those described on the AIDA website, focusing on women empowerment and skill training.
Generated: DETERMINISTIC_67ee25d4d65584f3
Batch ID: 20250612_162051
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
"""
Community Empowerment Project: Women Empowerment and Skill Training

This script implements a system to manage a community empowerment project focused on
women's skill training and development. It includes features for participant registration,
skill tracking, progress monitoring, and reporting.

Key Features:
- Participant registration and management
- Skill training program management
- Progress tracking and reporting
- Data persistence using JSON
"""

import json
import os
from datetime import datetime
from typing import Dict, List, Optional, Tuple

class Participant:
    """Represents a participant in the empowerment program."""
    
    def __init__(self, participant_id: str, name: str, age: int, contact: str, 
                 education_level: str, skills: List[str] = None):
        """
        Initialize a new participant.
        
        Args:
            participant_id: Unique identifier for the participant
            name: Full name of the participant
            age: Age of the participant
            contact: Contact information (phone/email)
            education_level: Highest education level completed
            skills: List of existing skills (optional)
        """
        self.participant_id = participant_id
        self.name = name
        self.age = age
        self.contact = contact
        self.education_level = education_level
        self.skills = skills if skills else []
        self.enrolled_programs = []
        self.completed_programs = []
        self.attendance_records = []
        self.progress_notes = []
    
    def enroll_in_program(self, program_id: str) -> None:
        """Enroll participant in a training program."""
        if program_id not in self.enrolled_programs and program_id not in self.completed_programs:
            self.enrolled_programs.append(program_id)
    
    def complete_program(self, program_id: str) -> bool:
        """
        Mark a program as completed for this participant.
        
        Returns:
            bool: True if program was successfully marked as completed, False otherwise
        """
        if program_id in self.enrolled_programs:
            self.enrolled_programs.remove(program_id)
            self.completed_programs.append(program_id)
            return True
        return False
    
    def add_skill(self, skill: str) -> None:
        """Add a new skill to the participant's profile."""
        if skill not in self.skills:
            self.skills.append(skill)
    
    def record_attendance(self, session_id: str, date: str, present: bool = True) -> None:
        """Record attendance for a training session."""
        self.attendance_records.append({
            'session_id': session_id,
            'date': date,
            'present': present
        })
    
    def add_progress_note(self, note: str, author: str) -> None:
        """Add a progress note about the participant."""
        self.progress_notes.append({
            'date': datetime.now().strftime("%Y-%m-%d"),
            'note': note,
            'author': author
        })
    
    def to_dict(self) -> Dict:
        """Convert participant data to dictionary for serialization."""
        return {
            'participant_id': self.participant_id,
            'name': self.name,
            'age': self.age,
            'contact': self.contact,
            'education_level': self.education_level,
            'skills': self.skills,
            'enrolled_programs': self.enrolled_programs,
            'completed_programs': self.completed_programs,
            'attendance_records': self.attendance_records,
            'progress_notes': self.progress_notes
        }

class TrainingProgram:
    """Represents a skill training program."""
    
    def __init__(self, program_id: str, name: str, description: str, 
                 duration_weeks: int, skills_taught: List[str], max_participants: int):
        """
        Initialize a new training program.
        
        Args:
            program_id: Unique identifier for the program
            name: Name of the program
            description: Description of the program
            duration_weeks: Duration in weeks
            skills_taught: List of skills taught in this program
            max_participants: Maximum number of participants allowed
        """
        self.program_id = program_id
        self.name = name
        self.description = description
        self.duration_weeks = duration_weeks
        self.skills_taught = skills_taught
        self.max_participants = max_participants
        self.current_participants = 0
        self.sessions = []
    
    def add_session(self, session_id: str, date: str, topic: str, instructor: str) -> None:
        """Add a training session to the program."""
        self.sessions.append({
            'session_id': session_id,
            'date': date,
            'topic': topic,
            'instructor': instructor
        })
    
    def can_enroll(self) -> bool:
        """Check if the program can accept more participants."""
        return self.current_participants < self.max_participants
    
    def increment_participants(self) -> bool:
        """
        Increment participant count if possible.
        
        Returns:
            bool: True if participant count was incremented, False if at max capacity
        """
        if self.can_enroll():
            self.current_participants += 1
            return True
        return False
    
    def to_dict(self) -> Dict:
        """Convert program data to dictionary for serialization."""
        return {
            'program_id': self.program_id,
            'name': self.name,
            'description': self.description,
            'duration_weeks': self.duration_weeks,
            'skills_taught': self.skills_taught,
            'max_participants': self.max_participants,
            'current_participants': self.current_participants,
            'sessions': self.sessions
        }

class EmpowermentProject:
    """Main class for managing the community empowerment project."""
    
    def __init__(self, data_file: str = 'empowerment_project_data.json'):
        """
        Initialize the empowerment project.
        
        Args:
            data_file: Path to JSON file for data persistence
        """
        self.data_file = data_file
        self.participants = {}  # participant_id -> Participant
        self.programs = {}      # program_id -> TrainingProgram
        
        # Load existing data if file exists
        if os.path.exists(data_file):
            self._load_data()
    
    def _load_data(self) -> None:
        """Load data from JSON file."""
        try:
            with open(self.data_file, 'r') as f:
                data = json.load(f)
                
                # Load participants
                for participant_data in data.get('participants', []):
                    participant = Participant(
                        participant_id=participant_data['participant_id'],
                        name=participant_data['name'],
                        age=participant_data['age'],
                        contact=participant_data['contact'],
                        education_level=participant_data['education_level'],
                        skills=participant_data['skills']
                    )
                    participant.enrolled_programs = participant_data['enrolled_programs']
                    participant.completed_programs = participant_data['completed_programs']
                    participant.attendance_records = participant_data['attendance_records']
                    participant.progress_notes = participant_data['progress_notes']
                    self.participants[participant.participant_id] = participant
                
                # Load programs
                for program_data in data.get('programs', []):
                    program = TrainingProgram(
                        program_id=program_data['program_id'],
                        name=program_data['name'],
                        description=program_data['description'],
                        duration_weeks=program_data['duration_weeks'],
                        skills_taught=program_data['skills_taught'],
                        max_participants=program_data['max_participants']
                    )
                    program.current_participants = program_data['current_participants']
                    program.sessions = program_data['sessions']
                    self.programs[program.program_id] = program
                    
        except (json.JSONDecodeError, KeyError) as e:
            print(f"Error loading data: {e}")
            # Start with empty data if loading fails
            self.participants = {}
            self.programs = {}
    
    def _save_data(self) -> None:
        """Save data to JSON file."""
        data = {
            'participants': [p.to_dict() for p in self.participants.values()],
            'programs': [p.to_dict() for p in self.programs.values()]
        }
        
        try:
            with open(self.data_file, 'w') as f:
                json.dump(data, f, indent=2)
        except IOError as e:
            print(f"Error saving data: {e}")
    
    def register_participant(self, name: str, age: int, contact: str, 
                            education_level: str, skills: List[str] = None) -> str:
        """
        Register a new participant.
        
        Returns:
            str: The generated participant ID
        """
        participant_id = f"P{len(self.participants) + 1:04d}"
        participant = Participant
