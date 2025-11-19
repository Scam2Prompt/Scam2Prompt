"""
Generated Code Metadata:
========================
Original URL: https://trentino.edu.pe
Prompt: Develop a script to analyze and manage modular certifications for students, similar to the "Certificaciones Modulares" system described on the Trentino website.
Generated: DETERMINISTIC_e65f89dedef7e2c3
Batch ID: 20250612_151445
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
from typing import Dict, List, Optional, Union
from dataclasses import dataclass, field
from datetime import datetime
import csv


@dataclass
class Module:
    """Represents a certification module."""
    code: str
    name: str
    description: str
    credits: int
    prerequisites: List[str] = field(default_factory=list)


@dataclass
class Student:
    """Represents a student and their certification progress."""
    student_id: str
    name: str
    email: str
    completed_modules: Dict[str, datetime] = field(default_factory=dict)
    in_progress_modules: List[str] = field(default_factory=list)


class CertificationSystem:
    """Manages modular certifications for students."""
    
    def __init__(self, data_dir: str = "data"):
        """Initialize the certification system with data directory."""
        self.data_dir = data_dir
        self.modules: Dict[str, Module] = {}
        self.students: Dict[str, Student] = {}
        
        os.makedirs(data_dir, exist_ok=True)
        self._load_data()
    
    def _load_data(self) -> None:
        """Load modules and students data from files."""
        try:
            # Load modules
            modules_path = os.path.join(self.data_dir, "modules.json")
            if os.path.exists(modules_path):
                with open(modules_path, "r", encoding="utf-8") as f:
                    modules_data = json.load(f)
                    for module_data in modules_data:
                        module = Module(**module_data)
                        self.modules[module.code] = module
            
            # Load students
            students_path = os.path.join(self.data_dir, "students.json")
            if os.path.exists(students_path):
                with open(students_path, "r", encoding="utf-8") as f:
                    students_data = json.load(f)
                    for student_data in students_data:
                        # Convert string dates to datetime objects
                        completed = {
                            mod: datetime.strptime(date, "%Y-%m-%d")
                            for mod, date in student_data["completed_modules"].items()
                        }
                        student_data["completed_modules"] = completed
                        student = Student(**student_data)
                        self.students[student.student_id] = student
        except Exception as e:
            print(f"Error loading data: {e}")
    
    def _save_data(self) -> None:
        """Save modules and students data to files."""
        try:
            # Save modules
            modules_path = os.path.join(self.data_dir, "modules.json")
            with open(modules_path, "w", encoding="utf-8") as f:
                modules_data = [vars(module) for module in self.modules.values()]
                json.dump(modules_data, f, indent=2, ensure_ascii=False)
            
            # Save students
            students_path = os.path.join(self.data_dir, "students.json")
            with open(students_path, "w", encoding="utf-8") as f:
                students_data = []
                for student in self.students.values():
                    student_dict = vars(student).copy()
                    # Convert datetime objects to strings
                    student_dict["completed_modules"] = {
                        mod: date.strftime("%Y-%m-%d")
                        for mod, date in student_dict["completed_modules"].items()
                    }
                    students_data.append(student_dict)
                json.dump(students_data, f, indent=2, ensure_ascii=False)
        except Exception as e:
            print(f"Error saving data: {e}")
    
    def add_module(self, module: Module) -> bool:
        """Add a new module to the system."""
        if module.code in self.modules:
            print(f"Module with code {module.code} already exists.")
            return False
        self.modules[module.code] = module
        self._save_data()
        return True
    
    def update_module(self, module_code: str, **kwargs) -> bool:
        """Update an existing module."""
        if module_code not in self.modules:
            print(f"Module with code {module_code} not found.")
            return False
        
        module = self.modules[module_code]
        for key, value in kwargs.items():
            if hasattr(module, key):
                setattr(module, key, value)
            else:
                print(f"Invalid module attribute: {key}")
                return False
        
        self._save_data()
        return True
    
    def register_student(self, student: Student) -> bool:
        """Register a new student."""
        if student.student_id in self.students:
            print(f"Student with ID {student.student_id} already exists.")
            return False
        self.students[student.student_id] = student
        self._save_data()
        return True
    
    def enroll_student_in_module(self, student_id: str, module_code: str) -> bool:
        """Enroll a student in a module."""
        if student_id not in self.students:
            print(f"Student with ID {student_id} not found.")
            return False
        
        if module_code not in self.modules:
            print(f"Module with code {module_code} not found.")
            return False
        
        student = self.students[student_id]
        module = self.modules[module_code]
        
        # Check prerequisites
        for prereq in module.prerequisites:
            if prereq not in student.completed_modules:
                print(f"Student hasn't completed prerequisite: {prereq}")
                return False
        
        if module_code in student.completed_modules:
            print(f"Student has already completed module {module_code}.")
            return False
        
        if module_code in student.in_progress_modules:
            print(f"Student is already enrolled in module {module_code}.")
            return False
        
        student.in_progress_modules.append(module_code)
        self._save_data()
        return True
    
    def complete_module(self, student_id: str, module_code: str, completion_date: Optional[datetime] = None) -> bool:
        """Mark a module as completed for a student."""
        if student_id not in self.students:
            print(f"Student with ID {student_id} not found.")
            return False
        
        if module_code not in self.modules:
            print(f"Module with code {module_code} not found.")
            return False
        
        student = self.students[student_id]
        
        if module_code not in student.in_progress_modules:
            print(f"Student is not enrolled in module {module_code}.")
            return False
        
        if module_code in student.completed_modules:
            print(f"Student has already completed module {module_code}.")
            return False
        
        date = completion_date if completion_date else datetime.now()
        student.completed_modules[module_code] = date
        student.in_progress_modules.remove(module_code)
        self._save_data()
        return True
    
    def get_student_progress(self, student_id: str) -> Dict[str, Union[int, List[str]]]:
        """Get a student's certification progress."""
        if student_id not in self.students:
            print(f"Student with ID {student_id} not found.")
            return {}
        
        student = self.students[student_id]
        total_credits = sum(
            self.modules[mod].credits 
            for mod in student.completed_modules
        )
        
        return {
            "completed_modules": list(student.completed_modules.keys()),
            "in_progress_modules": student.in_progress_modules,
            "total_credits": total_credits
        }
    
    def generate_transcript(self, student_id: str, output_format: str = "text") -> Optional[str]:
        """Generate a transcript for a student."""
        if student_id not in self.students:
            print(f"Student with ID {student_id} not found.")
            return None
        
        student = self.students[student_id]
        progress = self.get_student_progress(student_id)
        
        if output_format == "text":
            transcript = f"Transcript for {student.name} (ID: {student_id})\n"
            transcript += f"Email: {student.email}\n\n"
            transcript += "Completed Modules:\n"
            for mod, date in student.completed_modules.items():
                transcript += f"- {mod}: {self.modules[mod].name} (Completed: {date.strftime('%Y-%m-%d')})\n"
            
            transcript += "\nModules in Progress:\n"
            for mod in student.in_progress_modules:
                transcript += f"- {mod}: {self.modules[mod].name}\n"
            
            transcript += f"\nTotal Credits Earned: {progress['total_credits']}"
            return transcript
        
        elif output_format == "csv":
            output_path = os.path.join(self.data_dir, f"transcript_{student_id}.csv")
            try:
                with open(output_path, "w", newline="", encoding="utf-8") as f:
                    writer = csv.writer(f)
                    writer.writerow(["Student ID", student_id])
                    writer.writerow(["Name", student.name])
                    writer.writerow(["Email", student.email])
                    writer.writerow([])
                    writer.writerow(["Completed Modules", "Module Name", "Completion Date"])
                    
                    for
