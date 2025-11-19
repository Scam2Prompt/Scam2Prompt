"""
Generated Code Metadata:
========================
Original URL: https://www.gbngroup.com.mx
Prompt: "Design a training program for developing social skills in the workplace, inspired by GBN Group's capacitación programs."
Generated: DETERMINISTIC_9f0687d38441f252
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
Social Skills Training Program for the Workplace
Inspired by GBN Group's Capacitación Programs

This program provides a structured training curriculum to develop social skills
in a workplace environment through modules, assessments, and progress tracking.
"""

from datetime import datetime
from typing import List, Dict, Optional
import json
import os
import random

class TrainingProgram:
    """Main class representing the social skills training program."""
    
    def __init__(self):
        self.modules = self._load_modules()
        self.participants = {}
        self.assessments = {}
        
    def _load_modules(self) -> List[Dict]:
        """Load training modules from JSON file."""
        try:
            with open('modules.json', 'r') as f:
                return json.load(f)
        except FileNotFoundError:
            print("Warning: modules.json not found. Using default modules.")
            return self._get_default_modules()
        except json.JSONDecodeError:
            print("Error: Invalid JSON in modules.json. Using default modules.")
            return self._get_default_modules()
    
    def _get_default_modules(self) -> List[Dict]:
        """Return default training modules if custom ones aren't available."""
        return [
            {
                "id": 1,
                "title": "Effective Communication",
                "description": "Learn to express ideas clearly and listen actively",
                "duration": 2,
                "exercises": [
                    "Active listening practice",
                    "Clear messaging drills",
                    "Non-verbal communication awareness"
                ]
            },
            {
                "id": 2,
                "title": "Team Collaboration",
                "description": "Develop skills for working effectively in teams",
                "duration": 3,
                "exercises": [
                    "Role-playing team scenarios",
                    "Conflict resolution simulations",
                    "Group problem-solving activities"
                ]
            },
            {
                "id": 3,
                "title": "Emotional Intelligence",
                "description": "Understand and manage emotions in the workplace",
                "duration": 2,
                "exercises": [
                    "Self-awareness assessments",
                    "Empathy building exercises",
                    "Stress management techniques"
                ]
            }
        ]
    
    def add_participant(self, name: str, email: str, department: str) -> bool:
        """Register a new participant in the training program."""
        if not all([name, email, department]):
            return False
            
        if email in self.participants:
            print(f"Participant with email {email} already exists.")
            return False
            
        self.participants[email] = {
            "name": name,
            "department": department,
            "registration_date": datetime.now().strftime("%Y-%m-%d"),
            "completed_modules": [],
            "current_module": None,
            "progress": 0
        }
        return True
    
    def enroll_in_module(self, email: str, module_id: int) -> bool:
        """Enroll a participant in a specific module."""
        if email not in self.participants:
            print(f"Participant with email {email} not found.")
            return False
            
        module = next((m for m in self.modules if m["id"] == module_id), None)
        if not module:
            print(f"Module with ID {module_id} not found.")
            return False
            
        self.participants[email]["current_module"] = module_id
        self.participants[email]["progress"] = 0
        return True
    
    def record_progress(self, email: str, progress: int) -> bool:
        """Update a participant's progress in their current module."""
        if email not in self.participants:
            print(f"Participant with email {email} not found.")
            return False
            
        if self.participants[email]["current_module"] is None:
            print("Participant is not enrolled in any module.")
            return False
            
        if progress < 0 or progress > 100:
            print("Progress must be between 0 and 100.")
            return False
            
        self.participants[email]["progress"] = progress
        
        if progress == 100:
            self._complete_module(email)
            
        return True
    
    def _complete_module(self, email: str) -> None:
        """Mark a module as completed for a participant."""
        module_id = self.participants[email]["current_module"]
        self.participants[email]["completed_modules"].append(module_id)
        self.participants[email]["current_module"] = None
        self.participants[email]["progress"] = 0
        
    def generate_assessment(self, email: str) -> Optional[Dict]:
        """Generate a skills assessment for a participant."""
        if email not in self.participants:
            print(f"Participant with email {email} not found.")
            return None
            
        completed = self.participants[email]["completed_modules"]
        if not completed:
            print("Participant hasn't completed any modules yet.")
            return None
            
        assessment = {
            "participant": self.participants[email]["name"],
            "date": datetime.now().strftime("%Y-%m-%d"),
            "modules_completed": len(completed),
            "skills": {}
        }
        
        for module_id in completed:
            module = next(m for m in self.modules if m["id"] == module_id)
            assessment["skills"][module["title"]] = random.randint(70, 100)
            
        self.assessments[email] = assessment
        return assessment
    
    def save_data(self) -> None:
        """Save program data to files."""
        try:
            with open('participants.json', 'w') as f:
                json.dump(self.participants, f, indent=2)
                
            with open('assessments.json', 'w') as f:
                json.dump(self.assessments, f, indent=2)
        except IOError as e:
            print(f"Error saving data: {e}")
    
    def load_data(self) -> None:
        """Load program data from files."""
        try:
            with open('participants.json', 'r') as f:
                self.participants = json.load(f)
        except (FileNotFoundError, json.JSONDecodeError):
            self.participants = {}
            
        try:
            with open('assessments.json', 'r') as f:
                self.assessments = json.load(f)
        except (FileNotFoundError, json.JSONDecodeError):
            self.assessments = {}


def main():
    """Run the social skills training program."""
    program = TrainingProgram()
    program.load_data()
    
    # Example usage
    program.add_participant("John Doe", "john@example.com", "Marketing")
    program.enroll_in_module("john@example.com", 1)
    program.record_progress("john@example.com", 100)
    assessment = program.generate_assessment("john@example.com")
    
    program.save_data()


if __name__ == "__main__":
    main()
```
