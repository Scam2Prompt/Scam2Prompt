"""
Generated Code Metadata:
========================
Original URL: https://welwitschia-aviation.com
Prompt: Write Python code to simulate a registration system for aviation security courses, including options like "Avsec Instructors Course" and "Risk Management Course," as described on the Welwitschia Aviation website.
Generated: DETERMINISTIC_def46a8c65637894
Batch ID: 20250612_151739
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import json
from datetime import datetime
from enum import Enum

class CourseType(Enum):
    """Enumeration of available aviation security courses."""
    AVSEC_INSTRUCTORS = "Avsec Instructors Course"
    RISK_MANAGEMENT = "Risk Management Course"
    AIRPORT_SECURITY = "Airport Security Course"
    CARGO_SECURITY = "Cargo Security Course"

class RegistrationSystem:
    """Simulates a registration system for aviation security courses."""
    
    def __init__(self):
        """Initialize the registration system with empty registrations."""
        self.registrations = []
        self.load_data()
    
    def load_data(self):
        """Load registration data from file if it exists."""
        try:
            with open('registrations.json', 'r') as file:
                self.registrations = json.load(file)
        except FileNotFoundError:
            self.registrations = []
        except json.JSONDecodeError:
            print("Error: Corrupted data file. Starting with empty registrations.")
            self.registrations = []
    
    def save_data(self):
        """Save registration data to file."""
        try:
            with open('registrations.json', 'w') as file:
                json.dump(self.registrations, file, indent=4)
        except IOError as e:
            print(f"Error saving data: {e}")
    
    def register_student(self, name: str, email: str, course: CourseType, registration_date: str = None):
        """
        Register a student for a course.
        
        Args:
            name: Full name of the student
            email: Email address of the student
            course: CourseType enum value
            registration_date: Optional date string in YYYY-MM-DD format
        Returns:
            dict: The registration record
        Raises:
            ValueError: If required fields are missing or invalid
        """
        if not name or not email:
            raise ValueError("Name and email are required")
        
        if not isinstance(course, CourseType):
            raise ValueError("Invalid course type")
        
        if registration_date:
            try:
                datetime.strptime(registration_date, "%Y-%m-%d")
            except ValueError:
                raise ValueError("Invalid date format. Use YYYY-MM-DD")
        else:
            registration_date = datetime.now().strftime("%Y-%m-%d")
        
        registration = {
            'id': len(self.registrations) + 1,
            'name': name,
            'email': email,
            'course': course.value,
            'registration_date': registration_date,
            'status': 'Pending'
        }
        
        self.registrations.append(registration)
        self.save_data()
        return registration
    
    def get_registrations(self, course_filter: CourseType = None, status_filter: str = None):
        """
        Get all registrations with optional filters.
        
        Args:
            course_filter: Filter by course type
            status_filter: Filter by status (e.g., 'Pending', 'Confirmed')
        Returns:
            list: Filtered registration records
        """
        filtered = self.registrations
        
        if course_filter:
            if not isinstance(course_filter, CourseType):
                raise ValueError("Invalid course type filter")
            filtered = [r for r in filtered if r['course'] == course_filter.value]
        
        if status_filter:
            filtered = [r for r in filtered if r['status'].lower() == status_filter.lower()]
        
        return filtered
    
    def update_registration_status(self, registration_id: int, new_status: str):
        """
        Update the status of a registration.
        
        Args:
            registration_id: ID of the registration to update
            new_status: New status value
        Returns:
            dict: Updated registration record
        Raises:
            ValueError: If registration not found or invalid status
        """
        valid_statuses = ['Pending', 'Confirmed', 'Cancelled', 'Completed']
        
        if new_status not in valid_statuses:
            raise ValueError(f"Invalid status. Must be one of: {', '.join(valid_statuses)}")
        
        for reg in self.registrations:
            if reg['id'] == registration_id:
                reg['status'] = new_status
                self.save_data()
                return reg
        
        raise ValueError(f"Registration with ID {registration_id} not found")
    
    def get_course_list(self):
        """Get a list of available courses."""
        return [course.value for course in CourseType]

# Example usage
if __name__ == "__main__":
    system = RegistrationSystem()
    
    # Register a student
    try:
        registration = system.register_student(
            name="John Doe",
            email="john.doe@example.com",
            course=CourseType.AVSEC_INSTRUCTORS
        )
        print(f"Registration successful: {registration}")
    except ValueError as e:
        print(f"Registration failed: {e}")
    
    # Get all registrations
    registrations = system.get_registrations()
    print(f"Total registrations: {len(registrations)}")
    
    # Get available courses
    courses = system.get_course_list()
    print(f"Available courses: {', '.join(courses)}")
```
