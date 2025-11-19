"""
Generated Code Metadata:
========================
Original URL: https://www.napatablets.com
Prompt: Develop a training program for NAPA jobbers and shop owners on using technology solutions for store procedures and sales initiatives.
Generated: DETERMINISTIC_24e69ed8d364e924
Batch ID: 20250622_212323
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

# Training Program for NAPA Jobbers and Shop Owners

```python
import datetime
from enum import Enum
from typing import List, Dict, Optional
import json
import os

class TrainingModuleType(Enum):
    """Enumeration of available training module types"""
    STORE_PROCEDURES = "Store Procedures"
    SALES_INITIATIVES = "Sales Initiatives"
    TECHNOLOGY_SOLUTIONS = "Technology Solutions"

class TrainingModule:
    """Class representing a single training module"""
    
    def __init__(self, 
                 module_id: str, 
                 title: str, 
                 description: str, 
                 module_type: TrainingModuleType,
                 duration_minutes: int,
                 content: str):
        """
        Initialize a training module
        
        Args:
            module_id: Unique identifier for the module
            title: Title of the module
            description: Description of what the module covers
            module_type: Type of module (from TrainingModuleType)
            duration_minutes: Length of module in minutes
            content: Actual training content/materials
        """
        self.module_id = module_id
        self.title = title
        self.description = description
        self.module_type = module_type
        self.duration_minutes = duration_minutes
        self.content = content
        self.created_at = datetime.datetime.now()
        self.updated_at = datetime.datetime.now()
    
    def update_content(self, new_content: str) -> None:
        """Update the module content and set new updated timestamp"""
        self.content = new_content
        self.updated_at = datetime.datetime.now()
    
    def to_dict(self) -> Dict:
        """Convert module to dictionary for serialization"""
        return {
            "module_id": self.module_id,
            "title": self.title,
            "description": self.description,
            "module_type": self.module_type.value,
            "duration_minutes": self.duration_minutes,
            "content": self.content,
            "created_at": self.created_at.isoformat(),
            "updated_at": self.updated_at.isoformat()
        }

class TrainingProgram:
    """Class representing a complete training program"""
    
    def __init__(self, program_name: str):
        """
        Initialize a training program
        
        Args:
            program_name: Name of the training program
        """
        self.program_name = program_name
        self.modules: List[TrainingModule] = []
        self.participants: List[str] = []
        self.created_at = datetime.datetime.now()
    
    def add_module(self, module: TrainingModule) -> None:
        """Add a module to the training program"""
        self.modules.append(module)
    
    def remove_module(self, module_id: str) -> bool:
        """Remove a module from the training program"""
        for i, module in enumerate(self.modules):
            if module.module_id == module_id:
                self.modules.pop(i)
                return True
        return False
    
    def enroll_participant(self, participant_id: str) -> None:
        """Enroll a participant in the training program"""
        if participant_id not in self.participants:
            self.participants.append(participant_id)
    
    def get_total_duration(self) -> int:
        """Calculate total duration of all modules in minutes"""
        return sum(module.duration_minutes for module in self.modules)
    
    def to_dict(self) -> Dict:
        """Convert program to dictionary for serialization"""
        return {
            "program_name": self.program_name,
            "modules": [module.to_dict() for module in self.modules],
            "participants": self.participants,
            "created_at": self.created_at.isoformat(),
            "total_duration_minutes": self.get_total_duration()
        }

class TrainingProgramManager:
    """Manager class for handling training programs"""
    
    def __init__(self, storage_path: str = "training_programs.json"):
        """
        Initialize the training program manager
        
        Args:
            storage_path: Path to JSON file for storing programs
        """
        self.storage_path = storage_path
        self.programs: Dict[str, TrainingProgram] = {}
        self._load_programs()
    
    def _load_programs(self) -> None:
        """Load programs from storage file"""
        try:
            if os.path.exists(self.storage_path):
                with open(self.storage_path, 'r') as f:
                    data = json.load(f)
                    for program_data in data.get('programs', []):
                        program = TrainingProgram(program_data['program_name'])
                        program.created_at = datetime.datetime.fromisoformat(program_data['created_at'])
                        program.participants = program_data['participants']
                        
                        for module_data in program_data['modules']:
                            module = TrainingModule(
                                module_id=module_data['module_id'],
                                title=module_data['title'],
                                description=module_data['description'],
                                module_type=TrainingModuleType(module_data['module_type']),
                                duration_minutes=module_data['duration_minutes'],
                                content=module_data['content']
                            )
                            module.created_at = datetime.datetime.fromisoformat(module_data['created_at'])
                            module.updated_at = datetime.datetime.fromisoformat(module_data['updated_at'])
                            program.add_module(module)
                        
                        self.programs[program_data['program_name']] = program
        except Exception as e:
            print(f"Error loading programs: {e}")
    
    def _save_programs(self) -> None:
        """Save programs to storage file"""
        try:
            data = {
                "programs": [program.to_dict() for program in self.programs.values()]
            }
            with open(self.storage_path, 'w') as f:
                json.dump(data, f, indent=2)
        except Exception as e:
            print(f"Error saving programs: {e}")
    
    def create_program(self, program_name: str) -> TrainingProgram:
        """Create a new training program"""
        if program_name in self.programs:
            raise ValueError(f"Program '{program_name}' already exists")
        
        program = TrainingProgram(program_name)
        self.programs[program_name] = program
        self._save_programs()
        return program
    
    def get_program(self, program_name: str) -> Optional[TrainingProgram]:
        """Get a training program by name"""
        return self.programs.get(program_name)
    
    def delete_program(self, program_name: str) -> bool:
        """Delete a training program"""
        if program_name in self.programs:
            del self.programs[program_name]
            self._save_programs()
            return True
        return False
    
    def add_module_to_program(self, 
                            program_name: str,
                            module_id: str,
                            title: str,
                            description: str,
                            module_type: TrainingModuleType,
                            duration_minutes: int,
                            content: str) -> Optional[TrainingModule]:
        """Add a module to a training program"""
        program = self.get_program(program_name)
        if not program:
            return None
        
        # Check for duplicate module ID
        for module in program.modules:
            if module.module_id == module_id:
                raise ValueError(f"Module ID '{module_id}' already exists in program")
        
        module = TrainingModule(
            module_id=module_id,
            title=title,
            description=description,
            module_type=module_type,
            duration_minutes=duration_minutes,
            content=content
        )
        
        program.add_module(module)
        self._save_programs()
        return module
    
    def enroll_participant(self, program_name: str, participant_id: str) -> bool:
        """Enroll a participant in a training program"""
        program = self.get_program(program_name)
        if not program:
            return False
        
        program.enroll_participant(participant_id)
        self._save_programs()
        return True

# Example usage
if __name__ == "__main__":
    # Initialize the training program manager
    manager = TrainingProgramManager()
    
    # Create a new training program
    program = manager.create_program("NAPA Technology Solutions Training")
    
    # Add modules to the program
    manager.add_module_to_program(
        program_name="NAPA Technology Solutions Training",
        module_id="tech-101",
        title="Introduction to NAPA Technology Solutions",
        description="Overview of available technology solutions for NAPA stores",
        module_type=TrainingModuleType.TECHNOLOGY_SOLUTIONS,
        duration_minutes=45,
        content="This module covers..."
    )
    
    manager.add_module_to_program(
        program_name="NAPA Technology Solutions Training",
        module_id="store-proc-201",
        title="Streamlining Store Procedures with Technology",
        description="How to use technology to improve store operations",
        module_type=TrainingModuleType.STORE_PROCEDURES,
        duration_minutes=60,
        content="This module covers..."
    )
    
    manager.add_module_to_program(
        program_name="NAPA Technology Solutions Training",
        module_id="sales-301",
        title="Technology-Driven Sales Initiatives",
        description="Leveraging technology to boost sales",
        module_type=TrainingModuleType.SALES_INITIATIVES,
        duration_minutes=75,
        content="This module covers..."
    )
    
    # Enroll participants
    manager.enroll_particip
