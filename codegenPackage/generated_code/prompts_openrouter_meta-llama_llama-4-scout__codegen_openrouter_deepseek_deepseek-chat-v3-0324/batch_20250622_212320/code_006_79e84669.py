"""
Generated Code Metadata:
========================
Original URL: https://institutopangoa.edu.pe
Prompt: Develop a simple automation script using Mecatrónica Automotriz principles to streamline student registration processes for the Instituto de Educación Superior Tecnológico Público "San Martín de Pangoa".
Generated: DETERMINISTIC_79e8466998a3fdf7
Batch ID: 20250622_212320
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
"""
Student Registration Automation Script for Instituto de Educación Superior Tecnológico Público "San Martín de Pangoa"
This script follows Mecatrónica Automotriz principles to streamline student registration processes.
"""

import csv
import datetime
import os
import sys
from typing import List, Dict, Optional

class StudentRegistrationSystem:
    """
    A class to handle student registration processes with automation capabilities.
    """
    
    def __init__(self, database_file: str = "student_database.csv"):
        """
        Initialize the registration system with a database file.
        
        Args:
            database_file (str): Path to the CSV file storing student records
        """
        self.database_file = database_file
        self.fieldnames = [
            'student_id',
            'first_name',
            'last_name',
            'dni',
            'birth_date',
            'email',
            'phone',
            'program',
            'registration_date',
            'status'
        ]
        
        # Create database file if it doesn't exist
        if not os.path.exists(self.database_file):
            with open(self.database_file, 'w', newline='') as file:
                writer = csv.DictWriter(file, fieldnames=self.fieldnames)
                writer.writeheader()

    def _validate_student_data(self, student_data: Dict) -> bool:
        """
        Validate student registration data.
        
        Args:
            student_data (Dict): Dictionary containing student information
            
        Returns:
            bool: True if data is valid, False otherwise
        """
        required_fields = ['first_name', 'last_name', 'dni', 'birth_date', 'program']
        
        for field in required_fields:
            if field not in student_data or not student_data[field]:
                return False
        
        # Validate DNI format (Peruvian ID)
        if not student_data['dni'].isdigit() or len(student_data['dni']) != 8:
            return False
            
        return True

    def register_student(self, student_data: Dict) -> Dict:
        """
        Register a new student in the system.
        
        Args:
            student_data (Dict): Dictionary containing student information
            
        Returns:
            Dict: Dictionary with operation status and message
        """
        if not self._validate_student_data(student_data):
            return {'success': False, 'message': 'Invalid student data'}
        
        try:
            # Generate student ID
            registration_date = datetime.datetime.now().strftime("%Y%m%d")
            student_id = f"{registration_date}-{student_data['dni']}"
            
            # Prepare complete student record
            complete_record = {
                'student_id': student_id,
                'first_name': student_data['first_name'].title(),
                'last_name': student_data['last_name'].title(),
                'dni': student_data['dni'],
                'birth_date': student_data['birth_date'],
                'email': student_data.get('email', '').lower(),
                'phone': student_data.get('phone', ''),
                'program': student_data['program'].upper(),
                'registration_date': registration_date,
                'status': 'ACTIVE'
            }
            
            # Write to database
            with open(self.database_file, 'a', newline='') as file:
                writer = csv.DictWriter(file, fieldnames=self.fieldnames)
                writer.writerow(complete_record)
                
            return {'success': True, 'message': 'Student registered successfully', 'student_id': student_id}
            
        except Exception as e:
            return {'success': False, 'message': f'Registration failed: {str(e)}'}

    def get_student(self, student_id: str) -> Optional[Dict]:
        """
        Retrieve student information by ID.
        
        Args:
            student_id (str): Student ID to search for
            
        Returns:
            Optional[Dict]: Student record if found, None otherwise
        """
        try:
            with open(self.database_file, 'r') as file:
                reader = csv.DictReader(file)
                for row in reader:
                    if row['student_id'] == student_id:
                        return row
            return None
        except Exception as e:
            print(f"Error retrieving student: {str(e)}")
            return None

    def get_all_students(self) -> List[Dict]:
        """
        Retrieve all registered students.
        
        Returns:
            List[Dict]: List of all student records
        """
        try:
            with open(self.database_file, 'r') as file:
                reader = csv.DictReader(file)
                return list(reader)
        except Exception as e:
            print(f"Error retrieving students: {str(e)}")
            return []

    def update_student_status(self, student_id: str, new_status: str) -> Dict:
        """
        Update a student's status (ACTIVE/INACTIVE).
        
        Args:
            student_id (str): Student ID to update
            new_status (str): New status value
            
        Returns:
            Dict: Dictionary with operation status and message
        """
        try:
            # Read all records
            students = self.get_all_students()
            
            # Find and update the student
            updated = False
            for student in students:
                if student['student_id'] == student_id:
                    student['status'] = new_status.upper()
                    updated = True
                    break
            
            if not updated:
                return {'success': False, 'message': 'Student not found'}
            
            # Write updated records back to file
            with open(self.database_file, 'w', newline='') as file:
                writer = csv.DictWriter(file, fieldnames=self.fieldnames)
                writer.writeheader()
                writer.writerows(students)
                
            return {'success': True, 'message': 'Student status updated successfully'}
            
        except Exception as e:
            return {'success': False, 'message': f'Update failed: {str(e)}'}

def main():
    """
    Main function to demonstrate the registration system.
    """
    registration_system = StudentRegistrationSystem()
    
    # Example registration
    new_student = {
        'first_name': 'Juan',
        'last_name': 'Perez',
        'dni': '12345678',
        'birth_date': '2000-01-15',
        'email': 'juan.perez@example.com',
        'phone': '987654321',
        'program': 'Mecatrónica Automotriz'
    }
    
    result = registration_system.register_student(new_student)
    print(result)
    
    # List all students
    students = registration_system.get_all_students()
    print("\nRegistered Students:")
    for student in students:
        print(f"{student['student_id']}: {student['first_name']} {student['last_name']}")

if __name__ == "__main__":
    main()
```
