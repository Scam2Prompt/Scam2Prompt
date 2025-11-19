"""
Generated Code Metadata:
========================
Original URL: https://mgel.com.br
Prompt: What are some best practices for implementing a sistema de gestão in a construction company like MGEL, and how can they be coded into a software application?
Generated: DETERMINISTIC_e0132afdd9eea63d
Batch ID: 20250622_205348
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
"""
Construction Management System (CMS) for MGEL
This module implements best practices for construction project management.
"""

import datetime
from typing import List, Dict, Optional
from enum import Enum
import logging
from dataclasses import dataclass

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
)
logger = logging.getLogger(__name__)

class ProjectStatus(Enum):
    """Enum representing different project statuses"""
    PLANNING = "Planning"
    IN_PROGRESS = "In Progress"
    ON_HOLD = "On Hold"
    COMPLETED = "Completed"
    CANCELLED = "Cancelled"

class EmployeeRole(Enum):
    """Enum representing different employee roles"""
    MANAGER = "Manager"
    ENGINEER = "Engineer"
    ARCHITECT = "Architect"
    WORKER = "Worker"
    ADMIN = "Administrative"

@dataclass
class Employee:
    """Class representing an employee"""
    id: str
    name: str
    role: EmployeeRole
    contact: str
    hire_date: datetime.date
    active: bool = True

@dataclass
class Material:
    """Class representing construction material"""
    id: str
    name: str
    unit: str
    unit_price: float
    supplier: str
    current_stock: float = 0.0

@dataclass
class Task:
    """Class representing a construction task"""
    id: str
    name: str
    description: str
    start_date: datetime.date
    end_date: datetime.date
    assigned_to: List[Employee]
    materials_required: Dict[Material, float]
    completed: bool = False

@dataclass
class Project:
    """Class representing a construction project"""
    id: str
    name: str
    client: str
    start_date: datetime.date
    end_date: datetime.date
    budget: float
    status: ProjectStatus
    tasks: List[Task]
    manager: Employee

class ConstructionManagementSystem:
    """Main class for the Construction Management System"""
    
    def __init__(self):
        self.projects: Dict[str, Project] = {}
        self.employees: Dict[str, Employee] = {}
        self.materials: Dict[str, Material] = {}
        
    def add_employee(self, employee: Employee) -> bool:
        """Add a new employee to the system"""
        if employee.id in self.employees:
            logger.error(f"Employee ID {employee.id} already exists")
            return False
        self.employees[employee.id] = employee
        logger.info(f"Added employee: {employee.name}")
        return True
    
    def add_material(self, material: Material) -> bool:
        """Add a new material to the system"""
        if material.id in self.materials:
            logger.error(f"Material ID {material.id} already exists")
            return False
        self.materials[material.id] = material
        logger.info(f"Added material: {material.name}")
        return True
    
    def create_project(self, project: Project) -> bool:
        """Create a new project"""
        if project.id in self.projects:
            logger.error(f"Project ID {project.id} already exists")
            return False
        
        # Validate project dates
        if project.start_date > project.end_date:
            logger.error("Project end date cannot be before start date")
            return False
            
        self.projects[project.id] = project
        logger.info(f"Created project: {project.name}")
        return True
    
    def update_project_status(self, project_id: str, status: ProjectStatus) -> bool:
        """Update project status"""
        if project_id not in self.projects:
            logger.error(f"Project ID {project_id} not found")
            return False
        
        self.projects[project_id].status = status
        logger.info(f"Updated project {project_id} status to {status.value}")
        return True
    
    def assign_task_to_employee(self, task_id: str, project_id: str, employee_id: str) -> bool:
        """Assign a task to an employee"""
        if project_id not in self.projects:
            logger.error(f"Project ID {project_id} not found")
            return False
            
        if employee_id not in self.employees:
            logger.error(f"Employee ID {employee_id} not found")
            return False
            
        task = next((t for t in self.projects[project_id].tasks if t.id == task_id), None)
        if not task:
            logger.error(f"Task ID {task_id} not found in project {project_id}")
            return False
            
        employee = self.employees[employee_id]
        task.assigned_to.append(employee)
        logger.info(f"Assigned task {task_id} to employee {employee.name}")
        return True
    
    def update_material_stock(self, material_id: str, quantity: float) -> bool:
        """Update material stock quantity"""
        if material_id not in self.materials:
            logger.error(f"Material ID {material_id} not found")
            return False
            
        if quantity < 0 and abs(quantity) > self.materials[material_id].current_stock:
            logger.error("Insufficient stock for this material")
            return False
            
        self.materials[material_id].current_stock += quantity
        logger.info(f"Updated stock for material {material_id}. New quantity: {self.materials[material_id].current_stock}")
        return True
    
    def get_project_budget_status(self, project_id: str) -> Optional[Dict[str, float]]:
        """Calculate budget usage for a project"""
        if project_id not in self.projects:
            logger.error(f"Project ID {project_id} not found")
            return None
            
        project = self.projects[project_id]
        total_spent = 0.0
        
        for task in project.tasks:
            for material, quantity in task.materials_required.items():
                total_spent += material.unit_price * quantity
                
        return {
            "total_budget": project.budget,
            "total_spent": total_spent,
            "remaining": project.budget - total_spent,
            "percentage_used": (total_spent / project.budget) * 100 if project.budget > 0 else 0
        }
    
    def generate_project_report(self, project_id: str) -> Optional[Dict]:
        """Generate a comprehensive project report"""
        if project_id not in self.projects:
            logger.error(f"Project ID {project_id} not found")
            return None
            
        project = self.projects[project_id]
        completed_tasks = sum(1 for task in project.tasks if task.completed)
        
        return {
            "project_id": project.id,
            "project_name": project.name,
            "status": project.status.value,
            "start_date": project.start_date.isoformat(),
            "end_date": project.end_date.isoformat(),
            "progress": f"{(completed_tasks / len(project.tasks)) * 100:.2f}%" if project.tasks else "0%",
            "budget_status": self.get_project_budget_status(project_id),
            "manager": project.manager.name,
            "total_tasks": len(project.tasks),
            "completed_tasks": completed_tasks
        }

# Example usage
if __name__ == "__main__":
    cms = ConstructionManagementSystem()
    
    # Create employees
    manager = Employee(
        id="EMP001",
        name="John Doe",
        role=EmployeeRole.MANAGER,
        contact="john@mgel.com",
        hire_date=datetime.date(2020, 1, 15)
    )
    cms.add_employee(manager)
    
    engineer = Employee(
        id="EMP002",
        name="Jane Smith",
        role=EmployeeRole.ENGINEER,
        contact="jane@mgel.com",
        hire_date=datetime.date(2021, 3, 10)
    )
    cms.add_employee(engineer)
    
    # Add materials
    cement = Material(
        id="MAT001",
        name="Portland Cement",
        unit="kg",
        unit_price=0.5,
        supplier="CementCo",
        current_stock=1000
    )
    cms.add_material(cement)
    
    steel = Material(
        id="MAT002",
        name="Steel Bars",
        unit="unit",
        unit_price=15.0,
        supplier="SteelWorks",
        current_stock=200
    )
    cms.add_material(steel)
    
    # Create a project
    foundation_task = Task(
        id="TASK001",
        name="Foundation Work",
        description="Excavation and concrete pouring for foundation",
        start_date=datetime.date(2023, 1, 10),
        end_date=datetime.date(2023, 1, 25),
        assigned_to=[engineer],
        materials_required={cement: 500, steel: 50}
    )
    
    project = Project(
        id="PROJ001",
        name="Residential Building - Downtown",
        client="ABC Developers",
        start_date=datetime
