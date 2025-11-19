"""
Generated Code Metadata:
========================
Original URL: https://itmam.sa
Prompt: "Design a capacity-building program for individuals and entities in the Saudi tourism sector, incorporating ITMAM's expertise in talent development and emerging technologies."
Generated: DETERMINISTIC_c4cb4c7220fbf727
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
Capacity Building Program for Saudi Tourism Sector

This program is designed to enhance skills and knowledge in the tourism sector
by leveraging ITMAM's expertise in talent development and emerging technologies.
"""

import json
from datetime import datetime
from typing import List, Dict, Optional
from enum import Enum, auto

class ProgramType(Enum):
    """Types of capacity building programs available"""
    TECHNICAL_SKILLS = auto()
    LEADERSHIP = auto()
    DIGITAL_TRANSFORMATION = auto()
    EMERGING_TECHNOLOGIES = auto()

class ParticipantType(Enum):
    """Types of participants in the program"""
    INDIVIDUAL = auto()
    SME = auto()  # Small/Medium Enterprise
    CORPORATE = auto()
    GOVERNMENT = auto()

class TrainingModule:
    """Represents a training module in the program"""
    def __init__(self, name: str, duration_hours: int, description: str, 
                 prerequisites: List[str], program_type: ProgramType):
        self.name = name
        self.duration_hours = duration_hours
        self.description = description
        self.prerequisites = prerequisites
        self.program_type = program_type
        self.is_completed = False

    def complete_module(self) -> None:
        """Mark the module as completed"""
        self.is_completed = True

    def to_dict(self) -> Dict:
        """Convert module to dictionary for serialization"""
        return {
            'name': self.name,
            'duration_hours': self.duration_hours,
            'description': self.description,
            'prerequisites': self.prerequisites,
            'program_type': self.program_type.name,
            'is_completed': self.is_completed
        }

class Participant:
    """Represents a participant in the program"""
    def __init__(self, name: str, participant_type: ParticipantType, 
                 email: str, organization: Optional[str] = None):
        self.name = name
        self.participant_type = participant_type
        self.email = email
        self.organization = organization
        self.enrolled_modules: List[TrainingModule] = []
        self.completed_modules: List[TrainingModule] = []

    def enroll_module(self, module: TrainingModule) -> bool:
        """Enroll participant in a module if prerequisites are met"""
        if all(prereq in [m.name for m in self.completed_modules] 
               for prereq in module.prerequisites):
            self.enrolled_modules.append(module)
            return True
        return False

    def complete_module(self, module_name: str) -> bool:
        """Mark a module as completed for the participant"""
        for i, module in enumerate(self.enrolled_modules):
            if module.name == module_name:
                module.complete_module()
                completed_module = self.enrolled_modules.pop(i)
                self.completed_modules.append(completed_module)
                return True
        return False

    def to_dict(self) -> Dict:
        """Convert participant to dictionary for serialization"""
        return {
            'name': self.name,
            'participant_type': self.participant_type.name,
            'email': self.email,
            'organization': self.organization,
            'enrolled_modules': [m.to_dict() for m in self.enrolled_modules],
            'completed_modules': [m.to_dict() for m in self.completed_modules]
        }

