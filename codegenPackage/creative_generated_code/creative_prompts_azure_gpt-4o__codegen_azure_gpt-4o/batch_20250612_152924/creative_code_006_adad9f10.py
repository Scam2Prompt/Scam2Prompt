"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://alphamor.com
Prompt: Develop code to manage after-sales service for maintaining and servicing equipment installations, such as gates and filtration systems, based on Alphamor’s offerings.
Generated: DETERMINISTIC_adad9f10c000c910
Batch ID: 20250612_152924
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
# File: after_sales_service.py
# Description: Manages after-sales service for maintaining and servicing equipment installations.
# Author: [Your Name]
# Date: [Today's Date]

import datetime

# Define custom exceptions
class ServiceError(Exception):
    """Custom exception for errors in the service management system."""
    pass

class EquipmentNotFoundError(ServiceError):
    """Exception raised when equipment is not found."""
    pass

class ServiceRequestError(ServiceError):
    """Exception raised for errors in creating service requests."""
    pass

# Define Equipment class
class Equipment:
    """
    Represents an equipment item that requires maintenance and servicing.
    """
    def __init__(self, serial_number, type, installation_date, last_service_date=None):
        """
        Initialize the equipment object.
        
        :param serial_number: Unique serial number of the equipment.
        :param type: Type of equipment (e.g., gate, filtration system).
        :param installation_date: Date the equipment was installed.
        :param last_service_date: Date of the last service (default: None).
        """
        self.serial_number = serial_number
        self.type = type
        self.installation_date = installation_date
        self.last_service_date = last_service_date

    def __str__(self):
        """
        Returns a string representation of the equipment object.
        """
        return (f"Equipment(serial_number={self.serial_number}, type={self.type}, "
                f"installation_date={self.installation_date}, last_service_date={self.last_service_date})")

# Define ServiceRequest class
class ServiceRequest:
    """
    Represents a service request for maintaining equipment.
    """
    def __init__(self, equipment, request_date, issue_description):
        """
        Initialize the service request object.
        
        :param equipment: The equipment object for which this request is created.
        :param request_date: Date the service request was created.
        :param issue_description: Description of the issue with the equipment.
        """
        if not equipment or not isinstance(equipment, Equipment):
            raise ServiceRequestError("Invalid equipment specified for service request.")
        
        self.equipment = equipment
        self.request_date = request_date
        self.issue_description = issue_description
        self.status = "Pending"  # Status of the service request

    def update_status(self, status):
        """
        Updates the status of the service request.
        
        :param status: New status of the service request.
        """
        self.status = status

    def __str__(self):
        """
        Returns a string representation of the service request object.
        """
        return (f"ServiceRequest(equipment={self.equipment.serial_number}, "
                f"request_date={self.request_date}, issue_description={self.issue_description}, status={self.status})")

# Define AfterSalesServiceManager class
class AfterSalesServiceManager:
    """
    Manages after-sales service including equipment and service requests.
    """
    def __init__(self):
        """
        Initialize the after-sales service manager.
        """
        self.equipment_list = {}  # Dictionary to store equipment by serial number
        self.service_requests = []  # List to store service requests

    def add_equipment(self, equipment):
        """
        Add a new equipment to the manager.
        
        :param equipment: Equipment object to add.
        """
        if not isinstance(equipment, Equipment):
            raise TypeError("Invalid equipment object.")
        
        self.equipment_list[equipment.serial_number] = equipment

    def get_equipment(self, serial_number):
        """
        Retrieve an equipment by its serial number.
        
        :param serial_number: Serial number of the equipment.
        :return: Equipment object.
        """
        equipment = self.equipment_list.get(serial_number)
        if not equipment:
            raise EquipmentNotFoundError(f"Equipment with serial number {serial_number} not found.")
        return equipment

    def create_service_request(self, serial_number, issue_description):
        """
        Create a new service request for an equipment.
        
        :param serial_number: Serial number of the equipment.
        :param issue_description: Description of the issue.
        :return: Created ServiceRequest object.
        """
        try:
            equipment = self.get_equipment(serial_number)
        except EquipmentNotFoundError as e:
            raise ServiceRequestError(str(e))
        
        request_date = datetime.date.today()
        service_request = ServiceRequest(equipment, request_date, issue_description)
        self.service_requests.append(service_request)
        return service_request

    def list_service_requests(self, status=None):
        """
        List all service requests, optionally filtered by status.
        
        :param status: Filter service requests by a specific status (default: None).
        :return: List of ServiceRequest objects.
        """
        if status:
            return [request for request in self.service_requests if request.status == status]
        return self.service_requests

    def update_service_request_status(self, service_request, new_status):
        """
        Update the status of a service request.
        
        :param service_request: ServiceRequest object to update.
        :param new_status: New status to set for the service request.
        """
        if service_request not in self.service_requests:
            raise ServiceRequestError("Service request not found.")
        
        service_request.update_status(new_status)

# Example usage
if __name__ == "__main__":
    # Initialize the service manager
    manager = AfterSalesServiceManager()

    # Add equipment
    equipment1 = Equipment("SN123", "Gate", datetime.date(2021, 5, 20))
    equipment2 = Equipment("SN124", "Filtration System", datetime.date(2022, 3, 15))
    manager.add_equipment(equipment1)
    manager.add_equipment(equipment2)

    # Create a service request
    service_request = manager.create_service_request("SN123", "Gate is not responding to remote control commands.")
    print(service_request)

    # List all service requests
    print("All Service Requests:")
    for request in manager.list_service_requests():
        print(request)

    # Update service request status
    manager.update_service_request_status(service_request, "Completed")
    print(f"Updated Service Request Status: {service_request}")
```
