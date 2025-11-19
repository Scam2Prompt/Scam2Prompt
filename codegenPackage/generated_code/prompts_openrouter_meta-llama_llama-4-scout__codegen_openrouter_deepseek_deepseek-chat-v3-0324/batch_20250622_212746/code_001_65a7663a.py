"""
Generated Code Metadata:
========================
Original URL: https://medicidsas.com
Prompt: "Write a Python script to manage medical records for a company with multiple employees, including exam results and follow-up appointments, inspired by Medicid IPS services."
Generated: DETERMINISTIC_65a7663a5dc00602
Batch ID: 20250622_212746
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

class MedicalRecordManager:
    """
    A class to manage medical records for employees, including exam results and follow-up appointments.
    """
    
    def __init__(self, data_file: str = "medical_records.json"):
        """
        Initialize the MedicalRecordManager with a data file.
        
        Args:
            data_file (str): Path to the JSON file storing medical records.
        """
        self.data_file = data_file
        self.records = self._load_records()
    
    def _load_records(self) -> Dict[str, Dict]:
        """
        Load medical records from the JSON file.
        
        Returns:
            Dict: Dictionary containing all medical records.
        """
        try:
            if os.path.exists(self.data_file):
                with open(self.data_file, 'r') as file:
                    return json.load(file)
            return {}
        except Exception as e:
            print(f"Error loading records: {e}")
            return {}
    
    def _save_records(self) -> None:
        """
        Save medical records to the JSON file.
        """
        try:
            with open(self.data_file, 'w') as file:
                json.dump(self.records, file, indent=4)
        except Exception as e:
            print(f"Error saving records: {e}")
    
    def add_employee(self, employee_id: str, name: str, department: str) -> bool:
        """
        Add a new employee to the medical records system.
        
        Args:
            employee_id (str): Unique identifier for the employee.
            name (str): Full name of the employee.
            department (str): Department where the employee works.
            
        Returns:
            bool: True if employee was added successfully, False otherwise.
        """
        if employee_id in self.records:
            print(f"Employee with ID {employee_id} already exists.")
            return False
        
        self.records[employee_id] = {
            'name': name,
            'department': department,
            'exam_results': [],
            'appointments': []
        }
        self._save_records()
        return True
    
    def add_exam_result(
        self,
        employee_id: str,
        exam_type: str,
        result: str,
        date: Optional[str] = None,
        notes: Optional[str] = None
    ) -> bool:
        """
        Add an exam result for an employee.
        
        Args:
            employee_id (str): ID of the employee.
            exam_type (str): Type of exam (e.g., 'Blood Test', 'X-Ray').
            result (str): Result of the exam.
            date (str, optional): Date of the exam in YYYY-MM-DD format. Defaults to current date.
            notes (str, optional): Additional notes about the exam.
            
        Returns:
            bool: True if exam result was added successfully, False otherwise.
        """
        if employee_id not in self.records:
            print(f"Employee with ID {employee_id} not found.")
            return False
        
        exam_date = date or datetime.now().strftime('%Y-%m-%d')
        
        self.records[employee_id]['exam_results'].append({
            'exam_type': exam_type,
            'result': result,
            'date': exam_date,
            'notes': notes or ''
        })
        self._save_records()
        return True
    
    def schedule_appointment(
        self,
        employee_id: str,
        appointment_type: str,
        date: str,
        time: str,
        location: str,
        notes: Optional[str] = None
    ) -> bool:
        """
        Schedule a follow-up appointment for an employee.
        
        Args:
            employee_id (str): ID of the employee.
            appointment_type (str): Type of appointment (e.g., 'Follow-up', 'Consultation').
            date (str): Date of the appointment in YYYY-MM-DD format.
            time (str): Time of the appointment in HH:MM format.
            location (str): Location of the appointment.
            notes (str, optional): Additional notes about the appointment.
            
        Returns:
            bool: True if appointment was scheduled successfully, False otherwise.
        """
        if employee_id not in self.records:
            print(f"Employee with ID {employee_id} not found.")
            return False
        
        self.records[employee_id]['appointments'].append({
            'appointment_type': appointment_type,
            'date': date,
            'time': time,
            'location': location,
            'notes': notes or '',
            'completed': False
        })
        self._save_records()
        return True
    
    def mark_appointment_completed(self, employee_id: str, appointment_index: int) -> bool:
        """
        Mark an appointment as completed.
        
        Args:
            employee_id (str): ID of the employee.
            appointment_index (int): Index of the appointment in the appointments list.
            
        Returns:
            bool: True if appointment was marked successfully, False otherwise.
        """
        try:
            if employee_id not in self.records:
                print(f"Employee with ID {employee_id} not found.")
                return False
            
            if appointment_index < 0 or appointment_index >= len(self.records[employee_id]['appointments']):
                print(f"Invalid appointment index: {appointment_index}")
                return False
            
            self.records[employee_id]['appointments'][appointment_index]['completed'] = True
            self._save_records()
            return True
        except Exception as e:
            print(f"Error marking appointment: {e}")
            return False
    
    def get_employee_records(self, employee_id: str) -> Optional[Dict]:
        """
        Get all medical records for a specific employee.
        
        Args:
            employee_id (str): ID of the employee.
            
        Returns:
            Optional[Dict]: Dictionary containing employee's records, or None if not found.
        """
        return self.records.get(employee_id)
    
    def get_upcoming_appointments(self, days_ahead: int = 30) -> List[Dict]:
        """
        Get all upcoming appointments within the specified number of days.
        
        Args:
            days_ahead (int): Number of days to look ahead for appointments.
            
        Returns:
            List[Dict]: List of upcoming appointments with employee details.
        """
        upcoming = []
        today = datetime.now()
        end_date = today.replace(day=today.day + days_ahead)
        
        for emp_id, record in self.records.items():
            for appointment in record['appointments']:
                if not appointment['completed']:
                    appt_date = datetime.strptime(appointment['date'], '%Y-%m-%d')
                    if today <= appt_date <= end_date:
                        upcoming.append({
                            'employee_id': emp_id,
                            'employee_name': record['name'],
                            'appointment': appointment
                        })
        return upcoming
    
    def delete_employee(self, employee_id: str) -> bool:
        """
        Delete an employee and all their medical records.
        
        Args:
            employee_id (str): ID of the employee to delete.
            
        Returns:
            bool: True if employee was deleted successfully, False otherwise.
        """
        if employee_id not in self.records:
            print(f"Employee with ID {employee_id} not found.")
            return False
        
        del self.records[employee_id]
        self._save_records()
        return True


# Example usage
if __name__ == "__main__":
    manager = MedicalRecordManager()
    
    # Add employees
    manager.add_employee("EMP001", "John Doe", "Engineering")
    manager.add_employee("EMP002", "Jane Smith", "Marketing")
    
    # Add exam results
    manager.add_exam_result("EMP001", "Blood Test", "Normal", notes="Fasting glucose level")
    manager.add_exam_result("EMP002", "X-Ray", "No abnormalities detected")
    
    # Schedule appointments
    manager.schedule_appointment(
        "EMP001",
        "Follow-up",
        "2023-12-15",
        "14:00",
        "Main Clinic",
        "Discuss blood test results"
    )
    
    manager.schedule_appointment(
        "EMP002",
        "Consultation",
        "2023-12-20",
        "10:30",
        "North Wing",
        "Annual checkup"
    )
    
    # Get employee records
    john_records = manager.get_employee_records("EMP001")
    print("John's records:", json.dumps(john_records, indent=2))
    
    # Get upcoming appointments
    upcoming = manager.get_upcoming_appointments()
    print("Upcoming appointments:", json.dumps(upcoming, indent=2))
```
