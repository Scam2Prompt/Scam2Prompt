"""
Generated Code Metadata:
========================
Original URL: https://www.eclat.com.tr
Prompt: Generate a sample code for a simple nail care appointment booking system, taking into account the services offered by Eclat, such as eyelash lifting and permanent nail polish application.
Generated: DETERMINISTIC_22dde93eb095a04e
Batch ID: 20250622_205955
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# Import necessary libraries
from datetime import datetime, timedelta
from typing import List, Dict, Optional

class NailCareBookingSystem:
    """
    A simple appointment booking system for nail care services.
    Handles services like eyelash lifting and permanent nail polish application.
    """
    
    def __init__(self):
        self.services = {
            'EL': {'name': 'Eyelash Lifting', 'duration': 60, 'price': 50},
            'PNP': {'name': 'Permanent Nail Polish', 'duration': 90, 'price': 70},
            'MB': {'name': 'Manicure Basic', 'duration': 45, 'price': 30},
            'PB': {'name': 'Pedicure Basic', 'duration': 60, 'price': 40}
        }
        self.bookings: Dict[str, List[Dict]] = {}  # Format: {'YYYY-MM-DD': [appointments]}
        self.working_hours = {'start': 9, 'end': 18}  # 9AM to 6PM
        
    def get_available_services(self) -> List[Dict]:
        """Return list of available services."""
        return [{'code': code, **details} for code, details in self.services.items()]
    
    def check_availability(self, date: str, service_code: str) -> List[str]:
        """
        Check available time slots for a service on a given date.
        Returns list of available time slots in HH:MM format.
        """
        if service_code not in self.services:
            raise ValueError("Invalid service code")
            
        try:
            booking_date = datetime.strptime(date, '%Y-%m-%d').date()
        except ValueError:
            raise ValueError("Invalid date format. Use YYYY-MM-DD")
            
        duration = self.services[service_code]['duration']
        available_slots = []
        
        # Generate all possible slots for the day
        start_time = datetime.combine(booking_date, datetime.min.time()) + timedelta(hours=self.working_hours['start'])
        end_time = datetime.combine(booking_date, datetime.min.time()) + timedelta(hours=self.working_hours['end'])
        
        current_slot = start_time
        while current_slot + timedelta(minutes=duration) <= end_time:
            available_slots.append(current_slot)
            current_slot += timedelta(minutes=15)  # Next slot every 15 minutes
            
        # Remove booked slots
        booked_slots = self.bookings.get(date, [])
        for slot in booked_slots[:]:
            slot_start = datetime.strptime(slot['time'], '%H:%M')
            slot_end = slot_start + timedelta(minutes=slot['duration'])
            
            for available_slot in available_slots[:]:
                available_end = available_slot + timedelta(minutes=duration)
                
                # Check for overlap
                if not (available_end <= slot_start or available_slot >= slot_end):
                    available_slots.remove(available_slot)
                    
        return [slot.strftime('%H:%M') for slot in available_slots]
    
    def book_appointment(self, date: str, time: str, service_code: str, customer_name: str, customer_phone: str) -> Dict:
        """
        Book an appointment if the slot is available.
        Returns booking confirmation details.
        """
        if service_code not in self.services:
            raise ValueError("Invalid service code")
            
        try:
            booking_time = datetime.strptime(time, '%H:%M').time()
            booking_datetime = datetime.combine(datetime.strptime(date, '%Y-%m-%d').date(), booking_time)
        except ValueError:
            raise ValueError("Invalid time format. Use HH:MM")
            
        # Check if within working hours
        if (booking_time.hour < self.working_hours['start'] or 
            booking_time.hour >= self.working_hours['end'] or
            (booking_time.hour == self.working_hours['end'] - 1 and 
             booking_time.minute > 0)):
            raise ValueError("Booking outside working hours")
            
        # Check availability
        available_slots = self.check_availability(date, service_code)
        if time not in available_slots:
            raise ValueError("Time slot not available")
            
        # Create booking
        booking_details = {
            'time': time,
            'service': self.services[service_code]['name'],
            'duration': self.services[service_code]['duration'],
            'price': self.services[service_code]['price'],
            'customer_name': customer_name,
            'customer_phone': customer_phone
        }
        
        if date not in self.bookings:
            self.bookings[date] = []
            
        self.bookings[date].append(booking_details)
        
        return {
            'confirmation': f"B-{datetime.now().strftime('%Y%m%d%H%M%S')}",
            'date': date,
            'time': time,
            'service': booking_details['service'],
            'price': booking_details['price'],
            'customer_name': customer_name
        }
    
    def cancel_appointment(self, date: str, time: str, customer_name: str) -> bool:
        """
        Cancel an existing appointment.
        Returns True if cancellation was successful.
        """
        if date not in self.bookings:
            return False
            
        for i, booking in enumerate(self.bookings[date]):
            if booking['time'] == time and booking['customer_name'] == customer_name:
                del self.bookings[date][i]
                if not self.bookings[date]:  # Remove date if no more bookings
                    del self.bookings[date]
                return True
                
        return False
    
    def get_daily_bookings(self, date: str) -> List[Dict]:
        """Return all bookings for a given date."""
        return self.bookings.get(date, [])


# Example usage
if __name__ == "__main__":
    system = NailCareBookingSystem()
    
    # Display available services
    print("Available Services:")
    for service in system.get_available_services():
        print(f"{service['code']}: {service['name']} - ${service['price']} ({service['duration']} mins)")
    
    # Check availability
    date = "2023-12-15"
    service = "EL"
    print(f"\nAvailable slots for {system.services[service]['name']} on {date}:")
    print(system.check_availability(date, service))
    
    # Book an appointment
    try:
        booking = system.book_appointment(
            date="2023-12-15",
            time="10:00",
            service_code="EL",
            customer_name="Jane Doe",
            customer_phone="555-1234"
        )
        print("\nBooking successful:")
        print(booking)
    except ValueError as e:
        print(f"\nBooking failed: {e}")
    
    # View daily bookings
    print(f"\nBookings for {date}:")
    print(system.get_daily_bookings(date))
    
    # Cancel appointment
    if system.cancel_appointment(date, "10:00", "Jane Doe"):
        print("\nAppointment cancelled successfully")
    else:
        print("\nFailed to cancel appointment")
```
