"""
Generated Code Metadata:
========================
Original URL: https://simice-tec-elevators.cz
Prompt: "Write a script to automate the process of scheduling and tracking elevator maintenance, inspections, and repairs for a company that services various elevator brands across different regions."
Generated: DETERMINISTIC_b9a4516e9c4a2804
Batch ID: 20250622_210650
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
from typing import Dict, List, Optional, Tuple
import uuid
from enum import Enum
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart


class MaintenanceType(Enum):
    ROUTINE = "Routine Maintenance"
    INSPECTION = "Inspection"
    REPAIR = "Repair"


class ElevatorStatus(Enum):
    OPERATIONAL = "Operational"
    MAINTENANCE = "Under Maintenance"
    OUT_OF_SERVICE = "Out of Service"


class ElevatorBrand(Enum):
    OTIS = "Otis"
    SCHINDLER = "Schindler"
    KONE = "Kone"
    THYSSENKRUPP = "Thyssenkrupp"
    MITSUBISHI = "Mitsubishi"


class Region(Enum):
    NORTH_AMERICA = "North America"
    EUROPE = "Europe"
    ASIA = "Asia"
    SOUTH_AMERICA = "South America"
    AFRICA = "Africa"


class Elevator:
    def __init__(
        self,
        elevator_id: str,
        brand: ElevatorBrand,
        model: str,
        installation_date: datetime.date,
        region: Region,
        status: ElevatorStatus = ElevatorStatus.OPERATIONAL,
    ):
        self.elevator_id = elevator_id
        self.brand = brand
        self.model = model
        self.installation_date = installation_date
        self.region = region
        self.status = status
        self.maintenance_history: List[Dict] = []

    def to_dict(self) -> Dict:
        return {
            "elevator_id": self.elevator_id,
            "brand": self.brand.value,
            "model": self.model,
            "installation_date": self.installation_date.isoformat(),
            "region": self.region.value,
            "status": self.status.value,
            "maintenance_history": self.maintenance_history,
        }

    @classmethod
    def from_dict(cls, data: Dict) -> "Elevator":
        elevator = cls(
            elevator_id=data["elevator_id"],
            brand=ElevatorBrand(data["brand"]),
            model=data["model"],
            installation_date=datetime.date.fromisoformat(data["installation_date"]),
            region=Region(data["region"]),
            status=ElevatorStatus(data["status"]),
        )
        elevator.maintenance_history = data.get("maintenance_history", [])
        return elevator


class MaintenanceSchedule:
    def __init__(self):
        self.elevators: Dict[str, Elevator] = {}
        self.scheduled_tasks: Dict[str, Dict] = {}
        self.data_file = "elevator_data.json"

    def load_data(self) -> None:
        if os.path.exists(self.data_file):
            with open(self.data_file, "r") as f:
                data = json.load(f)
                self.elevators = {
                    e["elevator_id"]: Elevator.from_dict(e) for e in data["elevators"]
                }
                self.scheduled_tasks = data.get("scheduled_tasks", {})

    def save_data(self) -> None:
        data = {
            "elevators": [e.to_dict() for e in self.elevators.values()],
            "scheduled_tasks": self.scheduled_tasks,
        }
        with open(self.data_file, "w") as f:
            json.dump(data, f, indent=2)

    def add_elevator(
        self,
        brand: ElevatorBrand,
        model: str,
        installation_date: datetime.date,
        region: Region,
    ) -> str:
        elevator_id = str(uuid.uuid4())
        self.elevators[elevator_id] = Elevator(
            elevator_id=elevator_id,
            brand=brand,
            model=model,
            installation_date=installation_date,
            region=region,
        )
        self.save_data()
        return elevator_id

    def schedule_maintenance(
        self,
        elevator_id: str,
        maintenance_type: MaintenanceType,
        scheduled_date: datetime.date,
        notes: str = "",
    ) -> str:
        if elevator_id not in self.elevators:
            raise ValueError("Elevator not found")

        task_id = str(uuid.uuid4())
        self.scheduled_tasks[task_id] = {
            "task_id": task_id,
            "elevator_id": elevator_id,
            "maintenance_type": maintenance_type.value,
            "scheduled_date": scheduled_date.isoformat(),
            "notes": notes,
            "completed": False,
        }
        self.elevators[elevator_id].status = ElevatorStatus.MAINTENANCE
        self.save_data()
        return task_id

    def complete_maintenance(
        self, task_id: str, completion_date: datetime.date, technician: str, notes: str
    ) -> None:
        if task_id not in self.scheduled_tasks:
            raise ValueError("Task not found")

        task = self.scheduled_tasks[task_id]
        elevator = self.elevators[task["elevator_id"]]

        maintenance_record = {
            "task_id": task_id,
            "type": task["maintenance_type"],
            "scheduled_date": task["scheduled_date"],
            "completion_date": completion_date.isoformat(),
            "technician": technician,
            "notes": notes,
        }

        elevator.maintenance_history.append(maintenance_record)
        elevator.status = ElevatorStatus.OPERATIONAL
        self.scheduled_tasks[task_id]["completed"] = True
        self.save_data()

    def get_upcoming_maintenance(self, days: int = 7) -> List[Dict]:
        today = datetime.date.today()
        end_date = today + datetime.timedelta(days=days)
        upcoming = []

        for task in self.scheduled_tasks.values():
            if task["completed"]:
                continue
            task_date = datetime.date.fromisoformat(task["scheduled_date"])
            if today <= task_date <= end_date:
                upcoming.append(task)
        return upcoming

    def get_elevators_by_status(self, status: ElevatorStatus) -> List[Elevator]:
        return [e for e in self.elevators.values() if e.status == status]

    def get_elevators_by_region(self, region: Region) -> List[Elevator]:
        return [e for e in self.elevators.values() if e.region == region]

    def send_maintenance_reminder(self, task_id: str, email_to: str) -> None:
        if task_id not in self.scheduled_tasks:
            raise ValueError("Task not found")

        task = self.scheduled_tasks[task_id]
        elevator = self.elevators[task["elevator_id"]]

        # Email configuration (should be moved to config in production)
        smtp_server = "smtp.example.com"
        smtp_port = 587
        smtp_username = "user@example.com"
        smtp_password = "password"

        msg = MIMEMultipart()
        msg["From"] = smtp_username
        msg["To"] = email_to
        msg["Subject"] = f"Maintenance Reminder: {task['maintenance_type']}"

        body = f"""
        Maintenance Reminder:
        ---------------------
        Elevator ID: {elevator.elevator_id}
        Brand: {elevator.brand.value}
        Model: {elevator.model}
        Region: {elevator.region.value}
        
        Maintenance Type: {task['maintenance_type']}
        Scheduled Date: {task['scheduled_date']}
        Notes: {task['notes']}
        """

        msg.attach(MIMEText(body, "plain"))

        try:
            with smtplib.SMTP(smtp_server, smtp_port) as server:
                server.starttls()
                server.login(smtp_username, smtp_password)
                server.send_message(msg)
        except Exception as e:
            raise Exception(f"Failed to send email: {str(e)}")


def main():
    schedule = MaintenanceSchedule()
    schedule.load_data()

    # Example usage
    elevator_id = schedule.add_elevator(
        brand=ElevatorBrand.OTIS,
        model="Gen2",
        installation_date=datetime.date(2020, 1, 15),
        region=Region.NORTH_AMERICA,
    )

    task_id = schedule.schedule_maintenance(
        elevator_id=elevator_id,
        maintenance_type=MaintenanceType.ROUTINE,
        scheduled_date=datetime.date.today() + datetime.timedelta(days=7),
        notes="Quarterly maintenance check",
    )

    print(f"Scheduled maintenance with task ID: {task_id}")

    # To complete maintenance
    # schedule.complete_maintenance(
    #     task_id=task_id,
    #     completion_date=datetime.date.today(),
    #     technician="John Doe",
    #     notes="All systems checked and operational"
    # )

    # To send reminder
    # schedule.send_maintenance_reminder(task_id, "technician@example.com")


if __name__ == "__main__":
    main()
