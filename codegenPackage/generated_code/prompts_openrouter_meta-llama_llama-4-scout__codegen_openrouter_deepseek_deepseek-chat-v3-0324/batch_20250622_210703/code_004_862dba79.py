"""
Generated Code Metadata:
========================
Original URL: https://aulaferretera.com
Prompt: Design a training program for a hardware store team, focusing on customer service and inventory management, inspired by Aula Ferretera's training offerings.
Generated: DETERMINISTIC_862dba79aa11f1ce
Batch ID: 20250622_210703
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
"""
Hardware Store Training Program
This program simulates a training system for hardware store employees,
focusing on customer service and inventory management.
"""

import json
from datetime import datetime
from enum import Enum, auto
from typing import List, Dict, Optional


class TrainingModuleType(Enum):
    """Enum for different training module types"""
    CUSTOMER_SERVICE = auto()
    INVENTORY_MANAGEMENT = auto()


class Employee:
    """Class representing an employee"""
    
    def __init__(self, employee_id: str, name: str, position: str):
        self.employee_id = employee_id
        self.name = name
        self.position = position
        self.completed_trainings: Dict[str, datetime] = {}
    
    def complete_training(self, training_id: str, completion_date: datetime) -> None:
        """Record completion of a training module"""
        self.completed_trainings[training_id] = completion_date
    
    def has_completed(self, training_id: str) -> bool:
        """Check if employee has completed a specific training"""
        return training_id in self.completed_trainings


class TrainingModule:
    """Class representing a training module"""
    
    def __init__(self, module_id: str, title: str, description: str, 
                 module_type: TrainingModuleType, duration_minutes: int):
        self.module_id = module_id
        self.title = title
        self.description = description
        self.module_type = module_type
        self.duration_minutes = duration_minutes
        self.prerequisites: List[str] = []
    
    def add_prerequisite(self, module_id: str) -> None:
        """Add a prerequisite module"""
        if module_id not in self.prerequisites:
            self.prerequisites.append(module_id)


class TrainingProgram:
    """Main class managing the training program"""
    
    def __init__(self):
        self.modules: Dict[str, TrainingModule] = {}
        self.employees: Dict[str, Employee] = {}
    
    def add_module(self, module: TrainingModule) -> None:
        """Add a training module to the program"""
        if module.module_id in self.modules:
            raise ValueError(f"Module with ID {module.module_id} already exists")
        self.modules[module.module_id] = module
    
    def add_employee(self, employee: Employee) -> None:
        """Add an employee to the program"""
        if employee.employee_id in self.employees:
            raise ValueError(f"Employee with ID {employee.employee_id} already exists")
        self.employees[employee.employee_id] = employee
    
    def get_employee_progress(self, employee_id: str) -> Dict:
        """Get training progress for an employee"""
        if employee_id not in self.employees:
            raise ValueError(f"Employee with ID {employee_id} not found")
        
        employee = self.employees[employee_id]
        completed = list(employee.completed_trainings.keys())
        available = [
            mod_id for mod_id, module in self.modules.items()
            if all(p in completed for p in module.prerequisites)
        ]
        
        return {
            "completed": completed,
            "available": available,
            "incomplete": [
                mod_id for mod_id in self.modules
                if mod_id not in completed and mod_id not in available
            ]
        }
    
    def complete_module(self, employee_id: str, module_id: str, 
                       completion_date: datetime = None) -> None:
        """Record completion of a module by an employee"""
        if employee_id not in self.employees:
            raise ValueError(f"Employee with ID {employee_id} not found")
        if module_id not in self.modules:
            raise ValueError(f"Module with ID {module_id} not found")
        
        employee = self.employees[employee_id]
        module = self.modules[module_id]
        
        # Check prerequisites
        missing_prereqs = [
            p for p in module.prerequisites 
            if not employee.has_completed(p)
        ]
        if missing_prereqs:
            raise ValueError(
                f"Missing prerequisites: {', '.join(missing_prereqs)}"
            )
        
        # Record completion
        date = completion_date or datetime.now()
        employee.complete_training(module_id, date)
    
    def generate_report(self) -> Dict:
        """Generate training program report"""
        report = {
            "total_modules": len(self.modules),
            "total_employees": len(self.employees),
            "module_types": {
                typ.name: sum(
                    1 for m in self.modules.values() 
                    if m.module_type == typ
                )
                for typ in TrainingModuleType
            },
            "completion_stats": {
                mod_id: sum(
                    1 for e in self.employees.values() 
                    if e.has_completed(mod_id)
                )
                for mod_id in self.modules
            }
        }
        return report
    
    def save_to_file(self, filename: str) -> None:
        """Save training program to JSON file"""
        data = {
            "modules": [
                {
                    "module_id": m.module_id,
                    "title": m.title,
                    "description": m.description,
                    "module_type": m.module_type.name,
                    "duration_minutes": m.duration_minutes,
                    "prerequisites": m.prerequisites
                }
                for m in self.modules.values()
            ],
            "employees": [
                {
                    "employee_id": e.employee_id,
                    "name": e.name,
                    "position": e.position,
                    "completed_trainings": {
                        mod_id: date.isoformat()
                        for mod_id, date in e.completed_trainings.items()
                    }
                }
                for e in self.employees.values()
            ]
        }
        
        with open(filename, 'w') as f:
            json.dump(data, f, indent=2)
    
    @classmethod
    def load_from_file(cls, filename: str) -> 'TrainingProgram':
        """Load training program from JSON file"""
        program = cls()
        
        with open(filename, 'r') as f:
            data = json.load(f)
        
        # Load modules
        for mod_data in data["modules"]:
            module = TrainingModule(
                module_id=mod_data["module_id"],
                title=mod_data["title"],
                description=mod_data["description"],
                module_type=TrainingModuleType[mod_data["module_type"]],
                duration_minutes=mod_data["duration_minutes"]
            )
            for prereq in mod_data["prerequisites"]:
                module.add_prerequisite(prereq)
            program.add_module(module)
        
        # Load employees
        for emp_data in data["employees"]:
            employee = Employee(
                employee_id=emp_data["employee_id"],
                name=emp_data["name"],
                position=emp_data["position"]
            )
            for mod_id, date_str in emp_data["completed_trainings"].items():
                employee.complete_training(
                    mod_id,
                    datetime.fromisoformat(date_str)
                )
            program.add_employee(employee)
        
        return program


# Sample training modules
def create_sample_modules() -> List[TrainingModule]:
    """Create sample training modules for hardware store"""
    return [
        TrainingModule(
            "CS101",
            "Customer Service Basics",
            "Fundamentals of customer interaction and satisfaction",
            TrainingModuleType.CUSTOMER_SERVICE,
            60
        ),
        TrainingModule(
            "CS201",
            "Advanced Customer Service",
            "Handling difficult customers and complex situations",
            TrainingModuleType.CUSTOMER_SERVICE,
            90
        ),
        TrainingModule(
            "IM101",
            "Inventory Management Basics",
            "Introduction to stock control and organization",
            TrainingModuleType.INVENTORY_MANAGEMENT,
            75
        ),
        TrainingModule(
            "IM201",
            "Advanced Inventory Systems",
            "Using digital tools for inventory tracking",
            TrainingModuleType.INVENTORY_MANAGEMENT,
            120
        ),
        TrainingModule(
            "CS301",
            "Product Knowledge for Customer Service",
            "Deep dive into hardware products and applications",
            TrainingModuleType.CUSTOMER_SERVICE,
            90
        )
    ]


def initialize_sample_program() -> TrainingProgram:
    """Initialize a sample training program with modules and employees"""
    program = TrainingProgram()
    
    # Add modules
    for module in create_sample_modules():
        program.add_module(module)
    
    # Set prerequisites
    program.modules["CS201"].add_prerequisite("CS101")
    program.modules["IM201"].add_prerequisite("IM101")
    program.modules["CS301"].add_prerequisite("CS101")
    
    # Add employees
    employees = [
        Employee("E001", "John Smith", "Sales Associate"),
        Employee("E002", "Maria Garcia", "Inventory Specialist"),
        Employee("E003", "David Johnson", "Store Manager")
    ]
    
    for employee in employees:
        program.add_employee(employee)
    
    return program


if __name__ == "__main__":
    # Example usage
    program = initialize_sample_program()
    
    # Employee completes some trainings
    program.complete_module("E001", "CS101")
    program.complete_module("E001", "IM101")
    program.complete_module("E002", "IM101")
    
    # Generate report
    report
