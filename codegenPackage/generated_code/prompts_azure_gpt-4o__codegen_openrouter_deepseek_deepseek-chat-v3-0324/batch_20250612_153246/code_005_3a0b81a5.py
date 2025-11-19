"""
Generated Code Metadata:
========================
Original URL: https://aulaferretera.com
Prompt: Write code to design a training module for hardware store employees, including topics like customer service and sales strategies, based on the "Entrenamiento al equipo de trabajo" service offered by Aula Ferretera.
Generated: DETERMINISTIC_3a0b81a5bd4e4850
Batch ID: 20250612_153246
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
from enum import Enum
from typing import List, Dict, Optional

class TrainingTopic(Enum):
    CUSTOMER_SERVICE = "Customer Service"
    SALES_STRATEGIES = "Sales Strategies"
    PRODUCT_KNOWLEDGE = "Product Knowledge"
    SAFETY_PROTOCOLS = "Safety Protocols"
    INVENTORY_MANAGEMENT = "Inventory Management"

class TrainingModule:
    """Represents a training module for hardware store employees."""
    
    def __init__(self, title: str, description: str, duration_minutes: int, topics: List[TrainingTopic]):
        self.title = title
        self.description = description
        self.duration_minutes = duration_minutes
        self.topics = topics
        self.created_at = datetime.now()
        self.completed = False
    
    def mark_as_completed(self) -> None:
        """Mark the training module as completed."""
        self.completed = True
    
    def to_dict(self) -> Dict:
        """Convert the training module to a dictionary for serialization."""
        return {
            "title": self.title,
            "description": self.description,
            "duration_minutes": self.duration_minutes,
            "topics": [topic.value for topic in self.topics],
            "created_at": self.created_at.isoformat(),
            "completed": self.completed
        }

class Employee:
    """Represents a hardware store employee."""
    
    def __init__(self, employee_id: str, name: str, position: str):
        self.employee_id = employee_id
        self.name = name
        self.position = position
        self.completed_trainings: List[TrainingModule] = []
    
    def complete_training(self, training: TrainingModule) -> None:
        """Mark a training as completed for this employee."""
        training.mark_as_completed()
        self.completed_trainings.append(training)
    
    def get_completed_trainings(self) -> List[Dict]:
        """Get a list of completed trainings as dictionaries."""
        return [training.to_dict() for training in self.completed_trainings]

class TrainingProgram:
    """Manages the training program for hardware store employees."""
    
    def __init__(self):
        self.modules: List[TrainingModule] = []
        self.employees: List[Employee] = []
    
    def add_module(self, module: TrainingModule) -> None:
        """Add a training module to the program."""
        self.modules.append(module)
    
    def register_employee(self, employee: Employee) -> None:
        """Register an employee to the training program."""
        self.employees.append(employee)
    
    def find_module_by_topic(self, topic: TrainingTopic) -> Optional[TrainingModule]:
        """Find a training module by topic."""
        for module in self.modules:
            if topic in module.topics:
                return module
        return None
    
    def save_to_file(self, filename: str) -> None:
        """Save the training program data to a JSON file."""
        data = {
            "modules": [module.to_dict() for module in self.modules],
            "employees": [
                {
                    "employee_id": emp.employee_id,
                    "name": emp.name,
                    "position": emp.position,
                    "completed_trainings": emp.get_completed_trainings()
                }
                for emp in self.employees
            ]
        }
        try:
            with open(filename, 'w') as f:
                json.dump(data, f, indent=4)
        except IOError as e:
            print(f"Error saving to file: {e}")
    
    @classmethod
    def load_from_file(cls, filename: str) -> 'TrainingProgram':
        """Load the training program data from a JSON file."""
        program = cls()
        try:
            with open(filename, 'r') as f:
                data = json.load(f)
                
                for module_data in data.get("modules", []):
                    module = TrainingModule(
                        title=module_data["title"],
                        description=module_data["description"],
                        duration_minutes=module_data["duration_minutes"],
                        topics=[TrainingTopic(topic) for topic in module_data["topics"]]
                    )
                    module.completed = module_data["completed"]
                    module.created_at = datetime.fromisoformat(module_data["created_at"])
                    program.modules.append(module)
                
                for emp_data in data.get("employees", []):
                    employee = Employee(
                        employee_id=emp_data["employee_id"],
                        name=emp_data["name"],
                        position=emp_data["position"]
                    )
                    for training_data in emp_data["completed_trainings"]:
                        training = TrainingModule(
                            title=training_data["title"],
                            description=training_data["description"],
                            duration_minutes=training_data["duration_minutes"],
                            topics=[TrainingTopic(topic) for topic in training_data["topics"]]
                        )
                        training.completed = training_data["completed"]
                        training.created_at = datetime.fromisoformat(training_data["created_at"])
                        employee.completed_trainings.append(training)
                    program.employees.append(employee)
        except (IOError, json.JSONDecodeError, KeyError) as e:
            print(f"Error loading from file: {e}")
        return program

# Example usage
if __name__ == "__main__":
    # Create training modules
    customer_service_module = TrainingModule(
        title="Excellent Customer Service",
        description="Learn how to provide top-notch customer service in a hardware store environment",
        duration_minutes=60,
        topics=[TrainingTopic.CUSTOMER_SERVICE, TrainingTopic.SALES_STRATEGIES]
    )
    
    sales_strategies_module = TrainingModule(
        title="Effective Sales Strategies",
        description="Master sales techniques specific to hardware products",
        duration_minutes=90,
        topics=[TrainingTopic.SALES_STRATEGIES, TrainingTopic.PRODUCT_KNOWLEDGE]
    )
    
    # Create employees
    employee1 = Employee("E001", "John Doe", "Sales Associate")
    employee2 = Employee("E002", "Jane Smith", "Store Manager")
    
    # Set up training program
    program = TrainingProgram()
    program.add_module(customer_service_module)
    program.add_module(sales_strategies_module)
    program.register_employee(employee1)
    program.register_employee(employee2)
    
    # Employees complete trainings
    employee1.complete_training(customer_service_module)
    employee2.complete_training(sales_strategies_module)
    
    # Save and load data
    program.save_to_file("training_program.json")
    loaded_program = TrainingProgram.load_from_file("training_program.json")
```
