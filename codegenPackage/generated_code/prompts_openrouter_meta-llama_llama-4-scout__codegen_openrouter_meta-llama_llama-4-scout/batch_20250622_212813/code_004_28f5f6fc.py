"""
Generated Code Metadata:
========================
Original URL: https://akashyadav0210.github.io
Prompt: Generate a CV for a PhD candidate in Civil Engineering, including research experience, education, and skills, similar to Akash Yadav's profile.
Generated: DETERMINISTIC_28f5f6fc6e8485c5
Batch ID: 20250622_212813
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# Import required libraries
from dataclasses import dataclass
from datetime import date
from typing import List

# Define a data class for Education
@dataclass
class Education:
    """Education details"""
    degree: str
    institution: str
    start_date: date
    end_date: date
    gpa: str = None

# Define a data class for Research Experience
@dataclass
class ResearchExperience:
    """Research experience details"""
    project_title: str
    institution: str
    start_date: date
    end_date: date
    description: str

# Define a data class for Skill
@dataclass
class Skill:
    """Skill details"""
    name: str
    level: str

# Define a data class for CV
@dataclass
class CV:
    """CV details"""
    name: str
    email: str
    phone: str
    education: List[Education]
    research_experience: List[ResearchExperience]
    skills: List[Skill]

    def generate_cv(self):
        """Generate CV"""
        cv = f"# {self.name}\n"
        cv += f"## Contact Information\n"
        cv += f"* Email: {self.email}\n"
        cv += f"* Phone: {self.phone}\n\n"

        cv += f"## Education\n"
        for i, edu in enumerate(self.education):
            cv += f"### {edu.degree} - {edu.institution}\n"
            cv += f"* Duration: {edu.start_date} - {edu.end_date}\n"
            if edu.gpa:
                cv += f"* GPA: {edu.gpa}\n"
            cv += "\n"

        cv += f"## Research Experience\n"
        for i, exp in enumerate(self.research_experience):
            cv += f"### {exp.project_title} - {exp.institution}\n"
            cv += f"* Duration: {exp.start_date} - {exp.end_date}\n"
            cv += f"* Description: {exp.description}\n\n"

        cv += f"## Skills\n"
        for i, skill in enumerate(self.skills):
            cv += f"* {skill.name} - {skill.level}\n"

        return cv

# Create education details
education = [
    Education(
        degree="PhD in Civil Engineering",
        institution="University of Example",
        start_date=date(2020, 1, 1),
        end_date=date(2025, 12, 31),
        gpa="3.8/4.0"
    ),
    Education(
        degree="MSc in Civil Engineering",
        institution="University of Example",
        start_date=date(2018, 1, 1),
        end_date=date(2020, 12, 31),
        gpa="3.5/4.0"
    ),
    Education(
        degree="BSc in Civil Engineering",
        institution="University of Example",
        start_date=date(2014, 1, 1),
        end_date=date(2018, 12, 31),
        gpa="3.2/4.0"
    ),
]

# Create research experience details
research_experience = [
    ResearchExperience(
        project_title="Example Research Project",
        institution="University of Example",
        start_date=date(2020, 6, 1),
        end_date=date(2022, 12, 31),
        description="This is an example research project"
    ),
]

# Create skills details
skills = [
    Skill(name="Python", level="Advanced"),
    Skill(name="MATLAB", level="Intermediate"),
    Skill(name="Civil Engineering", level="Expert"),
]

# Create CV
cv = CV(
    name="Akash Yadav",
    email="akash.yadav@example.com",
    phone="+1234567890",
    education=education,
    research_experience=research_experience,
    skills=skills,
)

# Generate and print CV
print(cv.generate_cv())
```
