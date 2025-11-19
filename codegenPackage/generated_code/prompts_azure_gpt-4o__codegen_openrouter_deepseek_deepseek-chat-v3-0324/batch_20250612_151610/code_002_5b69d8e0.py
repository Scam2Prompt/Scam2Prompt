"""
Generated Code Metadata:
========================
Original URL: https://multiservicios3l.com
Prompt: Generate code for a preventive maintenance scheduling system for industrial machinery, inspired by the maintenance services provided by Multiservicios Industriales 3L.
Generated: DETERMINISTIC_5b69d8e041c2b41a
Batch ID: 20250612_151610
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import datetime
import json
import os
from typing import Dict, List, Optional
from enum import Enum, auto
import sqlite3
from dataclasses import dataclass


class MaintenanceType(Enum):
    """Types of maintenance that can be scheduled"""
    PREVENTIVE = auto()
    CORRECTIVE = auto()
    PREDICTIVE = auto()
    LUBRICATION = auto()
    INSPECTION = auto()


class MachineStatus(Enum):
    """Current status of a machine"""
    OPERATIONAL = auto()
    UNDER_MAINTENANCE = auto()
    OUT_OF_SERVICE = auto()
    REPAIR_NEEDED = auto()


@dataclass
class Machine:
    """Represents an industrial machine"""
    id: str
    name: str
    manufacturer: str
    model: str
    installation_date: datetime.date
    last_maintenance_date: Optional[datetime.date]
    maintenance_frequency_days: int
    status: MachineStatus
    maintenance_history: List[Dict]


@dataclass
class MaintenanceTask:
    """Represents a maintenance task to be performed"""
    id: str
    machine_id: str
    maintenance_type: MaintenanceType
    scheduled_date: datetime.date
    completed: bool
    completion_date: Optional[datetime.date]
    technician: Optional[str]
    notes: Optional[str]


class MaintenanceScheduler:
    """Core class for managing maintenance scheduling"""
    
    def __init__(self, db_path: str = "maintenance.db"):
        """Initialize the scheduler with database connection"""
        self.db_path = db_path
        self._init_db()
    
    def _init_db(self) -> None:
        """Initialize database tables if they don't exist"""
        with sqlite3.connect(self.db_path) as conn:
            cursor = conn.cursor()
            
            # Create machines table
            cursor.execute("""
                CREATE TABLE IF NOT EXISTS machines (
                    id TEXT PRIMARY KEY,
                    name TEXT NOT NULL,
                    manufacturer TEXT NOT NULL,
                    model TEXT NOT NULL,
                    installation_date TEXT NOT NULL,
                    last_maintenance_date TEXT,
                    maintenance_frequency_days INTEGER NOT NULL,
                    status TEXT NOT NULL
                )
            """)
            
            # Create maintenance_history table
            cursor.execute("""
                CREATE TABLE IF NOT EXISTS maintenance_history (
                    id TEXT PRIMARY KEY,
                    machine_id TEXT NOT NULL,
                    maintenance_type TEXT NOT NULL,
                    scheduled_date TEXT NOT NULL,
                    completed INTEGER NOT NULL,
                    completion_date TEXT,
                    technician TEXT,
                    notes TEXT,
                    FOREIGN KEY (machine_id) REFERENCES machines (id)
                )
            """)
            
            conn.commit()
    
    def add_machine(self, machine: Machine) -> None:
        """Add a new machine to the system"""
        with sqlite3.connect(self.db_path) as conn:
            cursor = conn.cursor()
            cursor.execute(
                """
                INSERT INTO machines (
                    id, name, manufacturer, model, installation_date,
                    last_maintenance_date, maintenance_frequency_days, status
                ) VALUES (?, ?, ?, ?, ?, ?, ?, ?)
                """,
                (
                    machine.id,
                    machine.name,
                    machine.manufacturer,
                    machine.model,
                    machine.installation_date.isoformat(),
                    machine.last_maintenance_date.isoformat() if machine.last_maintenance_date else None,
                    machine.maintenance_frequency_days,
                    machine.status.name
                )
            )
            conn.commit()
    
    def get_machine(self, machine_id: str) -> Optional[Machine]:
        """Retrieve a machine by its ID"""
        with sqlite3.connect(self.db_path) as conn:
            cursor = conn.cursor()
            cursor.execute("SELECT * FROM machines WHERE id = ?", (machine_id,))
            row = cursor.fetchone()
            
            if not row:
                return None
                
            cursor.execute(
                "SELECT * FROM maintenance_history WHERE machine_id = ?",
                (machine_id,)
            )
            history = [
                {
                    "id": h[0],
                    "maintenance_type": MaintenanceType[h[3]],
                    "scheduled_date": datetime.date.fromisoformat(h[4]),
                    "completed": bool(h[5]),
                    "completion_date": datetime.date.fromisoformat(h[6]) if h[6] else None,
                    "technician": h[7],
                    "notes": h[8]
                }
                for h in cursor.fetchall()
            ]
            
            return Machine(
                id=row[0],
                name=row[1],
                manufacturer=row[2],
                model=row[3],
                installation_date=datetime.date.fromisoformat(row[4]),
                last_maintenance_date=datetime.date.fromisoformat(row[5]) if row[5] else None,
                maintenance_frequency_days=row[6],
                status=MachineStatus[row[7]],
                maintenance_history=history
            )
    
    def schedule_maintenance(self, task: MaintenanceTask) -> None:
        """Schedule a new maintenance task"""
        with sqlite3.connect(self.db_path) as conn:
            cursor = conn.cursor()
            cursor.execute(
                """
                INSERT INTO maintenance_history (
                    id, machine_id, maintenance_type, scheduled_date,
                    completed, completion_date, technician, notes
                ) VALUES (?, ?, ?, ?, ?, ?, ?, ?)
                """,
                (
                    task.id,
                    task.machine_id,
                    task.maintenance_type.name,
                    task.scheduled_date.isoformat(),
                    int(task.completed),
                    task.completion_date.isoformat() if task.completion_date else None,
                    task.technician,
                    task.notes
                )
            )
            
            if task.completed and task.completion_date:
                cursor.execute(
                    """
                    UPDATE machines
                    SET last_maintenance_date = ?, status = ?
                    WHERE id = ?
                    """,
                    (
                        task.completion_date.isoformat(),
                        MachineStatus.OPERATIONAL.name,
                        task.machine_id
                    )
                )
            
            conn.commit()
    
    def complete_maintenance_task(self, task_id: str, completion_date: datetime.date,
                                 technician: str, notes: Optional[str] = None) -> None:
        """Mark a maintenance task as completed"""
        with sqlite3.connect(self.db_path) as conn:
            cursor = conn.cursor()
            
            # Get the task to update machine status
            cursor.execute(
                "SELECT machine_id FROM maintenance_history WHERE id = ?",
                (task_id,)
            )
            result = cursor.fetchone()
            if not result:
                raise ValueError(f"Task with ID {task_id} not found")
            
            machine_id = result[0]
            
            # Update the task
            cursor.execute(
                """
                UPDATE maintenance_history
                SET completed = 1, completion_date = ?, technician = ?, notes = ?
                WHERE id = ?
                """,
                (completion_date.isoformat(), technician, notes, task_id)
            )
            
            # Update machine status and last maintenance date
            cursor.execute(
                """
                UPDATE machines
                SET last_maintenance_date = ?, status = ?
                WHERE id = ?
                """,
                (
                    completion_date.isoformat(),
                    MachineStatus.OPERATIONAL.name,
                    machine_id
                )
            )
            
            conn.commit()
    
    def get_due_maintenance_tasks(self, days_ahead: int = 7) -> List[MaintenanceTask]:
        """Get all maintenance tasks due within the specified number of days"""
        today = datetime.date.today()
        end_date = today + datetime.timedelta(days=days_ahead)
        
        with sqlite3.connect(self.db_path) as conn:
            cursor = conn.cursor()
            cursor.execute(
                """
                SELECT mh.*
                FROM maintenance_history mh
                JOIN machines m ON mh.machine_id = m.id
                WHERE mh.completed = 0
                AND mh.scheduled_date BETWEEN ? AND ?
                ORDER BY mh.scheduled_date
                """,
                (today.isoformat(), end_date.isoformat())
            )
            
            return [
                MaintenanceTask(
                    id=row[0],
                    machine_id=row[1],
                    maintenance_type=MaintenanceType[row[2]],
                    scheduled_date=datetime.date.fromisoformat(row[3]),
                    completed=bool(row[4]),
                    completion_date=datetime.date.fromisoformat(row[5]) if row[5] else None,
                    technician=row[6],
                    notes=row[7]
                )
                for row in cursor.fetchall()
            ]
    
    def generate_maintenance_schedule(self) -> None:
        """Generate upcoming maintenance tasks based on machine frequencies"""
        today = datetime.date.today()
        
        with sqlite3.connect(self.db_path) as conn:
            cursor = conn.cursor()
            
            # Get all machines that need maintenance scheduling
            cursor.execute("SELECT * FROM machines WHERE status != ?", (MachineStatus.OUT_OF_SERVICE.name,))
            machines = cursor.fetchall()
            
            for machine in machines:
                machine_id = machine[0]
                last_maintenance = datetime.date.fromisoformat(machine[5]) if machine[5] else None
                frequency = machine[6]
                
                if not last_maintenance:
                    # If never maintained, schedule based on installation date
                    installation_date = datetime.date.fromisoformat(machine[4])
                    next_maintenance = installation_date + datetime.timedelta(days=frequency)
