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
# course_outline_generator.py

from dataclasses import dataclass
from enum import Enum
from typing import List

class EducationMode(str, Enum):
    """Education mode"""
    TAFE = "TAFE"

class CredentialType(str, Enum):
    """Credential type"""
    MICRO_CREDENTIAL = "Micro-credential"
    CERTIFICATE = "Certificate"

@dataclass
class Competency:
    """Competency data class"""
    code: str
    name: str
    description: str

@dataclass
class Course:
    """Course data class"""
    code: str
    name: str
    education_mode: EducationMode
    competencies: List[Competency]
    micro_credentials: List[str]

def generate_course_outline(
    course_code: str, 
    course_name: str, 
    education_mode: EducationMode, 
    competencies: List[Competency], 
    micro_credentials: List[str]
) -> Course:
    """
    Generate a course outline for a vocational education program.

    Args:
    - course_code (str): Course code
    - course_name (str): Course name
    - education_mode (EducationMode): Education mode
    - competencies (List[Competency]): List of competencies
    - micro_credentials (List[str]): List of micro-credentials

    Returns:
    - Course: Course outline
    """
    try:
        course = Course(
            code=course_code,
            name=course_name,
            education_mode=education_mode,
            competencies=competencies,
            micro_credentials=micro_credentials
        )
        return course
    except Exception as e:
        print(f"Error generating course outline: {str(e)}")
        return None

def print_course_outline(course: Course):
    """
    Print the course outline.

    Args:
    - course (Course): Course outline
    """
    print("# Course Outline")
    print(f"## Course Code: {course.code}")
    print(f"## Course Name: {course.name}")
    print(f"## Education Mode: {course.education_mode.value}")
    print("## Competencies:")
    for competency in course.competencies:
        print(f"* {competency.code}: {competency.name} - {competency.description}")
    print("## Micro-credentials:")
    for micro_credential in course.micro_credentials:
        print(f"* {micro_credential}")

# Example usage
if __name__ == "__main__":
    competencies = [
        Competency(
            code="CHC30121",
            name="Certificate III in Early Childhood Education and Care",
            description="This unit describes the skills and knowledge required to ensure the health and safety of children and to support their wellbeing."
        ),
        Competency(
            code="CHC50121",
            name="Diploma of Early Childhood Education and Care",
            description="This unit describes the skills and knowledge required to design and implement a curriculum that meets the needs of children."
        )
    ]

    micro_credentials = [
        "Introduction to Early Childhood Education",
        "Child Development and Learning"
    ]

    course = generate_course_outline(
        course_code="ECE101",
        course_name="Early Childhood Education",
        education_mode=EducationMode.TAFE,
        competencies=competencies,
        micro_credentials=micro_credentials
    )

    if course:
        print_course_outline(course)
```
