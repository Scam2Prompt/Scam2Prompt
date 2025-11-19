"""
Generated Code Metadata:
========================
Original URL: https://educarcomitan.mx
Prompt: Write a Python script to create a flexible schedule system for students preparing for admission exams, referencing the personalized class structure described on Educar Comitán's website.
Generated: DETERMINISTIC_b7ec97ec5b64b1b1
Batch ID: 20250612_153401
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import json
from datetime import datetime, timedelta
from typing import List, Dict, Optional, Union

class ScheduleSystem:
    """
    A flexible schedule system for students preparing for admission exams.
    Allows creating, managing, and tracking study schedules with personalized classes.
    """
    
    def __init__(self):
        self.students = {}
        self.subjects = []
        self.classes = []
        self.schedules = {}
    
    def add_student(self, student_id: str, name: str, contact: str, goals: List[str]) -> bool:
        """
        Add a new student to the system.
        
        Args:
            student_id: Unique identifier for the student
            name: Full name of the student
            contact: Contact information (email/phone)
            goals: List of exam preparation goals
            
        Returns:
            bool: True if student was added successfully, False if student already exists
        """
        if student_id in self.students:
            return False
            
        self.students[student_id] = {
            'name': name,
            'contact': contact,
            'goals': goals,
            'progress': {}
        }
        return True
    
    def add_subject(self, subject_id: str, name: str, topics: List[str]) -> bool:
        """
        Add a subject to be studied.
        
        Args:
            subject_id: Unique identifier for the subject
            name: Name of the subject
            topics: List of topics to cover in this subject
            
        Returns:
            bool: True if subject was added, False if subject already exists
        """
        if any(subj['id'] == subject_id for subj in self.subjects):
            return False
            
        self.subjects.append({
            'id': subject_id,
            'name': name,
            'topics': topics
        })
        return True
    
    def create_class(self, class_id: str, subject_id: str, duration: int, 
                    difficulty: str, required_materials: List[str]) -> bool:
        """
        Create a personalized class for a subject.
        
        Args:
            class_id: Unique identifier for the class
            subject_id: Subject this class belongs to
            duration: Duration in minutes
            difficulty: Difficulty level (beginner, intermediate, advanced)
            required_materials: List of required materials
            
        Returns:
            bool: True if class was created, False if subject doesn't exist or class ID exists
        """
        if not any(subj['id'] == subject_id for subj in self.subjects):
            return False
            
        if any(cls['id'] == class_id for cls in self.classes):
            return False
            
        self.classes.append({
            'id': class_id,
            'subject_id': subject_id,
            'duration': duration,
            'difficulty': difficulty,
            'materials': required_materials
        })
        return True
    
    def create_schedule(self, student_id: str, start_date: str, 
                       study_days: List[str], daily_hours: int) -> bool:
        """
        Create a study schedule for a student.
        
        Args:
            student_id: ID of the student
            start_date: Start date in YYYY-MM-DD format
            study_days: List of days to study (e.g., ['Mon', 'Wed', 'Fri'])
            daily_hours: Maximum study hours per day
            
        Returns:
            bool: True if schedule was created, False if student doesn't exist or schedule exists
        """
        if student_id not in self.students:
            return False
            
        if student_id in self.schedules:
            return False
            
        try:
            parsed_date = datetime.strptime(start_date, '%Y-%m-%d').date()
        except ValueError:
            return False
            
        self.schedules[student_id] = {
            'start_date': start_date,
            'study_days': study_days,
            'daily_hours': daily_hours,
            'assigned_classes': [],
            'completed_classes': []
        }
        return True
    
    def assign_class_to_schedule(self, student_id: str, class_id: str, 
                                scheduled_date: str) -> bool:
        """
        Assign a class to a student's schedule on a specific date.
        
        Args:
            student_id: ID of the student
            class_id: ID of the class to assign
            scheduled_date: Date in YYYY-MM-DD format
            
        Returns:
            bool: True if assignment was successful, False otherwise
        """
        if student_id not in self.schedules:
            return False
            
        if not any(cls['id'] == class_id for cls in self.classes):
            return False
            
        try:
            datetime.strptime(scheduled_date, '%Y-%m-%d').date()
        except ValueError:
            return False
            
        # Check if class is already assigned to this student
        if any(ac['class_id'] == class_id for ac in self.schedules[student_id]['assigned_classes']):
            return False
            
        # Get class duration
        class_duration = next(cls['duration'] for cls in self.classes if cls['id'] == class_id)
        
        self.schedules[student_id]['assigned_classes'].append({
            'class_id': class_id,
            'scheduled_date': scheduled_date,
            'duration': class_duration,
            'completed': False
        })
        return True
    
    def mark_class_completed(self, student_id: str, class_id: str) -> bool:
        """
        Mark a class as completed in the student's schedule.
        
        Args:
            student_id: ID of the student
            class_id: ID of the class to mark as completed
            
        Returns:
            bool: True if marking was successful, False otherwise
        """
        if student_id not in self.schedules:
            return False
            
        assigned_classes = self.schedules[student_id]['assigned_classes']
        for ac in assigned_classes:
            if ac['class_id'] == class_id and not ac['completed']:
                ac['completed'] = True
                self.schedules[student_id]['completed_classes'].append(class_id)
                
                # Update student progress
                class_info = next(cls for cls in self.classes if cls['id'] == class_id)
                subject_id = class_info['subject_id']
                
                if subject_id not in self.students[student_id]['progress']:
                    self.students[student_id]['progress'][subject_id] = 0
                self.students[student_id]['progress'][subject_id] += 1
                
                return True
        return False
    
    def get_student_schedule(self, student_id: str) -> Optional[Dict]:
        """
        Get a student's schedule with details.
        
        Args:
            student_id: ID of the student
            
        Returns:
            Optional[Dict]: The student's schedule if exists, None otherwise
        """
        if student_id not in self.schedules:
            return None
            
        return self.schedules[student_id]
    
    def get_student_progress(self, student_id: str) -> Optional[Dict]:
        """
        Get a student's progress across subjects.
        
        Args:
            student_id: ID of the student
            
        Returns:
            Optional[Dict]: The student's progress if exists, None otherwise
        """
        if student_id not in self.students:
            return None
            
        return self.students[student_id]['progress']
    
    def save_to_file(self, filename: str) -> bool:
        """
        Save the entire system data to a JSON file.
        
        Args:
            filename: Path to the output file
            
        Returns:
            bool: True if save was successful, False otherwise
        """
        try:
            data = {
                'students': self.students,
                'subjects': self.subjects,
                'classes': self.classes,
                'schedules': self.schedules
            }
            with open(filename, 'w') as f:
                json.dump(data, f, indent=2)
            return True
        except Exception as e:
            print(f"Error saving to file: {e}")
            return False
    
    def load_from_file(self, filename: str) -> bool:
        """
        Load system data from a JSON file.
        
        Args:
            filename: Path to the input file
            
        Returns:
            bool: True if load was successful, False otherwise
        """
        try:
            with open(filename, 'r') as f:
                data = json.load(f)
                self.students = data.get('students', {})
                self.subjects = data.get('subjects', [])
                self.classes = data.get('classes', [])
                self.schedules = data.get('schedules', {})
            return True
        except Exception as e:
            print(f"Error loading from file: {e}")
            return False

# Example usage
if __name__ == "__main__":
    system = ScheduleSystem()
    
    # Add a student
    system.add_student("s001", "Juan Perez", "juan@example.com", ["UNAM", "IPN"])
    
    # Add subjects
    system.add_subject("math", "Mathematics", ["Algebra", "Calculus", "Geometry"])
    system.add_subject("physics", "Physics", ["Mechanics", "Thermodynamics", "Electromagnetism"])
    
    # Create classes
