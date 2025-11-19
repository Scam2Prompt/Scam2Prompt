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
import json
from typing import List, Dict, Any

class StudyResource:
    """Class representing a study resource."""
    
    def __init__(self, title: str, subject: str, level: str, url: str):
        self.title = title
        self.subject = subject
        self.level = level
        self.url = url

    def to_dict(self) -> Dict[str, Any]:
        """Convert the resource to a dictionary."""
        return {
            "title": self.title,
            "subject": self.subject,
            "level": self.level,
            "url": self.url
        }

class StudyPlan:
    """Class representing a customized study plan for a student."""
    
    def __init__(self, student_name: str, exam_level: str):
        self.student_name = student_name
        self.exam_level = exam_level
        self.resources: List[StudyResource] = []

    def add_resource(self, resource: StudyResource):
        """Add a study resource to the study plan."""
        if resource.level == self.exam_level:
            self.resources.append(resource)
        else:
            raise ValueError(f"Resource level '{resource.level}' does not match study plan level '{self.exam_level}'.")

    def generate_plan(self) -> Dict[str, Any]:
        """Generate the study plan as a dictionary."""
        return {
            "student_name": self.student_name,
            "exam_level": self.exam_level,
            "resources": [resource.to_dict() for resource in self.resources]
        }

class ResourceLibrary:
    """Class representing a library of educational resources."""
    
    def __init__(self):
        self.resources: List[StudyResource] = []

    def load_resources(self, file_path: str):
        """Load resources from a JSON file."""
        try:
            with open(file_path, 'r') as file:
                data = json.load(file)
                for item in data:
                    resource = StudyResource(**item)
                    self.resources.append(resource)
        except FileNotFoundError:
            print(f"Error: The file '{file_path}' was not found.")
        except json.JSONDecodeError:
            print("Error: Failed to decode JSON from the file.")
        except Exception as e:
            print(f"An unexpected error occurred: {e}")

    def get_resources_by_level(self, level: str) -> List[StudyResource]:
        """Get resources filtered by exam level."""
        return [resource for resource in self.resources if resource.level == level]

def main():
    # Initialize the resource library and load resources
    library = ResourceLibrary()
    library.load_resources('resources.json')

    # Create a study plan for a student
    student_name = "John Doe"
    exam_level = "high school"
    study_plan = StudyPlan(student_name, exam_level)

    # Add resources to the study plan
    resources = library.get_resources_by_level(exam_level)
    for resource in resources:
        try:
            study_plan.add_resource(resource)
        except ValueError as e:
            print(e)

    # Generate and print the study plan
    plan = study_plan.generate_plan()
    print(json.dumps(plan, indent=4))

if __name__ == "__main__":
    main()
```

**Note:** Ensure that a `resources.json` file exists in the same directory with the appropriate structure for the code to run successfully. The JSON file should contain an array of objects with keys: `title`, `subject`, `level`, and `url`.
