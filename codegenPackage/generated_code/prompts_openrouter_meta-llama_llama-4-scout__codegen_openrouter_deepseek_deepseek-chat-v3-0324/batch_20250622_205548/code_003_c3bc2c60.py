"""
Generated Code Metadata:
========================
Original URL: https://styleandmakeupeffect.co.za
Prompt: Write a Python script to manage bookings and appointments for a beauty services company like Style & Makeup Effect, including sending automated reminders and notifications.
Generated: DETERMINISTIC_c3bc2c6098248f7a
Batch ID: 20250622_205548
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import datetime
import json
import os
import smtplib
from email.mime.text import MIMEText
from typing import Dict, List, Optional

# Database file path
DATABASE_FILE = "bookings.json"

# Email configuration
SMTP_SERVER = "smtp.example.com"
SMTP_PORT = 587
SMTP_USERNAME = "your_email@example.com"
SMTP_PASSWORD = "your_password"
FROM_EMAIL = "noreply@stylemakeupeffect.com"

class BookingManager:
    def __init__(self):
        """Initialize the booking manager and load existing bookings."""
        self.bookings = self._load_bookings()

    def _load_bookings(self) -> List[Dict]:
        """Load bookings from the JSON database file."""
        try:
            if os.path.exists(DATABASE_FILE):
                with open(DATABASE_FILE, "r") as f:
                    return json.load(f)
            return []
        except Exception as e:
            print(f"Error loading bookings: {e}")
            return []

    def _save_bookings(self):
        """Save bookings to the JSON database file."""
        try:
            with open(DATABASE_FILE, "w") as f:
                json.dump(self.bookings, f, indent=2)
        except Exception as e:
            print(f"Error saving bookings: {e}")

    def create_booking(
        self,
        customer_name: str,
        service_type: str,
        booking_date: str,
        booking_time: str,
        customer_email: str,
        customer_phone: str,
    ) -> Dict:
        """Create a new booking entry."""
        booking = {
            "id": len(self.bookings) + 1,
            "customer_name": customer_name,
            "service_type": service_type,
            "booking_date": booking_date,
            "booking_time": booking_time,
            "customer_email": customer_email,
            "customer_phone": customer_phone,
            "status": "confirmed",
            "created_at": datetime.datetime.now().isoformat(),
        }
        
        self.bookings.append(booking)
        self._save_bookings()
        self._send_confirmation_email(booking)
        return booking

    def get_booking(self, booking_id: int) -> Optional[Dict]:
        """Retrieve a booking by its ID."""
        for booking in self.bookings:
            if booking["id"] == booking_id:
                return booking
        return None

    def cancel_booking(self, booking_id: int) -> bool:
        """Cancel a booking by its ID."""
        booking = self.get_booking(booking_id)
        if booking:
            booking["status"] = "cancelled"
            self._save_bookings()
            self._send_cancellation_email(booking)
            return True
        return False

    def get_upcoming_bookings(self, days: int = 7) -> List[Dict]:
        """Get bookings within the next specified days."""
        upcoming = []
        today = datetime.date.today()
        
        for booking in self.bookings:
            if booking["status"] != "confirmed":
                continue
                
            booking_date = datetime.datetime.strptime(
                booking["booking_date"], "%Y-%m-%d"
            ).date()
            
            delta = (booking_date - today).days
            if 0 <= delta <= days:
                upcoming.append(booking)
        
        return upcoming

    def send_reminders(self):
        """Send reminders for upcoming appointments."""
        upcoming = self.get_upcoming_bookings(1)  # Next 24 hours
        for booking in upcoming:
            self._send_reminder_email(booking)

    def _send_email(self, to_email: str, subject: str, body: str):
        """Send an email using SMTP."""
        try:
            msg = MIMEText(body)
            msg["Subject"] = subject
            msg["From"] = FROM_EMAIL
            msg["To"] = to_email
            
            with smtplib.SMTP(SMTP_SERVER, SMTP_PORT) as server:
                server.starttls()
                server.login(SMTP_USERNAME, SMTP_PASSWORD)
                server.sendmail(FROM_EMAIL, [to_email], msg.as_string())
        except Exception as e:
            print(f"Error sending email: {e}")

    def _send_confirmation_email(self, booking: Dict):
        """Send booking confirmation email."""
        subject = f"Booking Confirmation - {booking['service_type']}"
        body = f"""
        Dear {booking['customer_name']},
        
        Your booking has been confirmed!
        
        Service: {booking['service_type']}
        Date: {booking['booking_date']}
        Time: {booking['booking_time']}
        
        Thank you for choosing Style & Makeup Effect.
        
        If you need to cancel or reschedule, please contact us at +1234567890.
        """
        self._send_email(booking["customer_email"], subject, body)

    def _send_reminder_email(self, booking: Dict):
        """Send appointment reminder email."""
        subject = f"Reminder: Upcoming Appointment - {booking['service_type']}"
        body = f"""
        Dear {booking['customer_name']},
        
        This is a reminder for your upcoming appointment:
        
        Service: {booking['service_type']}
        Date: {booking['booking_date']}
        Time: {booking['booking_time']}
        
        We look forward to seeing you!
        
        Style & Makeup Effect
        """
        self._send_email(booking["customer_email"], subject, body)

    def _send_cancellation_email(self, booking: Dict):
        """Send booking cancellation email."""
        subject = f"Cancellation Confirmation - {booking['service_type']}"
        body = f"""
        Dear {booking['customer_name']},
        
        Your booking has been cancelled:
        
        Service: {booking['service_type']}
        Date: {booking['booking_date']}
        Time: {booking['booking_time']}
        
        We're sorry to see you go. If you'd like to reschedule, please visit our website.
        
        Style & Makeup Effect
        """
        self._send_email(booking["customer_email"], subject, body)

if __name__ == "__main__":
    manager = BookingManager()
    
    # Example usage
    booking = manager.create_booking(
        customer_name="Jane Doe",
        service_type="Bridal Makeup",
        booking_date="2023-12-25",
        booking_time="10:00",
        customer_email="jane@example.com",
        customer_phone="+1234567890"
    )
    
    print(f"Created booking: {booking['id']}")
    
    # Send reminders for upcoming appointments
    manager.send_reminders()
```
