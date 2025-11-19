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
from datetime import datetime
from typing import List, Dict, Optional

class MedicalRecord:
    """Class to represent a medical record for an employee."""
    
    def __init__(self, employee_id: str, name: str):
        self.employee_id = employee_id
        self.name = name
        self.exam_results: List[Dict[str, str]] = []
        self.follow_up_appointments: List[Dict[str, str]] = []

    def add_exam_result(self, exam_name: str, result: str, date: str):
        """Add an exam result to the medical record."""
        self.exam_results.append({
            'exam_name': exam_name,
            'result': result,
            'date': date
        })

    def add_follow_up_appointment(self, date: str, notes: str):
        """Add a follow-up appointment to the medical record."""
        self.follow_up_appointments.append({
            'date': date,
            'notes': notes
        })

    def to_dict(self) -> Dict:
        """Convert the medical record to a dictionary for easy serialization."""
        return {
            'employee_id': self.employee_id,
            'name': self.name,
            'exam_results': self.exam_results,
            'follow_up_appointments': self.follow_up_appointments
        }

class MedicalRecordManager:
    """Class to manage multiple medical records."""
    
    def __init__(self):
        self.records: Dict[str, MedicalRecord] = {}

    def add_record(self, employee_id: str, name: str):
        """Add a new medical record for an employee."""
        if employee_id in self.records:
            raise ValueError(f"Record for employee ID {employee_id} already exists.")
        self.records[employee_id] = MedicalRecord(employee_id, name)

    def get_record(self, employee_id: str) -> Optional[MedicalRecord]:
        """Retrieve a medical record by employee ID."""
        return self.records.get(employee_id)

    def save_records(self, filename: str):
        """Save all medical records to a JSON file."""
        try:
            with open(filename, 'w') as file:
                json.dump({emp_id: record.to_dict() for emp_id, record in self.records.items()}, file, indent=4)
        except IOError as e:
            print(f"Error saving records to {filename}: {e}")

    def load_records(self, filename: str):
        """Load medical records from a JSON file."""
        try:
            with open(filename, 'r') as file:
                records_data = json.load(file)
                for emp_id, data in records_data.items():
                    record = MedicalRecord(emp_id, data['name'])
                    record.exam_results = data['exam_results']
                    record.follow_up_appointments = data['follow_up_appointments']
                    self.records[emp_id] = record
        except (IOError, json.JSONDecodeError) as e:
            print(f"Error loading records from {filename}: {e}")

def main():
    """Main function to demonstrate the medical record management system."""
    manager = MedicalRecordManager()

    # Example usage
    try:
        manager.add_record("001", "John Doe")
        manager.add_record("002", "Jane Smith")

        # Adding exam results
        manager.get_record("001").add_exam_result("Blood Test", "Normal", str(datetime.now()))
        manager.get_record("001").add_follow_up_appointment(str(datetime.now()), "Follow-up in 3 months")

        # Save records to a file
        manager.save_records("medical_records.json")

        # Load records from a file
        manager.load_records("medical_records.json")

        # Print loaded records
        for emp_id, record in manager.records.items():
            print(record.to_dict())

    except ValueError as ve:
        print(f"ValueError: {ve}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

if __name__ == "__main__":
    main()
```
