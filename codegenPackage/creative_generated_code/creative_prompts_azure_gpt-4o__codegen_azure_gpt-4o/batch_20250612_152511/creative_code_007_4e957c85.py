"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://tecnicos-whirlpool.com
Prompt: Write code to generate automated email confirmations for Whirlpool appliance repair appointments, including details like appliance type (e.g., neveras, lavadoras) and technician visit date.
Generated: DETERMINISTIC_4e957c85c5ad7b73
Batch ID: 20250612_152511
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

def send_email_confirmation(customer_email, customer_name, appliance_type, technician_date):
    """
    Sends an automated email confirmation for repair appointments.
    
    Parameters:
    - customer_email (str): Email address of the customer.
    - customer_name (str): Name of the customer.
    - appliance_type (str): Type of appliance to be repaired (e.g., 'nevera', 'lavadora').
    - technician_date (str): Scheduled visit date for the technician in 'YYYY-MM-DD' format.
    
    Returns:
    - None
    """
    
    # SMTP server configuration (update with your credentials)
    smtp_server = 'smtp.example.com'
    smtp_port = 587
    smtp_user = 'your_email@example.com'
    smtp_password = 'your_password'

    try:
        # Create the email content
        subject = "Confirmation: Whirlpool Appliance Repair Appointment"
        body = (f"Dear {customer_name},\n\n"
                f"Thank you for scheduling a repair appointment with Whirlpool.\n\n"
                f"Details of your appointment:\n"
                f"Appliance Type: {appliance_type}\n"
                f"Technician Visit Date: {technician_date}\n\n"
                f"If you have any questions, please contact us.\n\n"
                f"Best regards,\n"
                f"Whirlpool Service Team")

        # Create the email message object
        msg = MIMEMultipart()
        msg['From'] = smtp_user
        msg['To'] = customer_email
        msg['Subject'] = subject
        msg.attach(MIMEText(body, 'plain'))

        # Connect to the SMTP server and send the email
        with smtplib.SMTP(smtp_server, smtp_port) as server:
            server.starttls()  # Start TLS encryption
            server.login(smtp_user, smtp_password)  # Login to the SMTP server
            server.sendmail(smtp_user, customer_email, msg.as_string())  # Send the email

        print(f"Confirmation email successfully sent to {customer_email}.")
    
    except smtplib.SMTPException as e:
        # Handle any SMTP-related errors
        print(f"Failed to send email: {e}")
    except Exception as e:
        # Handle any other unexpected errors
        print(f"An error occurred: {e}")


# Example usage
if __name__ == "__main__":
    # Replace with actual customer details
    customer_email = "customer@example.com"
    customer_name = "John Doe"
    appliance_type = "lavadora"
    technician_date = "2023-10-15"

    send_email_confirmation(customer_email, customer_name, appliance_type, technician_date)
```
