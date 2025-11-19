"""
Generated Code Metadata:
========================
Original URL: https://plus.endeavorschools.com
Prompt: "Write a Python script to manage registrations for multiple Endeavor Plus programs across different schools, including fields for student information, program selection, and school location."
Generated: DETERMINISTIC_683bdef5f171ed5f
Batch ID: 20250622_210856
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import csv
import os
from datetime import datetime
from typing import List, Dict, Optional

class ProgramRegistration:
    """
    A class to manage student registrations for Endeavor Plus programs across multiple schools.
    """
    
    def __init__(self, data_file: str = "registrations.csv"):
        """
        Initialize the registration system with a data file.
        
        Args:
            data_file (str): Path to the CSV file storing registration data.
        """
        self.data_file = data_file
        self.fieldnames = [
            'student_id',
            'first_name',
            'last_name',
            'email',
            'phone',
            'grade_level',
            'program_name',
            'school_name',
            'school_location',
            'registration_date'
        ]
        
        # Create data file if it doesn't exist
        if not os.path.exists(self.data_file):
            with open(self.data_file, 'w', newline='') as file:
                writer = csv.DictWriter(file, fieldnames=self.fieldnames)
                writer.writeheader()

    def _validate_student_info(self, student_info: Dict) -> bool:
        """
        Validate student registration information.
        
        Args:
            student_info (Dict): Dictionary containing student registration data.
            
        Returns:
            bool: True if data is valid, False otherwise.
        """
        required_fields = ['first_name', 'last_name', 'email', 'program_name', 'school_name']
        for field in required_fields:
            if field not in student_info or not student_info[field]:
                return False
        
        if not isinstance(student_info.get('grade_level', ''), str):
            return False
            
        return True

    def register_student(self, student_info: Dict) -> Dict:
        """
        Register a student for a program.
        
        Args:
            student_info (Dict): Dictionary containing student registration data.
            
        Returns:
            Dict: Dictionary with success status and message or error.
        """
        if not self._validate_student_info(student_info):
            return {'success': False, 'message': 'Invalid student information provided'}
        
        try:
            registration_data = {
                'student_id': str(datetime.now().timestamp()),
                'first_name': student_info['first_name'].strip(),
                'last_name': student_info['last_name'].strip(),
                'email': student_info['email'].strip().lower(),
                'phone': student_info.get('phone', '').strip(),
                'grade_level': student_info.get('grade_level', '').strip(),
                'program_name': student_info['program_name'].strip(),
                'school_name': student_info['school_name'].strip(),
                'school_location': student_info.get('school_location', '').strip(),
                'registration_date': datetime.now().strftime('%Y-%m-%d %H:%M:%S')
            }
            
            with open(self.data_file, 'a', newline='') as file:
                writer = csv.DictWriter(file, fieldnames=self.fieldnames)
                writer.writerow(registration_data)
            
            return {'success': True, 'message': 'Registration successful', 'student_id': registration_data['student_id']}
        
        except Exception as e:
            return {'success': False, 'message': f'Registration failed: {str(e)}'}

    def get_registrations(self, school_name: Optional[str] = None, program_name: Optional[str] = None) -> List[Dict]:
        """
        Get all registrations, optionally filtered by school or program.
        
        Args:
            school_name (Optional[str]): Filter by school name.
            program_name (Optional[str]): Filter by program name.
            
        Returns:
            List[Dict]: List of registration records.
        """
        registrations = []
        
        try:
            with open(self.data_file, 'r', newline='') as file:
                reader = csv.DictReader(file)
                for row in reader:
                    if (school_name is None or row['school_name'].lower() == school_name.lower()) and \
                       (program_name is None or row['program_name'].lower() == program_name.lower()):
                        registrations.append(dict(row))
        
        except FileNotFoundError:
            pass
            
        return registrations

    def get_student_registrations(self, email: str) -> List[Dict]:
        """
        Get all registrations for a specific student by email.
        
        Args:
            email (str): Student's email address.
            
        Returns:
            List[Dict]: List of registration records for the student.
        """
        return self.get_registrations_by_field('email', email.lower())

    def get_registrations_by_field(self, field: str, value: str) -> List[Dict]:
        """
        Get registrations filtered by a specific field and value.
        
        Args:
            field (str): Field to filter by.
            value (str): Value to match.
            
        Returns:
            List[Dict]: List of matching registration records.
        """
        if field not in self.fieldnames:
            return []
            
        registrations = []
        
        try:
            with open(self.data_file, 'r', newline='') as file:
                reader = csv.DictReader(file)
                for row in reader:
                    if str(row[field]).lower() == value.lower():
                        registrations.append(dict(row))
        
        except FileNotFoundError:
            pass
            
        return registrations

    def count_registrations(self, school_name: Optional[str] = None, program_name: Optional[str] = None) -> int:
        """
        Count registrations, optionally filtered by school or program.
        
        Args:
            school_name (Optional[str]): Filter by school name.
            program_name (Optional[str]): Filter by program name.
            
        Returns:
            int: Number of matching registrations.
        """
        return len(self.get_registrations(school_name, program_name))

# Example usage
if __name__ == "__main__":
    registration_system = ProgramRegistration()
    
    # Register a student
    student_data = {
        'first_name': 'John',
        'last_name': 'Doe',
        'email': 'john.doe@example.com',
        'phone': '555-123-4567',
        'grade_level': '10',
        'program_name': 'Robotics',
        'school_name': 'Central High',
        'school_location': 'Springfield'
    }
    
    result = registration_system.register_student(student_data)
    print(result)
    
    # Get all registrations
    all_registrations = registration_system.get_registrations()
    print(f"Total registrations: {len(all_registrations)}")
    
    # Get registrations for a specific school
    central_registrations = registration_system.get_registrations(school_name='Central High')
    print(f"Central High registrations: {len(central_registrations)}")
```
