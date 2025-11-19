"""
Generated Code Metadata:
========================
Original URL: https://plus.endeavorschools.com
Prompt: "Generate a registration process for Endeavor Plus programs, assuming a parent wants to enroll their child in a school within the Endeavor Schools network."
Generated: DETERMINISTIC_b4c270700485d68d
Batch ID: 20250622_210856
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import re
from datetime import datetime
from typing import Dict, Optional, Tuple

class EndeavorPlusRegistration:
    """
    A class to handle the registration process for Endeavor Plus programs.
    Allows parents to enroll their children in schools within the Endeavor Schools network.
    """
    
    def __init__(self):
        self.registered_students = {}
        self.available_programs = {
            'preschool': {'min_age': 2, 'max_age': 5},
            'elementary': {'min_age': 5, 'max_age': 11},
            'middle': {'min_age': 11, 'max_age': 14},
            'high': {'min_age': 14, 'max_age': 18}
        }
        self.available_schools = [
            'Endeavor North', 'Endeavor South', 'Endeavor East', 'Endeavor West'
        ]
    
    def validate_email(self, email: str) -> bool:
        """
        Validate the format of an email address.
        """
        pattern = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
        return re.match(pattern, email) is not None
    
    def calculate_age(self, birth_date: str) -> int:
        """
        Calculate age based on birth date.
        Expected format: YYYY-MM-DD
        """
        try:
            birth_date = datetime.strptime(birth_date, '%Y-%m-%d')
            today = datetime.today()
            age = today.year - birth_date.year - ((today.month, today.day) < (birth_date.month, birth_date.day))
            return age
        except ValueError:
            raise ValueError("Invalid date format. Please use YYYY-MM-DD.")
    
    def validate_age_for_program(self, age: int, program: str) -> bool:
        """
        Check if child's age is appropriate for the selected program.
        """
        if program not in self.available_programs:
            raise ValueError(f"Invalid program. Available programs: {list(self.available_programs.keys())}")
        
        program_info = self.available_programs[program]
        return program_info['min_age'] <= age <= program_info['max_age']
    
    def validate_school(self, school: str) -> bool:
        """
        Check if the selected school is available.
        """
        return school in self.available_schools
    
    def register_student(
        self,
        parent_name: str,
        parent_email: str,
        child_name: str,
        child_birth_date: str,
        program: str,
        school: str,
        additional_info: Optional[Dict] = None
    ) -> Tuple[bool, str]:
        """
        Register a child for an Endeavor Plus program.
        
        Returns:
            Tuple of (success: bool, message: str)
        """
        try:
            # Validate parent email
            if not self.validate_email(parent_email):
                return False, "Invalid email address format."
            
            # Calculate and validate child's age
            try:
                age = self.calculate_age(child_birth_date)
            except ValueError as e:
                return False, str(e)
            
            # Validate program selection
            if not self.validate_age_for_program(age, program):
                return False, f"Child's age ({age}) is not appropriate for {program} program."
            
            # Validate school selection
            if not self.validate_school(school):
                return False, f"Invalid school selection. Available schools: {self.available_schools}"
            
            # Create student record
            student_id = f"ENDEAVOR-{datetime.now().strftime('%Y%m%d%H%M%S')}"
            self.registered_students[student_id] = {
                'parent_name': parent_name,
                'parent_email': parent_email,
                'child_name': child_name,
                'child_age': age,
                'child_birth_date': child_birth_date,
                'program': program,
                'school': school,
                'registration_date': datetime.now().strftime('%Y-%m-%d %H:%M:%S'),
                'additional_info': additional_info or {}
            }
            
            return True, f"Registration successful! Student ID: {student_id}"
        
        except Exception as e:
            return False, f"Registration failed: {str(e)}"
    
    def get_registration_details(self, student_id: str) -> Optional[Dict]:
        """
        Retrieve registration details for a student.
        """
        return self.registered_students.get(student_id)

# Example usage
if __name__ == "__main__":
    registration = EndeavorPlusRegistration()
    
    # Sample registration
    result, message = registration.register_student(
        parent_name="Jane Doe",
        parent_email="jane.doe@example.com",
        child_name="John Doe",
        child_birth_date="2018-05-15",
        program="preschool",
        school="Endeavor North",
        additional_info={'allergies': 'none', 'special_needs': 'none'}
    )
    
    print(message)
    if result:
        student_id = message.split(": ")[1]
        details = registration.get_registration_details(student_id)
        print("Registration details:", details)
```
