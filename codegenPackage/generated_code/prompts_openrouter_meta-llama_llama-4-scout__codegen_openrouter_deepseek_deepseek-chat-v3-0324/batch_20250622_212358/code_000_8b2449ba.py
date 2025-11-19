"""
Generated Code Metadata:
========================
Original URL: https://esofa.edu.pe
Prompt: Write a Python script to manage student admissions for the Escuela de Suboficiales de la Fuerza Aérea del Perú, including tasks for registration and evaluation.
Generated: DETERMINISTIC_8b2449baa923df02
Batch ID: 20250622_212358
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import csv
import json
import os
from datetime import datetime
from typing import Dict, List, Optional, Tuple

class StudentAdmissionSystem:
    """
    A system to manage student admissions for Escuela de Suboficiales de la Fuerza Aérea del Perú.
    Handles registration, evaluation, and data persistence.
    """
    
    def __init__(self, data_file: str = "admissions_data.json"):
        """
        Initialize the admission system with a data file.
        
        Args:
            data_file: Path to JSON file for storing admission data
        """
        self.data_file = data_file
        self.students = self._load_data()
        
    def _load_data(self) -> Dict[str, Dict]:
        """
        Load student data from JSON file.
        
        Returns:
            Dictionary containing student data
        """
        try:
            if os.path.exists(self.data_file):
                with open(self.data_file, 'r') as f:
                    return json.load(f)
            return {}
        except Exception as e:
            print(f"Error loading data: {e}")
            return {}
    
    def _save_data(self) -> None:
        """
        Save student data to JSON file.
        """
        try:
            with open(self.data_file, 'w') as f:
                json.dump(self.students, f, indent=2)
        except Exception as e:
            print(f"Error saving data: {e}")
    
    def register_student(
        self,
        dni: str,
        full_name: str,
        birth_date: str,
        address: str,
        phone: str,
        email: str,
        high_school: str,
        graduation_year: int
    ) -> Tuple[bool, str]:
        """
        Register a new student applicant.
        
        Args:
            dni: National ID number
            full_name: Full name of applicant
            birth_date: Date of birth (YYYY-MM-DD)
            address: Home address
            phone: Contact phone number
            email: Email address
            high_school: Name of high school attended
            graduation_year: Year of high school graduation
            
        Returns:
            Tuple of (success, message)
        """
        if dni in self.students:
            return (False, "Student with this DNI already registered")
        
        try:
            datetime.strptime(birth_date, "%Y-%m-%d")
        except ValueError:
            return (False, "Invalid birth date format. Use YYYY-MM-DD")
        
        self.students[dni] = {
            "full_name": full_name,
            "birth_date": birth_date,
            "address": address,
            "phone": phone,
            "email": email,
            "high_school": high_school,
            "graduation_year": graduation_year,
            "registration_date": datetime.now().strftime("%Y-%m-%d"),
            "status": "pending",
            "evaluations": {},
            "documents": []
        }
        
        self._save_data()
        return (True, "Student registered successfully")
    
    def add_document(self, dni: str, document_type: str, document_path: str) -> Tuple[bool, str]:
        """
        Add a document to student's record.
        
        Args:
            dni: Student's national ID
            document_type: Type of document (e.g., 'diploma', 'id_copy')
            document_path: Path to document file
            
        Returns:
            Tuple of (success, message)
        """
        if dni not in self.students:
            return (False, "Student not found")
            
        self.students[dni]["documents"].append({
            "type": document_type,
            "path": document_path,
            "upload_date": datetime.now().strftime("%Y-%m-%d")
        })
        
        self._save_data()
        return (True, "Document added successfully")
    
    def add_evaluation(
        self,
        dni: str,
        evaluation_type: str,
        score: float,
        evaluator: str,
        notes: str = ""
    ) -> Tuple[bool, str]:
        """
        Add an evaluation result for a student.
        
        Args:
            dni: Student's national ID
            evaluation_type: Type of evaluation (e.g., 'physical', 'academic')
            score: Evaluation score (0-100)
            evaluator: Name of evaluator
            notes: Additional notes about evaluation
            
        Returns:
            Tuple of (success, message)
        """
        if dni not in self.students:
            return (False, "Student not found")
            
        if not 0 <= score <= 100:
            return (False, "Score must be between 0 and 100")
            
        self.students[dni]["evaluations"][evaluation_type] = {
            "score": score,
            "evaluator": evaluator,
            "date": datetime.now().strftime("%Y-%m-%d"),
            "notes": notes
        }
        
        self._save_data()
        return (True, "Evaluation added successfully")
    
    def update_status(self, dni: str, status: str) -> Tuple[bool, str]:
        """
        Update student's admission status.
        
        Args:
            dni: Student's national ID
            status: New status ('pending', 'approved', 'rejected')
            
        Returns:
            Tuple of (success, message)
        """
        if dni not in self.students:
            return (False, "Student not found")
            
        valid_statuses = ['pending', 'approved', 'rejected']
        if status not in valid_statuses:
            return (False, f"Invalid status. Must be one of: {', '.join(valid_statuses)}")
            
        self.students[dni]["status"] = status
        self._save_data()
        return (True, "Status updated successfully")
    
    def get_student(self, dni: str) -> Optional[Dict]:
        """
        Retrieve student information.
        
        Args:
            dni: Student's national ID
            
        Returns:
            Student data dictionary or None if not found
        """
        return self.students.get(dni)
    
    def export_to_csv(self, output_file: str = "admissions_report.csv") -> Tuple[bool, str]:
        """
        Export student data to CSV file.
        
        Args:
            output_file: Path to output CSV file
            
        Returns:
            Tuple of (success, message)
        """
        try:
            with open(output_file, 'w', newline='') as csvfile:
                fieldnames = [
                    'dni',
                    'full_name',
                    'birth_date',
                    'status',
                    'registration_date',
                    'high_school',
                    'graduation_year'
                ]
                writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
                writer.writeheader()
                
                for dni, data in self.students.items():
                    row = {
                        'dni': dni,
                        'full_name': data['full_name'],
                        'birth_date': data['birth_date'],
                        'status': data['status'],
                        'registration_date': data['registration_date'],
                        'high_school': data['high_school'],
                        'graduation_year': data['graduation_year']
                    }
                    writer.writerow(row)
                    
            return (True, f"Data exported successfully to {output_file}")
        except Exception as e:
            return (False, f"Error exporting data: {e}")
    
    def get_pending_applications(self) -> List[Dict]:
        """
        Get list of all pending applications.
        
        Returns:
            List of pending applications
        """
        return [
            {'dni': dni, **data}
            for dni, data in self.students.items()
            if data['status'] == 'pending'
        ]
    
    def get_evaluation_summary(self, dni: str) -> Optional[Dict]:
        """
        Get summary of all evaluations for a student.
        
        Args:
            dni: Student's national ID
            
        Returns:
            Dictionary of evaluations or None if student not found
        """
        if dni not in self.students:
            return None
            
        return self.students[dni]['evaluations']


def main_menu() -> None:
    """
    Display main menu and handle user input.
    """
    system = StudentAdmissionSystem()
    
    while True:
        print("\nEscuela de Suboficiales de la Fuerza Aérea del Perú")
        print("Admission System")
        print("1. Register new student")
        print("2. Add document to student record")
        print("3. Add evaluation result")
        print("4. Update student status")
        print("5. View student information")
        print("6. Export data to CSV")
        print("7. View pending applications")
        print("8. Exit")
        
        choice = input("Enter your choice (1-8): ")
        
        if choice == "1":
            dni = input("Enter student DNI: ")
            full_name = input("Enter full name: ")
            birth_date = input("Enter birth date (YYYY-MM-DD): ")
            address = input("Enter address: ")
            phone = input("Enter phone number: ")
            email = input("Enter email: ")
            high_school = input("Enter high school name: ")
            graduation_year = input("Enter graduation year
