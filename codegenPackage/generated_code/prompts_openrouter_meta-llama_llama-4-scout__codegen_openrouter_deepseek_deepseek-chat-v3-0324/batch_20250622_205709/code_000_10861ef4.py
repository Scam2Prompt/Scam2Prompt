"""
Generated Code Metadata:
========================
Original URL: https://co-djs.com
Prompt: Write a Python script to manage DJ event bookings, including calculating overtime costs and generating invoices based on package deals like the "Pop-Up" DJ Package for $500 and the "Everything" DJ Package for $1250.
Generated: DETERMINISTIC_10861ef4b0b12edd
Batch ID: 20250622_205709
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
from typing import Dict, List, Optional, Tuple

# Constants
POP_UP_PACKAGE_PRICE = 500
EVERYTHING_PACKAGE_PRICE = 1250
OVERTIME_RATE_PER_HOUR = 150
STANDARD_EVENT_DURATION = timedelta(hours=4)
PACKAGES = {
    "Pop-Up": POP_UP_PACKAGE_PRICE,
    "Everything": EVERYTHING_PACKAGE_PRICE
}

class DJBooking:
    """Class to manage DJ event bookings and invoice generation."""
    
    def __init__(self):
        self.bookings: Dict[str, Dict] = {}
        self.invoices: Dict[str, Dict] = {}
    
    def create_booking(self, client_name: str, event_date: str, package: str, 
                      start_time: str, end_time: str, notes: Optional[str] = None) -> str:
        """Create a new DJ booking.
        
        Args:
            client_name: Name of the client
            event_date: Date of the event in YYYY-MM-DD format
            package: Package name ('Pop-Up' or 'Everything')
            start_time: Start time in HH:MM format (24-hour)
            end_time: End time in HH:MM format (24-hour)
            notes: Optional notes about the booking
            
        Returns:
            Booking ID
            
        Raises:
            ValueError: If package is invalid or time format is incorrect
        """
        if package not in PACKAGES:
            raise ValueError(f"Invalid package. Must be one of: {list(PACKAGES.keys())}")
        
        try:
            event_datetime = datetime.strptime(event_date, "%Y-%m-%d")
            start_datetime = datetime.strptime(start_time, "%H:%M")
            end_datetime = datetime.strptime(end_time, "%H:%M")
        except ValueError as e:
            raise ValueError("Invalid date or time format") from e
        
        booking_id = f"{client_name[:3].upper()}{event_datetime.strftime('%m%d')}"
        
        self.bookings[booking_id] = {
            "client_name": client_name,
            "event_date": event_date,
            "package": package,
            "start_time": start_time,
            "end_time": end_time,
            "notes": notes,
            "status": "Confirmed"
        }
        
        return booking_id
    
    def calculate_overtime(self, booking_id: str) -> Tuple[float, float]:
        """Calculate overtime hours and cost for a booking.
        
        Args:
            booking_id: ID of the booking to calculate
            
        Returns:
            Tuple of (overtime_hours, overtime_cost)
            
        Raises:
            KeyError: If booking ID doesn't exist
        """
        if booking_id not in self.bookings:
            raise KeyError(f"Booking ID {booking_id} not found")
        
        booking = self.bookings[booking_id]
        start_time = datetime.strptime(booking["start_time"], "%H:%M")
        end_time = datetime.strptime(booking["end_time"], "%H:%M")
        duration = end_time - start_time
        
        overtime_hours = max(0, (duration - STANDARD_EVENT_DURATION).total_seconds() / 3600)
        overtime_cost = overtime_hours * OVERTIME_RATE_PER_HOUR
        
        return overtime_hours, overtime_cost
    
    def generate_invoice(self, booking_id: str) -> Dict:
        """Generate an invoice for a booking.
        
        Args:
            booking_id: ID of the booking to invoice
            
        Returns:
            Dictionary containing invoice details
            
        Raises:
            KeyError: If booking ID doesn't exist
        """
        if booking_id not in self.bookings:
            raise KeyError(f"Booking ID {booking_id} not found")
        
        booking = self.bookings[booking_id]
        overtime_hours, overtime_cost = self.calculate_overtime(booking_id)
        
        subtotal = PACKAGES[booking["package"]]
        total = subtotal + overtime_cost
        
        invoice = {
            "invoice_id": f"INV-{booking_id}",
            "booking_id": booking_id,
            "client_name": booking["client_name"],
            "event_date": booking["event_date"],
            "package": booking["package"],
            "package_price": subtotal,
            "overtime_hours": round(overtime_hours, 2),
            "overtime_cost": round(overtime_cost, 2),
            "total": total,
            "issued_date": datetime.now().strftime("%Y-%m-%d"),
            "status": "Pending"
        }
        
        self.invoices[invoice["invoice_id"]] = invoice
        return invoice
    
    def save_to_file(self, filename: str) -> None:
        """Save bookings and invoices to a JSON file.
        
        Args:
            filename: Name of the file to save to
        """
        data = {
            "bookings": self.bookings,
            "invoices": self.invoices
        }
        
        with open(filename, 'w') as f:
            json.dump(data, f, indent=4)
    
    def load_from_file(self, filename: str) -> None:
        """Load bookings and invoices from a JSON file.
        
        Args:
            filename: Name of the file to load from
            
        Raises:
            FileNotFoundError: If file doesn't exist
            json.JSONDecodeError: If file is not valid JSON
        """
        try:
            with open(filename, 'r') as f:
                data = json.load(f)
                self.bookings = data.get("bookings", {})
                self.invoices = data.get("invoices", {})
        except FileNotFoundError:
            raise FileNotFoundError(f"File {filename} not found")
        except json.JSONDecodeError:
            raise json.JSONDecodeError("Invalid JSON file", "", 0)

# Example usage
if __name__ == "__main__":
    booking_manager = DJBooking()
    
    try:
        # Create a booking
        booking_id = booking_manager.create_booking(
            client_name="John Doe",
            event_date="2023-12-15",
            package="Everything",
            start_time="19:00",
            end_time="23:30",
            notes="Birthday party"
        )
        
        # Generate invoice
        invoice = booking_manager.generate_invoice(booking_id)
        print("Generated Invoice:")
        print(json.dumps(invoice, indent=4))
        
        # Save to file
        booking_manager.save_to_file("dj_bookings.json")
        
    except Exception as e:
        print(f"Error: {str(e)}")
```
