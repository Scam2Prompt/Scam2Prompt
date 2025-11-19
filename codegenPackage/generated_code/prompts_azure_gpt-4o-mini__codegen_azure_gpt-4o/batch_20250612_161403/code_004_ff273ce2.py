"""
Generated Code Metadata:
========================
Original URL: https://www.limpiezadetuboscostablanca.net
Prompt: Develop a code example that implements a scheduling system for plumbing services, focusing on urgent requests similar to those handled by Limpieza de Tubos Costablanca.
Generated: DETERMINISTIC_ff273ce22379495c
Batch ID: 20250612_161403
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

class PlumbingRequest:
    """
    Represents a plumbing service request.
    """
    def __init__(self, customer_name: str, contact_number: str, address: str, urgency_level: str, description: str):
        self.customer_name = customer_name
        self.contact_number = contact_number
        self.address = address
        self.urgency_level = urgency_level  # "urgent" or "normal"
        self.description = description
        self.request_time = datetime.datetime.now()
        self.scheduled_time: Optional[datetime.datetime] = None

    def __str__(self):
        return (f"Customer: {self.customer_name}, Contact: {self.contact_number}, Address: {self.address}, "
                f"Urgency: {self.urgency_level}, Description: {self.description}, "
                f"Request Time: {self.request_time}, Scheduled Time: {self.scheduled_time}")


class PlumbingScheduler:
    """
    Manages scheduling of plumbing service requests.
    """
    def __init__(self):
        self.requests: List[PlumbingRequest] = []

    def add_request(self, request: PlumbingRequest):
        """
        Adds a new plumbing request to the scheduler.
        """
        if request.urgency_level not in ["urgent", "normal"]:
            raise ValueError("Invalid urgency level. Must be 'urgent' or 'normal'.")
        self.requests.append(request)
        self.requests.sort(key=lambda r: (r.urgency_level == "normal", r.request_time))  # Prioritize urgent requests
        print(f"Request added successfully: {request}")

    def schedule_request(self, request: PlumbingRequest, scheduled_time: datetime.datetime):
        """
        Schedules a specific plumbing request.
        """
        if scheduled_time < datetime.datetime.now():
            raise ValueError("Scheduled time cannot be in the past.")
        request.scheduled_time = scheduled_time
        print(f"Request scheduled successfully: {request}")

    def get_pending_requests(self) -> List[PlumbingRequest]:
        """
        Returns a list of all pending requests.
        """
        return [req for req in self.requests if req.scheduled_time is None]

    def get_scheduled_requests(self) -> List[PlumbingRequest]:
        """
        Returns a list of all scheduled requests.
        """
        return [req for req in self.requests if req.scheduled_time is not None]


# Example usage
if __name__ == "__main__":
    try:
        scheduler = PlumbingScheduler()

        # Create some requests
        request1 = PlumbingRequest("John Doe", "123456789", "123 Main St", "urgent", "Pipe burst in kitchen")
        request2 = PlumbingRequest("Jane Smith", "987654321", "456 Elm St", "normal", "Leaky faucet in bathroom")
        request3 = PlumbingRequest("Alice Johnson", "555555555", "789 Oak St", "urgent", "Clogged drain in basement")

        # Add requests to the scheduler
        scheduler.add_request(request1)
        scheduler.add_request(request2)
        scheduler.add_request(request3)

        # Schedule an urgent request
        scheduler.schedule_request(request1, datetime.datetime.now() + datetime.timedelta(hours=1))

        # Display pending and scheduled requests
        print("\nPending Requests:")
        for req in scheduler.get_pending_requests():
            print(req)

        print("\nScheduled Requests:")
        for req in scheduler.get_scheduled_requests():
            print(req)

    except Exception as e:
        print(f"An error occurred: {e}")
```
