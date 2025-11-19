"""
Generated Code Metadata:
========================
Original URL: https://cpncg.edu.mx
Prompt: Write a Python script to manage student contact information for a school like Colegio Panamericano e Instituto Libertadores, including fields for student name, grade, and contact numbers.
Generated: DETERMINISTIC_48cdb2a69851cd64
Batch ID: 20250622_205254
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
from typing import Dict, List, Optional

class StudentContactManager:
    """
    A class to manage student contact information for a school.
    Handles operations like adding, updating, deleting, and searching student records.
    """
    
    def __init__(self, data_file: str = "student_contacts.json"):
        """
        Initialize the StudentContactManager with a data file.
        
        Args:
            data_file (str): Path to the JSON file storing student data.
        """
        self.data_file = data_file
        self.students = self._load_data()
    
    def _load_data(self) -> Dict[str, Dict]:
        """
        Load student data from the JSON file.
        
        Returns:
            Dict: Dictionary containing student records.
        """
        try:
            if os.path.exists(self.data_file):
                with open(self.data_file, 'r') as file:
                    return json.load(file)
            return {}
        except (json.JSONDecodeError, IOError) as e:
            print(f"Error loading data: {e}")
            return {}
    
    def _save_data(self) -> None:
        """
        Save student data to the JSON file.
        """
        try:
            with open(self.data_file, 'w') as file:
                json.dump(self.students, file, indent=4)
        except IOError as e:
            print(f"Error saving data: {e}")
    
    def add_student(self, student_id: str, name: str, grade: str, phone: str, emergency_phone: Optional[str] = None) -> bool:
        """
        Add a new student record.
        
        Args:
            student_id (str): Unique identifier for the student.
            name (str): Full name of the student.
            grade (str): Current grade/class of the student.
            phone (str): Primary contact number.
            emergency_phone (str, optional): Emergency contact number.
            
        Returns:
            bool: True if successful, False otherwise.
        """
        if student_id in self.students:
            print(f"Student ID {student_id} already exists.")
            return False
        
        self.students[student_id] = {
            'name': name,
            'grade': grade,
            'phone': phone,
            'emergency_phone': emergency_phone
        }
        self._save_data()
        return True
    
    def update_student(self, student_id: str, **kwargs) -> bool:
        """
        Update an existing student record.
        
        Args:
            student_id (str): ID of the student to update.
            **kwargs: Fields to update (name, grade, phone, emergency_phone).
            
        Returns:
            bool: True if successful, False otherwise.
        """
        if student_id not in self.students:
            print(f"Student ID {student_id} not found.")
            return False
        
        valid_fields = {'name', 'grade', 'phone', 'emergency_phone'}
        for field, value in kwargs.items():
            if field in valid_fields:
                self.students[student_id][field] = value
        
        self._save_data()
        return True
    
    def delete_student(self, student_id: str) -> bool:
        """
        Delete a student record.
        
        Args:
            student_id (str): ID of the student to delete.
            
        Returns:
            bool: True if successful, False otherwise.
        """
        if student_id not in self.students:
            print(f"Student ID {student_id} not found.")
            return False
        
        del self.students[student_id]
        self._save_data()
        return True
    
    def get_student(self, student_id: str) -> Optional[Dict]:
        """
        Retrieve a student record by ID.
        
        Args:
            student_id (str): ID of the student to retrieve.
            
        Returns:
            Optional[Dict]: Student record if found, None otherwise.
        """
        return self.students.get(student_id)
    
    def search_students(self, **kwargs) -> List[Dict]:
        """
        Search for students based on provided criteria.
        
        Args:
            **kwargs: Fields to search by (name, grade, phone, emergency_phone).
            
        Returns:
            List[Dict]: List of matching student records.
        """
        results = []
        for student_id, student_data in self.students.items():
            match = True
            for field, value in kwargs.items():
                if student_data.get(field) != value:
                    match = False
                    break
            if match:
                results.append({'student_id': student_id, **student_data})
        return results
    
    def list_all_students(self) -> List[Dict]:
        """
        List all student records.
        
        Returns:
            List[Dict]: List of all student records.
        """
        return [{'student_id': sid, **data} for sid, data in self.students.items()]


def main():
    manager = StudentContactManager()
    
    while True:
        print("\nStudent Contact Management System")
        print("1. Add Student")
        print("2. Update Student")
        print("3. Delete Student")
        print("4. View Student")
        print("5. Search Students")
        print("6. List All Students")
        print("7. Exit")
        
        choice = input("Enter your choice (1-7): ")
        
        if choice == '1':
            student_id = input("Enter student ID: ")
            name = input("Enter student name: ")
            grade = input("Enter student grade: ")
            phone = input("Enter student phone: ")
            emergency_phone = input("Enter emergency phone (optional): ") or None
            if manager.add_student(student_id, name, grade, phone, emergency_phone):
                print("Student added successfully.")
        
        elif choice == '2':
            student_id = input("Enter student ID to update: ")
            print("Leave field blank to keep current value.")
            name = input(f"Enter new name: ")
            grade = input(f"Enter new grade: ")
            phone = input(f"Enter new phone: ")
            emergency_phone = input(f"Enter new emergency phone: ")
            
            update_data = {}
            if name: update_data['name'] = name
            if grade: update_data['grade'] = grade
            if phone: update_data['phone'] = phone
            if emergency_phone: update_data['emergency_phone'] = emergency_phone
            
            if manager.update_student(student_id, **update_data):
                print("Student updated successfully.")
        
        elif choice == '3':
            student_id = input("Enter student ID to delete: ")
            if manager.delete_student(student_id):
                print("Student deleted successfully.")
        
        elif choice == '4':
            student_id = input("Enter student ID to view: ")
            student = manager.get_student(student_id)
            if student:
                print("\nStudent Details:")
                print(f"ID: {student_id}")
                print(f"Name: {student['name']}")
                print(f"Grade: {student['grade']}")
                print(f"Phone: {student['phone']}")
                print(f"Emergency Phone: {student.get('emergency_phone', 'N/A')}")
            else:
                print("Student not found.")
        
        elif choice == '5':
            print("Enter search criteria (leave blank to skip):")
            name = input("Name: ") or None
            grade = input("Grade: ") or None
            phone = input("Phone: ") or None
            emergency_phone = input("Emergency Phone: ") or None
            
            search_criteria = {}
            if name: search_criteria['name'] = name
            if grade: search_criteria['grade'] = grade
            if phone: search_criteria['phone'] = phone
            if emergency_phone: search_criteria['emergency_phone'] = emergency_phone
            
            results = manager.search_students(**search_criteria)
            if results:
                print("\nSearch Results:")
                for student in results:
                    print(f"\nID: {student['student_id']}")
                    print(f"Name: {student['name']}")
                    print(f"Grade: {student['grade']}")
                    print(f"Phone: {student['phone']}")
                    print(f"Emergency Phone: {student.get('emergency_phone', 'N/A')}")
            else:
                print("No matching students found.")
        
        elif choice == '6':
            students = manager.list_all_students()
            if students:
                print("\nAll Students:")
                for student in students:
                    print(f"\nID: {student['student_id']}")
                    print(f"Name: {student['name']}")
                    print(f"Grade: {student['grade']}")
                    print(f"Phone: {student['phone']}")
                    print(f"Emergency Phone: {student.get('emergency_phone', 'N/A')}")
            else:
                print("No students in the system.")
        
        elif choice == '7':
            print("Exiting the system.")
            break
        
        else:
            print("Invalid choice. Please enter a number between 1 and 7.")


if __name__ == "__main__":
    main()
```
