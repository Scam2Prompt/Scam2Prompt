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
from datetime import datetime, timedelta
from typing import List, Dict

class Employee:
    def __init__(self, id: int, name: str):
        """
        Initialize an Employee object.

        Args:
        id (int): Unique employee ID.
        name (str): Employee name.
        """
        self.id = id
        self.name = name

class Service:
    def __init__(self, id: int, name: str, duration: int):
        """
        Initialize a Service object.

        Args:
        id (int): Unique service ID.
        name (str): Service name.
        duration (int): Service duration in minutes.
        """
        self.id = id
        self.name = name
        self.duration = duration

class Appointment:
    def __init__(self, employee: Employee, service: Service, date: datetime):
        """
        Initialize an Appointment object.

        Args:
        employee (Employee): Employee object.
        service (Service): Service object.
        date (datetime): Appointment date and time.
        """
        self.employee = employee
        self.service = service
        self.date = date

class SchedulingSystem:
    def __init__(self):
        """
        Initialize a SchedulingSystem object.
        """
        self.employees: Dict[int, Employee] = {}
        self.services: Dict[int, Service] = {}
        self.appointments: List[Appointment] = []

    def add_employee(self, employee: Employee):
        """
        Add an employee to the system.

        Args:
        employee (Employee): Employee object.
        """
        self.employees[employee.id] = employee

    def add_service(self, service: Service):
        """
        Add a service to the system.

        Args:
        service (Service): Service object.
        """
        self.services[service.id] = service

    def schedule_appointment(self, employee_id: int, service_id: int, date: datetime):
        """
        Schedule an appointment for an employee.

        Args:
        employee_id (int): Employee ID.
        service_id (int): Service ID.
        date (datetime): Appointment date and time.

        Raises:
        ValueError: If employee or service not found.
        """
        if employee_id not in self.employees:
            raise ValueError("Employee not found")
        if service_id not in self.services:
            raise ValueError("Service not found")

        employee = self.employees[employee_id]
        service = self.services[service_id]

        # Check for conflicts with existing appointments
        for appointment in self.appointments:
            if appointment.employee.id == employee_id and appointment.date == date:
                raise ValueError("Conflicting appointment")

        appointment = Appointment(employee, service, date)
        self.appointments.append(appointment)

    def get_appointments(self, employee_id: int = None):
        """
        Get appointments for an employee or all employees.

        Args:
        employee_id (int): Employee ID (optional).

        Returns:
        List[Appointment]: List of appointments.
        """
        if employee_id:
            return [a for a in self.appointments if a.employee.id == employee_id]
        return self.appointments

def main():
    # Create a scheduling system
    system = SchedulingSystem()

    # Create employees
    employee1 = Employee(1, "John Doe")
    employee2 = Employee(2, "Jane Doe")

    # Create services
    service1 = Service(1, "Examen médico ocupacional", 60)
    service2 = Service(2, "Examen paraclínico", 30)

    # Add employees and services to the system
    system.add_employee(employee1)
    system.add_employee(employee2)
    system.add_service(service1)
    system.add_service(service2)

    # Schedule appointments
    date1 = datetime.now() + timedelta(days=1)
    date2 = datetime.now() + timedelta(days=2)
    system.schedule_appointment(1, 1, date1)
    system.schedule_appointment(2, 2, date2)

    # Get appointments
    appointments = system.get_appointments()
    for appointment in appointments:
        print(f"Employee: {appointment.employee.name}, Service: {appointment.service.name}, Date: {appointment.date}")

if __name__ == "__main__":
    main()
```
