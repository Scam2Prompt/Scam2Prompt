"""
Generated Code Metadata:
========================
Original URL: https://trackdieselperu.com
Prompt: Design a workflow in Python for scheduling field technical assistance for machinery repairs, incorporating Track Diesel Peru's focus on on-site and workshop services.
Generated: DETERMINISTIC_3ecd2e8b18f31aa2
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
from enum import Enum
from typing import Dict, List, Optional
from uuid import uuid4

# Database simulation
class Database:
    def __init__(self):
        self.technicians = []
        self.customers = []
        self.services = []
        self.equipment = []
        self.load_data()

    def load_data(self):
        try:
            if os.path.exists('technicians.json'):
                with open('technicians.json', 'r') as f:
                    self.technicians = json.load(f)
            if os.path.exists('customers.json'):
                with open('customers.json', 'r') as f:
                    self.customers = json.load(f)
            if os.path.exists('services.json'):
                with open('services.json', 'r') as f:
                    self.services = json.load(f)
            if os.path.exists('equipment.json'):
                with open('equipment.json', 'r') as f:
                    self.equipment = json.load(f)
        except Exception as e:
            print(f"Error loading data: {e}")

    def save_data(self):
        try:
            with open('technicians.json', 'w') as f:
                json.dump(self.technicians, f)
            with open('customers.json', 'w') as f:
                json.dump(self.customers, f)
            with open('services.json', 'w') as f:
                json.dump(self.services, f)
            with open('equipment.json', 'w') as f:
                json.dump(self.equipment, f)
        except Exception as e:
            print(f"Error saving data: {e}")

# Enums
class ServiceType(Enum):
    ON_SITE = "On-site"
    WORKSHOP = "Workshop"

class ServiceStatus(Enum):
    SCHEDULED = "Scheduled"
    IN_PROGRESS = "In Progress"
    COMPLETED = "Completed"
    CANCELLED = "Cancelled"

# Models
class Technician:
    def __init__(self, name: str, specialization: str, contact: str):
        self.id = str(uuid4())
        self.name = name
        self.specialization = specialization
        self.contact = contact
        self.availability = True

class Customer:
    def __init__(self, name: str, contact: str, location: str):
        self.id = str(uuid4())
        self.name = name
        self.contact = contact
        self.location = location

class Equipment:
    def __init__(self, customer_id: str, model: str, serial_number: str):
        self.id = str(uuid4())
        self.customer_id = customer_id
        self.model = model
        self.serial_number = serial_number
        self.service_history = []

class ServiceRequest:
    def __init__(
        self,
        customer_id: str,
        equipment_id: str,
        issue_description: str,
        service_type: ServiceType,
        preferred_date: datetime.date
    ):
        self.id = str(uuid4())
        self.customer_id = customer_id
        self.equipment_id = equipment_id
        self.issue_description = issue_description
        self.service_type = service_type
        self.preferred_date = preferred_date
        self.status = ServiceStatus.SCHEDULED
        self.assigned_technician = None
        self.actual_date = None
        self.resolution_notes = None

# Service Scheduler
class ServiceScheduler:
    def __init__(self, db: Database):
        self.db = db

    def create_service_request(
        self,
        customer_id: str,
        equipment_id: str,
        issue_description: str,
        service_type: ServiceType,
        preferred_date: datetime.date
    ) -> Optional[ServiceRequest]:
        try:
            # Validate customer and equipment
            customer = next((c for c in self.db.customers if c['id'] == customer_id), None)
            equipment = next((e for e in self.db.equipment if e['id'] == equipment_id), None)
            
            if not customer or not equipment:
                raise ValueError("Invalid customer or equipment ID")
            
            if equipment['customer_id'] != customer_id:
                raise ValueError("Equipment does not belong to customer")
            
            # Create service request
            service = ServiceRequest(
                customer_id=customer_id,
                equipment_id=equipment_id,
                issue_description=issue_description,
                service_type=service_type,
                preferred_date=preferred_date
            )
            
            # Save to database
            service_dict = {
                'id': service.id,
                'customer_id': service.customer_id,
                'equipment_id': service.equipment_id,
                'issue_description': service.issue_description,
                'service_type': service.service_type.value,
                'preferred_date': service.preferred_date.isoformat(),
                'status': service.status.value,
                'assigned_technician': service.assigned_technician,
                'actual_date': service.actual_date.isoformat() if service.actual_date else None,
                'resolution_notes': service.resolution_notes
            }
            
            self.db.services.append(service_dict)
            self.db.save_data()
            
            return service
        except Exception as e:
            print(f"Error creating service request: {e}")
            return None

    def assign_technician(self, service_id: str, technician_id: str) -> bool:
        try:
            service = next((s for s in self.db.services if s['id'] == service_id), None)
            technician = next((t for t in self.db.technicians if t['id'] == technician_id), None)
            
            if not service or not technician:
                raise ValueError("Invalid service or technician ID")
            
            if service['status'] != ServiceStatus.SCHEDULED.value:
                raise ValueError("Service is not in scheduled status")
            
            if not technician['availability']:
                raise ValueError("Technician is not available")
            
            # Update service
            service['assigned_technician'] = technician_id
            self.db.save_data()
            
            return True
        except Exception as e:
            print(f"Error assigning technician: {e}")
            return False

    def update_service_status(
        self,
        service_id: str,
        status: ServiceStatus,
        resolution_notes: str = None
    ) -> bool:
        try:
            service = next((s for s in self.db.services if s['id'] == service_id), None)
            
            if not service:
                raise ValueError("Invalid service ID")
            
            service['status'] = status.value
            
            if status == ServiceStatus.COMPLETED:
                if not resolution_notes:
                    raise ValueError("Resolution notes are required for completed services")
                service['resolution_notes'] = resolution_notes
                service['actual_date'] = datetime.date.today().isoformat()
            
            self.db.save_data()
            return True
        except Exception as e:
            print(f"Error updating service status: {e}")
            return False

    def get_available_technicians(self, service_type: ServiceType) -> List[Dict]:
        try:
            return [
                {
                    'id': t['id'],
                    'name': t['name'],
                    'specialization': t['specialization']
                }
                for t in self.db.technicians
                if t['availability'] and (
                    service_type == ServiceType.ON_SITE or 
                    t['specialization'].lower() in ['workshop', 'general']
                )
            ]
        except Exception as e:
            print(f"Error getting available technicians: {e}")
            return []

# Main Workflow
def main():
    db = Database()
    scheduler = ServiceScheduler(db)
    
    # Sample usage
    try:
        # Create customer
        customer = Customer("Mining Corp", "contact@miningcorp.com", "Lima")
        db.customers.append({
            'id': customer.id,
            'name': customer.name,
            'contact': customer.contact,
            'location': customer.location
        })
        
        # Create equipment
        equipment = Equipment(customer.id, "CAT 789D", "SN123456")
        db.equipment.append({
            'id': equipment.id,
            'customer_id': equipment.customer_id,
            'model': equipment.model,
            'serial_number': equipment.serial_number,
            'service_history': equipment.service_history
        })
        
        # Create technician
        technician = Technician("Juan Perez", "Engine Specialist", "juan@trackdiesel.com")
        db.technicians.append({
            'id': technician.id,
            'name': technician.name,
            'specialization': technician.specialization,
            'contact': technician.contact,
            'availability': technician.availability
        })
        
        # Create service request
        service = scheduler.create_service_request(
            customer_id=customer.id,
            equipment_id=equipment.id,
            issue_description="Engine overheating",
            service_type=ServiceType.ON_SITE,
            preferred_date=datetime.date.today() + datetime.timedelta(days=2)
        )
        
        if service:
            print(f"Created service request: {service.id}")
            
            # Assign technician
            if scheduler.assign_technician(service.id, technician.id):
                print(f"
