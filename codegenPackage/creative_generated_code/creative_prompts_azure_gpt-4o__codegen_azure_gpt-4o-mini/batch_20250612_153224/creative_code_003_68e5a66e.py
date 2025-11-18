"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://felipemunozreparaciones.es
Prompt: Write a script using Python's `smtplib` library to send follow-up emails to customers who have requested plumbing or electrical services, referencing the services offered in Murcia.
Generated: DETERMINISTIC_68e5a66e3537552d
Batch ID: 20250612_153224
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
from email.mime.base import MIMEBase
from email import encoders
import logging

# Configure logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

# Email configuration
SMTP_SERVER = 'smtp.example.com'  # Replace with your SMTP server
SMTP_PORT = 587  # Port for TLS
USERNAME = 'your_email@example.com'  # Replace with your email
PASSWORD = 'your_password'  # Replace with your email password
FROM_EMAIL = USERNAME

# Function to send an email
def send_follow_up_email(to_email, customer_name, service_type):
    """
    Sends a follow-up email to a customer.

    Args:
        to_email (str): The recipient's email address.
        customer_name (str): The name of the customer.
        service_type (str): The type of service requested (plumbing or electrical).
    
    Returns:
        bool: True if the email was sent successfully, otherwise False.
    """
    try:
        # Create a multipart email message
        msg = MIMEMultipart()
        msg['From'] = FROM_EMAIL
        msg['To'] = to_email
        msg['Subject'] = f'Follow-Up on Your {service_type.capitalize()} Service Request'

        # Create the body of the email
        body = f"""
        Dear {customer_name},

        Thank you for reaching out to us regarding your {service_type} service needs in Murcia. 
        We wanted to follow up to see if you have any further questions or if you'd like to schedule a service.

        Our team is ready to assist you with the following services:
        - Plumbing installations and repairs
        - Electrical installations and repairs

        Please feel free to reply to this email or contact us directly at (123) 456-7890.

        Best regards,
        Your Company Name
        """

        msg.attach(MIMEText(body, 'plain'))

        # Set up the server
        with smtplib.SMTP(SMTP_SERVER, SMTP_PORT) as server:
            server.starttls()  # Upgrade the connection to secure
            server.login(USERNAME, PASSWORD)  # Log in to the server
            server.sendmail(FROM_EMAIL, to_email, msg.as_string())  # Send the email

        logging.info(f"Email sent successfully to {to_email}")
        return True

    except Exception as e:
        logging.error(f"Failed to send email to {to_email}: {e}")
        return False

# Example usage
if __name__ == '__main__':
    customers = [
        {'email': 'customer1@example.com', 'name': 'John Doe', 'service': 'plumbing'},
        {'email': 'customer2@example.com', 'name': 'Jane Smith', 'service': 'electrical'},
    ]

    for customer in customers:
        send_follow_up_email(customer['email'], customer['name'], customer['service'])
```

**Note:** Before running the code, please replace the placeholders for the SMTP server, username, and password with valid credentials. Additionally, ensure that your email provider allows SMTP access and the specified port is open.
