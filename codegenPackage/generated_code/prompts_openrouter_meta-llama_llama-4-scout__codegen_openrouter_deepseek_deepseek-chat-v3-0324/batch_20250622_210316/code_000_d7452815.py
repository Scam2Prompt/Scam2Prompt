"""
Generated Code Metadata:
========================
Original URL: https://araform.org
Prompt: "Generate a Python script to manage course registrations for a vocational training program like those offered on araform.org."
Generated: DETERMINISTIC_d7452815c35aecba
Batch ID: 20250622_210316
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
from datetime import datetime
from typing import Dict, List, Optional, Union

class CourseRegistrationSystem:
    """
    A class to manage course registrations for a vocational training program.
    Handles student registration, course management, and enrollment tracking.
    """
    
    def __init__(self, data_file: str = "course_registrations.json"):
        """
        Initialize the registration system.
        
        Args:
            data_file (str): Path to the JSON file storing registration data.
        """
        self.data_file = data_file
        self.registrations = self._load_data()
    
    def _load_data(self) -> Dict:
        """
        Load registration data from JSON file or initialize empty structure.
        
        Returns:
            Dict: Loaded or initialized registration data.
        """
        try:
            if os.path.exists(self.data_file):
                with open(self.data_file, 'r') as f:
                    return json.load(f)
        except Exception as e:
            print(f"Error loading data file: {e}")
        
        return {
            "students": {},
            "courses": {},
            "enrollments": {}
        }
    
    def _save_data(self) -> None:
        """
        Save current registration data to JSON file.
        """
        try:
            with open(self.data_file, 'w') as f:
                json.dump(self.registrations, f, indent=2)
        except Exception as e:
            print(f"Error saving data file: {e}")
    
    def add_student(self, student_id: str, name: str, email: str) -> bool:
        """
        Register a new student.
        
        Args:
            student_id (str): Unique student identifier
            name (str): Student's full name
            email (str): Student's email address
            
        Returns:
            bool: True if successful, False if student already exists
        """
        if student_id in self.registrations["students"]:
            return False
            
        self.registrations["students"][student_id] = {
            "name": name,
            "email": email,
            "registration_date": datetime.now().isoformat()
        }
        self._save_data()
        return True
    
    def add_course(self, course_id: str, title: str, capacity: int) -> bool:
        """
        Add a new course to the system.
        
        Args:
            course_id (str): Unique course identifier
            title (str): Course title
            capacity (int): Maximum number of students
            
        Returns:
            bool: True if successful, False if course already exists
        """
        if course_id in self.registrations["courses"]:
            return False
            
        self.registrations["courses"][course_id] = {
            "title": title,
            "capacity": capacity,
            "enrolled": 0
        }
        self._save_data()
        return True
    
    def enroll_student(self, student_id: str, course_id: str) -> bool:
        """
        Enroll a student in a course.
        
        Args:
            student_id (str): ID of student to enroll
            course_id (str): ID of course to enroll in
            
        Returns:
            bool: True if successful, False if enrollment failed
        """
        if (student_id not in self.registrations["students"] or 
            course_id not in self.registrations["courses"]):
            return False
            
        enrollment_key = f"{student_id}_{course_id}"
        if enrollment_key in self.registrations["enrollments"]:
            return False
            
        course = self.registrations["courses"][course_id]
        if course["enrolled"] >= course["capacity"]:
            return False
            
        self.registrations["enrollments"][enrollment_key] = {
            "student_id": student_id,
            "course_id": course_id,
            "enrollment_date": datetime.now().isoformat()
        }
        course["enrolled"] += 1
        self._save_data()
        return True
    
    def get_student_enrollments(self, student_id: str) -> List[Dict]:
        """
        Get all courses a student is enrolled in.
        
        Args:
            student_id (str): ID of student
            
        Returns:
            List[Dict]: List of enrollment records
        """
        return [
            enrollment for key, enrollment in self.registrations["enrollments"].items()
            if enrollment["student_id"] == student_id
        ]
    
    def get_course_enrollments(self, course_id: str) -> List[Dict]:
        """
        Get all students enrolled in a course.
        
        Args:
            course_id (str): ID of course
            
        Returns:
            List[Dict]: List of enrollment records
        """
        return [
            enrollment for key, enrollment in self.registrations["enrollments"].items()
            if enrollment["course_id"] == course_id
        ]
    
    def drop_student(self, student_id: str, course_id: str) -> bool:
        """
        Drop a student from a course.
        
        Args:
            student_id (str): ID of student to drop
            course_id (str): ID of course to drop from
            
        Returns:
            bool: True if successful, False if drop failed
        """
        enrollment_key = f"{student_id}_{course_id}"
        if enrollment_key not in self.registrations["enrollments"]:
            return False
            
        del self.registrations["enrollments"][enrollment_key]
        self.registrations["courses"][course_id]["enrolled"] -= 1
        self._save_data()
        return True
    
    def get_course_info(self, course_id: str) -> Optional[Dict]:
        """
        Get information about a specific course.
        
        Args:
            course_id (str): ID of course
            
        Returns:
            Optional[Dict]: Course information if found, None otherwise
        """
        return self.registrations["courses"].get(course_id)
    
    def get_student_info(self, student_id: str) -> Optional[Dict]:
        """
        Get information about a specific student.
        
        Args:
            student_id (str): ID of student
            
        Returns:
            Optional[Dict]: Student information if found, None otherwise
        """
        return self.registrations["students"].get(student_id)
    
    def list_courses(self) -> List[Dict]:
        """
        Get list of all available courses.
        
        Returns:
            List[Dict]: List of all courses
        """
        return list(self.registrations["courses"].values())
    
    def list_students(self) -> List[Dict]:
        """
        Get list of all registered students.
        
        Returns:
            List[Dict]: List of all students
        """
        return list(self.registrations["students"].values())

# Example usage
if __name__ == "__main__":
    system = CourseRegistrationSystem()
    
    # Add some sample data
    system.add_student("S001", "John Doe", "john@example.com")
    system.add_student("S002", "Jane Smith", "jane@example.com")
    
    system.add_course("C001", "Web Development", 30)
    system.add_course("C002", "Data Science", 25)
    
    # Enroll students
    system.enroll_student("S001", "C001")
    system.enroll_student("S002", "C001")
    system.enroll_student("S002", "C002")
    
    # Display some information
    print("All Courses:")
    for course in system.list_courses():
        print(f"{course['title']} (Enrolled: {course['enrolled']}/{course['capacity']})")
    
    print("\nJohn's Enrollments:")
    for enrollment in system.get_student_enrollments("S001"):
        course = system.get_course_info(enrollment["course_id"])
        print(f"{course['title']} (Enrolled on: {enrollment['enrollment_date']})")
```
