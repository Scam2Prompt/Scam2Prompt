"""
Generated Code Metadata:
========================
Original URL: https://heartofjesuscollege.com
Prompt: "Generate a lesson plan for teaching English as a second language using the HJ-Thinking methodology and Reeduc platform, as used at Heart of Jesus College."
Generated: DETERMINISTIC_f05eab9a918e0036
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
ESL Lesson Plan Generator using HJ-Thinking Methodology and Reeduc Platform
Designed for Heart of Jesus College
"""

from datetime import datetime
from enum import Enum
from typing import List, Dict, Optional

class LessonPhase(Enum):
    WARM_UP = "Warm-up Activity"
    PRESENTATION = "Presentation of New Material"
    PRACTICE = "Guided Practice"
    PRODUCTION = "Independent Production"
    REVIEW = "Review and Assessment"
    CLOSURE = "Closure and Reflection"

class HJThinkingMethod:
    def __init__(self):
        self.phases = {
            LessonPhase.WARM_UP: "Activate prior knowledge with engaging starter",
            LessonPhase.PRESENTATION: "Introduce new language points through Reeduc multimedia",
            LessonPhase.PRACTICE: "Structured activities with gradual release of responsibility",
            LessonPhase.PRODUCTION: "Creative application in authentic contexts",
            LessonPhase.REVIEW: "Formative assessment with Reeduc analytics",
            LessonPhase.CLOSURE: "Reflective metacognitive discussion"
        }

class LessonPlan:
    def __init__(self, 
                 title: str, 
                 level: str, 
                 duration: int, 
                 objectives: List[str],
                 hj_method: HJThinkingMethod = HJThinkingMethod()):
        self.title = title
        self.level = level
        self.duration = duration  # in minutes
        self.objectives = objectives
        self.hj_method = hj_method
        self.created_at = datetime.now().strftime("%Y-%m-%d")
        self.components = []
        self.reeduc_resources = []
    
    def add_component(self, phase: LessonPhase, description: str, duration: int, 
                      reeduc_resource: Optional[str] = None):
        """Add a lesson component with optional Reeduc platform resource"""
        component = {
            "phase": phase,
            "description": description,
            "duration": duration,
            "reeduc_resource": reeduc_resource
        }
        self.components.append(component)
        if reeduc_resource:
            self.reeduc_resources.append(reeduc_resource)
    
    def generate_plan(self) -> Dict:
        """Generate structured lesson plan output"""
        if not self.validate_plan():
            raise ValueError("Lesson plan validation failed - check durations and components")
        
        return {
            "metadata": {
                "title": self.title,
                "level": self.level,
                "date": self.created_at,
                "total_duration": self.duration,
                "objectives": self.objectives
            },
            "phases": [{
                "name": phase.value,
                "hj_method": self.hj_method.phases[phase],
                "components": [c for c in self.components if c["phase"] == phase]
            } for phase in LessonPhase],
            "reeduc_resources": self.reeduc_resources
        }
    
    def validate_plan(self) -> bool:
        """Validate lesson plan structure and timing"""
        total_duration = sum(c["duration"] for c in self.components)
        if total_duration != self.duration:
            return False
        
        required_phases = set(LessonPhase)
        present_phases = set(c["phase"] for c in self.components)
        return required_phases.issubset(present_phases)

def create_sample_plan() -> LessonPlan:
    """Create a sample lesson plan for demonstration"""
    plan = LessonPlan(
        title="Describing Daily Routines",
        level="Pre-Intermediate",
        duration=60,
        objectives=[
            "Use present simple tense to describe routines",
            "Apply time expressions correctly",
            "Ask and answer questions about daily activities"
        ]
    )
    
    # Add components following HJ-Thinking methodology
    plan.add_component(
        LessonPhase.WARM_UP,
        "Miming game: Students act out daily routines",
        10,
        "Reeduc Warm-up Activity Bank #142"
    )
    
    plan.add_component(
        LessonPhase.PRESENTATION,
        "Introduce vocabulary and grammar through Reeduc interactive module",
        15,
        "Reeduc Daily Routines Module v3.2"
    )
    
    plan.add_component(
        LessonPhase.PRACTICE,
        "Guided worksheet completion with peer support",
        10,
        "Reeduc Worksheet Generator: Present Simple"
    )
    
    plan.add_component(
        LessonPhase.PRODUCTION,
        "Pair interviews about daily routines with recording",
        15,
        "Reeduc Recording Studio Tool"
    )
    
    plan.add_component(
        LessonPhase.REVIEW,
        "Class analysis of common errors using Reeduc analytics",
        5,
        "Reeduc Error Analysis Dashboard"
    )
    
    plan.add_component(
        LessonPhase.CLOSURE,
        "Reflection on learning process and difficulties",
        5
    )
    
    return plan

if __name__ == "__main__":
    try:
        lesson = create_sample_plan()
        plan_output = lesson.generate_plan()
        print("Successfully generated lesson plan:")
        print(plan_output)
    except Exception as e:
        print(f"Error generating lesson plan: {str(e)}")
```
