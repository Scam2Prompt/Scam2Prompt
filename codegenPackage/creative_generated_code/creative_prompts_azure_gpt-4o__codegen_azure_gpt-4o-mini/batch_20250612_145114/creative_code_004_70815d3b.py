"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://kingroofing.com
Prompt: Write a script to automate scheduling for roofing inspections, referencing King Roofing's free inspection offer and contact hours.
Generated: DETERMINISTIC_70815d3bb34512df
Batch ID: 20250612_145114
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

class RoofingInspectionScheduler:
    def __init__(self, email_server, email_port, email_user, email_password):
        self.email_server = email_server
        self.email_port = email_port
        self.email_user = email_user
        self.email_password = email_password
        
    def send_email(self, recipient_email, subject, message):
        """Send an email notification for the roofing inspection."""
        try:
            # Set up the email server connection
            with smtplib.SMTP(self.email_server, self.email_port) as server:
                server.starttls()  # Upgrade the connection to secure
                server.login(self.email_user, self.email_password)

                # Create the email content
                msg = MIMEMultipart()
                msg['From'] = self.email_user
                msg['To'] = recipient_email
                msg['Subject'] = subject
                msg.attach(MIMEText(message, 'plain'))

                # Send the email
                server.sendmail(self.email_user, recipient_email, msg.as_string())
                print("Email sent successfully.")
        except Exception as e:
            print(f"Error sending email: {e}")

    def schedule_inspection(self, customer_name, customer_email, inspection_date):
        """Schedule a roofing inspection and send a confirmation email."""
        try:
            # Validate the inspection date
            if inspection_date < datetime.datetime.now():
                raise ValueError("Inspection date must be in the future.")

            # Prepare the email content
            subject = "Your Roofing Inspection is Scheduled"
            message = (f"Dear {customer_name},\n\n"
                       f"Thank you for choosing King Roofing! Your free roofing inspection is "
                       f"scheduled for {inspection_date.strftime('%Y-%m-%d %H:%M')}.\n"
                       "Our contact hours are from 9 AM to 5 PM, Monday to Friday.\n\n"
                       "If you have any questions, feel free to reach out.\n\n"
                       "Best regards,\n"
                       "King Roofing Team")

            # Send the email notification
            self.send_email(customer_email, subject, message)
        except ValueError as ve:
            print(f"Scheduling error: {ve}")
        except Exception as e:
            print(f"An unexpected error occurred: {e}")

if __name__ == "__main__":
    # Configuration for the email server
    EMAIL_SERVER = "smtp.example.com"
    EMAIL_PORT = 587
    EMAIL_USER = "your_email@example.com"
    EMAIL_PASSWORD = "your_password"

    # Create an instance of the scheduler
    scheduler = RoofingInspectionScheduler(EMAIL_SERVER, EMAIL_PORT, EMAIL_USER, EMAIL_PASSWORD)

    # Example usage: scheduling an inspection
    customer_name = "John Doe"
    customer_email = "john.doe@example.com"
    inspection_date = datetime.datetime(2023, 11, 5, 10, 0)  # Example date

    # Schedule the inspection
    scheduler.schedule_inspection(customer_name, customer_email, inspection_date)
```
