"""
Generated Code Metadata:
========================
Original URL: https://wordoflifenw.com
Prompt: Develop a library recommendation for creating a worship service schedule and management system inspired by the ministries offered at Word of Life Northwest.
Generated: DETERMINISTIC_9f64a01eaa132d27
Batch ID: 20250622_210802
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# worship_service_scheduler.py

from datetime import datetime, timedelta
from typing import List, Dict, Optional

class Service:
    """Represents a worship service with a specific date, time, and ministry involved."""
    
    def __init__(self, date: datetime, ministry: str):
        self.date = date
        self.ministry = ministry

    def __repr__(self):
        return f"Service(date={self.date}, ministry='{self.ministry}')"


class WorshipServiceScheduler:
    """Manages a schedule of worship services."""
    
    def __init__(self):
        self.services: List[Service] = []

    def add_service(self, date: datetime, ministry: str) -> None:
        """Adds a new service to the schedule.
        
        Args:
            date (datetime): The date and time of the service.
            ministry (str): The ministry responsible for the service.
        
        Raises:
            ValueError: If the service date is in the past.
        """
        if date < datetime.now():
            raise ValueError("Cannot schedule a service in the past.")
        
        new_service = Service(date, ministry)
        self.services.append(new_service)

    def remove_service(self, date: datetime) -> None:
        """Removes a service from the schedule by date.
        
        Args:
            date (datetime): The date and time of the service to remove.
        
        Raises:
            ValueError: If no service is found for the given date.
        """
        for service in self.services:
            if service.date == date:
                self.services.remove(service)
                return
        raise ValueError("No service found for the specified date.")

    def get_services(self, start_date: Optional[datetime] = None, end_date: Optional[datetime] = None) -> List[Service]:
        """Retrieves a list of services within a specified date range.
        
        Args:
            start_date (Optional[datetime]): The start date for filtering services.
            end_date (Optional[datetime]): The end date for filtering services.
        
        Returns:
            List[Service]: A list of services within the specified date range.
        """
        filtered_services = []
        for service in self.services:
            if (start_date is None or service.date >= start_date) and (end_date is None or service.date <= end_date):
                filtered_services.append(service)
        return filtered_services

    def __repr__(self):
        return f"WorshipServiceScheduler(services={self.services})"


# Example usage
if __name__ == "__main__":
    scheduler = WorshipServiceScheduler()
    
    # Schedule some services
    try:
        scheduler.add_service(datetime(2023, 11, 1, 10, 0), "Youth Ministry")
        scheduler.add_service(datetime(2023, 11, 8, 10, 0), "Worship Team")
        scheduler.add_service(datetime(2023, 11, 15, 10, 0), "Community Outreach")
    except ValueError as e:
        print(f"Error scheduling service: {e}")

    # Retrieve services
    services = scheduler.get_services(datetime(2023, 11, 1), datetime(2023, 11, 30))
    print("Scheduled Services:", services)

    # Remove a service
    try:
        scheduler.remove_service(datetime(2023, 11, 8, 10, 0))
    except ValueError as e:
        print(f"Error removing service: {e}")

    # Final schedule
    print("Final Schedule:", scheduler)
```
