"""
Generated Code Metadata:
========================
Original URL: https://45ybook.ueh.edu.vn
Prompt: Suggest a framework for developing a multi-disciplinary curriculum in higher education, using examples from the UEH special issue.
Generated: DETERMINISTIC_bece29a20d20485a
Batch ID: 20250612_155417
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
"""
Framework for developing a multi-disciplinary curriculum in higher education.
Inspired by UEH (Urban and Environmental Humanities) special issue examples.
"""

from typing import List, Dict, Optional
from dataclasses import dataclass
from enum import Enum, auto
import json

class Discipline(Enum):
    """Core disciplines to be integrated in the curriculum"""
    HUMANITIES = auto()
    SOCIAL_SCIENCES = auto()
    NATURAL_SCIENCES = auto()
    ENGINEERING = auto()
    ARTS = auto()
    BUSINESS = auto()

@dataclass
class LearningOutcome:
    """Describes what students should achieve"""
    description: str
    discipline: Discipline
    level: int  # Bloom's taxonomy level (1-6)

@dataclass
class CourseModule:
    """A single module within a course"""
    name: str
    description: str
    learning_outcomes: List[LearningOutcome]
    disciplines: List[Discipline]
    credits: float

@dataclass
class Course:
    """A complete course consisting of modules"""
    name: str
    code: str
    modules: List[CourseModule]
    total_credits: float

class CurriculumBuilder:
    """Framework for building multi-disciplinary curricula"""
    
    def __init__(self):
        self.courses: List[Course] = []
        self.discipline_weights: Dict[Discipline, float] = {}
    
    def add_course(self, course: Course) -> None:
        """Add a course to the curriculum"""
        self.courses.append(course)
        self._update_discipline_weights(course)
    
    def _update_discipline_weights(self, course: Course) -> None:
        """Update discipline distribution based on added course"""
        for module in course.modules:
            for discipline in module.disciplines:
                self.discipline_weights[discipline] = (
                    self.discipline_weights.get(discipline, 0) + module.credits
                )
    
    def get_discipline_distribution(self) -> Dict[Discipline, float]:
        """Get current distribution of disciplines"""
        total = sum(self.discipline_weights.values())
        return {d: w/total for d, w in self.discipline_weights.items()}
    
    def validate_curriculum(self) -> bool:
        """Check if curriculum meets multi-disciplinary requirements"""
        if len(self.discipline_weights) < 3:
            raise ValueError("Curriculum must include at least 3 disciplines")
        return True
    
    def to_json(self, filepath: Optional[str] = None) -> str:
        """Serialize curriculum to JSON format"""
        data = {
            "courses": [
                {
                    "name": course.name,
                    "code": course.code,
                    "modules": [
                        {
                            "name": module.name,
                            "description": module.description,
                            "disciplines": [d.name for d in module.disciplines],
                            "credits": module.credits
                        }
                        for module in course.modules
                    ],
                    "total_credits": course.total_credits
                }
                for course in self.courses
            ],
            "discipline_distribution": {
                d.name: w for d, w in self.get_discipline_distribution().items()
            }
        }
        
        json_str = json.dumps(data, indent=2)
        if filepath:
            with open(filepath, 'w') as f:
                f.write(json_str)
        return json_str

# Example usage following UEH special issue approach
if __name__ == "__main__":
    # Create a sample curriculum
    builder = CurriculumBuilder()
    
    # Sample learning outcomes
    urban_analysis_outcomes = [
        LearningOutcome(
            "Analyze urban spaces through multiple disciplinary lenses",
            Discipline.SOCIAL_SCIENCES,
            4
        ),
        LearningOutcome(
            "Apply quantitative methods to urban data",
            Discipline.ENGINEERING,
            3
        )
    ]
    
    # Sample course module
    urban_module = CourseModule(
        name="Urban Analysis",
        description="Multi-disciplinary analysis of urban environments",
        learning_outcomes=urban_analysis_outcomes,
        disciplines=[Discipline.SOCIAL_SCIENCES, Discipline.ENGINEERING],
        credits=3.0
    )
    
    # Sample course
    urban_course = Course(
        name="Urban Studies",
        code="UEH101",
        modules=[urban_module],
        total_credits=3.0
    )
    
    # Add to curriculum
    builder.add_course(urban_course)
    
    # Validate and export
    try:
        builder.validate_curriculum()
        print(builder.to_json())
    except ValueError as e:
        print(f"Curriculum validation failed: {e}")
```
