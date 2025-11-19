"""
Generated Code Metadata:
========================
Original URL: https://www.azrvservices.com
Prompt: Write a Python script to schedule an appointment for RV repair services in Phoenix, Arizona, considering the company's operating hours and service radius.
Generated: DETERMINISTIC_2f329e782befa58a
Batch ID: 20250622_212848
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import datetime
import pytz
from typing import Optional, Tuple, List

class RVRepairScheduler:
    """
    A class to schedule RV repair appointments in Phoenix, Arizona.
    Handles business hours, service radius, and appointment conflicts.
    """
    
    def __init__(self):
        # Business hours: 8 AM to 5 PM, Monday to Friday
        self.business_hours = {
            'open': datetime.time(8, 0),
            'close': datetime.time(17, 0)
        }
        
        # Service radius in miles from central Phoenix coordinates
        self.service_radius_miles = 30
        self.central_phoenix_coords = (33.4484, -112.0740)  # (lat, lon)
        
        # Existing appointments storage
        self.appointments = {}
        
        # Phoenix timezone
        self.timezone = pytz.timezone('America/Phoenix')

    def is_within_service_area(self, lat: float, lon: float) -> bool:
        """
        Check if given coordinates are within service radius.
        Simplified calculation - in production would use proper geodistance.
        """
        # Approximate calculation (for demo purposes)
        lat_diff = abs(self.central_phoenix_coords[0] - lat)
        lon_diff = abs(self.central_phoenix_coords[1] - lon)
        return (lat_diff + lon_diff) * 69 <= self.service_radius_miles  # ~69 miles per degree

    def is_business_hours(self, dt: datetime.datetime) -> bool:
        """
        Check if the given datetime is during business hours.
        """
        if dt.weekday() >= 5:  # Saturday (5) or Sunday (6)
            return False
            
        dt = dt.astimezone(self.timezone)
        time = dt.time()
        return self.business_hours['open'] <= time <= self.business_hours['close']

    def is_available(self, start_time: datetime.datetime, duration_hours: float) -> bool:
        """
        Check if the time slot is available.
        """
        end_time = start_time + datetime.timedelta(hours=duration_hours)
        
        # Convert to Phoenix timezone
        start_time = start_time.astimezone(self.timezone)
        end_time = end_time.astimezone(self.timezone)
        
        # Check business hours
        if not (self.is_business_hours(start_time) and self.is_business_hours(end_time)):
            return False
            
        # Check for overlapping appointments
        for existing_start, existing_end in self.appointments.values():
            if not (end_time <= existing_start or start_time >= existing_end):
                return False
                
        return True

    def schedule_appointment(
        self,
        customer_name: str,
        start_time: datetime.datetime,
        duration_hours: float,
        location_lat: float,
        location_lon: float
    ) -> Tuple[bool, Optional[str]]:
        """
        Schedule an appointment if criteria are met.
        Returns (success, message) tuple.
        """
        try:
            # Validate location
            if not self.is_within_service_area(location_lat, location_lon):
                return (False, "Location is outside our service area")
            
            # Validate time
            if not self.is_available(start_time, duration_hours):
                return (False, "Requested time is not available")
            
            # Convert to Phoenix timezone
            phx_start = start_time.astimezone(self.timezone)
            phx_end = phx_start + datetime.timedelta(hours=duration_hours)
            
            # Store appointment
            appointment_id = f"{customer_name[:3]}{phx_start.strftime('%Y%m%d%H%M')}"
            self.appointments[appointment_id] = (phx_start, phx_end)
            
            return (True, f"Appointment scheduled with ID: {appointment_id}")
            
        except Exception as e:
            return (False, f"Error scheduling appointment: {str(e)}")

    def get_available_slots(
        self,
        date: datetime.date,
        duration_hours: float,
        max_slots: int = 5
    ) -> List[datetime.datetime]:
        """
        Get available time slots for a given date.
        """
        slots = []
        current_time = datetime.datetime.combine(
            date,
            self.business_hours['open'],
            tzinfo=self.timezone
        )
        
        end_of_day = datetime.datetime.combine(
            date,
            self.business_hours['close'],
            tzinfo=self.timezone
        ) - datetime.timedelta(hours=duration_hours)
        
        while current_time <= end_of_day and len(slots) < max_slots:
            if self.is_available(current_time, duration_hours):
                slots.append(current_time)
                current_time += datetime.timedelta(hours=1)  # Next possible slot
            else:
                current_time += datetime.timedelta(minutes=30)  # Check in 30 min increments
                
        return slots

# Example usage
if __name__ == "__main__":
    scheduler = RVRepairScheduler()
    
    # Test scheduling
    now = datetime.datetime.now(pytz.utc)
    test_time = now + datetime.timedelta(days=1, hours=10)  # Tomorrow at 10 AM UTC
    
    success, message = scheduler.schedule_appointment(
        "John Doe",
        test_time,
        2.0,
        33.45,
        -112.07
    )
    
    print(message)
    
    # Get available slots
    tomorrow = datetime.date.today() + datetime.timedelta(days=1)
    slots = scheduler.get_available_slots(tomorrow, 2.0)
    print("\nAvailable slots tomorrow:")
    for slot in slots:
        print(slot.strftime("%I:%M %p"))
```
