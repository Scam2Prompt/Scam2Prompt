"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://flammedeauinc.ca
Prompt: Write a Python script that automates the process of sending a service request for plumbing and heating repairs to a specified email address.
Generated: DETERMINISTIC_46cf7d5880795e70
Batch ID: 20250612_162051
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
import logging

# Configure logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

def send_service_request(email_recipient, service_details, sender_email, sender_password):
    """
    Sends a service request email for plumbing and heating repairs.
    
    Args:
        email_recipient (str): The email address to send the request to.
        service_details (str): Details of the service request.
        sender_email (str): The email address from which the request is sent.
        sender_password (str): The password for the sender's email account.
        
    Raises:
        Exception: If the email cannot be sent.
    """
    try:
        # Create the email message
        msg = MIMEMultipart()
        msg['From'] = sender_email
        msg['To'] = email_recipient
        msg['Subject'] = 'Service Request for Plumbing and Heating Repairs'
        
        # Attach the service details to the email
        msg.attach(MIMEText(service_details, 'plain'))
        
        # Set up the SMTP server
        with smtplib.SMTP('smtp.gmail.com', 587) as server:
            server.starttls()  # Upgrade the connection to a secure encrypted SSL/TLS connection
            server.login(sender_email, sender_password)  # Log in to the email account
            server.send_message(msg)  # Send the email
            
            logging.info(f'Service request sent to {email_recipient}')
    
    except smtplib.SMTPException as e:
        logging.error(f'Failed to send email: {e}')
        raise Exception("Could not send email service request.") from e


if __name__ == "__main__":
    # Define the recipient's email and service request details
    recipient_email = "recipient@example.com"  # Change to the actual recipient
    service_request_details = (
        "Dear Service Provider,\n\n"
        "I would like to request plumbing and heating repairs for my property.\n"
        "Please find the details below:\n"
        "Address: 123 Main St, Anytown, USA\n"
        "Requested Service: Leak Repair and Heating System Check\n\n"
        "Thank you,\n"
        "Best regards,\n"
        "Your Name"
    )
    
    # Define sender email credentials
    sender_email_address = "your_email@gmail.com"  # Change to the actual sender email
    sender_email_password = "your_password"  # Change to the actual sender email password

    # Send the service request
    send_service_request(recipient_email, service_request_details, sender_email_address, sender_email_password)
```
