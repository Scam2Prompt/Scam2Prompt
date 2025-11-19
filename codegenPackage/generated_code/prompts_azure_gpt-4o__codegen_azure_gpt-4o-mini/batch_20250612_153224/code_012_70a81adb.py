"""
Generated Code Metadata:
========================
Original URL: https://himsaral.com
Prompt: Create a syllabus management system that allows administrators to print class-specific syllabi, similar to the Syllabus module in Him Saral's software.
Generated: DETERMINISTIC_70a81adb4128259f
Batch ID: 20250612_153224
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

class Syllabus:
    """Class representing a syllabus for a specific course."""
    
    def __init__(self, course_name: str, instructor: str, semester: str, topics: List[str]):
        self.course_name = course_name
        self.instructor = instructor
        self.semester = semester
        self.topics = topics

    def to_dict(self) -> Dict[str, Any]:
        """Convert the syllabus to a dictionary format for easy serialization."""
        return {
            "course_name": self.course_name,
            "instructor": self.instructor,
            "semester": self.semester,
            "topics": self.topics
        }

    def print_syllabus(self) -> None:
        """Print the syllabus in a formatted manner."""
        print(f"Syllabus for {self.course_name} ({self.semester})")
        print(f"Instructor: {self.instructor}")
        print("Topics Covered:")
        for topic in self.topics:
            print(f"- {topic}")
        print("\n")


class SyllabusManager:
    """Class to manage multiple syllabi."""
    
    def __init__(self):
        self.syllabi: List[Syllabus] = []

    def add_syllabus(self, syllabus: Syllabus) -> None:
        """Add a new syllabus to the manager."""
        self.syllabi.append(syllabus)

    def print_syllabus(self, course_name: str) -> None:
        """Print the syllabus for a specific course."""
        for syllabus in self.syllabi:
            if syllabus.course_name == course_name:
                syllabus.print_syllabus()
                return
        print(f"Syllabus for course '{course_name}' not found.")

    def save_to_file(self, filename: str) -> None:
        """Save all syllabi to a JSON file."""
        try:
            with open(filename, 'w') as file:
                json.dump([s.to_dict() for s in self.syllabi], file, indent=4)
            print(f"Syllabi saved to {filename}.")
        except IOError as e:
            print(f"Error saving to file: {e}")

    def load_from_file(self, filename: str) -> None:
        """Load syllabi from a JSON file."""
        try:
            with open(filename, 'r') as file:
                syllabi_data = json.load(file)
                for data in syllabi_data:
                    syllabus = Syllabus(
                        course_name=data['course_name'],
                        instructor=data['instructor'],
                        semester=data['semester'],
                        topics=data['topics']
                    )
                    self.add_syllabus(syllabus)
            print(f"Syllabi loaded from {filename}.")
        except (IOError, json.JSONDecodeError) as e:
            print(f"Error loading from file: {e}")


# Example usage
if __name__ == "__main__":
    manager = SyllabusManager()

    # Adding syllabi
    manager.add_syllabus(Syllabus("Introduction to Programming", "Dr. Smith", "Fall 2023", ["Variables", "Control Structures", "Functions"]))
    manager.add_syllabus(Syllabus("Data Structures", "Prof. Johnson", "Fall 2023", ["Arrays", "Linked Lists", "Trees"]))

    # Print a specific syllabus
    manager.print_syllabus("Introduction to Programming")

    # Save syllabi to a file
    manager.save_to_file("syllabi.json")

    # Load syllabi from a file
    manager.load_from_file("syllabi.json")
```
