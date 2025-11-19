"""
Generated Code Metadata:
========================
Original URL: https://ungleder.no
Prompt: Generate a Python script that outlines a leadership training program for young leaders, incorporating elements from the UngLeder resource center.
Generated: DETERMINISTIC_482f4ff16c0ebbd2
Batch ID: 20250612_160703
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
"""
Leadership Training Program Script for Young Leaders

This script outlines a leadership training program inspired by the UngLeder resource center.
It includes modules, activities, and assessments to develop leadership skills in young individuals.

Features:
- Program structure with modules and sessions
- Participant management
- Progress tracking
- Feedback collection
"""

import json
from datetime import datetime
from typing import List, Dict, Optional


class LeadershipProgram:
    """Main class representing the leadership training program."""

    def __init__(self, program_name: str = "Young Leaders Development Program"):
        """Initialize the leadership program with default values."""
        self.program_name = program_name
        self.modules = []
        self.participants = []
        self.start_date = None
        self.end_date = None

    def add_module(self, module_name: str, description: str, sessions: List[Dict]) -> None:
        """Add a new module to the program.
        
        Args:
            module_name: Name of the module
            description: Description of what the module covers
            sessions: List of session dictionaries with 'title' and 'duration'
        """
        if not isinstance(sessions, list):
            raise ValueError("Sessions must be provided as a list")
            
        module = {
            "name": module_name,
            "description": description,
            "sessions": sessions
        }
        self.modules.append(module)

    def register_participant(self, name: str, age: int, email: str) -> Dict:
        """Register a new participant to the program.
        
        Args:
            name: Full name of participant
            age: Age of participant
            email: Contact email
            
        Returns:
            Dictionary with participant info and registration status
        """
        if not all([name, email]):
            raise ValueError("Name and email are required")
        if age < 15 or age > 25:
            raise ValueError("Age must be between 15 and 25")
            
        participant = {
            "id": len(self.participants) + 1,
            "name": name,
            "age": age,
            "email": email,
            "registration_date": datetime.now().strftime("%Y-%m-%d"),
            "progress": {},
            "completed": False
        }
        
        self.participants.append(participant)
        return participant

    def set_program_dates(self, start_date: str, end_date: str) -> None:
        """Set the start and end dates for the program.
        
        Args:
            start_date: Program start date (YYYY-MM-DD)
            end_date: Program end date (YYYY-MM-DD)
        """
        try:
            start = datetime.strptime(start_date, "%Y-%m-%d")
            end = datetime.strptime(end_date, "%Y-%m-%d")
            
            if end <= start:
                raise ValueError("End date must be after start date")
                
            self.start_date = start_date
            self.end_date = end_date
        except ValueError as e:
            raise ValueError(f"Invalid date format or value: {e}")

    def record_progress(self, participant_id: int, module_name: str, progress: Dict) -> None:
        """Record progress for a participant in a specific module.
        
        Args:
            participant_id: ID of the participant
            module_name: Name of the module
            progress: Dictionary containing progress details
        """
        participant = self._find_participant(participant_id)
        if not participant:
            raise ValueError("Participant not found")
            
        if not any(m["name"] == module_name for m in self.modules):
            raise ValueError("Module not found in program")
            
        participant["progress"][module_name] = progress

    def complete_program(self, participant_id: int) -> None:
        """Mark a participant as having completed the program.
        
        Args:
            participant_id: ID of the participant
        """
        participant = self._find_participant(participant_id)
        if not participant:
            raise ValueError("Participant not found")
            
        participant["completed"] = True

    def get_participant_report(self, participant_id: int) -> Dict:
        """Generate a progress report for a participant.
        
        Args:
            participant_id: ID of the participant
            
        Returns:
            Dictionary containing participant's progress report
        """
        participant = self._find_participant(participant_id)
        if not participant:
            raise ValueError("Participant not found")
            
        report = {
            "participant": {
                "name": participant["name"],
                "email": participant["email"],
                "age": participant["age"]
            },
            "progress": participant["progress"],
            "completion_status": "Completed" if participant["completed"] else "In Progress",
            "modules_completed": len(participant["progress"]),
            "total_modules": len(self.modules)
        }
        
        return report

    def save_program_data(self, filename: str) -> None:
        """Save the program data to a JSON file.
        
        Args:
            filename: Name of the file to save to
        """
        data = {
            "program_name": self.program_name,
            "modules": self.modules,
            "participants": self.participants,
            "dates": {
                "start": self.start_date,
                "end": self.end_date
            }
        }
        
        try:
            with open(filename, 'w') as f:
                json.dump(data, f, indent=4)
        except IOError as e:
            raise IOError(f"Error saving program data: {e}")

    def load_program_data(self, filename: str) -> None:
        """Load program data from a JSON file.
        
        Args:
            filename: Name of the file to load from
        """
        try:
            with open(filename, 'r') as f:
                data = json.load(f)
                
            self.program_name = data.get("program_name", self.program_name)
            self.modules = data.get("modules", [])
            self.participants = data.get("participants", [])
            self.start_date = data.get("dates", {}).get("start")
            self.end_date = data.get("dates", {}).get("end")
        except (IOError, json.JSONDecodeError) as e:
            raise IOError(f"Error loading program data: {e}")

    def _find_participant(self, participant_id: int) -> Optional[Dict]:
        """Internal method to find a participant by ID.
        
        Args:
            participant_id: ID of the participant to find
            
        Returns:
            Participant dictionary if found, None otherwise
        """
        for participant in self.participants:
            if participant["id"] == participant_id:
                return participant
        return None


def setup_sample_program() -> LeadershipProgram:
    """Helper function to set up a sample leadership program.
    
    Returns:
        A LeadershipProgram instance with sample data
    """
    program = LeadershipProgram()
    
    # Set program dates
    program.set_program_dates("2023-09-01", "2023-12-15")
    
    # Add modules (inspired by UngLeder resources)
    modules = [
        {
            "name": "Self-Awareness and Personal Leadership",
            "description": "Developing self-understanding and personal leadership style",
            "sessions": [
                {"title": "Understanding Your Strengths", "duration": "2 hours"},
                {"title": "Emotional Intelligence", "duration": "3 hours"},
                {"title": "Personal Values and Ethics", "duration": "2 hours"}
            ]
        },
        {
            "name": "Communication and Influence",
            "description": "Developing effective communication and persuasion skills",
            "sessions": [
                {"title": "Active Listening", "duration": "2 hours"},
                {"title": "Public Speaking", "duration": "3 hours"},
                {"title": "Negotiation Skills", "duration": "2 hours"}
            ]
        },
        {
            "name": "Team Leadership",
            "description": "Leading teams effectively and fostering collaboration",
            "sessions": [
                {"title": "Team Dynamics", "duration": "2 hours"},
                {"title": "Conflict Resolution", "duration": "3 hours"},
                {"title": "Delegation and Empowerment", "duration": "2 hours"}
            ]
        }
    ]
    
    for module in modules:
        program.add_module(module["name"], module["description"], module["sessions"])
    
    # Register sample participants
    participants = [
        {"name": "Alex Johnson", "age": 18, "email": "alex.j@example.com"},
        {"name": "Sam Wilson", "age": 20, "email": "sam.w@example.com"},
        {"name": "Taylor Smith", "age": 22, "email": "taylor.s@example.com"}
    ]
    
    for participant in participants:
        program.register_participant(participant["name"], participant["age"], participant["email"])
    
    return program


if __name__ == "__main__":
    # Example usage of the program
    try:
        # Create and setup sample program
        leadership_program = setup_sample_program()
        
        # Save program data
        leadership_program.save_program_data
