"""
Generated Code Metadata:
========================
Original URL: https://serveutah.com
Prompt: Write code to track court docket schedules and notify users of their case position for guardianship hearings, based on the Serve Utah process.
Generated: DETERMINISTIC_910b8aca49df7985
Batch ID: 20250612_154741
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import datetime
import smtplib
from email.mime.text import MIMEText
from typing import List, Dict, Any

class CourtDocket:
    def __init__(self):
        # Initialize an empty docket list
        self.docket: List[Dict[str, Any]] = []

    def add_case(self, case_id: str, hearing_date: str, user_email: str):
        """
        Add a new case to the docket.

        :param case_id: Unique identifier for the case
        :param hearing_date: Date of the hearing in 'YYYY-MM-DD' format
        :param user_email: Email address of the user to notify
        """
        try:
            # Convert hearing_date to a datetime object for validation
            hearing_date_obj = datetime.datetime.strptime(hearing_date, '%Y-%m-%d')
            self.docket.append({
                'case_id': case_id,
                'hearing_date': hearing_date_obj,
                'user_email': user_email
            })
        except ValueError as e:
            print(f"Error adding case: {e}")

    def notify_users(self):
        """
        Notify users of their case position for upcoming hearings.
        """
        today = datetime.datetime.now()
        for case in self.docket:
            if case['hearing_date'] <= today + datetime.timedelta(days=7):
                self.send_notification(case['user_email'], case['case_id'], case['hearing_date'])

    def send_notification(self, user_email: str, case_id: str, hearing_date: datetime.datetime):
        """
        Send an email notification to the user about their case hearing.

        :param user_email: Email address of the user to notify
        :param case_id: Unique identifier for the case
        :param hearing_date: Date of the hearing
        """
        subject = f"Upcoming Hearing Notification for Case {case_id}"
        body = f"Dear User,\n\nThis is a reminder that your guardianship hearing for case {case_id} is scheduled on {hearing_date.strftime('%Y-%m-%d')}.\n\nBest regards,\nCourt Docket System"

        # Create the email message
        msg = MIMEText(body)
        msg['Subject'] = subject
        msg['From'] = 'noreply@court-docket-system.com'
        msg['To'] = user_email

        try:
            # Send the email (using a dummy SMTP server for demonstration)
            with smtplib.SMTP('localhost') as server:
                server.send_message(msg)
            print(f"Notification sent to {user_email} for case {case_id}.")
        except Exception as e:
            print(f"Failed to send email to {user_email}: {e}")

# Example usage
if __name__ == "__main__":
    docket = CourtDocket()
    docket.add_case('G123', '2023-11-15', 'user@example.com')
    docket.add_case('G124', '2023-11-20', 'user2@example.com')
    docket.notify_users()
```
