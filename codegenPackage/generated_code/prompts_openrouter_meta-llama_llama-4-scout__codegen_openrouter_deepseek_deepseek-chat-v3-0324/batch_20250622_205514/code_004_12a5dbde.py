"""
Generated Code Metadata:
========================
Original URL: https://cartenoir.org
Prompt: "Create a training program for project managers on effective risk management and health and safety protocols, based on the services offered by Carte Noir Consulting."
Generated: DETERMINISTIC_12a5dbdee64e2986
Batch ID: 20250622_205514
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
"""
Project Manager Training Program - Risk Management & Health/Safety Protocols
Based on Carte Noir Consulting Services
"""

import datetime
from enum import Enum
from typing import List, Dict, Optional
import json
import random

class TrainingModuleType(Enum):
    RISK_MANAGEMENT = "Risk Management"
    HEALTH_SAFETY = "Health & Safety"

class TrainingModule:
    """Represents a training module with content and assessments"""
    
    def __init__(self, module_id: str, title: str, module_type: TrainingModuleType, 
                 content: str, duration_minutes: int, assessment_questions: List[Dict]):
        self.module_id = module_id
        self.title = title
        self.module_type = module_type
        self.content = content
        self.duration_minutes = duration_minutes
        self.assessment_questions = assessment_questions
        self.completed = False
        self.completion_date = None
    
    def mark_completed(self) -> None:
        """Mark module as completed with current date"""
        self.completed = True
        self.completion_date = datetime.date.today()
    
    def take_assessment(self) -> float:
        """Simulate taking the assessment and return score"""
        if not self.completed:
            raise ValueError("Module must be completed before assessment")
        
        correct = 0
        for question in self.assessment_questions:
            # Simulate user answering randomly
            user_answer = random.choice(question['options'])
            if user_answer == question['correct_answer']:
                correct += 1
        
        return correct / len(self.assessment_questions) * 100

class TrainingProgram:
    """Manages a collection of training modules"""
    
    def __init__(self, program_name: str):
        self.program_name = program_name
        self.modules: List[TrainingModule] = []
        self.participants: Dict[str, Dict] = {}  # email: {name, progress}
    
    def add_module(self, module: TrainingModule) -> None:
        """Add a training module to the program"""
        self.modules.append(module)
    
    def register_participant(self, name: str, email: str) -> None:
        """Register a new participant"""
        if email in self.participants:
            raise ValueError("Participant already registered")
        self.participants[email] = {
            'name': name,
            'progress': {m.module_id: False for m in self.modules},
            'scores': {}
        }
    
    def complete_module(self, email: str, module_id: str) -> float:
        """Mark module as completed and return assessment score"""
        if email not in self.participants:
            raise ValueError("Participant not found")
        
        module = next((m for m in self.modules if m.module_id == module_id), None)
        if not module:
            raise ValueError("Module not found")
        
        module.mark_completed()
        score = module.take_assessment()
        
        self.participants[email]['progress'][module_id] = True
        self.participants[email]['scores'][module_id] = score
        
        return score
    
    def get_progress(self, email: str) -> Dict:
        """Get participant's progress report"""
        if email not in self.participants:
            raise ValueError("Participant not found")
        
        completed = sum(self.participants[email]['progress'].values())
        total = len(self.modules)
        avg_score = sum(self.participants[email]['scores'].values()) / completed if completed > 0 else 0
        
        return {
            'name': self.participants[email]['name'],
            'completed_modules': completed,
            'total_modules': total,
            'completion_percentage': (completed / total) * 100,
            'average_score': avg_score,
            'module_details': [
                {
                    'module_id': m.module_id,
                    'title': m.title,
                    'completed': self.participants[email]['progress'][m.module_id],
                    'score': self.participants[email]['scores'].get(m.module_id, 0)
                } for m in self.modules
            ]
        }

