"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://jinlinghospital.com
Prompt: Write a Python script to simulate appointment scheduling for Jinling Hospital, including fields for patient name, department (e.g., cardiology, neurology, pediatrics), preferred date and time, and confirmation via email.
Generated: DETERMINISTIC_a588ee2f5a0f9141
Batch ID: 20250612_151024
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from datetime import datetime
import re

class Appointment:
    def __init__(self, patient_name, department, preferred_datetime, email):
        self.patient_name = patient_name
        self.department = department
        self.preferred_datetime = preferred_datetime
        self.email = email

    def validate_email(self):
        """Validate the email address format."""
        email_regex = r'^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$'
        return re.match(email_regex, self.email) is not None

    def confirm_appointment(self):
        """Send a confirmation email for the scheduled appointment."""
        if not self.validate_email():
            raise ValueError("Invalid email address format.")

        subject = "Appointment Confirmation"
        body = (f"Dear {self.patient_name},\n\n"
                f"Your appointment has been scheduled.\n"
                f"Department: {self.department}\n"
                f"Date and Time: {self.preferred_datetime.strftime('%Y-%m-%d %H:%M')}\n\n"
                "Thank you for choosing Jinling Hospital.\n\n"
                "Best regards,\n"
                "Jinling Hospital")

        # Create the email message
        msg = MIMEMultipart()
        msg['From'] = 'noreply@jinlinghospital.com'
        msg['To'] = self.email
        msg['Subject'] = subject
        msg.attach(MIMEText(body, 'plain'))

        try:
            # Setup the server
            with smtplib.SMTP('smtp.jinlinghospital.com', 587) as server:
                server.starttls()  # Secure the connection
                server.login('noreply@jinlinghospital.com', 'your_password')  # Use your email server credentials
                server.send_message(msg)
            print("Confirmation email sent successfully.")
        except Exception as e:
            print(f"Error sending email: {e}")

def schedule_appointment():
    """Gather appointment details from the user and schedule the appointment."""
    try:
        patient_name = input("Enter the patient's name: ")
        department = input("Enter the department (e.g., cardiology, neurology, pediatrics): ")
        date_str = input("Enter preferred date and time (YYYY-MM-DD HH:MM): ")
        preferred_datetime = datetime.strptime(date_str, '%Y-%m-%d %H:%M')
        email = input("Enter the patient's email: ")

        # Create the appointment object
        appointment = Appointment(patient_name, department, preferred_datetime, email)
        appointment.confirm_appointment()

    except ValueError as ve:
        print(f"Input error: {ve}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

if __name__ == "__main__":
    schedule_appointment()
```

**Note:** 
- Replace `'your_password'` with the actual password for the email account used to send confirmation emails.
- Ensure the SMTP server and credentials align with your email provider's specifications.
