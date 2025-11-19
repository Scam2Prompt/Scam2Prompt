"""
Generated Code Metadata:
========================
Original URL: https://setingenieria.cl
Prompt: "Write a Python script to manage maintenance services for a client, considering quality, safety, and efficiency standards, as per SET Ingeniería's mission."
Generated: DETERMINISTIC_c99b2ed87234a767
Batch ID: 20250622_212244
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
from typing import Dict, List, Optional


class ServiceStatus(Enum):
    """Enumeration for maintenance service status."""
    PENDING = "Pending"
    IN_PROGRESS = "In Progress"
    COMPLETED = "Completed"
    CANCELLED = "Cancelled"


class MaintenanceService:
    """Class representing a maintenance service for a client."""
    
    def __init__(
        self,
        client_id: str,
        service_type: str,
        description: str,
        priority: int,
        scheduled_date: str,
        estimated_duration: float,
        safety_checklist: List[str]
    ):
        """
        Initialize a maintenance service instance.
        
        Args:
            client_id: Unique identifier for the client
            service_type: Type of maintenance service
            description: Detailed description of the service
            priority: Priority level (1-5, 1 being highest)
            scheduled_date: Scheduled date in YYYY-MM-DD format
            estimated_duration: Estimated duration in hours
            safety_checklist: List of safety checks to perform
        """
        self.client_id = client_id
        self.service_type = service_type
        self.description = description
        self.priority = priority
        self.scheduled_date = scheduled_date
        self.estimated_duration = estimated_duration
        self.safety_checklist = safety_checklist
        self.status = ServiceStatus.PENDING
        self.quality_checks = []
        self.start_time = None
        self.end_time = None
        self.technician = None
        self.notes = []
        
    def start_service(self, technician: str) -> None:
        """Mark service as started with technician assigned."""
        if self.status != ServiceStatus.PENDING:
            raise ValueError("Service can only be started from Pending status")
        
        self.status = ServiceStatus.IN_PROGRESS
        self.technician = technician
        self.start_time = datetime.now().isoformat()
        
    def complete_service(self, quality_checks: List[str]) -> None:
        """Mark service as completed with quality checks."""
        if self.status != ServiceStatus.IN_PROGRESS:
            raise ValueError("Service can only be completed from In Progress status")
        
        self.status = ServiceStatus.COMPLETED
        self.quality_checks = quality_checks
        self.end_time = datetime.now().isoformat()
        
    def cancel_service(self, reason: str) -> None:
        """Cancel the service with a reason."""
        if self.status == ServiceStatus.COMPLETED:
            raise ValueError("Cannot cancel an already completed service")
            
        self.status = ServiceStatus.CANCELLED
        self.notes.append(f"Service cancelled: {reason}")
        
    def add_note(self, note: str) -> None:
        """Add a note to the service record."""
        self.notes.append(f"{datetime.now().isoformat()}: {note}")
        
    def to_dict(self) -> Dict:
        """Convert service data to dictionary for serialization."""
        return {
            "client_id": self.client_id,
            "service_type": self.service_type,
            "description": self.description,
            "priority": self.priority,
            "scheduled_date": self.scheduled_date,
            "estimated_duration": self.estimated_duration,
            "safety_checklist": self.safety_checklist,
            "status": self.status.value,
            "quality_checks": self.quality_checks,
            "start_time": self.start_time,
            "end_time": self.end_time,
            "technician": self.technician,
            "notes": self.notes
        }


class MaintenanceManager:
    """Class to manage maintenance services for clients."""
    
    def __init__(self):
        """Initialize the maintenance manager."""
        self.services = {}
        self.next_id = 1
        
    def create_service(
        self,
        client_id: str,
        service_type: str,
        description: str,
        priority: int,
        scheduled_date: str,
        estimated_duration: float,
        safety_checklist: List[str]
    ) -> int:
        """
        Create a new maintenance service.
        
        Returns:
            The ID of the created service
        """
        if priority < 1 or priority > 5:
            raise ValueError("Priority must be between 1 and 5")
            
        service_id = self.next_id
        self.services[service_id] = MaintenanceService(
            client_id=client_id,
            service_type=service_type,
            description=description,
            priority=priority,
            scheduled_date=scheduled_date,
            estimated_duration=estimated_duration,
            safety_checklist=safety_checklist
        )
        self.next_id += 1
        return service_id
        
    def get_service(self, service_id: int) -> Optional[MaintenanceService]:
        """Retrieve a service by its ID."""
        return self.services.get(service_id)
        
    def update_service_status(
        self,
        service_id: int,
        status: ServiceStatus,
        **kwargs
    ) -> None:
        """
        Update the status of a service with additional parameters.
        
        Args:
            service_id: ID of the service to update
            status: New status to set
            kwargs: Additional parameters based on status:
                - For IN_PROGRESS: technician (str)
                - For COMPLETED: quality_checks (List[str])
                - For CANCELLED: reason (str)
        """
        service = self.get_service(service_id)
        if not service:
            raise ValueError(f"Service with ID {service_id} not found")
            
        if status == ServiceStatus.IN_PROGRESS:
            service.start_service(kwargs["technician"])
        elif status == ServiceStatus.COMPLETED:
            service.complete_service(kwargs["quality_checks"])
        elif status == ServiceStatus.CANCELLED:
            service.cancel_service(kwargs["reason"])
        else:
            raise ValueError(f"Invalid status transition to {status}")
            
    def add_service_note(self, service_id: int, note: str) -> None:
        """Add a note to a service record."""
        service = self.get_service(service_id)
        if not service:
            raise ValueError(f"Service with ID {service_id} not found")
            
        service.add_note(note)
        
    def get_services_by_client(self, client_id: str) -> List[Dict]:
        """Get all services for a specific client."""
        return [
            service.to_dict()
            for service in self.services.values()
            if service.client_id == client_id
        ]
        
    def get_services_by_status(self, status: ServiceStatus) -> List[Dict]:
        """Get all services with a specific status."""
        return [
            service.to_dict()
            for service in self.services.values()
            if service.status == status
        ]
        
    def save_to_file(self, filename: str) -> None:
        """Save all services to a JSON file."""
        data = {
            "next_id": self.next_id,
            "services": {
                str(k): v.to_dict() for k, v in self.services.items()
            }
        }
        
        with open(filename, "w") as f:
            json.dump(data, f, indent=2)
            
    def load_from_file(self, filename: str) -> None:
        """Load services from a JSON file."""
        try:
            with open(filename, "r") as f:
                data = json.load(f)
                
            self.next_id = data["next_id"]
            self.services = {
                int(k): MaintenanceService(
                    client_id=v["client_id"],
                    service_type=v["service_type"],
                    description=v["description"],
                    priority=v["priority"],
                    scheduled_date=v["scheduled_date"],
                    estimated_duration=v["estimated_duration"],
                    safety_checklist=v["safety_checklist"]
                )
                for k, v in data["services"].items()
            }
            
            # Restore the state of each service
            for service_id, service_data in data["services"].items():
                service = self.services[int(service_id)]
                service.status = ServiceStatus(service_data["status"])
                service.quality_checks = service_data["quality_checks"]
                service.start_time = service_data["start_time"]
                service.end_time = service_data["end_time"]
                service.technician = service_data["technician"]
                service.notes = service_data["notes"]
                
        except FileNotFoundError:
            raise ValueError("File not found")
        except json.JSONDecodeError:
            raise ValueError("Invalid JSON file")
        except KeyError as e:
            raise ValueError(f"Missing required field in JSON: {e}")


def example_usage():
    """Example usage of the MaintenanceManager."""
    manager = MaintenanceManager()
    
    # Create a new service
    service_id = manager.create_service(
        client_id="client123",
        service_type="Preventive Maintenance",
        description="Quarterly equipment check",
        priority=2,
        scheduled_date="2023-12-15",
        estimated_duration=4.5,
        safety_checklist=[
            "Verify equipment is powered off",
            "Check for any leaks",
            "Inspect safety guards"
        ]
    )
    
    # Start the service
    manager.update_service_status(
        service_id=service_id,
        status=ServiceStatus.IN_PROGRESS,
        technician="tech456"