def load_sample_modules() -> List[TrainingModule]:
    """Create sample training modules based on Carte Noir Consulting services"""
    modules = [
        TrainingModule(
            module_id="RM101",
            title="Fundamentals of Risk Management",
            module_type=TrainingModuleType.RISK_MANAGEMENT,
            content="""This module covers the basic principles of risk management including:
- Risk identification techniques
- Risk assessment methodologies
- Risk mitigation strategies
- Monitoring and review processes""",
            duration_minutes=60,
            assessment_questions=[
                {
                    "question": "What is the first step in risk management?",
                    "options": ["Risk mitigation", "Risk identification", "Risk monitoring", "Risk assessment"],
                    "correct_answer": "Risk identification"
                },
                {
                    "question": "Which tool is commonly used for risk assessment?",
                    "options": ["Gantt chart", "Risk matrix", "PERT chart", "Kanban board"],
                    "correct_answer": "Risk matrix"
                }
            ]
        ),
        TrainingModule(
            module_id="RM201",
            title="Advanced Risk Analysis Techniques",
            module_type=TrainingModuleType.RISK_MANAGEMENT,
            content="""Advanced techniques for risk analysis including:
- Quantitative risk analysis
- Qualitative risk analysis
- Monte Carlo simulations
- Decision tree analysis""",
            duration_minutes=90,
            assessment_questions=[
                {
                    "question": "Which technique uses random sampling for risk analysis?",
                    "options": ["Decision tree", "Monte Carlo", "Sensitivity analysis", "SWOT analysis"],
                    "correct_answer": "Monte Carlo"
                },
                {
                    "question": "What does a decision tree help visualize?",
                    "options": ["Project timeline", "Risk probabilities and outcomes", "Team structure", "Budget allocation"],
                    "correct_answer": "Risk probabilities and outcomes"
                }
            ]
        ),
        TrainingModule(
            module_id="HS101",
            title="Workplace Health & Safety Fundamentals",
            module_type=TrainingModuleType.HEALTH_SAFETY,
            content="""Essential health and safety protocols including:
- Legal requirements and compliance
- Hazard identification
- Safety equipment and procedures
- Emergency response planning""",
            duration_minutes=75,
            assessment_questions=[
                {
                    "question": "What is the primary purpose of a risk assessment in health and safety?",
                    "options": ["To reduce insurance costs", "To identify potential hazards", "To increase productivity", "To document procedures"],
                    "correct_answer": "To identify potential hazards"
                },
                {
                    "question": "Which regulation governs workplace health and safety in most countries?",
                    "options": ["GDPR", "OSHA", "ISO 9001", "Six Sigma"],
                    "correct_answer": "OSHA"
                }
            ]
        ),
        TrainingModule(
            module_id="HS201",
            title="Implementing Safety Management Systems",
            module_type=TrainingModuleType.HEALTH_SAFETY,
            content="""Implementing comprehensive safety management systems:
- Safety policy development
- Safety performance metrics
- Continuous improvement processes
- Safety culture development""",
            duration_minutes=80,
            assessment_questions=[
                {
                    "question": "What is a key component of a safety management system?",
                    "options": ["Safety policy", "Marketing strategy", "Financial reporting", "Customer feedback"],
                    "correct_answer": "Safety policy"
                },
                {
                    "question": "What does SMS stand for in safety management?",
                    "options": ["Safety Management System", "Security Monitoring Service", "Standard Measurement Scale", "Systematic Maintenance Schedule"],
                    "correct_answer": "Safety Management System"
                }
            ]
        )
    ]
    return modules

def initialize_training_program() -> TrainingProgram:
    """Initialize a training program with sample modules"""
    program = TrainingProgram("Carte Noir Project Manager Certification")
    
    for module in load_sample_modules():
        program.add_module(module)
    
    return program

def save_program_state(program: TrainingProgram, filename: str) -> None:
    """Save program state to JSON file"""
    state = {
        'program_name': program.program_name,
        'modules': [
            {
                'module_id': m.module_id,
                'title': m.title,
                'module_type': m.module_type.value,
                'content': m.content,
                'duration_minutes': m.duration_minutes,
                'assessment_questions': m.assessment_questions,
                'completed': m.completed,
                'completion_date': str(m.completion_date) if m.completion_date else None
            } for m in program.modules
        ],
        'participants': program.participants
    }
    
    with open(filename, 'w') as f:
        json.dump(state, f, indent=2)

def load_program_state(filename: str) -> TrainingProgram:
    """Load program state from JSON file"""
    with open(filename, 'r') as f:
        state = json.load(f)
    
    program = TrainingProgram(state['program_name'])
    
    for module