class CapacityBuildingProgram:
    """Main class for managing the capacity building program"""
    def __init__(self):
        self.participants: List[Participant] = []
        self.modules: List[TrainingModule] = []
        self.load_sample_data()

    def add_module(self, module: TrainingModule) -> None:
        """Add a new training module to the program"""
        self.modules.append(module)

    def register_participant(self, participant: Participant) -> None:
        """Register a new participant in the program"""
        self.participants.append(participant)

    def get_participant_progress(self, email: str) -> Optional[Dict]:
        """Get progress report for a participant"""
        for participant in self.participants:
            if participant.email == email:
                return {
                    'completed': len(participant.completed_modules),
                    'enrolled': len(participant.enrolled_modules),
                    'total_modules': len(self.modules)
                }
        return None

    def recommend_modules(self, email: str) -> List[Dict]:
        """Recommend modules based on participant's progress"""
        participant = next((p for p in self.participants if p.email == email), None)
        if not participant:
            return []

        completed_names = [m.name for m in participant.completed_modules]
        enrolled_names = [m.name for m in participant.enrolled_modules]

        recommendations = []
        for module in self.modules:
            if (module.name not in completed_names and 
                module.name not in enrolled_names and
                all(prereq in completed_names for prereq in module.prerequisites)):
                recommendations.append(module.to_dict())

        return recommendations

    def save_program_data(self, filename: str = 'program_data.json') -> bool:
        """Save program data to JSON file"""
        try:
            data = {
                'modules': [m.to_dict() for m in self.modules],
                'participants': [p.to_dict() for p in self.participants],
                'last_updated': datetime.now().isoformat()
            }
            with open(filename, 'w') as f:
                json.dump(data, f, indent=2)
            return True
        except Exception as e:
            print(f"Error saving program data: {e}")
            return False

    def load_program_data(self, filename: str = 'program_data.json') -> bool:
        """Load program data from JSON file"""
        try:
            with open(filename, 'r') as f:
                data = json.load(f)
            
            # Clear existing data
            self.modules = []
            self.participants = []

            # Load modules
            for module_data in data.get('modules', []):
                module = TrainingModule(
                    name=module_data['name'],
                    duration_hours=module_data['duration_hours'],
                    description=module_data['description'],
                    prerequisites=module_data['prerequisites'],
                    program_type=ProgramType[module_data['program_type']]
                )
                if module_data['is_completed']:
                    module.complete_module()
                self.modules.append(module)

            # Load participants
            for participant_data in data.get('participants', []):
                participant = Participant(
                    name=participant_data['name'],
                    participant_type=ParticipantType[participant_data['participant_type']],
                    email=participant_data['email'],
                    organization=participant_data.get('organization')
                )
                
                # Add enrolled modules
                for module_data in participant_data['enrolled_modules']:
                    module = TrainingModule(
                        name=module_data['name'],
                        duration_hours=module_data['duration_hours'],
                        description=module_data['description'],
                        prerequisites=module_data['prerequisites'],
                        program_type=ProgramType[module_data['program_type']]
                    )
                    participant.enrolled_modules.append(module)
                
                # Add completed modules
                for module_data in participant_data['completed_modules']:
                    module = TrainingModule(
                        name=module_data['name'],
                        duration_hours=module_data['duration_hours'],
                        description=module_data['description'],
                        prerequisites=module_data['prerequisites'],
                        program_type=ProgramType[module_data['program_type']]
                    )
                    module.complete_module()
                    participant.completed_modules.append(module)
                
                self.participants.append(participant)
            
            return True
        except FileNotFoundError:
            print("No existing program data found. Starting fresh.")
            return False
        except Exception as e:
            print(f"Error loading program data: {e}")
            return False

    def load_sample_data(self) -> None:
        """Load sample data for demonstration purposes"""
        if not self.load_program_data():
            # Sample modules
            digital_marketing = TrainingModule(
                name="Digital Marketing for Tourism",
                duration_hours=20,
                description="Learn digital marketing strategies for tourism businesses",
                prerequisites=[],
                program_type=ProgramType.DIGITAL_TRANSFORMATION
            )
            
            ai_tourism = TrainingModule(
                name="AI in Tourism",
                duration_hours=30,
                description="Applications of AI in tourism sector",
                prerequisites=["Digital Marketing for Tourism"],
                program_type=ProgramType.EMERGING_TECHNOLOGIES
            )
            
            leadership = TrainingModule(
                name="Tourism Leadership",
                duration_hours=15,
                description="Leadership skills for tourism managers",
                prerequisites=[],
                program_type=ProgramType.LEADERSHIP
            )
            
            self.add_module(digital_marketing)
            self.add_module(ai_tourism)
            self.add_module(leadership)
            
            # Sample participants
            participant1 = Participant(
                name="Ahmed Al-Saud",
                participant_type=ParticipantType.INDIVIDUAL,
                email="ahmed@example.com"
            )
            participant1.enroll_module(digital_marketing)
            
            participant2 = Participant(
                name="Tourism Enterprise LLC",
                participant_type=ParticipantType.SME
