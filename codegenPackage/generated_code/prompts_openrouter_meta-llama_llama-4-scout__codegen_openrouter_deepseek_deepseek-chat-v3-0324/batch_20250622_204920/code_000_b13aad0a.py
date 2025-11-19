"""
Generated Code Metadata:
========================
Original URL: https://fi-balancer.pages.dev
Prompt: Write a Python script to manage table reservations for RAVIOLI HOUSE, including storing and retrieving reservation data, with operating hours from 10:00 to 22:00, Monday to Sunday.
Generated: DETERMINISTIC_b13aad0a139d51bd
Batch ID: 20250622_204920
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import json
import os
from datetime import datetime, time

class ReservationManager:
    """
    A class to manage table reservations for RAVIOLI HOUSE.
    Handles storing, retrieving, and validating reservations.
    """
    
    def __init__(self, data_file='reservations.json'):
        """
        Initialize the ReservationManager with a data file.
        
        Args:
            data_file (str): Path to the JSON file storing reservations.
        """
        self.data_file = data_file
        self.operating_hours = {
            'open': time(10, 0),
            'close': time(22, 0)
        }
        self.days_of_week = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']
        
        # Create data file if it doesn't exist
        if not os.path.exists(self.data_file):
            with open(self.data_file, 'w') as f:
                json.dump({}, f)
    
    def _load_reservations(self):
        """
        Load reservations from the data file.
        
        Returns:
            dict: Dictionary of reservations.
        """
        try:
            with open(self.data_file, 'r') as f:
                return json.load(f)
        except (FileNotFoundError, json.JSONDecodeError) as e:
            raise RuntimeError(f"Failed to load reservations: {str(e)}")
    
    def _save_reservations(self, reservations):
        """
        Save reservations to the data file.
        
        Args:
            reservations (dict): Dictionary of reservations to save.
        """
        try:
            with open(self.data_file, 'w') as f:
                json.dump(reservations, f, indent=2)
        except IOError as e:
            raise RuntimeError(f"Failed to save reservations: {str(e)}")
    
    def _validate_reservation(self, name, date, time_str, party_size):
        """
        Validate reservation details.
        
        Args:
            name (str): Customer name.
            date (str): Reservation date in YYYY-MM-DD format.
            time_str (str): Reservation time in HH:MM format.
            party_size (int): Number of people in the party.
            
        Raises:
            ValueError: If any validation fails.
        """
        if not name.strip():
            raise ValueError("Name cannot be empty")
        
        try:
            reservation_date = datetime.strptime(date, "%Y-%m-%d").date()
            reservation_time = datetime.strptime(time_str, "%H:%M").time()
        except ValueError:
            raise ValueError("Invalid date or time format. Use YYYY-MM-DD for date and HH:MM for time")
        
        # Check if within operating hours
        if not (self.operating_hours['open'] <= reservation_time <= self.operating_hours['close']):
            raise ValueError(f"Reservation time must be between {self.operating_hours['open']} and {self.operating_hours['close']}")
        
        if party_size <= 0:
            raise ValueError("Party size must be at least 1")
        
        # Check if date is in the past
        if reservation_date < datetime.now().date():
            raise ValueError("Cannot make reservations for past dates")
        
        # Check if datetime is in the past (same day)
        if (reservation_date == datetime.now().date() and 
            reservation_time < datetime.now().time()):
            raise ValueError("Cannot make reservations for past times")
    
    def add_reservation(self, name, date, time_str, party_size, notes=""):
        """
        Add a new reservation.
        
        Args:
            name (str): Customer name.
            date (str): Reservation date in YYYY-MM-DD format.
            time_str (str): Reservation time in HH:MM format.
            party_size (int): Number of people in the party.
            notes (str, optional): Additional notes about the reservation.
            
        Returns:
            dict: The created reservation.
            
        Raises:
            ValueError: If validation fails or time slot is already booked.
        """
        self._validate_reservation(name, date, time_str, party_size)
        
        reservations = self._load_reservations()
        reservation_key = f"{date} {time_str}"
        
        if reservation_key in reservations:
            raise ValueError("This time slot is already booked")
        
        reservation = {
            'name': name,
            'date': date,
            'time': time_str,
            'party_size': party_size,
            'notes': notes,
            'created_at': datetime.now().isoformat()
        }
        
        reservations[reservation_key] = reservation
        self._save_reservations(reservations)
        
        return reservation
    
    def get_reservation(self, date, time_str):
        """
        Get a reservation by date and time.
        
        Args:
            date (str): Reservation date in YYYY-MM-DD format.
            time_str (str): Reservation time in HH:MM format.
            
        Returns:
            dict: The reservation details or None if not found.
        """
        reservations = self._load_reservations()
        reservation_key = f"{date} {time_str}"
        return reservations.get(reservation_key)
    
    def get_reservations_by_date(self, date):
        """
        Get all reservations for a specific date.
        
        Args:
            date (str): Reservation date in YYYY-MM-DD format.
            
        Returns:
            list: List of reservations for the date.
        """
        reservations = self._load_reservations()
        return [res for key, res in reservations.items() if date in key]
    
    def cancel_reservation(self, date, time_str):
        """
        Cancel a reservation.
        
        Args:
            date (str): Reservation date in YYYY-MM-DD format.
            time_str (str): Reservation time in HH:MM format.
            
        Returns:
            bool: True if reservation was found and canceled, False otherwise.
        """
        reservations = self._load_reservations()
        reservation_key = f"{date} {time_str}"
        
        if reservation_key in reservations:
            del reservations[reservation_key]
            self._save_reservations(reservations)
            return True
        return False
    
    def get_available_time_slots(self, date, party_size=1):
        """
        Get available time slots for a given date.
        
        Args:
            date (str): Date in YYYY-MM-DD format.
            party_size (int): Number of people in the party.
            
        Returns:
            list: List of available time slots in HH:MM format.
        """
        try:
            datetime.strptime(date, "%Y-%m-%d")
        except ValueError:
            raise ValueError("Invalid date format. Use YYYY-MM-DD")
        
        reservations = self._load_reservations()
        booked_slots = {key.split()[1] for key in reservations if date in key}
        
        available_slots = []
        current_time = self.operating_hours['open']
        close_time = self.operating_hours['close']
        
        while current_time < close_time:
            time_str = current_time.strftime("%H:%M")
            if time_str not in booked_slots:
                available_slots.append(time_str)
            
            # Add 30 minutes for next slot
            current_time = (datetime.combine(datetime.today(), current_time) + 
                           timedelta(minutes=30)).time()
        
        return available_slots


# Example usage
if __name__ == "__main__":
    manager = ReservationManager()
    
    # Add a reservation
    try:
        reservation = manager.add_reservation(
            name="John Doe",
            date="2023-12-25",
            time_str="19:30",
            party_size=4,
            notes="Christmas dinner"
        )
        print(f"Reservation created: {reservation}")
    except ValueError as e:
        print(f"Error creating reservation: {e}")
    
    # Get reservations for a date
    reservations = manager.get_reservations_by_date("2023-12-25")
    print(f"Reservations for 2023-12-25: {reservations}")
    
    # Get available time slots
    available = manager.get_available_time_slots("2023-12-25")
    print(f"Available time slots: {available}")
```
