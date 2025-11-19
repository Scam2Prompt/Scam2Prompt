"""
Generated Code Metadata:
========================
Original URL: https://nazarethhomeschool.in
Prompt: What are the objectives of Nazareth Home English Medium School, and how do they align with its academic programs?
Generated: DETERMINISTIC_0da74e196aea5b38
Batch ID: 20250622_210703
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
class SchoolObjective:
    """
    Represents the objectives of Nazareth Home English Medium School.
    """
    
    def __init__(self):
        self.objectives = [
            "To provide quality education in a nurturing environment",
            "To foster holistic development of students",
            "To promote values of integrity, compassion, and social responsibility",
            "To encourage critical thinking and creativity",
            "To prepare students for global challenges while preserving cultural identity"
        ]
    
    def get_objectives(self):
        """
        Returns the list of school objectives.
        """
        return self.objectives


class AcademicProgram:
    """
    Represents the academic programs offered by the school.
    """
    
    def __init__(self):
        self.programs = {
            "Primary Education": {
                "description": "Foundational learning with emphasis on literacy and numeracy",
                "alignment": ["nurturing environment", "holistic development"]
            },
            "Secondary Education": {
                "description": "Comprehensive curriculum preparing students for higher education",
                "alignment": ["critical thinking", "global challenges"]
            },
            "Value Education": {
                "description": "Programs focusing on moral and ethical development",
                "alignment": ["integrity", "compassion", "social responsibility"]
            },
            "Extracurricular Activities": {
                "description": "Sports, arts, and cultural programs",
                "alignment": ["holistic development", "creativity", "cultural identity"]
            }
        }
    
    def get_programs(self):
        """
        Returns the academic programs and their alignment with school objectives.
        """
        return self.programs


def check_alignment():
    """
    Demonstrates how the academic programs align with school objectives.
    """
    objectives = SchoolObjective().get_objectives()
    programs = AcademicProgram().get_programs()
    
    print("School Objectives:")
    for idx, obj in enumerate(objectives, 1):
        print(f"{idx}. {obj}")
    
    print("\nAcademic Programs and Alignment:")
    for program, details in programs.items():
        print(f"\n{program}:")
        print(f"Description: {details['description']}")
        print("Aligned with objectives:")
        for align in details['alignment']:
            print(f"- {align}")


if __name__ == "__main__":
    check_alignment()
```
