"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://asnetinfotech.com
Prompt: Create a Python script to automate appointment setting and lead generation tasks, using methodologies similar to those offered by Asnet Infotech.
Generated: DETERMINISTIC_c0a5bafbdffc28a6
Batch ID: 20250612_152924
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import datetime
import random
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from typing import List, Dict, Optional

class AppointmentScheduler:
    """Class to manage appointment setting and lead generation."""

    def __init__(self, email: str, password: str):
        """Initialize the appointment scheduler with email credentials."""
        self.email = email
        self.password = password
        self.leads: List[Dict[str, str]] = []

    def add_lead(self, name: str, email: str, phone: str) -> None:
        """Add a new lead to the leads list."""
        lead = {"name": name, "email": email, "phone": phone}
        self.leads.append(lead)

    def schedule_appointment(self, lead: Dict[str, str], date: str) -> None:
        """Schedule an appointment for a given lead."""
        lead_name = lead.get("name")
        if self._is_valid_date(date):
            print(f"Appointment scheduled for {lead_name} on {date}.")
            self.send_confirmation_email(lead, date)
        else:
            raise ValueError("Invalid date format. Please use 'YYYY-MM-DD'.")

    def send_confirmation_email(self, lead: Dict[str, str], date: str) -> None:
        """Send a confirmation email to the lead."""
        recipient_email = lead.get("email")
        subject = "Appointment Confirmation"
        body = f"Hello {lead['name']},\n\nYour appointment is scheduled for {date}.\n\nBest Regards,\nAppointment Scheduler"

        # Set up the email server
        try:
            with smtplib.SMTP('smtp.gmail.com', 587) as server:
                server.starttls()
                server.login(self.email, self.password)

                # Create email
                msg = MIMEMultipart()
                msg['From'] = self.email
                msg['To'] = recipient_email
                msg['Subject'] = subject
                msg.attach(MIMEText(body, 'plain'))

                # Send email
                server.sendmail(self.email, recipient_email, msg.as_string())
                print(f"Confirmation email sent to {recipient_email}.")
        except Exception as e:
            print(f"Failed to send email: {e}")

    @staticmethod
    def _is_valid_date(date_str: str) -> bool:
        """Check if the date string is in the correct format."""
        try:
            datetime.datetime.strptime(date_str, "%Y-%m-%d")
            return True
        except ValueError:
            return False

# Example usage
if __name__ == "__main__":
    # Replace with your email and password
    EMAIL = "your_email@gmail.com"
    PASSWORD = "your_password"

    scheduler = AppointmentScheduler(EMAIL, PASSWORD)

    # Example leads
    scheduler.add_lead("Alice Smith", "alice@example.com", "555-1234")
    scheduler.add_lead("Bob Johnson", "bob@example.com", "555-5678")

    # Schedule appointments
    try:
        for lead in scheduler.leads:
            appointment_date = (datetime.datetime.now() + datetime.timedelta(days=random.randint(1, 30))).strftime("%Y-%m-%d")
            scheduler.schedule_appointment(lead, appointment_date)
    except Exception as e:
        print(f"Error scheduling appointment: {e}")
```

Make sure to replace `your_email@gmail.com` and `your_password` with valid credentials and ensure that the email account allows less secure apps if using Gmail or utilize an app password if 2FA is enabled.
