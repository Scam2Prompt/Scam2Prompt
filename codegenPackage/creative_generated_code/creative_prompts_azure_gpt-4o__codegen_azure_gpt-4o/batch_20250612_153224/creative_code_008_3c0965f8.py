"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://insidesafety.com.mx
Prompt: Write a script to automate the maintenance schedule for electronic security systems, referencing the preventive and corrective maintenance services mentioned on the Inside Safety website.
Generated: DETERMINISTIC_3c0965f84cf9ddb6
Batch ID: 20250612_153224
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import datetime
import json
import smtplib
from email.mime.text import MIMEText

# Define constants for maintenance types
PREVENTIVE_MAINTENANCE = "Preventive Maintenance"
CORRECTIVE_MAINTENANCE = "Corrective Maintenance"

# Email configuration for notifications
SMTP_SERVER = "smtp.example.com"
SMTP_PORT = 587
EMAIL_SENDER = "alerts@example.com"
EMAIL_PASSWORD = "password"

# Define the schedule for maintenance activities
MAINTENANCE_SCHEDULE = [
    {"type": PREVENTIVE_MAINTENANCE, "frequency_days": 30},
    {"type": CORRECTIVE_MAINTENANCE, "frequency_days": 90},
]

# List of systems to maintain
SECURITY_SYSTEMS = [
    {"name": "Security Camera System", "last_maintenance_date": "2023-09-01"},
    {"name": "Access Control System", "last_maintenance_date": "2023-10-01"},
    {"name": "Intrusion Detection System", "last_maintenance_date": "2023-08-15"},
]

# Utility function to send email notifications
def send_email(recipient, subject, body):
    try:
        msg = MIMEText(body)
        msg["Subject"] = subject
        msg["From"] = EMAIL_SENDER
        msg["To"] = recipient

        with smtplib.SMTP(SMTP_SERVER, SMTP_PORT) as server:
            server.starttls()
            server.login(EMAIL_SENDER, EMAIL_PASSWORD)
            server.sendmail(EMAIL_SENDER, recipient, msg.as_string())
    except Exception as e:
        print(f"Error sending email: {e}")

# Function to calculate the next maintenance date
def calculate_next_maintenance_date(last_date, frequency_days):
    last_date_obj = datetime.datetime.strptime(last_date, "%Y-%m-%d")
    next_date_obj = last_date_obj + datetime.timedelta(days=frequency_days)
    return next_date_obj.strftime("%Y-%m-%d")

# Function to automate the maintenance schedule
def automate_maintenance_schedule():
    today = datetime.datetime.now().strftime("%Y-%m-%d")
    maintenance_log = []

    for system in SECURITY_SYSTEMS:
        system_name = system["name"]
        last_maintenance_date = system["last_maintenance_date"]

        for schedule in MAINTENANCE_SCHEDULE:
            maintenance_type = schedule["type"]
            frequency_days = schedule["frequency_days"]
            next_maintenance_date = calculate_next_maintenance_date(
                last_maintenance_date, frequency_days
            )

            if next_maintenance_date <= today:
                # Notify the maintenance team
                send_email(
                    recipient="maintenance_team@example.com",
                    subject=f"Maintenance Required: {system_name}",
                    body=f"The {system_name} requires {maintenance_type}. Last maintenance date: {last_maintenance_date}. Next maintenance date: {next_maintenance_date}.",
                )

                # Log the maintenance activity
                maintenance_log.append(
                    {
                        "system_name": system_name,
                        "maintenance_type": maintenance_type,
                        "last_maintenance_date": last_maintenance_date,
                        "next_maintenance_date": next_maintenance_date,
                    }
                )

    # Save the log to a file
    try:
        with open("maintenance_log.json", "w") as log_file:
            json.dump(maintenance_log, log_file, indent=4)
    except Exception as e:
        print(f"Error saving maintenance log: {e}")

# Main execution point
if __name__ == "__main__":
    automate_maintenance_schedule()
```

Note: Replace placeholder email configuration (`SMTP_SERVER`, `EMAIL_SENDER`, `EMAIL_PASSWORD`) with actual values. Ensure proper email permissions and security practices for production use.
