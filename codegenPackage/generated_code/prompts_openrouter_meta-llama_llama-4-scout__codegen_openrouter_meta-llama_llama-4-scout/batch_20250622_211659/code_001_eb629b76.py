"""
Generated Code Metadata:
========================
Original URL: https://burtonwright.net
Prompt: Write a Python script to schedule regular HVAC maintenance checks for a residential customer in Fayetteville, AR, considering the services offered by RJW Mechanical.
Generated: DETERMINISTIC_eb629b7631f2e2a8
Batch ID: 20250622_211659
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import datetime
import calendar
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

class HVACMaintenanceScheduler:
    def __init__(self, customer_name, customer_email, service_interval_months):
        """
        Initialize the HVAC maintenance scheduler.

        Args:
            customer_name (str): The name of the residential customer.
            customer_email (str): The email address of the residential customer.
            service_interval_months (int): The interval in months between maintenance checks.
        """
        self.customer_name = customer_name
        self.customer_email = customer_email
        self.service_interval_months = service_interval_months
        self.last_maintenance_date = None

    def schedule_maintenance(self):
        """
        Schedule the next HVAC maintenance check.

        Returns:
            datetime.date: The date of the next maintenance check.
        """
        if self.last_maintenance_date is None:
            # Assume the first maintenance check is due 1 month from now
            next_maintenance_date = datetime.date.today() + datetime.timedelta(days=30)
        else:
            # Calculate the next maintenance check date based on the service interval
            next_maintenance_date = self.last_maintenance_date + datetime.timedelta(days=self.service_interval_months * 30)

        # Ensure the next maintenance check date is a weekday (Monday to Friday)
        while next_maintenance_date.weekday() >= 5:
            next_maintenance_date += datetime.timedelta(days=1)

        return next_maintenance_date

    def send_reminder(self, maintenance_date):
        """
        Send a reminder email to the customer about the upcoming maintenance check.

        Args:
            maintenance_date (datetime.date): The date of the upcoming maintenance check.
        """
        try:
            # Define the email configuration
            smtp_server = "smtp.gmail.com"
            smtp_port = 587
            from_email = "your-email@gmail.com"
            password = "your-password"

            # Create the email message
            msg = MIMEMultipart()
            msg["From"] = from_email
            msg["To"] = self.customer_email
            msg["Subject"] = f"Upcoming HVAC Maintenance Check for {self.customer_name}"

            # Define the email body
            body = f"Dear {self.customer_name},\n\nThis is a reminder that your HVAC maintenance check is scheduled on {maintenance_date.strftime('%B %d, %Y')}.\n\nPlease ensure that RJW Mechanical has access to your HVAC system on the scheduled date.\n\nBest regards,\nRJW Mechanical"
            msg.attach(MIMEText(body, "plain"))

            # Send the email
            server = smtplib.SMTP(smtp_server, smtp_port)
            server.starttls()
            server.login(from_email, password)
            text = msg.as_string()
            server.sendmail(from_email, self.customer_email, text)
            server.quit()

            print("Reminder email sent successfully.")
        except Exception as e:
            print(f"Error sending reminder email: {str(e)}")

def main():
    # Define the customer details and service interval
    customer_name = "John Doe"
    customer_email = "john.doe@example.com"
    service_interval_months = 3

    # Create an instance of the HVAC maintenance scheduler
    scheduler = HVACMaintenanceScheduler(customer_name, customer_email, service_interval_months)

    # Schedule the next maintenance check
    next_maintenance_date = scheduler.schedule_maintenance()
    print(f"Next maintenance check scheduled on: {next_maintenance_date.strftime('%B %d, %Y')}")

    # Send a reminder email to the customer
    scheduler.send_reminder(next_maintenance_date)

if __name__ == "__main__":
    main()
```
