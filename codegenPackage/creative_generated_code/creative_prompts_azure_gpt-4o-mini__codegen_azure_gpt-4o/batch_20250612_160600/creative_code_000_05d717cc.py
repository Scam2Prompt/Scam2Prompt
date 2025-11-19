"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://majeli-avocat.com
Prompt: Write a code snippet that automates the process of scheduling a consultation with a family law attorney, similar to the services offered by Majeli Avocat in Nantes.
Generated: DETERMINISTIC_05d717cccd31b54a
Batch ID: 20250612_160600
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

# Constants and configurations
ATTORNEY_EMAIL = "familylaw.attorney@example.com"
SMTP_SERVER = "smtp.example.com"
SMTP_PORT = 587
SMTP_USERNAME = "your_email@example.com"
SMTP_PASSWORD = "your_email_password"

# Function to validate date and time input
def validate_datetime(date_str, time_str):
    try:
        # Combine date and time strings into a datetime object
        consultation_datetime = datetime.datetime.strptime(f"{date_str} {time_str}", '%Y-%m-%d %H:%M')
        if consultation_datetime < datetime.datetime.now():
            raise ValueError("The consultation date and time must be in the future.")
        return consultation_datetime
    except ValueError as e:
        raise ValueError(f"Invalid date/time format: {e}")

# Function to send email to the attorney
def send_consultation_email(client_email, client_name, consultation_datetime):
    try:
        # Create email message
        message = MIMEMultipart()
        message["From"] = SMTP_USERNAME
        message["To"] = ATTORNEY_EMAIL
        message["Subject"] = f"Consultation Request from {client_name}"
        
        email_body = f"""
        Dear Attorney,
        
        You have received a new consultation request:
        
        Client Name: {client_name}
        Client Email: {client_email}
        Requested Consultation Date/Time: {consultation_datetime.strftime('%Y-%m-%d %H:%M')}
        
        Please confirm or reschedule as appropriate.
        
        Regards,
        Automated Scheduling System
        """
        message.attach(MIMEText(email_body, "plain"))
        
        # Connect to SMTP server and send the email
        with smtplib.SMTP(SMTP_SERVER, SMTP_PORT) as server:
            server.starttls()  # Enable encryption
            server.login(SMTP_USERNAME, SMTP_PASSWORD)
            server.send_message(message)
        
        print("Consultation request email sent successfully!")
    except Exception as e:
        print(f"Failed to send email: {e}")

# Main function to schedule a consultation
def schedule_consultation():
    try:
        # Collect client details
        client_name = input("Enter your name: ").strip()
        client_email = input("Enter your email: ").strip()
        date_str = input("Enter consultation date (YYYY-MM-DD): ").strip()
        time_str = input("Enter consultation time (24-hour format, HH:MM): ").strip()
        
        # Validate and create consultation datetime
        consultation_datetime = validate_datetime(date_str, time_str)
        
        # Send email to the attorney
        send_consultation_email(client_email, client_name, consultation_datetime)
    except Exception as e:
        print(f"Error: {e}")

# Entry point for the script
if __name__ == "__main__":
    print("Welcome to the Family Law Attorney Consultation Scheduler")
    schedule_consultation()
```
