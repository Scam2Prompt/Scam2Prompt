"""
Generated Code Metadata:
========================
Original URL: https://aveaorg.com
Prompt: "Generate a course outline for a vocational education program in early childhood education using the TAFE education mode, incorporating micro-credentials and competency-based training."
Generated: DETERMINISTIC_db68d2942ad5dd5d
Batch ID: 20250622_210914
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
"""
TAFE Early Childhood Education Program Outline Generator
This script generates a structured course outline for a vocational education program
in Early Childhood Education following TAFE standards, incorporating micro-credentials
and competency-based training.
"""

from dataclasses import dataclass, field
from typing import List, Dict, Optional
import json

@dataclass
class CompetencyUnit:
    code: str
    title: str
    description: str
    hours: int
    micro_credential: bool = False

@dataclass
class Module:
    name: str
    description: str
    competency_units: List[CompetencyUnit]
    duration_weeks: int

@dataclass
class CourseOutline:
    program_name: str
    program_code: str
    total_duration: str
    delivery_mode: str
    modules: List[Module]
    entry_requirements: List[str]
    assessment_methods: List[str]
    certification: str

def generate_early_childhood_education_outline() -> CourseOutline:
    """Generate a TAFE-style course outline for Early Childhood Education."""
    
    # Core competency units
    competency_units = [
        CompetencyUnit(
            code="CHCECE030",
            title="Support inclusion and diversity",
            description="This unit describes the skills and knowledge required to support children's inclusion and diversity in early childhood education and care.",
            hours=50,
            micro_credential=True
        ),
        CompetencyUnit(
            code="CHCECE031",
            title="Support children's health, safety and wellbeing",
            description="This unit describes the skills and knowledge required to support children's health, safety and wellbeing in early childhood education and care.",
            hours=60
        ),
        CompetencyUnit(
            code="CHCECE032",
            title="Nurture babies and toddlers",
            description="This unit describes the skills and knowledge required to develop and implement nurturing practices for babies and toddlers.",
            hours=40,
            micro_credential=True
        ),
        CompetencyUnit(
            code="CHCECE033",
            title="Develop positive and respectful relationships with children",
            description="This unit describes the skills and knowledge required to communicate and interact respectfully with children.",
            hours=50
        ),
        CompetencyUnit(
            code="CHCECE034",
            title="Use an approved learning framework to guide practice",
            description="This unit describes the skills and knowledge required to enable educators to provide children with opportunities to maximize their potential.",
            hours=60
        )
    ]

    # Elective competency units
    elective_units = [
        CompetencyUnit(
            code="CHCECE035",
            title="Support the holistic learning and development of children",
            description="This unit describes the skills and knowledge required to support and recognize the interconnectedness of learning and development areas.",
            hours=70,
            micro_credential=True
        ),
        CompetencyUnit(
            code="CHCECE036",
            title="Provide experiences to support children's play and learning",
            description="This unit describes the skills and knowledge required to organize and implement play and leisure experiences for children.",
            hours=50
        )
    ]

    # Modules
    modules = [
        Module(
            name="Foundations of Early Childhood Education",
            description="Introduction to key concepts and practices in early childhood education.",
            competency_units=[competency_units[0], competency_units[1]],
            duration_weeks=10
        ),
        Module(
            name="Child Development and Learning",
            description="Understanding child development stages and supporting learning processes.",
            competency_units=[competency_units[2], competency_units[3]],
            duration_weeks=12
        ),
        Module(
            name="Curriculum Planning and Implementation",
            description="Developing and implementing early childhood education programs.",
            competency_units=[competency_units[4], elective_units[0]],
            duration_weeks=14
        ),
        Module(
            name="Professional Practice",
            description="Developing professional skills and reflective practice in early childhood settings.",
            competency_units=[elective_units[1]],
            duration_weeks=8
        )
    ]

    # Course outline
    outline = CourseOutline(
        program_name="Diploma of Early Childhood Education and Care",
        program_code="CHC50121",
        total_duration="12 months",
        delivery_mode="Blended (online and face-to-face)",
        modules=modules,
        entry_requirements=[
            "Year 12 certificate or equivalent",
            "Working with Children Check",
            "Language, Literacy and Numeracy (LLN) assessment"
        ],
        assessment_methods=[
            "Practical demonstrations",
            "Portfolio of work",
            "Written assessments",
            "Workplace observations"
        ],
        certification="Upon successful completion, students will receive a Diploma of Early Childhood Education and Care (CHC50121) and micro-credentials for completed competency units."
    )

    return outline

def save_outline_to_json(outline: CourseOutline, filename: str) -> None:
    """Save course outline to JSON file."""
    try:
        with open(filename, 'w') as f:
            json.dump(outline.__dict__, f, indent=4, default=lambda o: o.__dict__)
    except IOError as e:
        print(f"Error saving file: {e}")

def main():
    """Generate and save the course outline."""
    outline = generate_early_childhood_education_outline()
    save_outline_to_json(outline, "early_childhood_education_outline.json")
    print("Course outline generated successfully.")

if __name__ == "__main__":
    main()
```
