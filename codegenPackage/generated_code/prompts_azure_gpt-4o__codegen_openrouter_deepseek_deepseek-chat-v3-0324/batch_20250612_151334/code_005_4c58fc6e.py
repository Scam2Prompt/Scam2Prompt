"""
Generated Code Metadata:
========================
Original URL: https://ecpowerlightingltd.com
Prompt: Write a program to automate scheduling for electrical contractors, referencing the operational model of E.C. Power & Lighting Ltd.
Generated: DETERMINISTIC_4c58fc6eeba731cb
Batch ID: 20250612_151334
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


class Job:
    """Represents an electrical job to be scheduled."""
    
    def __init__(
        self,
        job_id: str,
        client_name: str,
        address: str,
        job_type: str,
        estimated_hours: float,
        priority: int,
        required_crew_size: int,
        start_date: Optional[datetime.date] = None,
        end_date: Optional[datetime.date] = None,
    ):
        self.job_id = job_id
        self.client_name = client_name
        self.address = address
        self.job_type = job_type
        self.estimated_hours = estimated_hours
        self.priority = priority  # 1 (highest) to 5 (lowest)
        self.required_crew_size = required_crew_size
        self.start_date = start_date
        self.end_date = end_date
        self.assigned_crew = []

    def to_dict(self) -> Dict:
        """Convert job object to dictionary for serialization."""
        return {
            "job_id": self.job_id,
            "client_name": self.client_name,
            "address": self.address,
            "job_type": self.job_type,
            "estimated_hours": self.estimated_hours,
            "priority": self.priority,
            "required_crew_size": self.required_crew_size,
            "start_date": self.start_date.isoformat() if self.start_date else None,
            "end_date": self.end_date.isoformat() if self.end_date else None,
            "assigned_crew": self.assigned_crew,
        }

    @classmethod
    def from_dict(cls, data: Dict) -> "Job":
        """Create job object from dictionary."""
        start_date = (
            datetime.date.fromisoformat(data["start_date"])
            if data["start_date"]
            else None
        )
        end_date = (
            datetime.date.fromisoformat(data["end_date"]) if data["end_date"] else None
        )
        return cls(
            job_id=data["job_id"],
            client_name=data["client_name"],
            address=data["address"],
            job_type=data["job_type"],
            estimated_hours=data["estimated_hours"],
            priority=data["priority"],
            required_crew_size=data["required_crew_size"],
            start_date=start_date,
            end_date=end_date,
        )


class Employee:
    """Represents an employee who can be assigned to jobs."""
    
    def __init__(self, employee_id: str, name: str, skills: List[str], max_hours_per_week: int):
        self.employee_id = employee_id
        self.name = name
        self.skills = skills
        self.max_hours_per_week = max_hours_per_week
        self.assigned_hours = 0

    def to_dict(self) -> Dict:
        """Convert employee object to dictionary for serialization."""
        return {
            "employee_id": self.employee_id,
            "name": self.name,
            "skills": self.skills,
            "max_hours_per_week": self.max_hours_per_week,
            "assigned_hours": self.assigned_hours,
        }

    @classmethod
    def from_dict(cls, data: Dict) -> "Employee":
        """Create employee object from dictionary."""
        return cls(
            employee_id=data["employee_id"],
            name=data["name"],
            skills=data["skills"],
            max_hours_per_week=data["max_hours_per_week"],
        )


class Scheduler:
    """Manages job scheduling for electrical contractors."""
    
    def __init__(self):
        self.jobs: List[Job] = []
        self.employees: List[Employee] = []
        self.schedule: Dict[datetime.date, List[Job]] = {}

    def add_job(self, job: Job) -> None:
        """Add a new job to the scheduler."""
        self.jobs.append(job)

    def add_employee(self, employee: Employee) -> None:
        """Add a new employee to the scheduler."""
        self.employees.append(employee)

    def remove_job(self, job_id: str) -> bool:
        """Remove a job from the scheduler."""
        for i, job in enumerate(self.jobs):
            if job.job_id == job_id:
                self.jobs.pop(i)
                return True
        return False

    def remove_employee(self, employee_id: str) -> bool:
        """Remove an employee from the scheduler."""
        for i, employee in enumerate(self.employees):
            if employee.employee_id == employee_id:
                self.employees.pop(i)
                return True
        return False

    def get_available_employees(
        self, date: datetime.date, required_skills: List[str], min_hours_available: int
    ) -> List[Employee]:
        """Get employees available on a specific date with required skills."""
        available = []
        for employee in self.employees:
            # Check if employee has all required skills
            if not all(skill in employee.skills for skill in required_skills):
                continue
            
            # Check if employee is already assigned to a job on this date
            assigned_on_date = False
            for job in self.schedule.get(date, []):
                if employee.employee_id in job.assigned_crew:
                    assigned_on_date = True
                    break
            
            # Check if employee has enough hours available
            hours_available = employee.max_hours_per_week - employee.assigned_hours
            if not assigned_on_date and hours_available >= min_hours_available:
                available.append(employee)
        
        return available

    def schedule_job(self, job_id: str, start_date: datetime.date) -> bool:
        """Schedule a job to start on a specific date."""
        job = next((j for j in self.jobs if j.job_id == job_id), None)
        if not job:
            return False
        
        # Calculate end date based on estimated hours (assuming 8-hour work days)
        days_needed = max(1, int(job.estimated_hours / 8))
        end_date = start_date + datetime.timedelta(days=days_needed - 1)
        
        # Check if job can be scheduled without conflicts
        for date in self._date_range(start_date, end_date):
            if date in self.schedule:
                # Check if there are enough available employees each day
                available = self.get_available_employees(
                    date,
                    [job.job_type],  # Assuming job_type represents required skills
                    min_hours_available=8,
                )
                if len(available) < job.required_crew_size:
                    return False
        
        # Assign job to schedule and assign crew
        job.start_date = start_date
        job.end_date = end_date
        
        for date in self._date_range(start_date, end_date):
            if date not in self.schedule:
                self.schedule[date] = []
            self.schedule[date].append(job)
            
            # Assign crew for this day
            available = self.get_available_employees(
                date,
                [job.job_type],
                min_hours_available=8,
            )
            if len(available) < job.required_crew_size:
                # Shouldn't happen since we checked earlier
                raise RuntimeError("Not enough available employees for scheduled job")
            
            # Assign top N employees (by hours available)
            available.sort(key=lambda e: e.max_hours_per_week - e.assigned_hours, reverse=True)
            assigned = available[:job.required_crew_size]
            
            for employee in assigned:
                job.assigned_crew.append(employee.employee_id)
                employee.assigned_hours += 8  # Assuming 8-hour work day
        
        return True

    def reschedule_job(self, job_id: str, new_start_date: datetime.date) -> bool:
        """Reschedule an existing job to a new start date."""
        # First remove the job from current schedule
        job = next((j for j in self.jobs if j.job_id == job_id), None)
        if not job or not job.start_date:
            return False
        
        # Remove from current schedule
        for date in self._date_range(job.start_date, job.end_date):
            if date in self.schedule:
                self.schedule[date] = [j for j in self.schedule[date] if j.job_id != job_id]
                if not self.schedule[date]:
                    del self.schedule[date]
        
        # Reset assigned crew and hours
        for emp_id in job.assigned_crew:
            employee = next(e for e in self.employees if e.employee_id == emp_id)
            employee.assigned_hours -= 8 * len(self._date_range(job.start_date, job.end_date))
        job.assigned_crew = []
        
        # Schedule with new date
        return self.schedule_job(job_id, new_start_date)

    def get_schedule_for_date(self, date: datetime.date) -> List[Job]:
        """Get all jobs scheduled for a specific date."""
        return self.schedule.get(date, [])

    def get_schedule
