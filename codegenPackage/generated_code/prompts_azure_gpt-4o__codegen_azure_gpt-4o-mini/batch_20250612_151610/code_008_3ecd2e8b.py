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
from typing import List, Optional

class TechnicalAssistanceRequest:
    """Class to represent a technical assistance request for machinery repairs."""
    
    def __init__(self, request_id: int, client_name: str, machine_type: str, 
                 service_type: str, requested_date: datetime.date):
        self.request_id = request_id
        self.client_name = client_name
        self.machine_type = machine_type
        self.service_type = service_type  # 'on-site' or 'workshop'
        self.requested_date = requested_date
        self.status = 'Pending'  # Initial status of the request

    def __str__(self):
        return f"Request ID: {self.request_id}, Client: {self.client_name}, " \
               f"Machine: {self.machine_type}, Service: {self.service_type}, " \
               f"Date: {self.requested_date}, Status: {self.status}"


class TechnicalAssistanceScheduler:
    """Class to manage scheduling of technical assistance requests."""
    
    def __init__(self):
        self.requests: List[TechnicalAssistanceRequest] = []
        self.next_request_id = 1  # To keep track of request IDs

    def add_request(self, client_name: str, machine_type: str, 
                    service_type: str, requested_date: datetime.date) -> TechnicalAssistanceRequest:
        """Add a new technical assistance request."""
        if service_type not in ['on-site', 'workshop']:
            raise ValueError("Service type must be 'on-site' or 'workshop'.")

        request = TechnicalAssistanceRequest(
            request_id=self.next_request_id,
            client_name=client_name,
            machine_type=machine_type,
            service_type=service_type,
            requested_date=requested_date
        )
        self.requests.append(request)
        self.next_request_id += 1
        return request

    def get_requests(self, status: Optional[str] = None) -> List[TechnicalAssistanceRequest]:
        """Retrieve all requests, optionally filtered by status."""
        if status:
            return [request for request in self.requests if request.status == status]
        return self.requests

    def update_request_status(self, request_id: int, new_status: str) -> bool:
        """Update the status of a specific request."""
        for request in self.requests:
            if request.request_id == request_id:
                request.status = new_status
                return True
        return False

    def schedule_service(self, request_id: int) -> bool:
        """Schedule the service for a specific request."""
        if self.update_request_status(request_id, 'Scheduled'):
            # Here you could add additional logic for scheduling (e.g., assigning a technician)
            return True
        return False


# Example usage
if __name__ == "__main__":
    scheduler = TechnicalAssistanceScheduler()

    # Adding a new request
    try:
        request = scheduler.add_request(
            client_name="ABC Corp",
            machine_type="Excavator",
            service_type="on-site",
            requested_date=datetime.date(2023, 10, 15)
        )
        print(f"Added request: {request}")

        # Scheduling the service
        if scheduler.schedule_service(request.request_id):
            print(f"Service scheduled for request ID: {request.request_id}")
        else:
            print(f"Failed to schedule service for request ID: {request.request_id}")

    except ValueError as e:
        print(f"Error: {e}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
```
