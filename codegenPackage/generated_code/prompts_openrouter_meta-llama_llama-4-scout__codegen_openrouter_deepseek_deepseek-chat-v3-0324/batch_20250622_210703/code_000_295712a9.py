"""
Generated Code Metadata:
========================
Original URL: https://afms.in
Prompt: Write a Python script to manage housekeeping services, including scheduling and employee assignment, for a facility management company like Ashvi Facility Management Services.
Generated: DETERMINISTIC_295712a98c063808
Batch ID: 20250622_210703
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

class HousekeepingServiceManager:
    """
    Manages housekeeping services including scheduling and employee assignment.
    """
    
    def __init__(self, data_file: str = "housekeeping_data.json"):
        """
        Initialize the manager with a data file for persistence.
        
        Args:
            data_file: Path to the JSON file storing service data.
        """
        self.data_file = data_file
        self.services = []
        self.employees = []
        self.load_data()
    
    def load_data(self) -> None:
        """
        Load service and employee data from the JSON file.
        Creates file if it doesn't exist.
        """
        try:
            if os.path.exists(self.data_file):
                with open(self.data_file, 'r') as f:
                    data = json.load(f)
                    self.services = data.get('services', [])
                    self.employees = data.get('employees', [])
            else:
                self.services = []
                self.employees = []
                self.save_data()
        except (json.JSONDecodeError, IOError) as e:
            print(f"Error loading data: {e}")
            self.services = []
            self.employees = []
    
    def save_data(self) -> None:
        """
        Save current service and employee data to the JSON file.
        """
        try:
            data = {
                'services': self.services,
                'employees': self.employees
            }
            with open(self.data_file, 'w') as f:
                json.dump(data, f, indent=2)
        except IOError as e:
            print(f"Error saving data: {e}")
    
    def add_service_request(
        self,
        location: str,
        service_type: str,
        scheduled_time: datetime.datetime,
        priority: str = "normal"
    ) -> str:
        """
        Add a new service request to the system.
        
        Args:
            location: Where the service is needed.
            service_type: Type of service (cleaning, maintenance, etc.).
            scheduled_time: When the service should be performed.
            priority: Priority level (low, normal, high).
            
        Returns:
            Service ID for the new request.
        """
        service_id = f"SRV-{datetime.datetime.now().strftime('%Y%m%d%H%M%S')}"
        self.services.append({
            'id': service_id,
            'location': location,
            'service_type': service_type,
            'scheduled_time': scheduled_time.isoformat(),
            'priority': priority,
            'assigned_employee': None,
            'status': 'pending'
        })
        self.save_data()
        return service_id
    
    def add_employee(
        self,
        name: str,
        skills: List[str],
        availability: Dict[str, List[str]]
    ) -> str:
        """
        Add a new employee to the system.
        
        Args:
            name: Employee name.
            skills: List of skills the employee has.
            availability: Dict of days with available time slots.
            
        Returns:
            Employee ID for the new employee.
        """
        employee_id = f"EMP-{datetime.datetime.now().strftime('%Y%m%d%H%M%S')}"
        self.employees.append({
            'id': employee_id,
            'name': name,
            'skills': skills,
            'availability': availability,
            'assigned_services': []
        })
        self.save_data()
        return employee_id
    
    def assign_employee_to_service(
        self,
        service_id: str,
        employee_id: str
    ) -> bool:
        """
        Assign an employee to a service request.
        
        Args:
            service_id: ID of the service to assign.
            employee_id: ID of the employee to assign.
            
        Returns:
            True if assignment was successful, False otherwise.
        """
        service = next((s for s in self.services if s['id'] == service_id), None)
        employee = next((e for e in self.employees if e['id'] == employee_id), None)
        
        if not service or not employee:
            return False
        
        if service['assigned_employee']:
            return False
        
        # Check if employee has required skills
        if service['service_type'] not in employee['skills']:
            return False
        
        # Check employee availability
        scheduled_time = datetime.datetime.fromisoformat(service['scheduled_time'])
        day_of_week = scheduled_time.strftime('%A').lower()
        
        if day_of_week not in employee['availability']:
            return False
        
        time_slot = scheduled_time.strftime('%H:%M')
        if time_slot not in employee['availability'][day_of_week]:
            return False
        
        # Assign the employee
        service['assigned_employee'] = employee_id
        service['status'] = 'assigned'
        employee['assigned_services'].append(service_id)
        
        self.save_data()
        return True
    
    def complete_service(self, service_id: str) -> bool:
        """
        Mark a service as completed.
        
        Args:
            service_id: ID of the service to complete.
            
        Returns:
            True if service was marked completed, False otherwise.
        """
        service = next((s for s in self.services if s['id'] == service_id), None)
        if not service or service['status'] == 'completed':
            return False
        
        service['status'] = 'completed'
        self.save_data()
        return True
    
    def get_pending_services(self) -> List[Dict]:
        """
        Get all pending service requests.
        
        Returns:
            List of pending service dictionaries.
        """
        return [s for s in self.services if s['status'] == 'pending']
    
    def get_employee_schedule(
        self,
        employee_id: str,
        start_date: datetime.datetime,
        end_date: datetime.datetime
    ) -> List[Dict]:
        """
        Get an employee's schedule between two dates.
        
        Args:
            employee_id: ID of the employee.
            start_date: Start of date range.
            end_date: End of date range.
            
        Returns:
            List of services assigned to the employee in the date range.
        """
        employee = next((e for e in self.employees if e['id'] == employee_id), None)
        if not employee:
            return []
        
        result = []
        for service_id in employee['assigned_services']:
            service = next((s for s in self.services if s['id'] == service_id), None)
            if service:
                service_time = datetime.datetime.fromisoformat(service['scheduled_time'])
                if start_date <= service_time <= end_date:
                    result.append(service)
        
        return result
    
    def get_available_employees(
        self,
        service_type: str,
        scheduled_time: datetime.datetime
    ) -> List[Dict]:
        """
        Get employees available for a specific service at a given time.
        
        Args:
            service_type: Type of service needed.
            scheduled_time: When the service is scheduled.
            
        Returns:
            List of available employee dictionaries.
        """
        day_of_week = scheduled_time.strftime('%A').lower()
        time_slot = scheduled_time.strftime('%H:%M')
        
        available_employees = []
        for employee in self.employees:
            if (service_type in employee['skills'] and
                day_of_week in employee['availability'] and
                time_slot in employee['availability'][day_of_week]):
                
                # Check if employee is already assigned to another service at this time
                conflicting = False
                for service_id in employee['assigned_services']:
                    service = next((s for s in self.services if s['id'] == service_id), None)
                    if service:
                        st = datetime.datetime.fromisoformat(service['scheduled_time'])
                        if st == scheduled_time:
                            conflicting = True
                            break
                
                if not conflicting:
                    available_employees.append(employee)
        
        return available_employees

# Example usage
if __name__ == "__main__":
    manager = HousekeepingServiceManager()
    
    # Add some employees
    emp1 = manager.add_employee(
        name="John Doe",
        skills=["cleaning", "maintenance"],
        availability={
            "monday": ["09:00", "10:00", "11:00"],
            "tuesday": ["09:00", "10:00", "11:00"]
        }
    )
    
    emp2 = manager.add_employee(
        name="Jane Smith",
        skills=["cleaning"],
        availability={
            "monday": ["14:00", "15:00", "16:00"],
            "wednesday": ["09:00", "10:00", "11:00"]
        }
    )
    
    # Add some service requests
    service_time = datetime.datetime.now().replace(hour=10, minute=0, second=0, microsecond=0)
    service1 = manager.add_service_request(
        location="Office 101",
        service_type="cleaning",
        scheduled_time=service_time,
        priority="high"
    )
    
    # Assign employee to service
    if manager.assign_employee_to_service(service1, emp1):
        print(f"Assigned employee {emp1} to service {service1
