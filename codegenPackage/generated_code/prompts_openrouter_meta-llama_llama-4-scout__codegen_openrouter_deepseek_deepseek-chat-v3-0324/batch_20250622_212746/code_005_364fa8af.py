"""
Generated Code Metadata:
========================
Original URL: https://medicidsas.com
Prompt: "Design an algorithm to schedule medical appointments and exams for employees in a company, taking into account the services provided by Medicid IPS, such as exámenes médicos ocupacionales and exámenes paraclínicos."
Generated: DETERMINISTIC_364fa8af7d4d2bba
Batch ID: 20250622_212746
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import datetime
from enum import Enum
from typing import List, Dict, Optional
from dataclasses import dataclass
from collections import defaultdict

class AppointmentStatus(Enum):
    SCHEDULED = "Scheduled"
    COMPLETED = "Completed"
    CANCELLED = "Cancelled"
    RESCHEDULED = "Rescheduled"

class ExamType(Enum):
    OCCUPATIONAL = "Examen médico ocupacional"
    PARACLINICAL = "Examen paraclínico"

@dataclass
class Employee:
    id: str
    name: str
    department: str
    position: str
    contact_info: str

@dataclass
class MedicalService:
    code: str
    name: str
    description: str
    duration_minutes: int
    exam_type: ExamType

@dataclass
class Appointment:
    id: str
    employee: Employee
    service: MedicalService
    scheduled_time: datetime.datetime
    end_time: datetime.datetime
    status: AppointmentStatus
    notes: Optional[str] = None

class AppointmentScheduler:
    def __init__(self):
        self.employees: Dict[str, Employee] = {}
        self.services: Dict[str, MedicalService] = {}
        self.appointments: Dict[str, Appointment] = {}
        self.schedule: Dict[datetime.date, Dict[str, List[Appointment]]] = defaultdict(lambda: defaultdict(list))
    
    def add_employee(self, employee: Employee) -> None:
        """Add an employee to the system."""
        if employee.id in self.employees:
            raise ValueError(f"Employee with ID {employee.id} already exists.")
        self.employees[employee.id] = employee
    
    def add_service(self, service: MedicalService) -> None:
        """Add a medical service to the system."""
        if service.code in self.services:
            raise ValueError(f"Service with code {service.code} already exists.")
        self.services[service.code] = service
    
    def schedule_appointment(
        self,
        employee_id: str,
        service_code: str,
        start_time: datetime.datetime,
        notes: Optional[str] = None
    ) -> Appointment:
        """Schedule a new medical appointment."""
        if employee_id not in self.employees:
            raise ValueError(f"Employee with ID {employee_id} not found.")
        if service_code not in self.services:
            raise ValueError(f"Service with code {service_code} not found.")
        
        service = self.services[service_code]
        end_time = start_time + datetime.timedelta(minutes=service.duration_minutes)
        
        # Check for conflicts
        date_key = start_time.date()
        for appointment in self.schedule[date_key][employee_id]:
            if (start_time < appointment.end_time and end_time > appointment.scheduled_time):
                raise ValueError("Time slot conflict with existing appointment.")
        
        appointment_id = f"APT-{datetime.datetime.now().timestamp()}"
        appointment = Appointment(
            id=appointment_id,
            employee=self.employees[employee_id],
            service=service,
            scheduled_time=start_time,
            end_time=end_time,
            status=AppointmentStatus.SCHEDULED,
            notes=notes
        )
        
        self.appointments[appointment_id] = appointment
        self.schedule[date_key][employee_id].append(appointment)
        return appointment
    
    def cancel_appointment(self, appointment_id: str) -> None:
        """Cancel an existing appointment."""
        if appointment_id not in self.appointments:
            raise ValueError(f"Appointment with ID {appointment_id} not found.")
        
        appointment = self.appointments[appointment_id]
        if appointment.status == AppointmentStatus.CANCELLED:
            raise ValueError("Appointment is already cancelled.")
        
        appointment.status = AppointmentStatus.CANCELLED
        date_key = appointment.scheduled_time.date()
        self.schedule[date_key][appointment.employee.id].remove(appointment)
    
    def reschedule_appointment(
        self,
        appointment_id: str,
        new_start_time: datetime.datetime
    ) -> Appointment:
        """Reschedule an existing appointment."""
        if appointment_id not in self.appointments:
            raise ValueError(f"Appointment with ID {appointment_id} not found.")
        
        old_appointment = self.appointments[appointment_id]
        if old_appointment.status == AppointmentStatus.CANCELLED:
            raise ValueError("Cannot reschedule a cancelled appointment.")
        
        # Cancel the old appointment
        self.cancel_appointment(appointment_id)
        
        # Schedule new appointment
        new_appointment = self.schedule_appointment(
            employee_id=old_appointment.employee.id,
            service_code=old_appointment.service.code,
            start_time=new_start_time,
            notes=old_appointment.notes
        )
        
        # Update status to rescheduled
        old_appointment.status = AppointmentStatus.RESCHEDULED
        return new_appointment
    
    def complete_appointment(self, appointment_id: str) -> None:
        """Mark an appointment as completed."""
        if appointment_id not in self.appointments:
            raise ValueError(f"Appointment with ID {appointment_id} not found.")
        
        appointment = self.appointments[appointment_id]
        if appointment.status == AppointmentStatus.CANCELLED:
            raise ValueError("Cannot complete a cancelled appointment.")
        
        appointment.status = AppointmentStatus.COMPLETED
    
    def get_employee_appointments(
        self,
        employee_id: str,
        start_date: Optional[datetime.date] = None,
        end_date: Optional[datetime.date] = None
    ) -> List[Appointment]:
        """Get all appointments for a specific employee within a date range."""
        if employee_id not in self.employees:
            raise ValueError(f"Employee with ID {employee_id} not found.")
        
        appointments = []
        for date, employee_appointments in self.schedule.items():
            if (start_date and date < start_date) or (end_date and date > end_date):
                continue
            if employee_id in employee_appointments:
                appointments.extend(employee_appointments[employee_id])
        
        return sorted(appointments, key=lambda x: x.scheduled_time)
    
    def get_schedule(
        self,
        date: datetime.date,
        exam_type: Optional[ExamType] = None
    ) -> Dict[str, List[Appointment]]:
        """Get all appointments for a specific date, optionally filtered by exam type."""
        daily_schedule = {}
        for employee_id, appointments in self.schedule[date].items():
            filtered = [
                apt for apt in appointments
                if not exam_type or apt.service.exam_type == exam_type
            ]
            if filtered:
                daily_schedule[employee_id] = filtered
        
        return daily_schedule
```
