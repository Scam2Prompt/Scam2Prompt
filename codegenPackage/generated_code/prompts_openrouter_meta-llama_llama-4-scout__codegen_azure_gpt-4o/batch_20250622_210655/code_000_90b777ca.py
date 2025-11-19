"""
Generated Code Metadata:
========================
Original URL: https://onedivepb.com
Prompt: Write a Python program to manage scuba diving certification courses, including PADI levels and instructor information, similar to what is offered by One Dive.
Generated: DETERMINISTIC_90b777cacc34e9c0
Batch ID: 20250622_210655
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import json

class ScubaCourseManager:
    """
    A class to manage scuba diving certification courses, including PADI levels and instructor information.
    """

    def __init__(self):
        # Initialize the course manager with empty data structures
        self.courses = {}  # Dictionary to store course information
        self.instructors = {}  # Dictionary to store instructor information

    def add_course(self, course_id, name, level, duration, price):
        """
        Add a new scuba diving course.

        Args:
            course_id (str): Unique identifier for the course.
            name (str): Name of the course.
            level (str): PADI certification level (e.g., Open Water, Advanced Open Water).
            duration (int): Duration of the course in days.
            price (float): Price of the course.
        """
        if course_id in self.courses:
            raise ValueError(f"Course with ID '{course_id}' already exists.")
        
        self.courses[course_id] = {
            "name": name,
            "level": level,
            "duration": duration,
            "price": price
        }

    def add_instructor(self, instructor_id, name, certification_level, contact_info):
        """
        Add a new instructor.

        Args:
            instructor_id (str): Unique identifier for the instructor.
            name (str): Name of the instructor.
            certification_level (str): Highest PADI certification level of the instructor.
            contact_info (str): Contact information for the instructor.
        """
        if instructor_id in self.instructors:
            raise ValueError(f"Instructor with ID '{instructor_id}' already exists.")
        
        self.instructors[instructor_id] = {
            "name": name,
            "certification_level": certification_level,
            "contact_info": contact_info
        }

    def assign_instructor_to_course(self, course_id, instructor_id):
        """
        Assign an instructor to a course.

        Args:
            course_id (str): ID of the course.
            instructor_id (str): ID of the instructor.
        """
        if course_id not in self.courses:
            raise ValueError(f"Course with ID '{course_id}' does not exist.")
        if instructor_id not in self.instructors:
            raise ValueError(f"Instructor with ID '{instructor_id}' does not exist.")
        
        self.courses[course_id]["instructor_id"] = instructor_id

    def get_course_details(self, course_id):
        """
        Retrieve details of a specific course.

        Args:
            course_id (str): ID of the course.

        Returns:
            dict: Details of the course.
        """
        if course_id not in self.courses:
            raise ValueError(f"Course with ID '{course_id}' does not exist.")
        
        course = self.courses[course_id]
        instructor_id = course.get("instructor_id")
        instructor = self.instructors.get(instructor_id, None)
        
        return {
            "course": course,
            "instructor": instructor
        }

    def save_data_to_file(self, file_path):
        """
        Save course and instructor data to a JSON file.

        Args:
            file_path (str): Path to the file where data will be saved.
        """
        data = {
            "courses": self.courses,
            "instructors": self.instructors
        }
        try:
            with open(file_path, 'w') as file:
                json.dump(data, file, indent=4)
        except IOError as e:
            raise IOError(f"Failed to save data to file: {e}")

    def load_data_from_file(self, file_path):
        """
        Load course and instructor data from a JSON file.

        Args:
            file_path (str): Path to the file from which data will be loaded.
        """
        try:
            with open(file_path, 'r') as file:
                data = json.load(file)
                self.courses = data.get("courses", {})
                self.instructors = data.get("instructors", {})
        except IOError as e:
            raise IOError(f"Failed to load data from file: {e}")
        except json.JSONDecodeError as e:
            raise ValueError(f"Failed to parse JSON data: {e}")


# Example usage
if __name__ == "__main__":
    manager = ScubaCourseManager()

    # Add courses
    manager.add_course("C001", "Open Water Diver", "Beginner", 3, 300.0)
    manager.add_course("C002", "Advanced Open Water Diver", "Intermediate", 2, 400.0)

    # Add instructors
    manager.add_instructor("I001", "John Doe", "Master Scuba Diver Trainer", "john.doe@example.com")
    manager.add_instructor("I002", "Jane Smith", "IDC Staff Instructor", "jane.smith@example.com")

    # Assign instructors to courses
    manager.assign_instructor_to_course("C001", "I001")
    manager.assign_instructor_to_course("C002", "I002")

    # Get course details
    print(manager.get_course_details("C001"))

    # Save data to file
    manager.save_data_to_file("scuba_data.json")

    # Load data from file
    manager.load_data_from_file("scuba_data.json")
    print(manager.get_course_details("C002"))
```
