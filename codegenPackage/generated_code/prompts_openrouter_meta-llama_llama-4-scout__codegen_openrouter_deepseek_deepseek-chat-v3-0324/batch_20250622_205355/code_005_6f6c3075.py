"""
Generated Code Metadata:
========================
Original URL: https://debridgeadvisory.com
Prompt: "Develop a project-led training plan for upskilling a sales team in the insurance industry, with a focus on practical scenarios."
Generated: DETERMINISTIC_6f6c30756f93c629
Batch ID: 20250622_205355
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
"""
Project-Led Training Plan for Upskilling Insurance Sales Team

This module implements a practical, scenario-based training program for insurance sales teams.
It includes course modules, practical exercises, progress tracking, and feedback mechanisms.
"""

from datetime import datetime
from typing import List, Dict, Optional
import enum
import json
import random


class TrainingModule:
    """Represents a training module with practical scenarios"""
    
    def __init__(self, name: str, description: str, duration_hours: float, 
                 scenarios: List[str], prerequisites: List[str] = None):
        self.name = name
        self.description = description
        self.duration_hours = duration_hours
        self.scenarios = scenarios
        self.prerequisites = prerequisites or []
        self.created_at = datetime.now()
        self.updated_at = datetime.now()
    
    def add_scenario(self, scenario: str) -> None:
        """Add a new practical scenario to the module"""
        self.scenarios.append(scenario)
        self.updated_at = datetime.now()
    
    def to_dict(self) -> Dict:
        """Convert module to dictionary for serialization"""
        return {
            'name': self.name,
            'description': self.description,
            'duration_hours': self.duration_hours,
            'scenarios': self.scenarios,
            'prerequisites': self.prerequisites,
            'created_at': self.created_at.isoformat(),
            'updated_at': self.updated_at.isoformat()
        }


class TrainingProgress(enum.Enum):
    """Enum for tracking training progress status"""
    NOT_STARTED = "Not Started"
    IN_PROGRESS = "In Progress"
    COMPLETED = "Completed"


class TeamMember:
    """Represents a sales team member participating in training"""
    
    def __init__(self, name: str, role: str, experience_years: int):
        self.name = name
        self.role = role
        self.experience_years = experience_years
        self.completed_modules = []
        self.current_module = None
        self.progress = TrainingProgress.NOT_STARTED
        self.performance_scores = {}
    
    def start_module(self, module: TrainingModule) -> None:
        """Begin working on a training module"""
        if self.current_module and self.progress == TrainingProgress.IN_PROGRESS:
            raise ValueError("Already working on another module")
        
        self.current_module = module.name
        self.progress = TrainingProgress.IN_PROGRESS
    
    def complete_module(self, score: float) -> None:
        """Mark a module as completed with performance score"""
        if not self.current_module:
            raise ValueError("No active module to complete")
        
        self.completed_modules.append(self.current_module)
        self.performance_scores[self.current_module] = score
        self.current_module = None
        self.progress = TrainingProgress.COMPLETED
    
    def get_random_scenario(self, module: TrainingModule) -> str:
        """Get a random practical scenario from a module"""
        if not module.scenarios:
            raise ValueError("Module has no scenarios")
        return random.choice(module.scenarios)
    
    def to_dict(self) -> Dict:
        """Convert team member to dictionary for serialization"""
        return {
            'name': self.name,
            'role': self.role,
            'experience_years': self.experience_years,
            'completed_modules': self.completed_modules,
            'current_module': self.current_module,
            'progress': self.progress.value,
            'performance_scores': self.performance_scores
        }


class TrainingProgram:
    """Main class managing the training program"""
    
    def __init__(self):
        self.modules = {}
        self.team_members = {}
        self.module_dependencies = {}
    
    def add_module(self, module: TrainingModule) -> None:
        """Add a training module to the program"""
        self.modules[module.name] = module
        self.module_dependencies[module.name] = module.prerequisites
    
    def add_team_member(self, member: TeamMember) -> None:
        """Register a team member for training"""
        self.team_members[member.name] = member
    
    def get_next_module(self, member_name: str) -> Optional[TrainingModule]:
        """Get the next recommended module for a team member"""
        member = self.team_members.get(member_name)
        if not member:
            raise ValueError("Team member not found")
        
        completed = set(member.completed_modules)
        
        for module_name, module in self.modules.items():
            if (module_name not in completed and 
                all(p in completed for p in module.prerequisites)):
                return module
        
        return None
    
    def generate_training_report(self) -> Dict:
        """Generate a summary report of training progress"""
        report = {
            'total_modules': len(self.modules),
            'total_participants': len(self.team_members),
            'completion_stats': {},
            'performance_averages': {}
        }
        
        for module_name in self.modules:
            completed_count = sum(
                1 for member in self.team_members.values() 
                if module_name in member.completed_modules
            )
            report['completion_stats'][module_name] = completed_count
            
            scores = [
                member.performance_scores[module_name]
                for member in self.team_members.values()
                if module_name in member.performance_scores
            ]
            if scores:
                report['performance_averages'][module_name] = sum(scores) / len(scores)
        
        return report
    
    def save_to_file(self, filename: str) -> None:
        """Save the training program state to a file"""
        data = {
            'modules': {name: module.to_dict() for name, module in self.modules.items()},
            'team_members': {name: member.to_dict() for name, member in self.team_members.items()}
        }
        
        with open(filename, 'w') as f:
            json.dump(data, f, indent=2)
    
    def load_from_file(self, filename: str) -> None:
        """Load the training program state from a file"""
        with open(filename, 'r') as f:
            data = json.load(f)
        
        self.modules = {}
        for name, module_data in data['modules'].items():
            module = TrainingModule(
                name=module_data['name'],
                description=module_data['description'],
                duration_hours=module_data['duration_hours'],
                scenarios=module_data['scenarios'],
                prerequisites=module_data['prerequisites']
            )
            self.modules[name] = module
        
        self.team_members = {}
        for name, member_data in data['team_members'].items():
            member = TeamMember(
                name=member_data['name'],
                role=member_data['role'],
                experience_years=member_data['experience_years']
            )
            member.completed_modules = member_data['completed_modules']
            member.current_module = member_data['current_module']
            member.progress = TrainingProgress(member_data['progress'])
            member.performance_scores = member_data['performance_scores']
            self.team_members[name] = member


# Example usage
if __name__ == "__main__":
    # Create training program
    program = TrainingProgram()
    
    # Add modules with practical scenarios
    product_knowledge = TrainingModule(
        name="Insurance Product Knowledge",
        description="Deep dive into insurance products and features",
        duration_hours=8,
        scenarios=[
            "Explain term life insurance to a young professional",
            "Compare whole life vs universal life policies",
            "Handle objections about policy costs"
        ]
    )
    
    sales_techniques = TrainingModule(
        name="Advanced Sales Techniques",
        description="Practical sales methodologies for insurance",
        duration_hours=10,
        scenarios=[
            "Role-play a cold call with a reluctant prospect",
            "Demonstrate needs-based selling approach",
            "Practice closing techniques with different client types"
        ],
        prerequisites=["Insurance Product Knowledge"]
    )
    
    regulatory_compliance = TrainingModule(
        name="Regulatory Compliance",
        description="Understanding insurance regulations and ethics",
        duration_hours=6,
        scenarios=[
            "Handle a client request that violates compliance rules",
            "Explain privacy regulations to a concerned customer",
            "Document a policy sale with proper compliance checks"
        ]
    )
    
    program.add_module(product_knowledge)
    program.add_module(sales_techniques)
    program.add_module(regulatory_compliance)
    
    # Add team members
    member1 = TeamMember("John Doe", "Sales Agent", 2)
    member2 = TeamMember("Jane Smith", "Senior Sales Agent", 5)
    
    program.add_team_member(member1)
    program.add_team_member(member2)
    
    # Simulate training progress
    member1.start_module(product_knowledge)
    member1.complete_module(85.5)
    
    member2.start_module(product_knowledge)
    member2.complete_module(92.0)
    member2.start_module(sales_techniques)
    
    # Generate report
    report = program.generate_training_report()
    print(json.dumps(report, indent=2))
    
    # Save program state
    program.save_to_file("insurance_training_program.json")
```
