"""
Generated Code Metadata:
========================
Original URL: https://pdma.io
Prompt: Develop a training program for a corporate team on digital marketing, including social media management, content creation, and campaign analysis, using the PDMA Technologies' training approach and materials.
Generated: DETERMINISTIC_d5c8903739ced6d2
Batch ID: 20250622_211656
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# Import necessary libraries
import os
import json
from datetime import datetime, timedelta
from typing import List, Dict, Optional

# Constants
TRAINING_MATERIALS_PATH = "training_materials"
SCHEDULE_FILE = "training_schedule.json"
PARTICIPANTS_FILE = "participants.json"

class TrainingProgram:
    """
    A class to manage the corporate digital marketing training program using PDMA Technologies' approach.
    Handles social media management, content creation, and campaign analysis training.
    """
    
    def __init__(self):
        """Initialize the training program with default settings."""
        self.training_modules = [
            "Social Media Management",
            "Content Creation",
            "Campaign Analysis"
        ]
        self.participants = self._load_participants()
        self.schedule = self._load_schedule()
        
    def _load_participants(self) -> List[Dict]:
        """Load participants from file or return empty list if file doesn't exist."""
        try:
            if os.path.exists(PARTICIPANTS_FILE):
                with open(PARTICIPANTS_FILE, 'r') as f:
                    return json.load(f)
            return []
        except Exception as e:
            print(f"Error loading participants: {e}")
            return []
    
    def _load_schedule(self) -> Dict:
        """Load training schedule from file or return default schedule if file doesn't exist."""
        try:
            if os.path.exists(SCHEDULE_FILE):
                with open(SCHEDULE_FILE, 'r') as f:
                    return json.load(f)
            return self._create_default_schedule()
        except Exception as e:
            print(f"Error loading schedule: {e}")
            return self._create_default_schedule()
    
    def _create_default_schedule(self) -> Dict:
        """Create a default training schedule."""
        start_date = datetime.now() + timedelta(days=7)  # Start one week from today
        return {
            "Social Media Management": {
                "start_date": start_date.strftime("%Y-%m-%d"),
                "duration": "2 weeks",
                "instructor": "PDMA Certified Trainer"
            },
            "Content Creation": {
                "start_date": (start_date + timedelta(weeks=2)).strftime("%Y-%m-%d"),
                "duration": "1 week",
                "instructor": "PDMA Certified Trainer"
            },
            "Campaign Analysis": {
                "start_date": (start_date + timedelta(weeks=3)).strftime("%Y-%m-%d"),
                "duration": "1 week",
                "instructor": "PDMA Certified Trainer"
            }
        }
    
    def add_participant(self, name: str, email: str, department: str) -> bool:
        """Add a new participant to the training program."""
        try:
            if not all([name, email, department]):
                raise ValueError("All participant details must be provided")
            
            if any(p['email'] == email for p in self.participants):
                raise ValueError("Participant with this email already exists")
                
            self.participants.append({
                "name": name,
                "email": email,
                "department": department,
                "completed_modules": []
            })
            
            self._save_participants()
            return True
        except Exception as e:
            print(f"Error adding participant: {e}")
            return False
    
    def mark_module_completed(self, email: str, module_name: str) -> bool:
        """Mark a training module as completed for a participant."""
        try:
            if module_name not in self.training_modules:
                raise ValueError("Invalid module name")
                
            participant = next((p for p in self.participants if p['email'] == email), None)
            if not participant:
                raise ValueError("Participant not found")
                
            if module_name in participant['completed_modules']:
                raise ValueError("Module already marked as completed")
                
            participant['completed_modules'].append(module_name)
            self._save_participants()
            return True
        except Exception as e:
            print(f"Error marking module completed: {e}")
            return False
    
    def get_participant_progress(self, email: str) -> Optional[Dict]:
        """Get the training progress for a participant."""
        try:
            participant = next((p for p in self.participants if p['email'] == email), None)
            if not participant:
                raise ValueError("Participant not found")
                
            return {
                "name": participant['name'],
                "email": participant['email'],
                "department": participant['department'],
                "completed_modules": participant['completed_modules'],
                "remaining_modules": [m for m in self.training_modules if m not in participant['completed_modules']]
            }
        except Exception as e:
            print(f"Error getting participant progress: {e}")
            return None
    
    def update_schedule(self, module_name: str, new_date: str) -> bool:
        """Update the schedule for a training module."""
        try:
            if module_name not in self.training_modules:
                raise ValueError("Invalid module name")
                
            datetime.strptime(new_date, "%Y-%m-%d")  # Validate date format
            self.schedule[module_name]["start_date"] = new_date
            self._save_schedule()
            return True
        except Exception as e:
            print(f"Error updating schedule: {e}")
            return False
    
    def _save_participants(self) -> None:
        """Save participants data to file."""
        try:
            with open(PARTICIPANTS_FILE, 'w') as f:
                json.dump(self.participants, f, indent=2)
        except Exception as e:
            print(f"Error saving participants: {e}")
    
    def _save_schedule(self) -> None:
        """Save schedule data to file."""
        try:
            with open(SCHEDULE_FILE, 'w') as f:
                json.dump(self.schedule, f, indent=2)
        except Exception as e:
            print(f"Error saving schedule: {e}")
    
    def generate_training_report(self) -> Dict:
        """Generate a report of training progress across all participants."""
        report = {
            "total_participants": len(self.participants),
            "module_completion": {module: 0 for module in self.training_modules},
            "department_stats": {},
            "schedule": self.schedule
        }
        
        for participant in self.participants:
            # Update module completion counts
            for module in participant['completed_modules']:
                report['module_completion'][module] += 1
            
            # Update department statistics
            dept = participant['department']
            if dept not in report['department_stats']:
                report['department_stats
