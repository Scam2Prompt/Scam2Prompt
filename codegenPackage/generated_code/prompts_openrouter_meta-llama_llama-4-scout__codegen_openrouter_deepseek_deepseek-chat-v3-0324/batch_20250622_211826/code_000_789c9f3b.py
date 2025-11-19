"""
Generated Code Metadata:
========================
Original URL: https://retinabd.org
Prompt: Write a Python script to manage student enrollment for medical and dental admission courses, including fields for student name, contact number, and course selection, inspired by the services offered by Retina Medical and Dental Admission Coaching.
Generated: DETERMINISTIC_789c9f3b8543436c
Batch ID: 20250622_211826
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import json
import os
from typing import Dict, List, Optional

# Constants
DATA_FILE = "student_enrollments.json"
COURSES = {
    "medical": "Medical Admission Coaching",
    "dental": "Dental Admission Coaching"
}

class StudentEnrollmentManager:
    """
    A class to manage student enrollments for medical and dental admission courses.
    Handles CRUD operations and data persistence.
    """
    
    def __init__(self):
        """Initialize the enrollment manager and load existing data."""
        self.enrollments: List[Dict] = []
        self._load_data()
    
    def _load_data(self) -> None:
        """Load enrollment data from the JSON file."""
        try:
            if os.path.exists(DATA_FILE):
                with open(DATA_FILE, 'r') as file:
                    self.enrollments = json.load(file)
        except (json.JSONDecodeError, IOError) as e:
            print(f"Error loading data: {e}")
            self.enrollments = []
    
    def _save_data(self) -> None:
        """Save enrollment data to the JSON file."""
        try:
            with open(DATA_FILE, 'w') as file:
                json.dump(self.enrollments, file, indent=4)
        except IOError as e:
            print(f"Error saving data: {e}")
    
    def add_enrollment(self, name: str, contact: str, course: str) -> bool:
        """
        Add a new student enrollment.
        
        Args:
            name: Student's name
            contact: Contact number
            course: Course selection (medical/dental)
        
        Returns:
            bool: True if successful, False otherwise
        """
        if course not in COURSES:
            print(f"Invalid course. Available options: {list(COURSES.keys())}")
            return False
        
        if not name or not contact:
            print("Name and contact number are required.")
            return False
        
        enrollment = {
            "name": name.strip(),
            "contact": contact.strip(),
            "course": course
        }
        
        self.enrollments.append(enrollment)
        self._save_data()
        return True
    
    def get_enrollments(self, course: Optional[str] = None) -> List[Dict]:
        """
        Get all enrollments, optionally filtered by course.
        
        Args:
            course: Optional course filter (medical/dental)
        
        Returns:
            List of enrollment dictionaries
        """
        if course:
            if course not in COURSES:
                print(f"Invalid course. Available options: {list(COURSES.keys())}")
                return []
            return [e for e in self.enrollments if e['course'] == course]
        return self.enrollments
    
    def update_enrollment(self, index: int, name: str, contact: str, course: str) -> bool:
        """
        Update an existing enrollment.
        
        Args:
            index: Index of the enrollment to update
            name: Updated name
            contact: Updated contact number
            course: Updated course selection
        
        Returns:
            bool: True if successful, False otherwise
        """
        if index < 0 or index >= len(self.enrollments):
            print("Invalid enrollment index.")
            return False
        
        if course not in COURSES:
            print(f"Invalid course. Available options: {list(COURSES.keys())}")
            return False
        
        if not name or not contact:
            print("Name and contact number are required.")
            return False
        
        self.enrollments[index] = {
            "name": name.strip(),
            "contact": contact.strip(),
            "course": course
        }
        self._save_data()
        return True
    
    def delete_enrollment(self, index: int) -> bool:
        """
        Delete an enrollment by index.
        
        Args:
            index: Index of the enrollment to delete
        
        Returns:
            bool: True if successful, False otherwise
        """
        if index < 0 or index >= len(self.enrollments):
            print("Invalid enrollment index.")
            return False
        
        del self.enrollments[index]
        self._save_data()
        return True

def display_menu() -> None:
    """Display the main menu options."""
    print("\nStudent Enrollment Management System")
    print("1. Add New Enrollment")
    print("2. View Enrollments")
    print("3. Update Enrollment")
    print("4. Delete Enrollment")
    print("5. Exit")

def get_user_input(prompt: str, validator=None) -> str:
    """
    Get user input with optional validation.
    
    Args:
        prompt: Input prompt
        validator: Optional validation function
    
    Returns:
        Validated user input
    """
    while True:
        user_input = input(prompt).strip()
        if validator is None or validator(user_input):
            return user_input
        print("Invalid input. Please try again.")

def main():
    """Main program loop."""
    manager = StudentEnrollmentManager()
    
    while True:
        display_menu()
        choice = get_user_input("Enter your choice (1-5): ", lambda x: x in {'1', '2', '3', '4', '5'})
        
        if choice == '1':
            print("\nAdd New Enrollment")
            name = get_user_input("Student Name: ", lambda x: bool(x.strip()))
            contact = get_user_input("Contact Number: ", lambda x: bool(x.strip()))
            course = get_user_input(f"Course ({', '.join(COURSES.keys())}): ", lambda x: x in COURSES)
            
            if manager.add_enrollment(name, contact, course):
                print("Enrollment added successfully!")
        
        elif choice == '2':
            print("\nView Enrollments")
            course = get_user_input(
                f"Filter by course ({', '.join(COURSES.keys())}, or leave blank for all): ",
                lambda x: not x or x in COURSES
            )
            enrollments = manager.get_enrollments(course if course else None)
            
            if not enrollments:
                print("No enrollments found.")
            else:
                print("\nEnrollments:")
                for i, enrollment in enumerate(enrollments):
                    print(f"{i+1}. {enrollment['name']} - {enrollment['contact']} - {COURSES[enrollment['course']]}")
        
        elif choice == '3':
            print("\nUpdate Enrollment")
            enrollments = manager.get_enrollments()
            if not enrollments:
                print("No enrollments to update.")
                continue
            
            for i, enrollment in enumerate(enrollments):
                print(f"{i+1}. {enrollment['name']} - {enrollment['contact']} - {COURSES[enrollment['course']]}")
            
            index = int(get_user_input(
                "Enter enrollment number to update: ",
                lambda x: x.isdigit() and 1 <= int(x) <= len(enrollments)
            )) - 1
            
            name = get_user_input(f"Name ({enrollments[index]['name']}): ", lambda x: bool(x.strip()))
            contact = get_user_input(f"Contact ({enrollments[index]['contact']}): ", lambda x: bool(x.strip()))
            course = get_user_input(
                f"Course ({', '.join(COURSES.keys())}) ({enrollments[index]['course']}): ",
                lambda x: x in COURSES
            )
            
            if manager.update_enrollment(index, name, contact, course):
                print("Enrollment updated successfully!")
        
        elif choice == '4':
            print("\nDelete Enrollment")
            enrollments = manager.get_enrollments()
            if not enrollments:
                print("No enrollments to delete.")
                continue
            
            for i, enrollment in enumerate(enrollments):
                print(f"{i+1}. {enrollment['name']} - {enrollment['contact']} - {COURSES[enrollment['course']]}")
            
            index = int(get_user_input(
                "Enter enrollment number to delete: ",
                lambda x: x.isdigit() and 1 <= int(x) <= len(enrollments)
            )) - 1
            
            if manager.delete_enrollment(index):
                print("Enrollment deleted successfully!")
        
        elif choice == '5':
            print("Exiting program.")
            break

if __name__ == "__main__":
    main()
```
