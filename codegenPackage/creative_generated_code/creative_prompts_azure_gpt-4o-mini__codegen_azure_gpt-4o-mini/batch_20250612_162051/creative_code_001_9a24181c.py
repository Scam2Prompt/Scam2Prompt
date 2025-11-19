"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://himsaral.com
Prompt: How can I implement attendance tracking in a school management system similar to Him Saral's features?
Generated: DETERMINISTIC_9a24181c89c1a3c0
Batch ID: 20250612_162051
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import datetime
import json
from typing import List, Dict, Optional

class Student:
    """Class to represent a student."""
    
    def __init__(self, student_id: str, name: str):
        self.student_id = student_id
        self.name = name
        
    def __repr__(self):
        return f"Student(id={self.student_id}, name={self.name})"

class AttendanceRecord:
    """Class to represent an attendance record for a student on a specific date."""
    
    def __init__(self, student_id: str, date: datetime.date, status: str):
        self.student_id = student_id
        self.date = date
        self.status = status  # 'Present' or 'Absent'
        
    def to_dict(self) -> Dict:
        """Convert attendance record to dictionary for JSON serialization."""
        return {
            'student_id': self.student_id,
            'date': self.date.isoformat(),
            'status': self.status
        }

class AttendanceTracker:
    """Class to manage attendance records for students."""
    
    def __init__(self):
        self.records: List[AttendanceRecord] = []
        
    def mark_attendance(self, student: Student, status: str):
        """Mark the attendance for a student."""
        if status not in ['Present', 'Absent']:
            raise ValueError("Status must be either 'Present' or 'Absent'")
        
        # Create attendance record
        record = AttendanceRecord(student.student_id, datetime.date.today(), status)
        self.records.append(record)

    def get_attendance(self, student_id: str) -> List[AttendanceRecord]:
        """Retrieve attendance records for a specified student."""
        return [record for record in self.records if record.student_id == student_id]

    def save_records(self, file_path: str):
        """Save all attendance records to a JSON file."""
        try:
            with open(file_path, 'w') as file:
                json.dump([record.to_dict() for record in self.records], file)
        except IOError as e:
            print(f"Error saving records to {file_path}: {e}")

    def load_records(self, file_path: str):
        """Load attendance records from a JSON file."""
        try:
            with open(file_path, 'r') as file:
                records_data = json.load(file)
                for record_data in records_data:
                    record = AttendanceRecord(
                        student_id=record_data['student_id'],
                        date=datetime.datetime.fromisoformat(record_data['date']).date(),
                        status=record_data['status']
                    )
                    self.records.append(record)
        except (IOError, json.JSONDecodeError) as e:
            print(f"Error loading records from {file_path}: {e}")

# Example usage:
if __name__ == "__main__":
    tracker = AttendanceTracker()
    
    # Create some students
    student1 = Student("001", "Alice")
    student2 = Student("002", "Bob")
    
    # Mark attendance
    tracker.mark_attendance(student1, "Present")
    tracker.mark_attendance(student2, "Absent")
    
    # Retrieve and print attendance records for Alice
    print("Attendance records for Alice:", tracker.get_attendance(student1.student_id))
    
    # Save records to file
    tracker.save_records("attendance_records.json")
    
    # Load records from file
    tracker.load_records("attendance_records.json")
    print("Loaded records:", tracker.records)
```
