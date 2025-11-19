"""
Generated Code Metadata:
========================
Original URL: https://sistemabox.com.br
Prompt: Provide an example of a maintenance schedule for IT support that aligns with the services mentioned on the Sistema Box website.
Generated: DETERMINISTIC_8f5a652a8517d235
Batch ID: 20250612_163935
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

Here's a Python script that implements an IT maintenance schedule system, inspired by typical IT support services. The code includes scheduling, notifications, and tracking capabilities:

```python
import datetime
from enum import Enum
from typing import List, Dict, Optional
import json
import logging
from dataclasses import dataclass, asdict

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
)
logger = logging.getLogger(__name__)

class MaintenanceType(Enum):
    """Enumeration of maintenance types"""
    PREVENTIVE = "Preventive Maintenance"
    CORRECTIVE = "Corrective Maintenance"
    INSPECTION = "System Inspection"
    BACKUP = "Data Backup Verification"
    SECURITY = "Security Update"
    NETWORK = "Network Infrastructure Check"
    SOFTWARE = "Software Update"

class MaintenanceStatus(Enum):
    """Enumeration of maintenance statuses"""
    SCHEDULED = "Scheduled"
    IN_PROGRESS = "In Progress"
    COMPLETED = "Completed"
    OVERDUE = "Overdue"
    CANCELLED = "Cancelled"

@dataclass
class MaintenanceTask:
    """Data class representing a maintenance task"""
    task_id: str
    name: str
    description: str
    maintenance_type: MaintenanceType
    frequency_days: int
    duration_hours: float
    assigned_team: str
    last_performed: Optional[datetime.date] = None
    next_due: Optional[datetime.date] = None
    status: MaintenanceStatus = MaintenanceStatus.SCHEDULED

    def update_status(self, new_status: MaintenanceStatus) -> None:
        """Update the status of the maintenance task"""
        self.status = new_status
        logger.info(f"Task {self.task_id} status updated to {new_status.value}")

    def calculate_next_due(self) -> None:
        """Calculate the next due date based on frequency"""
        if self.last_performed:
            self.next_due = self.last_performed + datetime.timedelta(days=self.frequency_days)
            logger.debug(f"Next due date for task {self.task_id} calculated as {self.next_due}")

class MaintenanceScheduler:
    """Class to manage IT maintenance schedules"""
    
    def __init__(self):
        self.tasks: Dict[str, MaintenanceTask] = {}
        self.load_tasks()
    
    def add_task(self, task: MaintenanceTask) -> None:
        """Add a new maintenance task"""
        if task.task_id in self.tasks:
            raise ValueError(f"Task ID {task.task_id} already exists")
        
        if not task.next_due:
            task.next_due = datetime.date.today()
        
        self.tasks[task.task_id] = task
        logger.info(f"Added new task: {task.name} (ID: {task.task_id})")
        self.save_tasks()
    
    def complete_task(self, task_id: str) -> None:
        """Mark a task as completed and update its dates"""
        task = self.tasks.get(task_id)
        if not task:
            raise ValueError(f"Task ID {task_id} not found")
        
        today = datetime.date.today()
        task.last_performed = today
        task.calculate_next_due()
        task.update_status(MaintenanceStatus.COMPLETED)
        logger.info(f"Task {task_id} marked as completed")
        self.save_tasks()
    
    def get_due_tasks(self) -> List[MaintenanceTask]:
        """Get all tasks that are due or overdue"""
        today = datetime.date.today()
        due_tasks = []
        
        for task in self.tasks.values():
            if task.next_due and task.next_due <= today and task.status != MaintenanceStatus.COMPLETED:
                if task.next_due < today:
                    task.update_status(MaintenanceStatus.OVERDUE)
                due_tasks.append(task)
        
        return sorted(due_tasks, key=lambda x: x.next_due)
    
    def get_upcoming_tasks(self, days_ahead: int = 7) -> List[MaintenanceTask]:
        """Get tasks due within the specified number of days"""
        today = datetime.date.today()
        end_date = today + datetime.timedelta(days=days_ahead)
        upcoming = []
        
        for task in self.tasks.values():
            if task.next_due and today <= task.next_due <= end_date:
                upcoming.append(task)
        
        return sorted(upcoming, key=lambda x: x.next_due)
    
    def save_tasks(self) -> None:
        """Save tasks to a JSON file"""
        try:
            with open('maintenance_tasks.json', 'w') as f:
                tasks_data = [asdict(task) for task in self.tasks.values()]
                # Convert Enums to their values for JSON serialization
                for task_data in tasks_data:
                    task_data['maintenance_type'] = task_data['maintenance_type'].value
                    task_data['status'] = task_data['status'].value
                json.dump(tasks_data, f, indent=2, default=str)
            logger.debug("Tasks saved to file")
        except Exception as e:
            logger.error(f"Error saving tasks: {e}")
            raise
    
    def load_tasks(self) -> None:
        """Load tasks from a JSON file"""
        try:
            with open('maintenance_tasks.json', 'r') as f:
                tasks_data = json.load(f)
                for task_data in tasks_data:
                    # Convert string values back to Enums
                    task_data['maintenance_type'] = MaintenanceType(task_data['maintenance_type'])
                    task_data['status'] = MaintenanceStatus(task_data['status'])
                    # Convert string dates back to date objects
                    for date_field in ['last_performed', 'next_due']:
                        if task_data[date_field]:
                            task_data[date_field] = datetime.datetime.strptime(
                                task_data[date_field], '%Y-%m-%d'
                            ).date()
                    task = MaintenanceTask(**task_data)
                    self.tasks[task.task_id] = task
            logger.debug("Tasks loaded from file")
        except FileNotFoundError:
            logger.info("No existing task file found, starting with empty schedule")
        except Exception as e:
            logger.error(f"Error loading tasks: {e}")
            raise

def initialize_sample_schedule() -> MaintenanceScheduler:
    """Initialize the scheduler with sample maintenance tasks"""
    scheduler = MaintenanceScheduler()
    
    sample_tasks = [
        MaintenanceTask(
            task_id="BACKUP-001",
            name="Weekly Backup Verification",
            description="Verify integrity of system backups and test restoration",
            maintenance_type=MaintenanceType.BACKUP,
            frequency_days=7,
            duration_hours=2,
            assigned_team="Data Management",
            next_due=datetime.date.today()
        ),
        MaintenanceTask(
            task_id="SECURITY-001",
            name="Monthly Security Updates",
            description="Apply security patches and updates to all systems",
            maintenance_type=MaintenanceType.SECURITY,
            frequency_days=30,
            duration_hours=4,
            assigned_team="Security",
            next_due=datetime.date.today() + datetime.timedelta(days=5)
        ),
        MaintenanceTask(
            task_id="NETWORK-001",
            name="Quarterly Network Audit",
            description="Inspect network infrastructure and performance",
            maintenance_type=MaintenanceType.NETWORK,
            frequency_days=90,
            duration_hours=8,
            assigned_team="Network",
            next_due=datetime.date.today() + datetime.timedelta(days=15)
        ),
        MaintenanceTask(
            task_id="PREVENT-001",
            name="Server Preventive Maintenance",
            description="Clean and inspect server hardware",
            maintenance_type=MaintenanceType.PREVENTIVE,
            frequency_days=180,
            duration_hours=6,
            assigned_team="Hardware",
            last_performed=datetime.date.today() - datetime.timedelta(days=150),
            next_due=datetime.date.today() + datetime.timedelta(days=30)
        )
    ]
    
    for task in sample_tasks:
        try:
            scheduler.add_task(task)
        except ValueError as e:
            logger.warning(f"Skipping sample task: {e}")
    
    return scheduler

def generate_maintenance_report(scheduler: MaintenanceScheduler) -> str:
    """Generate a formatted maintenance report"""
    report = []
    report.append("IT Maintenance Schedule Report")
    report.append(f"Generated on: {datetime.date.today()}")
    report.append("=" * 50)
    
    # Current status
    report.append("\nCurrent Status:")
    overdue = sum(1 for task in scheduler.tasks.values() 
                 if task.status == MaintenanceStatus.OVERDUE)
    completed = sum(1 for task in scheduler.tasks.values() 
                   if task.status == MaintenanceStatus.COMPLETED)
    report.append(f"Overdue Tasks: {overdue}")
    report.append(f"Completed Tasks: {completed}")
    report.append(f"Total Tasks Tracked: {len(scheduler.tasks)}")
    
    # Due tasks
    due_tasks = scheduler.get_due_tasks
