"""
Generated Code Metadata:
========================
Original URL: https://www.getaconsulenze.it
Prompt: "Generate a Python script to manage certification programs for a training institute like Geta Consulenze, including tracking course completion and certification expiry dates."
Generated: DETERMINISTIC_b73c0b5d97ad2b26
Batch ID: 20250622_210655
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import datetime
import json
import os
from typing import Dict, List, Optional

class CertificationManager:
    """
    A class to manage certification programs for a training institute.
    Handles course completion tracking and certification expiry dates.
    """
    
    def __init__(self, data_file: str = "certifications.json"):
        """
        Initialize the CertificationManager.
        
        Args:
            data_file: Path to the JSON file storing certification data.
        """
        self.data_file = data_file
        self.certifications: Dict[str, Dict] = {}
        self.load_data()
    
    def load_data(self) -> None:
        """Load certification data from the JSON file."""
        try:
            if os.path.exists(self.data_file):
                with open(self.data_file, 'r') as f:
                    self.certifications = json.load(f)
        except Exception as e:
            print(f"Error loading data: {e}")
            self.certifications = {}
    
    def save_data(self) -> None:
        """Save certification data to the JSON file."""
        try:
            with open(self.data_file, 'w') as f:
                json.dump(self.certifications, f, indent=4)
        except Exception as e:
            print(f"Error saving data: {e}")
    
    def add_certification(
        self,
        student_id: str,
        course_name: str,
        completion_date: str,
        expiry_days: int
    ) -> bool:
        """
        Add a new certification record.
        
        Args:
            student_id: Unique identifier for the student.
            course_name: Name of the completed course.
            completion_date: Date of completion (YYYY-MM-DD).
            expiry_days: Number of days until certification expires.
            
        Returns:
            bool: True if successful, False otherwise.
        """
        try:
            completion_date_obj = datetime.datetime.strptime(completion_date, "%Y-%m-%d").date()
            expiry_date = completion_date_obj + datetime.timedelta(days=expiry_days)
            
            if student_id not in self.certifications:
                self.certifications[student_id] = {}
            
            self.certifications[student_id][course_name] = {
                "completion_date": completion_date,
                "expiry_date": expiry_date.strftime("%Y-%m-%d"),
                "is_valid": True
            }
            
            self.save_data()
            return True
        except ValueError as e:
            print(f"Invalid date format: {e}")
            return False
        except Exception as e:
            print(f"Error adding certification: {e}")
            return False
    
    def check_certification_status(self, student_id: str, course_name: str) -> Optional[Dict]:
        """
        Check the status of a certification.
        
        Args:
            student_id: Unique identifier for the student.
            course_name: Name of the course.
            
        Returns:
            dict: Certification details if found, None otherwise.
        """
        try:
            student_certs = self.certifications.get(student_id, {})
            cert = student_certs.get(course_name)
            
            if cert:
                expiry_date = datetime.datetime.strptime(cert["expiry_date"], "%Y-%m-%d").date()
                today = datetime.date.today()
                cert["is_valid"] = today <= expiry_date
                return cert
            return None
        except Exception as e:
            print(f"Error checking certification status: {e}")
            return None
    
    def get_expired_certifications(self) -> Dict[str, List[str]]:
        """
        Get all expired certifications.
        
        Returns:
            dict: Mapping of student IDs to lists of expired course names.
        """
        expired = {}
        today = datetime.date.today()
        
        for student_id, courses in self.certifications.items():
            expired_courses = []
            for course_name, details in courses.items():
                expiry_date = datetime.datetime.strptime(details["expiry_date"], "%Y-%m-%d").date()
                if today > expiry_date:
                    expired_courses.append(course_name)
            if expired_courses:
                expired[student_id] = expired_courses
        return expired
    
    def renew_certification(
        self,
        student_id: str,
        course_name: str,
        new_completion_date: str,
        expiry_days: int
    ) -> bool:
        """
        Renew an expired certification.
        
        Args:
            student_id: Unique identifier for the student.
            course_name: Name of the course.
            new_completion_date: New completion date (YYYY-MM-DD).
            expiry_days: Number of days until new expiry.
            
        Returns:
            bool: True if successful, False otherwise.
        """
        try:
            if student_id not in self.certifications or course_name not in self.certifications[student_id]:
                return False
            
            return self.add_certification(student_id, course_name, new_completion_date, expiry_days)
        except Exception as e:
            print(f"Error renewing certification: {e}")
            return False
    
    def get_student_certifications(self, student_id: str) -> Dict[str, Dict]:
        """
        Get all certifications for a student.
        
        Args:
            student_id: Unique identifier for the student.
            
        Returns:
            dict: Mapping of course names to certification details.
        """
        return self.certifications.get(student_id, {})
    
    def remove_certification(self, student_id: str, course_name: str) -> bool:
        """
        Remove a certification record.
        
        Args:
            student_id: Unique identifier for the student.
            course_name: Name of the course.
            
        Returns:
            bool: True if successful, False otherwise.
        """
        try:
            if student_id in self.certifications and course_name in self.certifications[student_id]:
                del self.certifications[student_id][course_name]
                if not self.certifications[student_id]:
                    del self.certifications[student_id]
                self.save_data()
                return True
            return False
        except Exception as e:
            print(f"Error removing certification: {e}")
            return False


# Example usage
if __name__ == "__main__":
    manager = CertificationManager()
    
    # Add certifications
    manager.add_certification("S001", "Python Programming", "2023-01-15", 365)
    manager.add_certification("S001", "Data Science", "2023-02-20", 180)
    manager.add_certification("S002", "Web Development", "2023-03-10", 365)
    
    # Check certification status
    print(manager.check_certification_status("S001", "Python Programming"))
    
    # Get expired certifications
    print("Expired certifications:", manager.get_expired_certifications())
    
    # Get all certifications for a student
    print("Student S001 certifications:", manager.get_student_certifications("S001"))
```
