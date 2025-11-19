"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://www.limpiezadetuboscostablanca.net
Prompt: Develop a code example that implements a scheduling system for plumbing services, focusing on urgent requests similar to those handled by Limpieza de Tubos Costablanca.
Generated: DETERMINISTIC_ff273ce22379495c
Batch ID: 20250612_161403
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
from datetime import datetime, timedelta
import random

class PlumbingServiceRequest:
    """
    Represents a plumbing service request.
    """

    def __init__(self, customer_name, address, urgency_level):
        self.request_id = self.generate_request_id()
        self.customer_name = customer_name
        self.address = address
        self.urgency_level = urgency_level  # 1 (highest) to 5 (lowest)
        self.timestamp = datetime.now()

    @staticmethod
    def generate_request_id():
        """Generate a unique request ID."""
        return random.randint(1000, 9999)

class PlumbingServiceScheduler:
    """
    Manages the scheduling of plumbing service requests.
    """

    def __init__(self):
        self.requests = []

    def add_request(self, request):
        """Add a new plumbing service request to the scheduler."""
        if not isinstance(request, PlumbingServiceRequest):
            raise ValueError("Invalid request. Must be an instance of PlumbingServiceRequest.")
        self.requests.append(request)
        self.requests.sort(key=lambda r: r.urgency_level)  # Sort by urgency level

    def schedule_services(self):
        """Schedule services based on urgency."""
        scheduled_services = []
        for request in self.requests:
            scheduled_time = self.calculate_scheduled_time(request.urgency_level)
            scheduled_services.append((request, scheduled_time))
        return scheduled_services

    @staticmethod
    def calculate_scheduled_time(urgency_level):
        """Calculate the scheduled time based on urgency level."""
        if urgency_level == 1:
            return datetime.now() + timedelta(minutes=30)  # Urgent
        elif urgency_level == 2:
            return datetime.now() + timedelta(hours=1)  # High
        elif urgency_level == 3:
            return datetime.now() + timedelta(hours=3)  # Medium
        elif urgency_level == 4:
            return datetime.now() + timedelta(hours=6)  # Low
        elif urgency_level == 5:
            return datetime.now() + timedelta(days=1)  # Not urgent
        else:
            raise ValueError("Urgency level must be between 1 and 5.")

    def display_schedule(self):
        """Display the scheduled services in a readable format."""
        scheduled_services = self.schedule_services()
        for request, scheduled_time in scheduled_services:
            print(f"Request ID: {request.request_id}, Customer: {request.customer_name}, "
                  f"Address: {request.address}, Scheduled Time: {scheduled_time.strftime('%Y-%m-%d %H:%M:%S')}")

# Example usage
if __name__ == "__main__":
    try:
        scheduler = PlumbingServiceScheduler()
        
        # Adding multiple service requests
        scheduler.add_request(PlumbingServiceRequest("John Doe", "123 Elm St", 1))
        scheduler.add_request(PlumbingServiceRequest("Jane Smith", "456 Oak St", 3))
        scheduler.add_request(PlumbingServiceRequest("Bob Johnson", "789 Pine St", 2))
        
        # Display scheduled services
        scheduler.display_schedule()
    except ValueError as ve:
        print(f"Error: {ve}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
```
