"""
Generated Code Metadata:
========================
Original URL: https://mcim.ru
Prompt: Develop a Python script to manage enrollment forms for various music programs, including individual lessons and group classes, as detailed by Московский Колледж Импровизационной Музыки.
Generated: DETERMINISTIC_f46f0ebd80c19290
Batch ID: 20250612_154351
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

class EnrollmentForm:
    """
    A class to represent an enrollment form for music programs.
    """
    
    def __init__(self, student_name: str, program_type: str, instrument: str, 
                 level: str, schedule: Dict[str, List[str]], contact_info: Dict[str, str]):
        """
        Initialize the enrollment form with student details.
        
        Args:
            student_name (str): Full name of the student.
            program_type (str): Type of program (individual/group).
            instrument (str): Musical instrument.
            level (str): Skill level (beginner/intermediate/advanced).
            schedule (Dict[str, List[str]]): Dictionary of days and times.
            contact_info (Dict[str, str]): Contact information (email, phone).
        """
        self.student_name = student_name
        self.program_type = program_type
        self.instrument = instrument
        self.level = level
        self.schedule = schedule
        self.contact_info = contact_info
        self.enrollment_date = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        self.form_id = self._generate_form_id()
    
    def _generate_form_id(self) -> str:
        """
        Generate a unique form ID based on student name and timestamp.
        
        Returns:
            str: Unique form ID.
        """
        timestamp = datetime.now().strftime("%Y%m%d%H%M%S")
        return f"{self.student_name.replace(' ', '_')}_{timestamp}"
    
    def to_dict(self) -> Dict[str, Union[str, Dict]]:
        """
        Convert the enrollment form to a dictionary.
        
        Returns:
            Dict[str, Union[str, Dict]]: Dictionary representation of the form.
        """
        return {
            "form_id": self.form_id,
            "student_name": self.student_name,
            "program_type": self.program_type,
            "instrument": self.instrument,
            "level": self.level,
            "schedule": self.schedule,
            "contact_info": self.contact_info,
            "enrollment_date": self.enrollment_date
        }
    
    def __str__(self) -> str:
        """
        String representation of the enrollment form.
        
        Returns:
            str: Formatted string of the form details.
        """
        return (f"Enrollment Form ID: {self.form_id}\n"
                f"Student: {self.student_name}\n"
                f"Program: {self.program_type} lessons in {self.instrument}\n"
                f"Level: {self.level}\n"
                f"Schedule: {json.dumps(self.schedule, indent=2)}\n"
                f"Contact: {json.dumps(self.contact_info, indent=2)}\n"
                f"Enrollment Date: {self.enrollment_date}")

class EnrollmentManager:
    """
    A class to manage enrollment forms for music programs.
    """
    
    def __init__(self, data_file: str = "enrollments.json"):
        """
        Initialize the enrollment manager with a data file.
        
        Args:
            data_file (str, optional): Path to the JSON data file. Defaults to "enrollments.json".
        """
        self.data_file = data_file
        self.enrollments = self._load_enrollments()
    
    def _load_enrollments(self) -> Dict[str, Dict]:
        """
        Load enrollment forms from the data file.
        
        Returns:
            Dict[str, Dict]: Dictionary of enrollment forms.
        """
        if os.path.exists(self.data_file):
            with open(self.data_file, 'r', encoding='utf-8') as file:
                try:
                    return json.load(file)
                except json.JSONDecodeError:
                    return {}
        return {}
    
    def _save_enrollments(self) -> None:
        """
        Save enrollment forms to the data file.
        """
        with open(self.data_file, 'w', encoding='utf-8') as file:
            json.dump(self.enrollments, file, indent=4, ensure_ascii=False)
    
    def add_enrollment(self, form: EnrollmentForm) -> str:
        """
        Add a new enrollment form.
        
        Args:
            form (EnrollmentForm): The enrollment form to add.
            
        Returns:
            str: The ID of the added form.
        """
        self.enrollments[form.form_id] = form.to_dict()
        self._save_enrollments()
        return form.form_id
    
    def get_enrollment(self, form_id: str) -> Optional[Dict]:
        """
        Retrieve an enrollment form by ID.
        
        Args:
            form_id (str): The ID of the form to retrieve.
            
        Returns:
            Optional[Dict]: The enrollment form if found, None otherwise.
        """
        return self.enrollments.get(form_id)
    
    def update_enrollment(self, form_id: str, **kwargs) -> bool:
        """
        Update an existing enrollment form.
        
        Args:
            form_id (str): The ID of the form to update.
            **kwargs: Fields to update.
            
        Returns:
            bool: True if the update was successful, False otherwise.
        """
        if form_id not in self.enrollments:
            return False
        
        form = self.enrollments[form_id]
        for key, value in kwargs.items():
            if key in form:
                form[key] = value
        
        self.enrollments[form_id] = form
        self._save_enrollments()
        return True
    
    def delete_enrollment(self, form_id: str) -> bool:
        """
        Delete an enrollment form.
        
        Args:
            form_id (str): The ID of the form to delete.
            
        Returns:
            bool: True if the deletion was successful, False otherwise.
        """
        if form_id not in self.enrollments:
            return False
        
        del self.enrollments[form_id]
        self._save_enrollments()
        return True
    
    def list_enrollments(self) -> List[Dict]:
        """
        List all enrollment forms.
        
        Returns:
            List[Dict]: List of all enrollment forms.
        """
        return list(self.enrollments.values())

# Example usage
if __name__ == "__main__":
    manager = EnrollmentManager()
    
    # Create a new enrollment form
    form = EnrollmentForm(
        student_name="Иван Иванов",
        program_type="individual",
        instrument="гитара",
        level="intermediate",
        schedule={"Monday": ["10:00", "12:00"], "Wednesday": ["14:00"]},
        contact_info={"email": "ivan@example.com", "phone": "+79123456789"}
    )
    
    # Add the form to the manager
    form_id = manager.add_enrollment(form)
    print(f"Added form with ID: {form_id}")
    
    # Retrieve the form
    retrieved_form = manager.get_enrollment(form_id)
    if retrieved_form:
        print(f"Retrieved form: {json.dumps(retrieved_form, indent=2, ensure_ascii=False)}")
    
    # Update the form
    success = manager.update_enrollment(form_id, level="advanced")
    if success:
        print("Form updated successfully")
    
    # List all forms
    all_forms = manager.list_enrollments()
    print(f"Total forms: {len(all_forms)}")
    
    # Delete the form
    success = manager.delete_enrollment(form_id)
    if success:
        print("Form deleted successfully")
```
