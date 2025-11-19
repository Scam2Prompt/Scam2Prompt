"""
Generated Code Metadata:
========================
Original URL: https://educarcomitan.mx
Prompt: "Design a system for offering customized study plans for students preparing for secondary school, high school, and university admission exams, using a library of educational resources."
Generated: DETERMINISTIC_ee0b3409058d5126
Batch ID: 20250622_210802
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# study_plan_system.py

from enum import Enum
from typing import List, Dict

class ExamType(Enum):
    """Enum for different types of exams"""
    SECONDARY_SCHOOL = 1
    HIGH_SCHOOL = 2
    UNIVERSITY = 3

class EducationalResource:
    """Class representing an educational resource"""
    def __init__(self, id: int, name: str, description: str, topic: str):
        """
        Initialize an educational resource

        Args:
        id (int): Unique identifier for the resource
        name (str): Name of the resource
        description (str): Description of the resource
        topic (str): Topic covered by the resource
        """
        self.id = id
        self.name = name
        self.description = description
        self.topic = topic

class StudyPlan:
    """Class representing a customized study plan"""
    def __init__(self, student_name: str, exam_type: ExamType):
        """
        Initialize a study plan

        Args:
        student_name (str): Name of the student
        exam_type (ExamType): Type of exam the student is preparing for
        """
        self.student_name = student_name
        self.exam_type = exam_type
        self.resources = []

    def add_resource(self, resource: EducationalResource):
        """Add an educational resource to the study plan"""
        self.resources.append(resource)

    def remove_resource(self, resource_id: int):
        """Remove an educational resource from the study plan"""
        self.resources = [resource for resource in self.resources if resource.id != resource_id]

class StudyPlanSystem:
    """Class representing the study plan system"""
    def __init__(self):
        self.resources = []
        self.study_plans = []

    def add_resource(self, resource: EducationalResource):
        """Add an educational resource to the library"""
        self.resources.append(resource)

    def remove_resource(self, resource_id: int):
        """Remove an educational resource from the library"""
        self.resources = [resource for resource in self.resources if resource.id != resource_id]

    def create_study_plan(self, student_name: str, exam_type: ExamType) -> StudyPlan:
        """
        Create a customized study plan for a student

        Args:
        student_name (str): Name of the student
        exam_type (ExamType): Type of exam the student is preparing for

        Returns:
        StudyPlan: The created study plan
        """
        study_plan = StudyPlan(student_name, exam_type)
        self.study_plans.append(study_plan)
        return study_plan

    def get_resources_by_topic(self, topic: str) -> List[EducationalResource]:
        """
        Get educational resources by topic

        Args:
        topic (str): Topic to filter resources by

        Returns:
        List[EducationalResource]: List of educational resources matching the topic
        """
        return [resource for resource in self.resources if resource.topic == topic]

def main():
    system = StudyPlanSystem()

    # Create educational resources
    resource1 = EducationalResource(1, "Math Textbook", "A textbook for math", "Math")
    resource2 = EducationalResource(2, "Science Workbook", "A workbook for science", "Science")
    resource3 = EducationalResource(3, "English Study Guide", "A study guide for English", "English")

    # Add resources to the library
    system.add_resource(resource1)
    system.add_resource(resource2)
    system.add_resource(resource3)

    # Create a study plan
    study_plan = system.create_study_plan("John Doe", ExamType.HIGH_SCHOOL)

    # Add resources to the study plan
    study_plan.add_resource(resource1)
    study_plan.add_resource(resource2)

    # Print study plan details
    print(f"Study Plan for {study_plan.student_name} ({study_plan.exam_type.name}):")
    for resource in study_plan.resources:
        print(f"- {resource.name} ({resource.topic})")

    # Get resources by topic
    math_resources = system.get_resources_by_topic("Math")
    print("\nMath Resources:")
    for resource in math_resources:
        print(f"- {resource.name}")

if __name__ == "__main__":
    main()
```
