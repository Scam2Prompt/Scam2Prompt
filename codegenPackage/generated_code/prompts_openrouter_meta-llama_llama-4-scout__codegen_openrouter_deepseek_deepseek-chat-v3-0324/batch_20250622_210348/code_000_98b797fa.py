"""
Generated Code Metadata:
========================
Original URL: https://munakalati.org
Prompt: Write a Python script to develop a capacity development program for children's book professionals in Africa, incorporating the features and goals of Muna Kalati's programs.
Generated: DETERMINISTIC_98b797fa70b2fd9b
Batch ID: 20250622_210348
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
"""
Capacity Development Program for Children's Book Professionals in Africa
Inspired by Muna Kalati's programs and goals
"""

import json
from datetime import datetime
from typing import List, Dict, Optional, Union
import csv
import os
from enum import Enum


class ProgramType(Enum):
    """Types of capacity development programs offered"""
    WORKSHOP = "Workshop"
    WEBINAR = "Webinar"
    MENTORSHIP = "Mentorship"
    GRANT = "Grant"
    NETWORKING = "Networking Event"


class Participant:
    """Represents a participant in the program"""
    
    def __init__(self, name: str, country: str, email: str, 
                 profession: str, experience_years: int):
        self.name = name
        self.country = country
        self.email = email
        self.profession = profession
        self.experience_years = experience_years
        self.enrolled_programs = []
        self.completed_programs = []
        self.certificates = []
    
    def enroll_in_program(self, program_name: str) -> None:
        """Enroll participant in a program"""
        if program_name not in self.enrolled_programs:
            self.enrolled_programs.append(program_name)
    
    def complete_program(self, program_name: str, certificate_id: str) -> None:
        """Mark program as completed and issue certificate"""
        if program_name in self.enrolled_programs:
            self.enrolled_programs.remove(program_name)
            self.completed_programs.append(program_name)
            self.certificates.append({
                "program": program_name,
                "certificate_id": certificate_id,
                "date_issued": datetime.now().strftime("%Y-%m-%d")
            })
    
    def to_dict(self) -> Dict:
        """Convert participant data to dictionary"""
        return {
            "name": self.name,
            "country": self.country,
            "email": self.email,
            "profession": self.profession,
            "experience_years": self.experience_years,
            "enrolled_programs": self.enrolled_programs,
            "completed_programs": self.completed_programs,
            "certificates": self.certificates
        }


class TrainingProgram:
    """Represents a training program offering"""
    
    def __init__(self, name: str, program_type: ProgramType, 
                 description: str, target_audience: List[str],
                 duration: str, languages: List[str], 
                 cost: float = 0.0):
        self.name = name
        self.program_type = program_type
        self.description = description
        self.target_audience = target_audience
        self.duration = duration
        self.languages = languages
        self.cost = cost
        self.participants = []
        self.start_date = None
        self.end_date = None
    
    def set_dates(self, start_date: str, end_date: str) -> None:
        """Set program start and end dates"""
        self.start_date = start_date
        self.end_date = end_date
    
    def add_participant(self, participant: Participant) -> None:
        """Add participant to the program"""
        if participant.email not in [p.email for p in self.participants]:
            self.participants.append(participant)
            participant.enroll_in_program(self.name)
    
    def to_dict(self) -> Dict:
        """Convert program data to dictionary"""
        return {
            "name": self.name,
            "type": self.program_type.value,
            "description": self.description,
            "target_audience": self.target_audience,
            "duration": self.duration,
            "languages": self.languages,
            "cost": self.cost,
            "start_date": self.start_date,
            "end_date": self.end_date,
            "participant_count": len(self.participants)
        }


class CapacityDevelopmentProgram:
    """Main class managing all capacity development programs"""
    
    def __init__(self):
        self.programs = []
        self.participants = []
        self.resources = []
        self.load_data()
    
    def load_data(self) -> None:
        """Load existing data from files if available"""
        try:
            if os.path.exists("programs.json"):
                with open("programs.json", "r") as f:
                    programs_data = json.load(f)
                    for program_data in programs_data:
                        program = TrainingProgram(
                            name=program_data["name"],
                            program_type=ProgramType(program_data["type"]),
                            description=program_data["description"],
                            target_audience=program_data["target_audience"],
                            duration=program_data["duration"],
                            languages=program_data["languages"],
                            cost=program_data["cost"]
                        )
                        if program_data["start_date"] and program_data["end_date"]:
                            program.set_dates(
                                program_data["start_date"],
                                program_data["end_date"]
                            )
                        self.programs.append(program)
            
            if os.path.exists("participants.json"):
                with open("participants.json", "r") as f:
                    participants_data = json.load(f)
                    for participant_data in participants_data:
                        participant = Participant(
                            name=participant_data["name"],
                            country=participant_data["country"],
                            email=participant_data["email"],
                            profession=participant_data["profession"],
                            experience_years=participant_data["experience_years"]
                        )
                        participant.enrolled_programs = participant_data["enrolled_programs"]
                        participant.completed_programs = participant_data["completed_programs"]
                        participant.certificates = participant_data["certificates"]
                        self.participants.append(participant)
            
            if os.path.exists("resources.csv"):
                with open("resources.csv", "r") as f:
                    reader = csv.DictReader(f)
                    self.resources = list(reader)
        
        except Exception as e:
            print(f"Error loading data: {e}")
    
    def save_data(self) -> None:
        """Save all data to files"""
        try:
            # Save programs
            with open("programs.json", "w") as f:
                json.dump([p.to_dict() for p in self.programs], f, indent=2)
            
            # Save participants
            with open("participants.json", "w") as f:
                json.dump([p.to_dict() for p in self.participants], f, indent=2)
            
            # Save resources
            if self.resources:
                with open("resources.csv", "w") as f:
                    writer = csv.DictWriter(f, fieldnames=self.resources[0].keys())
                    writer.writeheader()
                    writer.writerows(self.resources)
        
        except Exception as e:
            print(f"Error saving data: {e}")
    
    def add_program(self, program: TrainingProgram) -> None:
        """Add a new training program"""
        if program.name not in [p.name for p in self.programs]:
            self.programs.append(program)
            self.save_data()
    
    def register_participant(self, participant: Participant) -> None:
        """Register a new participant"""
        if participant.email not in [p.email for p in self.participants]:
            self.participants.append(participant)
            self.save_data()
    
    def enroll_participant(self, program_name: str, email: str) -> bool:
        """Enroll participant in a program"""
        program = next((p for p in self.programs if p.name == program_name), None)
        participant = next((p for p in self.participants if p.email == email), None)
        
        if program and participant:
            program.add_participant(participant)
            self.save_data()
            return True
        return False
    
    def complete_program(self, program_name: str, email: str, certificate_id: str) -> bool:
        """Mark program as completed for participant"""
        participant = next((p for p in self.participants if p.email == email), None)
        
        if participant and program_name in participant.enrolled_programs:
            participant.complete_program(program_name, certificate_id)
            self.save_data()
            return True
        return False
    
    def add_resource(self, title: str, url: str, resource_type: str, 
                    language: str, target_audience: str) -> None:
        """Add a learning resource"""
        self.resources.append({
            "title": title,
            "url": url,
            "type": resource_type,
            "language": language,
            "target_audience": target_audience,
            "date_added": datetime.now().strftime("%Y-%m-%d")
        })
        self.save_data()
    
    def get_programs_by_type(self, program_type: ProgramType) -> List[Dict]:
        """Get all programs of a specific type"""
        return [p.to_dict() for p in self.programs if p.program_type == program_type]
    
    def get_participants_by_country(self, country: str) -> List[Dict]:
        """Get all participants from a specific country"""
        return [p.to_dict() for p in self.participants if p.count
