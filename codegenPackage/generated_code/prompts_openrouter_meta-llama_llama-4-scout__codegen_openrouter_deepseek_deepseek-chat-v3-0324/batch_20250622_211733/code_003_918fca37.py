"""
Generated Code Metadata:
========================
Original URL: https://starplumbingelectrical.com
Prompt: "Design a system for emergency plumbing services, including 24/7 support and rapid response times, similar to Certified Plumbers Graham, TX's approach."
Generated: DETERMINISTIC_918fca37bd5b7f0a
Batch ID: 20250622_211733
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import datetime
import logging
from enum import Enum
from typing import Optional, List, Dict
from dataclasses import dataclass
from abc import ABC, abstractmethod

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    handlers=[
        logging.FileHandler('plumbing_service.log'),
        logging.StreamHandler()
    ]
)
logger = logging.getLogger(__name__)

class EmergencyLevel(Enum):
    """Enum representing the emergency level of a plumbing issue."""
    LOW = 1
    MEDIUM = 2
    HIGH = 3
    CRITICAL = 4

@dataclass
class Customer:
    """Represents a customer requiring plumbing services."""
    name: str
    phone: str
    address: str
    email: Optional[str] = None

@dataclass
class ServiceRequest:
    """Represents a plumbing service request."""
    customer: Customer
    description: str
    emergency_level: EmergencyLevel
    timestamp: datetime.datetime = datetime.datetime.now()
    assigned_plumber: Optional[str] = None
    is_completed: bool = False

class Plumber:
    """Represents a plumber available for service."""
    def __init__(self, name: str, license_number: str, contact: str, specialties: List[str]):
        self.name = name
        self.license_number = license_number
        self.contact = contact
        self.specialties = specialties
        self.is_available = True

    def __str__(self):
        return f"{self.name} ({self.license_number})"

class NotificationService(ABC):
    """Abstract base class for notification services."""
    @abstractmethod
    def send_notification(self, recipient: str, message: str) -> bool:
        pass

class SMSNotificationService(NotificationService):
    """Concrete implementation of SMS notifications."""
    def send_notification(self, recipient: str, message: str) -> bool:
        try:
            # In a real implementation, this would connect to an SMS gateway
            logger.info(f"SMS sent to {recipient}: {message}")
            return True
        except Exception as e:
            logger.error(f"Failed to send SMS to {recipient}: {e}")
            return False

class EmailNotificationService(NotificationService):
    """Concrete implementation of email notifications."""
    def send_notification(self, recipient: str, message: str) -> bool:
        try:
            # In a real implementation, this would connect to an email service
            logger.info(f"Email sent to {recipient}: {message}")
            return True
        except Exception as e:
            logger.error(f"Failed to send email to {recipient}: {e}")
            return False

class PlumbingService:
    """Main plumbing service system."""
    def __init__(self):
        self.plumbers: List[Plumber] = []
        self.service_requests: List[ServiceRequest] = []
        self.notification_services: Dict[str, NotificationService] = {
            'sms': SMSNotificationService(),
            'email': EmailNotificationService()
        }

    def add_plumber(self, plumber: Plumber) -> None:
        """Add a plumber to the available pool."""
        self.plumbers.append(plumber)
        logger.info(f"Added plumber: {plumber}")

    def create_service_request(self, customer: Customer, description: str, emergency_level: EmergencyLevel) -> ServiceRequest:
        """Create a new service request."""
        request = ServiceRequest(customer, description, emergency_level)
        self.service_requests.append(request)
        logger.info(f"Created service request: {request}")
        return request

    def assign_plumber(self, request: ServiceRequest) -> Optional[Plumber]:
        """Assign an available plumber to a service request."""
        try:
            available_plumbers = [p for p in self.plumbers if p.is_available]
            if not available_plumbers:
                logger.warning("No available plumbers to assign")
                return None

            # Simple assignment logic - in production would be more sophisticated
            plumber = available_plumbers[0]
            plumber.is_available = False
            request.assigned_plumber = plumber.name
            logger.info(f"Assigned plumber {plumber} to request")
            return plumber
        except Exception as e:
            logger.error(f"Error assigning plumber: {e}")
            return None

    def notify_customer(self, request: ServiceRequest, message: str, methods: List[str] = ['sms']) -> bool:
        """Notify the customer using specified methods."""
        success = False
        for method in methods:
            if method in self.notification_services:
                notification_service = self.notification_services[method]
                recipient = request.customer.phone if method == 'sms' else request.customer.email
                if recipient:
                    success = notification_service.send_notification(recipient, message) or success
        return success

    def complete_service_request(self, request: ServiceRequest) -> bool:
        """Mark a service request as completed."""
        try:
            request.is_completed = True
            for plumber in self.plumbers:
                if plumber.name == request.assigned_plumber:
                    plumber.is_available = True
                    break
            logger.info(f"Completed service request: {request}")
            return True
        except Exception as e:
            logger.error(f"Error completing service request: {e}")
            return False

    def get_active_requests(self) -> List[ServiceRequest]:
        """Get all active (incomplete) service requests."""
        return [r for r in self.service_requests if not r.is_completed]

    def get_available_plumbers(self) -> List[Plumber]:
        """Get all available plumbers."""
        return [p for p in self.plumbers if p.is_available]

# Example usage
if __name__ == "__main__":
    service = PlumbingService()

    # Add some plumbers
    service.add_plumber(Plumber(
        name="John Doe",
        license_number="TX12345",
        contact="555-1234",
        specialties=["leak repair", "pipe installation"]
    ))
    service.add_plumber(Plumber(
        name="Jane Smith",
        license_number="TX67890",
        contact="555-5678",
        specialties=["water heater", "sewer line"]
    ))

    # Create a customer and service request
    customer = Customer(
        name="Bob Johnson",
        phone="555-9876",
        address="123 Main St, Graham, TX",
        email="bob@example.com"
    )
    request = service.create_service_request(
        customer=customer,
        description="Burst pipe in bathroom",
        emergency_level=EmergencyLevel.CRITICAL
    )

    # Assign a plumber and notify customer
    plumber = service.assign_plumber(request)
    if plumber:
        service.notify_customer(
            request,
            f"Emergency plumbing service assigned. Plumber: {plumber.name}, Contact: {plumber.contact}",
            methods=['sms', 'email']
        )

    # Complete the request
    service.complete_service_request(request)
```
