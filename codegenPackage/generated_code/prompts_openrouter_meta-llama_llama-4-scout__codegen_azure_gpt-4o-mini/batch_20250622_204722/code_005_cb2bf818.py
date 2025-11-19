"""
Generated Code Metadata:
========================
Original URL: https://ankarateknikservisi.com
Prompt: What are the benefits of regular maintenance for white goods appliances, and how can I schedule a periodic maintenance service with Ankara Beyaz Eşya Teknik Servisi for my Arçelik and Beko devices?
Generated: DETERMINISTIC_cb2bf8182fd5e1cd
Batch ID: 20250622_204722
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
from email.mime.multipart import MIMEMultipart

class ApplianceMaintenanceScheduler:
    def __init__(self, service_email, user_email):
        """
        Initializes the scheduler with service and user email addresses.
        
        :param service_email: Email address of the maintenance service
        :param user_email: User's email address for notifications
        """
        self.service_email = service_email
        self.user_email = user_email

    def schedule_maintenance(self, appliance_type, date):
        """
        Schedules a maintenance service for the specified appliance type on the given date.
        
        :param appliance_type: Type of the appliance (e.g., 'Arçelik', 'Beko')
        :param date: Date for the maintenance service (datetime object)
        :return: Confirmation message
        """
        if not isinstance(date, datetime.date):
            raise ValueError("Date must be a datetime.date object.")
        
        if date < datetime.date.today():
            raise ValueError("Scheduled date cannot be in the past.")
        
        # Prepare the email content
        subject = f"Maintenance Request for {appliance_type}"
        body = f"Requesting maintenance for {appliance_type} on {date.strftime('%Y-%m-%d')}."
        
        # Send the email
        self.send_email(subject, body)
        
        return f"Maintenance scheduled for {appliance_type} on {date.strftime('%Y-%m-%d')}."

    def send_email(self, subject, body):
        """
        Sends an email to the maintenance service.
        
        :param subject: Subject of the email
        :param body: Body content of the email
        """
        try:
            # Create the email message
            msg = MIMEMultipart()
            msg['From'] = self.user_email
            msg['To'] = self.service_email
            msg['Subject'] = subject
            
            msg.attach(MIMEText(body, 'plain'))
            
            # Connect to the SMTP server and send the email
            with smtplib.SMTP('smtp.example.com', 587) as server:  # Replace with actual SMTP server
                server.starttls()
                server.login(self.user_email, 'your_password')  # Replace with actual password
                server.send_message(msg)
        
        except Exception as e:
            print(f"Error sending email: {e}")

# Example usage
if __name__ == "__main__":
    try:
        service_email = "service@ankarabeyazesya.com"  # Replace with actual service email
        user_email = "user@example.com"  # Replace with actual user email
        scheduler = ApplianceMaintenanceScheduler(service_email, user_email)
        
        # Schedule maintenance for an Arçelik appliance
        maintenance_date = datetime.date(2023, 12, 15)  # Example date
        confirmation = scheduler.schedule_maintenance("Arçelik", maintenance_date)
        print(confirmation)
        
    except Exception as e:
        print(f"An error occurred: {e}")
```
