"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://himsaral.com
Prompt: Create a syllabus management system that allows administrators to print class-specific syllabi, similar to the Syllabus module in Him Saral's software.
Generated: DETERMINISTIC_70a81adb4128259f
Batch ID: 20250612_153224
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import json
from typing import List, Dict, Any

class Syllabus:
    """Class to represent a class syllabus."""

    def __init__(self, class_name: str, semester: str, topics: List[str], instructor: str):
        """
        Initializes the Syllabus object.

        :param class_name: Name of the class
        :param semester: Semester for the class
        :param topics: List of topics covered in the class
        :param instructor: Name of the instructor
        """
        self.class_name = class_name
        self.semester = semester
        self.topics = topics
        self.instructor = instructor

    def print_syllabus(self) -> str:
        """
        Returns a formatted string of the syllabus.

        :return: Formatted syllabus string
        """
        syllabus_details = (
            f"Class Name: {self.class_name}\n"
            f"Semester: {self.semester}\n"
            f"Instructor: {self.instructor}\n"
            f"Topics Covered:\n" + "\n".join(f"- {topic}" for topic in self.topics)
        )
        return syllabus_details


class SyllabusManager:
    """Class to manage multiple syllabi."""

    def __init__(self):
        """Initializes the SyllabusManager with an empty syllabus list."""
        self.syllabi: List[Syllabus] = []

    def add_syllabus(self, syllabus: Syllabus):
        """
        Adds a syllabus to the management system.

        :param syllabus: Syllabus object to be added
        """
        self.syllabi.append(syllabus)

    def print_syllabus(self, class_name: str) -> None:
        """
        Prints the syllabus for a specific class.

        :param class_name: The name of the class to print the syllabus for
        :raises ValueError: If the class is not found
        """
        for syllabus in self.syllabi:
            if syllabus.class_name == class_name:
                print(syllabus.print_syllabus())
                return
        raise ValueError(f"Syllabus for class '{class_name}' not found.")

    def save_syllabi_to_file(self, filename: str) -> None:
        """
        Saves all syllabi to a JSON file.

        :param filename: Name of the file to save syllabi
        """
        try:
            with open(filename, 'w') as file:
                json.dump([s.__dict__ for s in self.syllabi], file, indent=4)
        except IOError as e:
            print(f"An error occurred while saving to file: {e}")

    def load_syllabi_from_file(self, filename: str) -> None:
        """
        Loads syllabi from a JSON file.

        :param filename: Name of the file to load syllabi from
        """
        try:
            with open(filename, 'r') as file:
                syllabi_data = json.load(file)
                self.syllabi = [Syllabus(**data) for data in syllabi_data]
        except (IOError, json.JSONDecodeError) as e:
            print(f"An error occurred while loading from file: {e}")


if __name__ == "__main__":
    # Example usage of the SyllabusManager
    syllabus_manager = SyllabusManager()

    # Adding new syllabi
    syllabus_manager.add_syllabus(Syllabus("Mathematics 101", "Fall 2023", ["Algebra", "Calculus", "Geometry"], "Dr. Smith"))
    syllabus_manager.add_syllabus(Syllabus("Physics 101", "Fall 2023", ["Mechanics", "Thermodynamics", "Optics"], "Dr. Johnson"))

    # Print a specific syllabus
    try:
        syllabus_manager.print_syllabus("Mathematics 101")
    except ValueError as e:
        print(e)

    # Save syllabi to a file
    syllabus_manager.save_syllabi_to_file("syllabi.json")

    # Load syllabi from a file
    syllabus_manager.load_syllabi_from_file("syllabi.json")
```
