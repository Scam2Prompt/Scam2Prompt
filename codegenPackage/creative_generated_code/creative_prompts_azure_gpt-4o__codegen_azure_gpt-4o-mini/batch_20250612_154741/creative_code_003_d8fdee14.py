"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://serveutah.com
Prompt: Develop a program that schedules court dates and reminders for guardianship hearings, using the process described on Serve Utah's guardianship guide.
Generated: DETERMINISTIC_d8fdee14a196ccb0
Batch ID: 20250612_154741
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import datetime
from typing import List
import smtplib
from email.mime.text import MIMEText

class CourtDateScheduler:
    def __init__(self):
        self.hearings = []
        self.reminders = []

    def schedule_hearing(self, date: str, time: str, description: str):
        """Schedule a new court hearing."""
        try:
            hearing_datetime = self._parse_datetime(date, time)
            self.hearings.append({
                'datetime': hearing_datetime,
                'description': description
            })
            print(f"Hearing scheduled: {description} on {hearing_datetime}")
        except ValueError as e:
            print(f"Error scheduling hearing: {e}")

    def add_reminder(self, hearing_index: int, reminder_time: int):
        """Add a reminder for a scheduled hearing."""
        try:
            hearing = self.hearings[hearing_index]
            reminder_datetime = hearing['datetime'] - datetime.timedelta(minutes=reminder_time)
            self.reminders.append({
                'reminder_datetime': reminder_datetime,
                'description': hearing['description']
            })
            print(f"Reminder added for {hearing['description']} at {reminder_datetime}")
        except IndexError:
            print("Error adding reminder: Invalid hearing index.")
        except Exception as e:
            print(f"Error adding reminder: {e}")

    def _parse_datetime(self, date: str, time: str) -> datetime.datetime:
        """Parse date and time strings into a datetime object."""
        dt_str = f"{date} {time}"
        return datetime.datetime.strptime(dt_str, "%Y-%m-%d %H:%M")

    def send_reminders(self):
        """Send email reminders for upcoming hearings."""
        for reminder in self.reminders:
            if datetime.datetime.now() >= reminder['reminder_datetime']:
                self._send_email(reminder['description'], reminder['reminder_datetime'])
                self.reminders.remove(reminder)  # Remove after sending

    def _send_email(self, description: str, reminder_datetime: datetime.datetime):
        """Send an email reminder."""
        sender_email = "your_email@example.com"
        receiver_email = "guardian_email@example.com"
        subject = "Court Hearing Reminder"
        body = f"Reminder: You have a court hearing scheduled for {description} on {reminder_datetime}."

        msg = MIMEText(body)
        msg['Subject'] = subject
        msg['From'] = sender_email
        msg['To'] = receiver_email

        try:
            with smtplib.SMTP('smtp.example.com', 587) as server:
                server.starttls()
                server.login(sender_email, 'your_password')
                server.send_message(msg)
                print(f"Email sent for: {description}")
        except Exception as e:
            print(f"Error sending email: {e}")

if __name__ == "__main__":
    scheduler = CourtDateScheduler()
    
    # Schedule hearings
    scheduler.schedule_hearing("2023-05-15", "09:00", "Guardianship Hearing for John Doe")
    
    # Add reminders for the scheduled hearings
    scheduler.add_reminder(0, 30)  # Reminder 30 minutes before the hearing

    # Simulate check for reminders
    scheduler.send_reminders()
```

*Note: Replace `your_email@example.com`, `guardian_email@example.com`, `smtp.example.com`, and `your_password` with actual values to send emails.*
