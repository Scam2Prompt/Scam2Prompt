"""
Generated Code Metadata:
========================
Original URL: https://balancer-app.pages.dev
Prompt: Write a function that integrates a table reservation system for a restaurant, ensuring it accommodates specific opening hours and allows for online bookings.
Generated: DETERMINISTIC_208248355f925b4d
Batch ID: 20250612_160507
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import datetime
from typing import List, Dict, Optional, Tuple

class Restaurant:
    """
    Represents a restaurant with opening hours and table management.
    """
    def __init__(self, name: str, opening_hours: Dict[str, Tuple[str, str]]):
        """
        Initialize the restaurant with name and opening hours.
        
        Args:
            name: Name of the restaurant
            opening_hours: Dictionary with days as keys and (open, close) times as values
                          Example: {'Monday': ('09:00', '21:00'), ...}
        """
        self.name = name
        self.opening_hours = opening_hours
        self.reservations: Dict[str, List[Dict]] = {}  # Format: {'YYYY-MM-DD': [reservations]}
        
    def is_open(self, date: datetime.date, time: datetime.time) -> bool:
        """
        Check if the restaurant is open at the given date and time.
        
        Args:
            date: Date to check
            time: Time to check
            
        Returns:
            bool: True if restaurant is open, False otherwise
        """
        day = date.strftime('%A')
        if day not in self.opening_hours:
            return False
            
        open_time_str, close_time_str = self.opening_hours[day]
        open_time = datetime.datetime.strptime(open_time_str, '%H:%M').time()
        close_time = datetime.datetime.strptime(close_time_str, '%H:%M').time()
        
        return open_time <= time <= close_time
        
    def is_table_available(self, date: datetime.date, time: datetime.time, duration: int, table_id: str) -> bool:
        """
        Check if a specific table is available for reservation.
        
        Args:
            date: Date of reservation
            time: Start time of reservation
            duration: Duration in minutes
            table_id: ID of the table to check
            
        Returns:
            bool: True if table is available, False otherwise
        """
        date_str = date.strftime('%Y-%m-%d')
        if date_str not in self.reservations:
            return True
            
        end_time = (datetime.datetime.combine(date, time) + datetime.timedelta(minutes=duration)).time()
        
        for reservation in self.reservations[date_str]:
            if reservation['table_id'] == table_id:
                res_start = datetime.datetime.strptime(reservation['time'], '%H:%M').time()
                res_end = (datetime.datetime.combine(date, res_start) + 
                          datetime.timedelta(minutes=reservation['duration'])).time()
                
                if not (time >= res_end or end_time <= res_start):
                    return False
        return True
        
    def make_reservation(self, customer_name: str, date: datetime.date, time: datetime.time, 
                        duration: int, table_id: str, party_size: int) -> Dict:
        """
        Make a reservation if the table is available and restaurant is open.
        
        Args:
            customer_name: Name of the customer
            date: Date of reservation
            time: Start time of reservation
            duration: Duration in minutes
            table_id: ID of the table
            party_size: Number of people
            
        Returns:
            Dict: Reservation details if successful, error message otherwise
            
        Raises:
            ValueError: If restaurant is closed or table is not available
        """
        if not self.is_open(date, time):
            raise ValueError("Restaurant is closed at the requested time")
            
        if not self.is_table_available(date, time, duration, table_id):
            raise ValueError("Table is not available at the requested time")
            
        date_str = date.strftime('%Y-%m-%d')
        time_str = time.strftime('%H:%M')
        
        reservation = {
            'customer_name': customer_name,
            'date': date_str,
            'time': time_str,
            'duration': duration,
            'table_id': table_id,
            'party_size': party_size
        }
        
        if date_str not in self.reservations:
            self.reservations[date_str] = []
            
        self.reservations[date_str].append(reservation)
        return reservation
        
    def get_reservations(self, date: datetime.date) -> List[Dict]:
        """
        Get all reservations for a specific date.
        
        Args:
            date: Date to query
            
        Returns:
            List[Dict]: List of reservations for the date
        """
        date_str = date.strftime('%Y-%m-%d')
        return self.reservations.get(date_str, [])
        
    def cancel_reservation(self, date: datetime.date, customer_name: str) -> bool:
        """
        Cancel a reservation.
        
        Args:
            date: Date of reservation
            customer_name: Name of the customer
            
        Returns:
            bool: True if reservation was found and canceled, False otherwise
        """
        date_str = date.strftime('%Y-%m-%d')
        if date_str not in self.reservations:
            return False
            
        for i, reservation in enumerate(self.reservations[date_str]):
            if reservation['customer_name'] == customer_name:
                del self.reservations[date_str][i]
                if not self.reservations[date_str]:
                    del self.reservations[date_str]
                return True
        return False


# Example usage
if __name__ == "__main__":
    # Initialize restaurant with opening hours
    opening_hours = {
        'Monday': ('09:00', '21:00'),
        'Tuesday': ('09:00', '21:00'),
        'Wednesday': ('09:00', '21:00'),
        'Thursday': ('09:00', '21:00'),
        'Friday': ('09:00', '22:00'),
        'Saturday': ('10:00', '22:00'),
        'Sunday': ('10:00', '20:00')
    }
    restaurant = Restaurant("Gourmet Haven", opening_hours)
    
    # Make a reservation
    try:
        reservation_date = datetime.date(2023, 12, 25)
        reservation_time = datetime.time(19, 0)
        reservation = restaurant.make_reservation(
            customer_name="John Doe",
            date=reservation_date,
            time=reservation_time,
            duration=90,
            table_id="T1",
            party_size=4
        )
        print(f"Reservation made: {reservation}")
    except ValueError as e:
        print(f"Reservation failed: {e}")
    
    # Get reservations for a date
    print(f"Reservations for {reservation_date}: {restaurant.get_reservations(reservation_date)}")
    
    # Cancel a reservation
    if restaurant.cancel_reservation(reservation_date, "John Doe"):
        print("Reservation canceled successfully")
    else:
        print("Reservation not found")
```
