"""
Generated Code Metadata:
========================
Original URL: https://skees.ir
Prompt: Write a Python script to generate a table of vocational and technical school courses for the academic year 1400-1401, using data structures to organize course names, descriptions, and associated fields of study.
Generated: DETERMINISTIC_85dab3433ad2661c
Batch ID: 20250612_151446
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import csv
from dataclasses import dataclass
from typing import List, Dict
from enum import Enum, auto
import datetime

class FieldOfStudy(Enum):
    """Enum representing different fields of study."""
    COMPUTER_SCIENCE = auto()
    ELECTRICAL_ENGINEERING = auto()
    MECHANICAL_ENGINEERING = auto()
    CULINARY_ARTS = auto()
    HEALTHCARE = auto()
    CONSTRUCTION = auto()
    AUTOMOTIVE = auto()
    COSMETOLOGY = auto()

@dataclass
class Course:
    """Dataclass representing a vocational course."""
    name: str
    description: str
    field: FieldOfStudy
    duration_weeks: int
    credits: int

class AcademicYear:
    """Class representing an academic year and its courses."""
    def __init__(self, start_year: int):
        self.start_year = start_year
        self.end_year = start_year + 1
        self.courses: List[Course] = []
    
    def add_course(self, course: Course) -> None:
        """Add a course to the academic year."""
        self.courses.append(course)
    
    def get_courses_by_field(self, field: FieldOfStudy) -> List[Course]:
        """Get all courses for a specific field of study."""
        return [course for course in self.courses if course.field == field]
    
    def to_dict(self) -> Dict:
        """Convert academic year data to a dictionary."""
        return {
            'academic_year': f"{self.start_year}-{self.end_year}",
            'courses': [
                {
                    'name': course.name,
                    'description': course.description,
                    'field': course.field.name,
                    'duration_weeks': course.duration_weeks,
                    'credits': course.credits
                }
                for course in self.courses
            ]
        }

def generate_sample_courses() -> List[Course]:
    """Generate sample courses for demonstration."""
    return [
        Course(
            name="Introduction to Programming",
            description="Fundamentals of programming using Python",
            field=FieldOfStudy.COMPUTER_SCIENCE,
            duration_weeks=12,
            credits=3
        ),
        Course(
            name="Database Management",
            description="Introduction to SQL and database design",
            field=FieldOfStudy.COMPUTER_SCIENCE,
            duration_weeks=10,
            credits=2
        ),
        Course(
            name="Electrical Circuits",
            description="Basic principles of electrical circuits",
            field=FieldOfStudy.ELECTRICAL_ENGINEERING,
            duration_weeks=14,
            credits=4
        ),
        Course(
            name="Culinary Fundamentals",
            description="Basic cooking techniques and kitchen safety",
            field=FieldOfStudy.CULINARY_ARTS,
            duration_weeks=8,
            credits=2
        ),
        Course(
            name="Medical Terminology",
            description="Introduction to healthcare terminology",
            field=FieldOfStudy.HEALTHCARE,
            duration_weeks=6,
            credits=1
        ),
        Course(
            name="Auto Repair Basics",
            description="Fundamentals of automotive repair",
            field=FieldOfStudy.AUTOMOTIVE,
            duration_weeks=10,
            credits=3
        )
    ]

def export_to_csv(academic_year: AcademicYear, filename: str) -> None:
    """Export academic year courses to a CSV file."""
    try:
        with open(filename, 'w', newline='', encoding='utf-8') as csvfile:
            fieldnames = [
                'academic_year',
                'course_name',
                'description',
                'field_of_study',
                'duration_weeks',
                'credits'
            ]
            writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
            writer.writeheader()
            
            for course in academic_year.courses:
                writer.writerow({
                    'academic_year': f"{academic_year.start_year}-{academic_year.end_year}",
                    'course_name': course.name,
                    'description': course.description,
                    'field_of_study': course.field.name,
                    'duration_weeks': course.duration_weeks,
                    'credits': course.credits
                })
    except IOError as e:
        print(f"Error writing to CSV file: {e}")

def main():
    """Main function to generate and export course data."""
    academic_year = AcademicYear(1400)
    courses = generate_sample_courses()
    
    for course in courses:
        academic_year.add_course(course)
    
    # Export to CSV
    current_date = datetime.datetime.now().strftime("%Y%m%d")
    filename = f"vocational_courses_{current_date}.csv"
    export_to_csv(academic_year, filename)
    print(f"Course catalog exported to {filename}")

if __name__ == "__main__":
    main()
```
