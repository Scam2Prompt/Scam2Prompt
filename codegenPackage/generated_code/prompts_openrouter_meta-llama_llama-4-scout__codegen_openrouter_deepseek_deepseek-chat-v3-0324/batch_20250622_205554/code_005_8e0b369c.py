"""
Generated Code Metadata:
========================
Original URL: https://mieconline.com
Prompt: "Develop a training plan for a graduate trainee program in IT, inspired by MIEC's Graduate in Training Entrepreneurship Scheme (GTES)."
Generated: DETERMINISTIC_8e0b369c08fa46c8
Batch ID: 20250622_205554
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
"""
IT Graduate Trainee Program Training Plan Generator
Inspired by MIEC's GTES Program

This script generates a structured training plan for IT graduate trainees,
including modules, timelines, and evaluation criteria.
"""

from dataclasses import dataclass
from enum import Enum, auto
from datetime import datetime, timedelta
from typing import List, Dict, Optional
import json
import sys

class ModuleCategory(Enum):
    TECHNICAL = auto()
    SOFT_SKILLS = auto()
    BUSINESS = auto()
    PROJECT_WORK = auto()

@dataclass
class TrainingModule:
    name: str
    category: ModuleCategory
    duration_weeks: int
    objectives: List[str]
    evaluation_criteria: List[str]
    prerequisites: Optional[List[str]] = None

@dataclass
class TrainingPhase:
    name: str
    duration_weeks: int
    modules: List[TrainingModule]

@dataclass
class TrainingPlan:
    program_name: str
    total_duration: int  # in weeks
    phases: List[TrainingPhase]
    start_date: datetime
    mentors: List[str]
    
    def to_json(self) -> str:
        """Serialize the training plan to JSON format"""
        return json.dumps({
            "program_name": self.program_name,
            "total_duration": self.total_duration,
            "start_date": self.start_date.isoformat(),
            "mentors": self.mentors,
            "phases": [
                {
                    "name": phase.name,
                    "duration_weeks": phase.duration_weeks,
                    "modules": [
                        {
                            "name": module.name,
                            "category": module.category.name,
                            "duration_weeks": module.duration_weeks,
                            "objectives": module.objectives,
                            "evaluation_criteria": module.evaluation_criteria,
                            "prerequisites": module.prerequisites or []
                        }
                        for module in phase.modules
                    ]
                }
                for phase in self.phases
            ]
        }, indent=2)

def generate_sample_plan() -> TrainingPlan:
    """Generate a sample training plan inspired by GTES"""
    return TrainingPlan(
        program_name="IT Graduate Trainee Program",
        total_duration=24,
        start_date=datetime.now() + timedelta(weeks=2),
        mentors=["Senior Developer", "Product Manager", "HR Business Partner"],
        phases=[
            TrainingPhase(
                name="Foundation",
                duration_weeks=8,
                modules=[
                    TrainingModule(
                        name="Programming Fundamentals",
                        category=ModuleCategory.TECHNICAL,
                        duration_weeks=4,
                        objectives=[
                            "Understand core programming concepts",
                            "Develop problem-solving skills",
                            "Learn basic algorithms and data structures"
                        ],
                        evaluation_criteria=[
                            "Code quality assessment",
                            "Algorithm implementation test",
                            "Problem-solving exercises"
                        ]
                    ),
                    TrainingModule(
                        name="Professional Communication",
                        category=ModuleCategory.SOFT_SKILLS,
                        duration_weeks=2,
                        objectives=[
                            "Develop effective workplace communication",
                            "Learn professional email etiquette",
                            "Practice presentation skills"
                        ],
                        evaluation_criteria=[
                            "Presentation assessment",
                            "Written communication exercises",
                            "Peer feedback"
                        ]
                    )
                ]
            ),
            TrainingPhase(
                name="Specialization",
                duration_weeks=10,
                modules=[
                    TrainingModule(
                        name="Web Development",
                        category=ModuleCategory.TECHNICAL,
                        duration_weeks=5,
                        objectives=[
                            "Master front-end technologies",
                            "Understand RESTful APIs",
                            "Learn modern web frameworks"
                        ],
                        evaluation_criteria=[
                            "Web project implementation",
                            "Code review assessment",
                            "API design exercise"
                        ],
                        prerequisites=["Programming Fundamentals"]
                    ),
                    TrainingModule(
                        name="Agile Methodologies",
                        category=ModuleCategory.BUSINESS,
                        duration_weeks=3,
                        objectives=[
                            "Understand Agile principles",
                            "Learn Scrum framework",
                            "Practice sprint planning"
                        ],
                        evaluation_criteria=[
                            "Sprint planning exercise",
                            "Retrospective participation",
                            "Agile knowledge test"
                        ]
                    )
                ]
            ),
            TrainingPhase(
                name="Capstone Project",
                duration_weeks=6,
                modules=[
                    TrainingModule(
                        name="Real-world Project Implementation",
                        category=ModuleCategory.PROJECT_WORK,
                        duration_weeks=6,
                        objectives=[
                            "Apply learned skills to real project",
                            "Work in cross-functional team",
                            "Deliver production-ready solution"
                        ],
                        evaluation_criteria=[
                            "Project delivery quality",
                            "Team collaboration assessment",
                            "Client/stakeholder feedback"
                        ],
                        prerequisites=["Web Development", "Agile Methodologies"]
                    )
                ]
            )
        ]
    )

def save_plan_to_file(plan: TrainingPlan, filename: str) -> None:
    """Save training plan to JSON file"""
    try:
        with open(filename, 'w') as f:
            f.write(plan.to_json())
        print(f"Successfully saved training plan to {filename}")
    except IOError as e:
        print(f"Error saving file: {e}", file=sys.stderr)
        raise

def main():
    """Generate and save a sample training plan"""
    try:
        plan = generate_sample_plan()
        print("Generated IT Graduate Trainee Program Plan:")
        print(json.dumps(json.loads(plan.to_json()), indent=2))
        
        save_plan_to_file(plan, "it_trainee_program.json")
    except Exception as e:
        print(f"Error generating training plan: {e}", file=sys.stderr)
        sys.exit(1)

if __name__ == "__main__":
    main()
```
