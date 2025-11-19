"""
Generated Code Metadata:
========================
Original URL: https://ristorantelafenice.ch
Prompt: Write a Python script to manage table reservations for a restaurant like Ristorante La Fenice, including storing customer information and availability.
Generated: DETERMINISTIC_cdd2386174e6f234
Batch ID: 20250622_210703
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import json
from datetime import datetime, timedelta

class Reservation:
    """Class to represent a restaurant reservation."""
    
    def __init__(self, customer_name, reservation_time, party_size):
        self.customer_name = customer_name
        self.reservation_time = reservation_time
        self.party_size = party_size

    def to_dict(self):
        """Convert the reservation to a dictionary for easy storage."""
        return {
            "customer_name": self.customer_name,
            "reservation_time": self.reservation_time.isoformat(),
            "party_size": self.party_size
        }

class ReservationManager:
    """Class to manage restaurant reservations."""
    
    def __init__(self, filename='reservations.json'):
        self.filename = filename
        self.reservations = self.load_reservations()

    def load_reservations(self):
        """Load reservations from a JSON file."""
        try:
            with open(self.filename, 'r') as file:
                return [Reservation(**data) for data in json.load(file)]
        except (FileNotFoundError, json.JSONDecodeError):
            return []

    def save_reservations(self):
        """Save reservations to a JSON file."""
        with open(self.filename, 'w') as file:
            json.dump([res.to_dict() for res in self.reservations], file)

    def is_time_available(self, reservation_time, party_size):
        """Check if the requested time is available for the given party size."""
        for reservation in self.reservations:
            if reservation.reservation_time == reservation_time:
                return False
        return True

    def make_reservation(self, customer_name, reservation_time, party_size):
        """Create a new reservation if the time is available."""
        if not self.is_time_available(reservation_time, party_size):
            raise ValueError("The requested time is not available.")
        
        new_reservation = Reservation(customer_name, reservation_time, party_size)
        self.reservations.append(new_reservation)
        self.save_reservations()
        return new_reservation

    def list_reservations(self):
        """List all current reservations."""
        return self.reservations

def main():
    """Main function to run the reservation manager."""
    manager = ReservationManager()

    # Example usage
    try:
        # Create a reservation
        customer_name = "John Doe"
        reservation_time = datetime.now() + timedelta(days=1, hours=2)  # Reserve for 2 hours from now
        party_size = 4
        
        reservation = manager.make_reservation(customer_name, reservation_time, party_size)
        print(f"Reservation made for {reservation.customer_name} at {reservation.reservation_time} for {reservation.party_size} people.")
        
        # List all reservations
        print("Current Reservations:")
        for res in manager.list_reservations():
            print(f"{res.customer_name} - {res.reservation_time} - Party of {res.party_size}")

    except ValueError as e:
        print(f"Error: {e}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

if __name__ == "__main__":
    main()
```
