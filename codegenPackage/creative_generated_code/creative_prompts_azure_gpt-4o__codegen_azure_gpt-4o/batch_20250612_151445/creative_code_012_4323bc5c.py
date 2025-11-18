"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://demoablabs.com
Prompt: Write a program to track sample turnaround times and send notifications based on A & B Labs' standard TAT policies.
Generated: DETERMINISTIC_4323bc5c7a49ab7d
Batch ID: 20250612_151445
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

class TurnaroundTimeTracker:
    def __init__(self):
        # Define standard TAT policies for A & B Labs in days
        self.lab_tat_policies = {
            "A Lab": 7,  # A Lab standard turnaround time in days
            "B Lab": 5   # B Lab standard turnaround time in days
        }
        self.sample_records = []  # List to track sample data

    def add_sample(self, sample_id, lab_name, submission_date):
        """
        Add a sample to the tracking system.
        :param sample_id: Unique identifier for the sample
        :param lab_name: Name of the lab ('A Lab' or 'B Lab')
        :param submission_date: Date the sample was submitted (datetime.date object)
        """
        if lab_name not in self.lab_tat_policies:
            raise ValueError(f"Lab name '{lab_name}' is not recognized.")
        self.sample_records.append({
            "sample_id": sample_id,
            "lab_name": lab_name,
            "submission_date": submission_date,
            "notified": False  # Flag to track whether a notification was sent
        })

    def check_turnaround_times(self):
        """
        Check all samples for overdue TAT and send notifications if required.
        """
        today = datetime.date.today()
        for record in self.sample_records:
            lab_name = record["lab_name"]
            submission_date = record["submission_date"]
            tat_days = self.lab_tat_policies[lab_name]

            # Calculate the due date
            due_date = submission_date + datetime.timedelta(days=tat_days)
            
            # If overdue and notification hasn't been sent yet
            if today > due_date and not record["notified"]:
                self.send_notification(record["sample_id"], lab_name, due_date)
                record["notified"] = True  # Mark as notified

    def send_notification(self, sample_id, lab_name, due_date):
        """
        Send an email notification about a delayed sample.
        :param sample_id: Unique identifier for the sample
        :param lab_name: Name of the lab ('A Lab' or 'B Lab')
        :param due_date: Due date when the sample should have been completed
        """
        try:
            # Email settings (customize these for your environment)
            sender_email = "notifications@example.com"
            recipient_email = "labmanager@example.com"
            smtp_server = "smtp.example.com"
            smtp_port = 587
            smtp_username = "your_username"
            smtp_password = "your_password"

            # Email content
            subject = f"Sample {sample_id} Delayed in {lab_name}"
            body = f"The sample with ID {sample_id} submitted to {lab_name} is overdue.\n" \
                   f"It was due on {due_date.strftime('%Y-%m-%d')}. Please take appropriate action."

            # Create and send the email
            msg = MIMEText(body)
            msg['Subject'] = subject
            msg['From'] = sender_email
            msg['To'] = recipient_email

            with smtplib.SMTP(smtp_server, smtp_port) as server:
                server.starttls()  # Secure the connection
                server.login(smtp_username, smtp_password)
                server.send_message(msg)

            print(f"Notification sent for sample {sample_id} overdue in {lab_name}.")
        except Exception as e:
            print(f"Failed to send notification for sample {sample_id}: {e}")

# Example usage (Uncomment this code block for testing)
# tracker = TurnaroundTimeTracker()
# tracker.add_sample("SAMPLE123", "A Lab", datetime.date(2023, 10, 1))
# tracker.add_sample("SAMPLE456", "B Lab", datetime.date(2023, 10, 5))
# tracker.check_turnaround_times()
```
