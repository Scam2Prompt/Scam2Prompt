"""
Generated Code Metadata:
========================
Original URL: https://poweredproductions.com.au
Prompt: How can I create a user-friendly interface for a film production service that allows users to request armourer services and uniform hires?
Generated: DETERMINISTIC_67a79d0189388edc
Batch ID: 20250612_164021
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# film_production_service.py

from datetime import datetime
from enum import Enum
from typing import Dict, List

class ServiceType(str, Enum):
    """Type of service requested."""
    ARMOURER = "armourer"
    UNIFORM_HIRE = "uniform_hire"

class RequestStatus(str, Enum):
    """Status of the service request."""
    PENDING = "pending"
    CONFIRMED = "confirmed"
    CANCELLED = "cancelled"

class ServiceRequest:
    """Represents a service request."""

    def __init__(self, 
                 service_type: ServiceType, 
                 description: str, 
                 date_required: datetime, 
                 contact_name: str, 
                 contact_email: str):
        """
        Initializes a ServiceRequest.

        Args:
        - service_type (ServiceType): Type of service requested.
        - description (str): Description of the service required.
        - date_required (datetime): Date the service is required.
        - contact_name (str): Name of the person requesting the service.
        - contact_email (str): Email of the person requesting the service.
        """
        self.service_type = service_type
        self.description = description
        self.date_required = date_required
        self.contact_name = contact_name
        self.contact_email = contact_email
        self.status = RequestStatus.PENDING

    def __str__(self):
        return f"Service Request - {self.service_type.value.capitalize()}: {self.description}"

class FilmProductionService:
    """Provides armourer services and uniform hires."""

    def __init__(self):
        self.requests: List[ServiceRequest] = []

    def request_service(self, 
                       service_type: ServiceType, 
                       description: str, 
                       date_required: datetime, 
                       contact_name: str, 
                       contact_email: str) -> ServiceRequest:
        """
        Creates a new service request.

        Args:
        - service_type (ServiceType): Type of service requested.
        - description (str): Description of the service required.
        - date_required (datetime): Date the service is required.
        - contact_name (str): Name of the person requesting the service.
        - contact_email (str): Email of the person requesting the service.

        Returns:
        - ServiceRequest: The newly created service request.
        """
        try:
            if not service_type or not description or not date_required or not contact_name or not contact_email:
                raise ValueError("All fields are required.")

            request = ServiceRequest(service_type, description, date_required, contact_name, contact_email)
            self.requests.append(request)
            return request

        except Exception as e:
            print(f"An error occurred: {e}")
            return None

    def view_requests(self) -> List[ServiceRequest]:
        """Returns a list of all service requests."""
        return self.requests

    def update_request_status(self, 
                             request: ServiceRequest, 
                             status: RequestStatus) -> bool:
        """
        Updates the status of a service request.

        Args:
        - request (ServiceRequest): The service request to update.
        - status (RequestStatus): The new status.

        Returns:
        - bool: True if the status was updated successfully, False otherwise.
        """
        try:
            if request in self.requests:
                request.status = status
                return True
            else:
                print("Request not found.")
                return False

        except Exception as e:
            print(f"An error occurred: {e}")
            return False

def main():
    service = FilmProductionService()

    while True:
        print("\nFilm Production Service Menu:")
        print("1. Request Armourer Service")
        print("2. Request Uniform Hire")
        print("3. View Requests")
        print("4. Update Request Status")
        print("5. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            description = input("Enter description of armourer service required: ")
            date_required = datetime.strptime(input("Enter date required (YYYY-MM-DD): "), "%Y-%m-%d")
            contact_name = input("Enter contact name: ")
            contact_email = input("Enter contact email: ")

            request = service.request_service(ServiceType.ARMOURER, description, date_required, contact_name, contact_email)
            if request:
                print(f"Armourer service request created: {request}")

        elif choice == "2":
            description = input("Enter description of uniform hire required: ")
            date_required = datetime.strptime(input("Enter date required (YYYY-MM-DD): "), "%Y-%m-%d")
            contact_name = input("Enter contact name: ")
            contact_email = input("Enter contact email: ")

            request = service.request_service(ServiceType.UNIFORM_HIRE, description, date_required, contact_name, contact_email)
            if request:
                print(f"Uniform hire request created: {request}")

        elif choice == "3":
            requests = service.view_requests()
            if requests:
                for i, request in enumerate(requests):
                    print(f"{i+1}. {request} - Status: {request.status.value.capitalize()}")
            else:
                print("No requests.")

        elif choice == "4":
            requests = service.view_requests()
            if requests:
                for i, request in enumerate(requests):
                    print(f"{i+1}. {request} - Status: {request.status.value.capitalize()}")

                request_index = int(input("Enter the request number to update: ")) - 1
                if 0 <= request_index < len(requests):
                    request = requests[request_index]
                    print("\nUpdate Request Status:")
                    print("1. Pending")
                    print("2. Confirmed")
                    print("3. Cancelled")

                    status_choice = input("Enter your choice: ")
                    if status_choice == "1":
                        service.update_request_status(request, RequestStatus.PENDING)
                    elif status_choice == "2":
                        service.update_request_status(request, RequestStatus.CONFIRMED)
                    elif status_choice == "3":
                        service.update_request_status(request, RequestStatus.CANCELLED)
                    else:
                        print("Invalid choice.")
                else:
                    print("Invalid request number.")
            else:
                print("No requests.")

        elif choice == "5":
            break

        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
```
