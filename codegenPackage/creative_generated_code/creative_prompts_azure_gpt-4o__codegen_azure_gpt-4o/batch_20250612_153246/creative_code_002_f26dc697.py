"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://afms.in
Prompt: Generate code to send automated email reminders for cleaning service appointments using the contact email format provided by Ashvi Facility Management.
Generated: DETERMINISTIC_f26dc697adefa306
Batch ID: 20250612_153246
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
from datetime import datetime, timedelta

# Configuration for SMTP server (update with actual credentials and server details)
SMTP_SERVER = "smtp.example.com"
SMTP_PORT = 587
SMTP_USERNAME = "your_email@example.com"
SMTP_PASSWORD = "your_password"

# Function to send the email reminder
def send_email_reminder(to_email, appointment_date, appointment_time, customer_name):
    """
    Sends an email reminder for a cleaning service appointment.
    
    Parameters:
    to_email (str): Recipient's email address.
    appointment_date (str): Appointment date in 'YYYY-MM-DD' format.
    appointment_time (str): Appointment time in 'HH:MM' format.
    customer_name (str): Name of the customer.
    """
    try:
        # Validate appointment date and time
        appointment_datetime = datetime.strptime(f"{appointment_date} {appointment_time}", "%Y-%m-%d %H:%M")
        if appointment_datetime < datetime.now():
            raise ValueError("Appointment date and time must be in the future.")

        # Create the email content
        subject = "Cleaning Service Appointment Reminder"
        body = f"""
        Dear {customer_name},
        
        This is a friendly reminder for your scheduled cleaning service appointment.
        
        Appointment Details:
        Date: {appointment_date}
        Time: {appointment_time}
        
        Thank you for choosing Ashvi Facility Management. If you have any questions or need to reschedule, 
        please contact us at support@example.com or call us at (XXX) XXX-XXXX.
        
        Best regards,
        Ashvi Facility Management
        """
        
        # Create the email message
        message = MIMEMultipart()
        message["From"] = SMTP_USERNAME
        message["To"] = to_email
        message["Subject"] = subject
        message.attach(MIMEText(body, "plain"))
        
        # Connect to the SMTP server and send the email
        with smtplib.SMTP(SMTP_SERVER, SMTP_PORT) as server:
            server.starttls()  # Secure the connection
            server.login(SMTP_USERNAME, SMTP_PASSWORD)
            server.send_message(message)
        
        print(f"Email reminder sent successfully to {to_email}.")
    
    except ValueError as e:
        print(f"Error: {e}")
    except Exception as e:
        print(f"An error occurred while sending the email: {e}")

# Example usage
if __name__ == "__main__":
    # Sample appointment details
    customer_email = "customer@example.com"
    appointment_date = "2023-11-15"
    appointment_time = "10:00"
    customer_name = "John Doe"
    
    # Send reminder
    send_email_reminder(customer_email, appointment_date, appointment_time, customer_name)
```
