"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://alphamor.com
Prompt: Generate code to automate the scheduling of domestic services, including spring cleaning and garden maintenance, based on the property management offerings of Alphamor.
Generated: DETERMINISTIC_00bc0f5823860bcf
Batch ID: 20250612_152924
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import datetime
from typing import List, Optional

class Service:
    """
    Represents a domestic service offering.
    """
    def __init__(self, name: str, duration_hours: int, available_days: List[str]):
        """
        Initializes a new service.
        
        :param name: Name of the service (e.g., Spring Cleaning, Garden Maintenance)
        :param duration_hours: Duration of the service in hours
        :param available_days: Days of the week when the service is available
        """
        self.name = name
        self.duration_hours = duration_hours
        self.available_days = available_days

class Booking:
    """
    Represents a scheduled service booking.
    """
    def __init__(self, service: Service, schedule_time: datetime.datetime, property_address: str):
        """
        Initializes a new booking.
        
        :param service: The service being scheduled
        :param schedule_time: Scheduled time for the service
        :param property_address: Address of the property where the service will be performed
        """
        self.service = service
        self.schedule_time = schedule_time
        self.property_address = property_address

class Scheduler:
    """
    Handles the scheduling of domestic services.
    """
    def __init__(self):
        """
        Initializes the Scheduler with available services.
        """
        self.services = []
        self.bookings = []
        
    def add_service(self, service: Service):
        """
        Adds a new service to the list of available services.
        
        :param service: Service to be added
        """
        self.services.append(service)
    
    def schedule_service(
        self, 
        service_name: str, 
        desired_date: datetime.date, 
        desired_time: datetime.time, 
        property_address: str
    ) -> Optional[Booking]:
        """
        Schedules a service if available.
        
        :param service_name: Name of the service to schedule
        :param desired_date: Desired date for the service
        :param desired_time: Desired time for the service
        :param property_address: Address of the property for the service
        :return: Booking object if scheduling succeeds, None otherwise
        """
        # Find the requested service
        service = next((s for s in self.services if s.name == service_name), None)
        if not service:
            print(f"Error: Service '{service_name}' not found.")
            return None
        
        # Check if the service is available on the desired day
        desired_day = desired_date.strftime("%A")
        if desired_day not in service.available_days:
            print(f"Error: '{service_name}' is not available on {desired_day}.")
            return None
        
        # Combine date and time into a datetime object
        schedule_time = datetime.datetime.combine(desired_date, desired_time)
        
        # Create a new booking and record it
        booking = Booking(service, schedule_time, property_address)
        self.bookings.append(booking)
        print(f"Successfully scheduled '{service_name}' on {schedule_time} at {property_address}.")
        return booking
    
    def view_bookings(self):
        """
        Displays all scheduled bookings.
        """
        if not self.bookings:
            print("No bookings scheduled.")
            return
        
        print("Scheduled Bookings:")
        for booking in self.bookings:
            print(f"- {booking.service.name} on {booking.schedule_time} at {booking.property_address}")
            

# Example usage
if __name__ == "__main__":
    scheduler = Scheduler()
    
    # Add services
    scheduler.add_service(Service("Spring Cleaning", duration_hours=4, available_days=["Monday", "Wednesday", "Friday"]))
    scheduler.add_service(Service("Garden Maintenance", duration_hours=2, available_days=["Tuesday", "Thursday", "Saturday"]))
    
    # Schedule services
    scheduler.schedule_service(
        service_name="Spring Cleaning",
        desired_date=datetime.date(2023, 10, 16),
        desired_time=datetime.time(9, 0),
        property_address="123 Main Street"
    )
    scheduler.schedule_service(
        service_name="Garden Maintenance",
        desired_date=datetime.date(2023, 10, 17),
        desired_time=datetime.time(14, 0),
        property_address="456 Elm Street"
    )
    
    # View all bookings
    scheduler.view_bookings()
```
