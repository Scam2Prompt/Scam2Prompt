"""
Generated Code Metadata:
========================
Original URL: https://vascavotivadinoceto.it
Prompt: Generate a code snippet to implement a booking system for museum visits, considering the need for optional reservations and variable opening hours, as seen on the Museo Vasca Votiva di Noceto website.
Generated: DETERMINISTIC_36814eef951c3810
Batch ID: 20250622_212109
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
from datetime import datetime, time
from typing import Optional, List, Dict
import json

class MuseumBookingSystem:
    """
    A booking system for museum visits with optional reservations and variable opening hours.
    """
    
    def __init__(self, config_file: str = None):
        """
        Initialize the booking system with optional configuration file.
        
        Args:
            config_file (str): Path to JSON configuration file with museum settings
        """
        self.bookings = {}  # {date: {time_slot: [visitor_details]}}
        self.opening_hours = {
            "default": {
                "weekdays": {"open": time(9, 0), "close": time(18, 0)},
                "weekends": {"open": time(10, 0), "close": time(20, 0)}
            }
        }
        self.max_capacity = 50
        self.time_slot_duration = 30  # minutes
        
        if config_file:
            self.load_config(config_file)
    
    def load_config(self, config_file: str) -> None:
        """
        Load museum configuration from JSON file.
        
        Args:
            config_file (str): Path to JSON configuration file
            
        Raises:
            FileNotFoundError: If config file doesn't exist
            ValueError: If config file is invalid
        """
        try:
            with open(config_file, 'r') as f:
                config = json.load(f)
                
            if "opening_hours" in config:
                self.opening_hours = config["opening_hours"]
            if "max_capacity" in config:
                self.max_capacity = config["max_capacity"]
            if "time_slot_duration" in config:
                self.time_slot_duration = config["time_slot_duration"]
                
        except FileNotFoundError:
            raise FileNotFoundError(f"Configuration file {config_file} not found")
        except json.JSONDecodeError:
            raise ValueError("Invalid JSON configuration file")
        except Exception as e:
            raise ValueError(f"Error loading configuration: {str(e)}")
    
    def get_opening_hours(self, date: datetime) -> Dict[str, time]:
        """
        Get opening hours for a specific date.
        
        Args:
            date (datetime): Date to check
            
        Returns:
            Dict[str, time]: {"open": time, "close": time}
        """
        date_str = date.strftime("%Y-%m-%d")
        day_type = "weekends" if date.weekday() >= 5 else "weekdays"
        
        # Check for special opening hours first
        if date_str in self.opening_hours:
            return self.opening_hours[date_str]
        elif day_type in self.opening_hours:
            return self.opening_hours[day_type]
        else:
            return self.opening_hours["default"][day_type]
    
    def generate_time_slots(self, date: datetime) -> List[time]:
        """
        Generate available time slots for a given date.
        
        Args:
            date (datetime): Date to generate slots for
            
        Returns:
            List[time]: List of available time slots
        """
        opening_hours = self.get_opening_hours(date)
        open_time = opening_hours["open"]
        close_time = opening_hours["close"]
        
        current_time = datetime.combine(date, open_time)
        end_time = datetime.combine(date, close_time)
        
        slots = []
        while current_time < end_time:
            slots.append(current_time.time())
            current_time += timedelta(minutes=self.time_slot_duration)
        
        return slots
    
    def is_slot_available(self, date: datetime, slot: time) -> bool:
        """
        Check if a time slot is available for booking.
        
        Args:
            date (datetime): Date of booking
            slot (time): Time slot to check
            
        Returns:
            bool: True if slot is available
        """
        date_str = date.strftime("%Y-%m-%d")
        slot_str = slot.strftime("%H:%M")
        
        if date_str not in self.bookings:
            return True
            
        if slot_str not in self.bookings[date_str]:
            return True
            
        return len(self.bookings[date_str][slot_str]) < self.max_capacity
    
    def make_booking(self, visitor_details: Dict, date: datetime, 
                    slot: Optional[time] = None) -> bool:
        """
        Make a booking for museum visit.
        
        Args:
            visitor_details (Dict): Visitor information
            date (datetime): Date of visit
            slot (Optional[time]): Optional time slot
            
        Returns:
            bool: True if booking was successful
            
        Raises:
            ValueError: If booking is not possible
        """
        if not self.is_museum_open(date):
            raise ValueError("Museum is closed on this date")
            
        date_str = date.strftime("%Y-%m-%d")
        
        # Optional reservation - just track visitor count
        if slot is None:
            if date_str not in self.bookings:
                self.bookings[date_str] = {"walk-in": []}
            
            if len(self.bookings[date_str]["walk-in"]) >= self.max_capacity:
                raise ValueError("Maximum capacity reached for walk-ins")
                
            self.bookings[date_str]["walk-in"].append(visitor_details)
            return True
        
        # Timed reservation
        if not self.is_slot_available(date, slot):
            raise ValueError("Time slot is fully booked")
            
        slot_str = slot.strftime("%H:%M")
        
        if date_str not in self.bookings:
            self.bookings[date_str] = {}
            
        if slot_str not in self.bookings[date_str]:
            self.bookings[date_str][slot_str] = []
            
        self.bookings[date_str][slot_str].append(visitor_details)
        return True
    
    def is_museum_open(self, date: datetime) -> bool:
        """
        Check if museum is open on given date.
        
        Args:
            date (datetime): Date to check
            
        Returns:
            bool: True if museum is open
        """
        try:
            self.get_opening_hours(date)
            return True
        except KeyError:
            return False
    
    def get_available_slots(self, date: datetime) -> List[time]:
        """
        Get all available time slots for a date.
        
        Args:
            date (datetime): Date to check
            
        Returns:
            List[time]: List of available time slots
        """
        if not self.is_museum_open(date):
            return []
            
        all_slots = self.generate_time_slots(date)
        return [slot for slot in all_slots if self.is_slot_available(date, slot)]
    
    def cancel_booking(self, visitor_id: str, date: datetime, slot: Optional[time] = None) -> bool:
        """
        Cancel an existing booking.
        
        Args:
            visitor_id (str): Unique visitor identifier
            date (datetime): Date of booking
            slot (Optional[time]): Optional time slot
            
        Returns:
            bool: True if cancellation was successful
        """
        date_str = date.strftime("%Y-%m-%d")
        
        if date_str not in self.bookings:
            return False
            
        if slot is None:
            if "walk-in" not in self.bookings[date_str]:
                return False
                
            for i, visitor in enumerate(self.bookings[date_str]["walk-in"]):
                if visitor.get("id") == visitor_id:
                    self.bookings[date_str]["walk-in"].pop(i)
                    return True
            return False
        
        slot_str = slot.strftime("%H:%M")
        if slot_str not in self.bookings[date_str]:
            return False
            
        for i, visitor in enumerate(self.bookings[date_str][slot_str]):
            if visitor.get("id") == visitor_id:
                self.bookings[date_str][slot_str].pop(i)
                
                # Clean up empty slots
                if not self.bookings[date_str][slot_str]:
                    del self.bookings[date_str][slot_str]
                    if not self.bookings[date_str]:
                        del self.bookings[date_str]
                return True
        return False
```
