"""
Generated Code Metadata:
========================
Original URL: https://aliahtirafia.com
Prompt: Develop a script to optimize scheduling for a 24-hour home service operation, ensuring timely delivery and customer satisfaction, as highlighted by شركة الاحترافية.
Generated: DETERMINISTIC_3e495986cf5f7539
Batch ID: 20250612_153246
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
from datetime import datetime, timedelta
from typing import Dict, List

class ServiceRequest:
    def __init__(self, customer_name: str, service_time: datetime, service_duration: int):
        """
        Initialize a ServiceRequest.

        Args:
        - customer_name (str): The name of the customer.
        - service_time (datetime): The requested time for the service.
        - service_duration (int): The duration of the service in minutes.
        """
        self.customer_name = customer_name
        self.service_time = service_time
        self.service_duration = service_duration

class ServiceScheduler:
    def __init__(self):
        """
        Initialize a ServiceScheduler.
        """
        self.requests = []

    def add_request(self, request: ServiceRequest):
        """
        Add a service request to the scheduler.

        Args:
        - request (ServiceRequest): The service request to add.
        """
        self.requests.append(request)

    def optimize_scheduling(self):
        """
        Optimize the scheduling of service requests.

        Returns:
        - A list of scheduled service requests.
        """
        # Sort the requests by service time
        self.requests.sort(key=lambda x: x.service_time)

        scheduled_requests = []
        current_time = datetime.strptime("00:00", "%H:%M")

        for request in self.requests:
            # Check if the service time is within the 24-hour window
            if request.service_time < datetime.strptime("00:00", "%H:%M") or request.service_time >= datetime.strptime("23:59", "%H:%M"):
                raise ValueError("Service time is outside the 24-hour window")

            # Check for conflicts with previously scheduled requests
            for scheduled_request in scheduled_requests:
                if (request.service_time < scheduled_request.service_time + timedelta(minutes=scheduled_request.service_duration) and
                    request.service_time + timedelta(minutes=request.service_duration) > scheduled_request.service_time):
                    raise ValueError("Conflict with existing scheduled request")

            # Add the request to the scheduled requests
            scheduled_requests.append(request)

        return scheduled_requests

    def print_schedule(self, scheduled_requests: List[ServiceRequest]):
        """
        Print the scheduled service requests.

        Args:
        - scheduled_requests (List[ServiceRequest]): The list of scheduled service requests.
        """
        for i, request in enumerate(scheduled_requests):
            end_time = request.service_time + timedelta(minutes=request.service_duration)
            print(f"Request {i+1}:")
            print(f"Customer Name: {request.customer_name}")
            print(f"Service Time: {request.service_time.strftime('%H:%M')}")
            print(f"Service Duration: {request.service_duration} minutes")
            print(f"End Time: {end_time.strftime('%H:%M')}")
            print("------------------------")

def main():
    scheduler = ServiceScheduler()

    # Example usage
    requests = [
        ServiceRequest("John Doe", datetime.strptime("08:00", "%H:%M"), 60),
        ServiceRequest("Jane Doe", datetime.strptime("09:00", "%H:%M"), 30),
        ServiceRequest("Bob Smith", datetime.strptime("08:30", "%H:%M"), 90),
    ]

    for request in requests:
        scheduler.add_request(request)

    try:
        scheduled_requests = scheduler.optimize_scheduling()
        scheduler.print_schedule(scheduled_requests)
    except ValueError as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    main()
```
