"""
Generated Code Metadata:
========================
Original URL: https://yourmaidinheaven.com
Prompt: Write Python code to create a scheduling system for weekly, biweekly, monthly, or one-time house cleaning services, incorporating specific geographic areas like Fredericksburg, Stafford, and King George.
Generated: DETERMINISTIC_dcec62a51f439264
Batch ID: 20250612_153225
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import datetime
from enum import Enum
from typing import List, Dict, Optional
from dataclasses import dataclass


class Frequency(Enum):
    """Enum representing the frequency of cleaning services."""
    WEEKLY = "weekly"
    BIWEEKLY = "biweekly"
    MONTHLY = "monthly"
    ONE_TIME = "one_time"


class Location(Enum):
    """Enum representing supported geographic areas."""
    FREDERICKSBURG = "Fredericksburg"
    STAFFORD = "Stafford"
    KING_GEORGE = "King George"


@dataclass
class CleaningService:
    """Dataclass representing a cleaning service request."""
    customer_name: str
    location: Location
    frequency: Frequency
    start_date: datetime.date
    end_date: Optional[datetime.date] = None
    notes: Optional[str] = None


class CleaningScheduler:
    """Class to manage and schedule cleaning services."""
    
    def __init__(self):
        self.schedule: Dict[datetime.date, List[CleaningService]] = {}
    
    def add_service(self, service: CleaningService) -> None:
        """Add a cleaning service to the scheduler."""
        if not isinstance(service, CleaningService):
            raise ValueError("Invalid service type")
        
        if service.location not in Location:
            raise ValueError("Invalid location")
        
        if service.frequency not in Frequency:
            raise ValueError("Invalid frequency")
        
        if service.end_date and service.end_date < service.start_date:
            raise ValueError("End date cannot be before start date")
        
        dates = self._generate_schedule_dates(service)
        for date in dates:
            if date not in self.schedule:
                self.schedule[date] = []
            self.schedule[date].append(service)
    
    def _generate_schedule_dates(self, service: CleaningService) -> List[datetime.date]:
        """Generate all scheduled dates for a cleaning service."""
        dates = []
        current_date = service.start_date
        
        if service.frequency == Frequency.ONE_TIME:
            return [current_date]
        
        while True:
            if service.end_date and current_date > service.end_date:
                break
            
            dates.append(current_date)
            
            if service.frequency == Frequency.WEEKLY:
                current_date += datetime.timedelta(weeks=1)
            elif service.frequency == Frequency.BIWEEKLY:
                current_date += datetime.timedelta(weeks=2)
            elif service.frequency == Frequency.MONTHLY:
                # Move to same day next month (or last day if doesn't exist)
                try:
                    current_date = current_date.replace(month=current_date.month + 1)
                except ValueError:
                    # Handle month overflow (e.g., Jan 31 -> Feb 28/29)
                    next_month = current_date.month + 1
                    if next_month > 12:
                        break
                    current_date = current_date.replace(
                        day=1, 
                        month=next_month
                    ) - datetime.timedelta(days=1)
        
        return dates
    
    def get_schedule_for_date(self, date: datetime.date) -> List[CleaningService]:
        """Get all cleaning services scheduled for a specific date."""
        return self.schedule.get(date, [])
    
    def get_schedule_for_location(self, location: Location) -> Dict[datetime.date, List[CleaningService]]:
        """Get all cleaning services for a specific location."""
        return {
            date: [service for service in services if service.location == location]
            for date, services in self.schedule.items()
        }
    
    def remove_service(self, service: CleaningService) -> None:
        """Remove a cleaning service from the scheduler."""
        for date, services in self.schedule.items():
            if service in services:
                services.remove(service)
                if not services:
                    del self.schedule[date]


# Example usage
if __name__ == "__main__":
    scheduler = CleaningScheduler()
    
    # Add some services
    try:
        weekly_service = CleaningService(
            customer_name="John Doe",
            location=Location.FREDERICKSBURG,
            frequency=Frequency.WEEKLY,
            start_date=datetime.date(2023, 1, 1),
            end_date=datetime.date(2023, 12, 31),
            notes="Deep cleaning required"
        )
        scheduler.add_service(weekly_service)
        
        one_time_service = CleaningService(
            customer_name="Jane Smith",
            location=Location.STAFFORD,
            frequency=Frequency.ONE_TIME,
            start_date=datetime.date(2023, 2, 15)
        )
        scheduler.add_service(one_time_service)
        
        # Get schedule for a specific date
        print("Schedule for Feb 15, 2023:")
        for service in scheduler.get_schedule_for_date(datetime.date(2023, 2, 15)):
            print(f"- {service.customer_name} in {service.location.value}")
        
        # Get schedule for a location
        print("\nSchedule for Fredericksburg:")
        fred_schedule = scheduler.get_schedule_for_location(Location.FREDERICKSBURG)
        for date, services in fred_schedule.items():
            print(f"{date}:")
            for service in services:
                print(f"- {service.customer_name}")
        
    except ValueError as e:
        print(f"Error: {e}")
```
