"""
Generated Code Metadata:
========================
Original URL: https://bufordsecurityblog.com
Prompt: "Generate a training plan for new security guards, including essential qualities and skills for success in the field."
Generated: DETERMINISTIC_766eea68cfa723fe
Batch ID: 20250622_210650
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
"""
Security Guard Training Plan Generator
This script generates a structured training plan for new security guards,
including essential qualities and skills needed for success in the field.
"""

from dataclasses import dataclass
from typing import List, Dict
import json
from datetime import timedelta, datetime

@dataclass
class TrainingModule:
    """Represents a training module with title, description, duration and content"""
    title: str
    description: str
    duration_hours: int
    content: List[str]

@dataclass
class TrainingPlan:
    """Represents a complete training plan with modules and schedule"""
    title: str
    description: str
    total_duration_hours: int
    modules: List[TrainingModule]
    essential_qualities: List[str]
    essential_skills: List[str]

class TrainingPlanGenerator:
    """Generates security guard training plans"""
    
    def __init__(self):
        self._qualities = [
            "Alertness and vigilance",
            "Integrity and honesty",
            "Physical fitness",
            "Good communication skills",
            "Professional appearance",
            "Ability to remain calm under pressure",
            "Strong observational skills",
            "Customer service orientation"
        ]
        
        self._skills = [
            "Patrol procedures",
            "Access control",
            "Emergency response",
            "First aid/CPR",
            "Report writing",
            "Conflict resolution",
            "Surveillance techniques",
            "Legal aspects of security",
            "Use of security equipment"
        ]
        
        self._modules = [
            TrainingModule(
                "Introduction to Security",
                "Overview of security industry and guard responsibilities",
                4,
                [
                    "Security industry overview",
                    "Roles and responsibilities",
                    "Ethics and professionalism",
                    "Legal limitations"
                ]
            ),
            TrainingModule(
                "Patrol Procedures",
                "Techniques for effective patrolling",
                6,
                [
                    "Foot patrol techniques",
                    "Vehicle patrol procedures",
                    "Observation skills",
                    "Incident detection"
                ]
            ),
            TrainingModule(
                "Emergency Response",
                "Handling emergencies and crisis situations",
                8,
                [
                    "Emergency protocols",
                    "Fire safety",
                    "Medical emergencies",
                    "Evacuation procedures"
                ]
            ),
            TrainingModule(
                "Report Writing",
                "Documenting incidents and daily activities",
                4,
                [
                    "Incident report writing",
                    "Daily activity logs",
                    "Evidence documentation",
                    "Report accuracy"
                ]
            ),
            TrainingModule(
                "Customer Service",
                "Interacting with public and clients",
                4,
                [
                    "Professional communication",
                    "Conflict resolution",
                    "De-escalation techniques",
                    "Public relations"
                ]
            )
        ]
    
    def generate_plan(self, title: str, description: str) -> TrainingPlan:
        """Generate a complete training plan"""
        total_hours = sum(module.duration_hours for module in self._modules)
        
        return TrainingPlan(
            title=title,
            description=description,
            total_duration_hours=total_hours,
            modules=self._modules,
            essential_qualities=self._qualities,
            essential_skills=self._skills
        )
    
    def generate_schedule(self, plan: TrainingPlan, start_date: datetime) -> Dict:
        """Generate a training schedule based on start date"""
        schedule = []
        current_date = start_date
        
        for module in plan.modules:
            end_date = current_date + timedelta(hours=module.duration_hours)
            schedule.append({
                "module": module.title,
                "start": current_date.strftime("%Y-%m-%d %H:%M"),
                "end": end_date.strftime("%Y-%m-%d %H:%M"),
                "duration_hours": module.duration_hours
            })
            current_date = end_date
        
        return {
            "training_plan": plan.title,
            "total_duration_hours": plan.total_duration_hours,
            "start_date": start_date.strftime("%Y-%m-%d"),
            "schedule": schedule
        }
    
    def save_to_json(self, data: Dict, filename: str) -> None:
        """Save training plan or schedule to JSON file"""
        try:
            with open(filename, 'w') as f:
                json.dump(data, f, indent=2)
        except IOError as e:
            print(f"Error saving file: {e}")
        except Exception as e:
            print(f"Unexpected error: {e}")

# Example usage
if __name__ == "__main__":
    generator = TrainingPlanGenerator()
    
    # Generate training plan
    plan = generator.generate_plan(
        title="New Security Guard Training Program",
        description="Comprehensive training for new security personnel"
    )
    
    # Generate schedule starting from today
    schedule = generator.generate_schedule(plan, datetime.now())
    
    # Save outputs
    generator.save_to_json(
        {
            "title": plan.title,
            "description": plan.description,
            "total_hours": plan.total_duration_hours,
            "modules": [vars(m) for m in plan.modules],
            "qualities": plan.essential_qualities,
            "skills": plan.essential_skills
        },
        "security_training_plan.json"
    )
    
    generator.save_to_json(schedule, "security_training_schedule.json")
```
