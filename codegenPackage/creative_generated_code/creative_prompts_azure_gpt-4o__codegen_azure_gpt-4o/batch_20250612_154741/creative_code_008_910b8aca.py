"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://serveutah.com
Prompt: Write code to track court docket schedules and notify users of their case position for guardianship hearings, based on the Serve Utah process.
Generated: DETERMINISTIC_910b8aca49df7985
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
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart


class CourtDocketScheduler:
    """
    Class to manage and track court docket schedules, notify users of their case positions,
    and schedule guardianship hearings based on Serve Utah process.
    """

    def __init__(self, smtp_server, smtp_port, email, password):
        """
        Initialize the scheduler with email configuration for notifications.

        :param smtp_server: SMTP server address for sending emails
        :param smtp_port: SMTP server port
        :param email: Email address used to send notifications
        :param password: Password for email authentication
        """
        self.docket_schedule = []
        self.smtp_server = smtp_server
        self.smtp_port = smtp_port
        self.email = email
        self.password = password

    def add_case(self, case_number, claimant_email, hearing_date):
        """
        Add a case to the docket schedule.

        :param case_number: Unique case number
        :param claimant_email: Email address of the claimant
        :param hearing_date: Scheduled date and time of the hearing (datetime object)
        """
        case_entry = {
            "case_number": case_number,
            "claimant_email": claimant_email,
            "hearing_date": hearing_date,
        }
        self.docket_schedule.append(case_entry)
        self.docket_schedule.sort(key=lambda x: x["hearing_date"])  # Sort by hearing date for proper scheduling

    def get_case_position(self, case_number):
        """
        Get current position of a case in the docket schedule.

        :param case_number: Unique case number
        :return: Position of the case in the schedule (1-indexed). Returns None if case not found.
        """
        for index, case in enumerate(self.docket_schedule):
            if case["case_number"] == case_number:
                return index + 1
        return None

    def notify_claimant(self, case_number):
        """
        Notify claimant of their case position via email.

        :param case_number: Unique case number
        """
        case = next((case for case in self.docket_schedule if case["case_number"] == case_number), None)
        if not case:
            raise ValueError("Case number not found in docket schedule.")

        position = self.get_case_position(case_number)
        hearing_date = case["hearing_date"].strftime('%Y-%m-%d %H:%M:%S')
        claimant_email = case["claimant_email"]

        # Create email content
        subject = f"Notification for Case #{case_number}"
        body = (
            f"Dear claimant,\n\n"
            f"You are scheduled for a guardianship hearing on {hearing_date}. "
            f"Your current position in the docket is: {position}.\n\n"
            f"Thank you,\nServe Utah"
        )

        # Send the email
        self._send_email(claimant_email, subject, body)

    def _send_email(self, to_email, subject, body):
        """
        Send an email using SMTP.

        :param to_email: Recipient's email address
        :param subject: Subject of the email
        :param body: Body content of the email
        """
        try:
            # Create email message
            msg = MIMEMultipart()
            msg["From"] = self.email
            msg["To"] = to_email
            msg["Subject"] = subject
            msg.attach(MIMEText(body, "plain"))

            # Connect to SMTP server and send email
            with smtplib.SMTP(self.smtp_server, self.smtp_port) as server:
                server.starttls()  # Start TLS for security
                server.login(self.email, self.password)
                server.send_message(msg)

        except Exception as e:
            print(f"Failed to send email to {to_email}: {e}")

    def remove_case(self, case_number):
        """
        Remove a case from the docket schedule.

        :param case_number: Unique case number
        """
        self.docket_schedule = [case for case in self.docket_schedule if case["case_number"] != case_number]


# Example Usage - Replace with actual system initialization and input sources
if __name__ == "__main__":
    # Initialize scheduler with email configuration
    scheduler = CourtDocketScheduler(
        smtp_server="smtp.example.com",
        smtp_port=587,
        email="your_email@example.com",
        password="your_password"
    )

    # Add cases to schedule
    scheduler.add_case(case_number="12345", claimant_email="claimant1@example.com",
                       hearing_date=datetime.datetime(2023, 11, 5, 10, 30))
    scheduler.add_case(case_number="67890", claimant_email="claimant2@example.com",
                       hearing_date=datetime.datetime(2023, 11, 5, 11, 30))

    # Notify claimants about their case position
    scheduler.notify_claimant(case_number="12345")
    scheduler.notify_claimant(case_number="67890")
```
